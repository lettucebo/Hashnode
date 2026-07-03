#!/usr/bin/env python3
"""Create a Hashnode draft from a Markdown file.

This script is intentionally dependency-free so it can run in GitHub Actions
without npm/pip install steps.

Required for real API calls:
  HASHNODE_API_TOKEN
  HASHNODE_PUBLICATION_ID or HASHNODE_PUBLICATION_HOST

Safe default: it only creates a draft. It never publishes a post.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

HASHNODE_ENDPOINT = "https://gql.hashnode.com"


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse a small YAML-frontmatter subset used by Hashnode exports.

    Supports:
    - key: value
    - quoted strings
    - comma-separated tags
    - simple arrays: [a, b, c]

    This is not a full YAML parser. It avoids third-party dependencies on
    purpose. If a value is too complex, keep it as a string.
    """
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text

    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.DOTALL)
    if not match:
        return {}, text

    raw_fm = match.group(1)
    body = text[match.end() :]
    data: dict[str, Any] = {}

    for line in raw_fm.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if not key:
            continue

        if (
            len(value) >= 2
            and ((value[0] == value[-1] == '"') or (value[0] == value[-1] == "'"))
        ):
            value = value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            value = [v.strip().strip('"\'') for v in value[1:-1].split(",") if v.strip()]

        data[key] = value

    return data, body.lstrip("\r\n")


def normalize_tags(value: Any) -> list[dict[str, str]]:
    if not value:
        return []
    if isinstance(value, str):
        names = [x.strip() for x in value.split(",") if x.strip()]
    elif isinstance(value, list):
        names = [str(x).strip() for x in value if str(x).strip()]
    else:
        return []

    tags: list[dict[str, str]] = []
    for name in names:
        # Hashnode accepts TagInput with name/slug/id. Supplying both name and
        # slug makes drafts readable even when tag IDs are not known yet.
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or name.lower()
        tags.append({"name": name, "slug": slug})
    return tags


def is_external_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://") or url.startswith("data:")


def normalize_local_asset_url(url: str, markdown_path: Path, raw_base_url: str | None) -> str:
    """Convert a local/relative asset URL to a public raw URL when possible."""
    if not raw_base_url or is_external_url(url) or url.startswith("#"):
        return url

    raw_base_url = raw_base_url.rstrip("/")
    repo_root = Path.cwd().resolve()
    markdown_dir = markdown_path.resolve().parent

    if url.startswith("/"):
        rel = url.lstrip("/")
    else:
        abs_from_markdown = (markdown_dir / url).resolve()
        abs_from_root = (repo_root / url).resolve()
        # Prefer the path relative to the markdown file when it exists. If it
        # does not exist, fall back to repo-root relative paths. This lets both
        # `![](assets/x.png)` from a root-level post and from a nested draft work
        # in the common repo layout.
        abs_img = abs_from_markdown if abs_from_markdown.exists() else abs_from_root
        try:
            rel = abs_img.relative_to(repo_root).as_posix()
        except ValueError:
            # Do not invent a GitHub raw URL for paths outside this repository.
            # Leaving the original URL unchanged makes the issue visible to the
            # author instead of silently pointing Hashnode at the wrong asset.
            return url

    return f"{raw_base_url}/{rel}"


def rewrite_relative_images(markdown: str, markdown_path: Path, raw_base_url: str | None) -> str:
    """Rewrite relative Markdown image URLs to a public raw GitHub base URL.

    Hashnode cannot render local files like ./assets/foo.png. If raw_base_url is
    provided, relative image paths are converted to:
      {raw_base_url}/{path-relative-to-repo-root}
    """
    if not raw_base_url:
        return markdown

    raw_base_url = raw_base_url.rstrip("/")

    def replace(match: re.Match[str]) -> str:
        alt = match.group(1)
        url_and_title = match.group(2).strip()
        # Keep optional title if present: image.png "title"
        parts = re.match(r"([^\s]+)(.*)", url_and_title)
        if not parts:
            return match.group(0)
        url = parts.group(1)
        suffix = parts.group(2)
        normalized = normalize_local_asset_url(url, markdown_path, raw_base_url)
        if normalized == url:
            return match.group(0)
        return f"![{alt}]({normalized}{suffix})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace, markdown)


def graphql_request(query: str, variables: dict[str, Any], token: str) -> dict[str, Any]:
    req = urllib.request.Request(
        HASHNODE_ENDPOINT,
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            # Hashnode examples and current MCP implementations send the raw PAT.
            "Authorization": token,
            "User-Agent": "hashnode-draft-action/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Hashnode HTTP {exc.code}: {body}") from exc

    if payload.get("errors"):
        raise RuntimeError("Hashnode GraphQL errors: " + json.dumps(payload["errors"], ensure_ascii=False))
    return payload.get("data") or {}


def get_publication_id(host: str, token: str) -> str:
    query = """
    query GetPublication($host: String!) {
      publication(host: $host) {
        id
        title
        url
      }
    }
    """
    data = graphql_request(query, {"host": host}, token)
    publication = data.get("publication")
    if not publication or not publication.get("id"):
        raise RuntimeError(f"Could not find Hashnode publication for host: {host}")
    print(f"Resolved publication: {publication.get('title')} ({publication.get('url')})", file=sys.stderr)
    return publication["id"]


def build_draft_input(
    markdown_file: Path,
    publication_id: str,
    raw_base_url: str | None,
) -> dict[str, Any]:
    text = markdown_file.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    body = rewrite_relative_images(body, markdown_file, raw_base_url)

    title = str(frontmatter.get("title") or "").strip()
    if not title:
        raise RuntimeError("Missing required frontmatter: title")

    draft_input: dict[str, Any] = {
        "publicationId": publication_id,
        "title": title,
        "contentMarkdown": body,
    }

    if frontmatter.get("subtitle"):
        draft_input["subtitle"] = str(frontmatter["subtitle"])
    if frontmatter.get("slug"):
        draft_input["slug"] = str(frontmatter["slug"])
        draft_input["settings"] = {"slugOverridden": True}
    if frontmatter.get("canonical"):
        draft_input["originalArticleURL"] = str(frontmatter["canonical"])
    if frontmatter.get("disableComments"):
        draft_input["disableComments"] = str(frontmatter["disableComments"]).lower() == "true"

    tags = normalize_tags(frontmatter.get("tags"))
    if tags:
        draft_input["tags"] = tags

    cover = frontmatter.get("cover") or frontmatter.get("ogImage")
    if cover:
        cover_url = normalize_local_asset_url(str(cover), markdown_file, raw_base_url)
        if is_external_url(cover_url):
            draft_input["coverImageOptions"] = {"coverImageURL": cover_url}

    meta: dict[str, str] = {}
    if frontmatter.get("seoTitle"):
        meta["title"] = str(frontmatter["seoTitle"])
    if frontmatter.get("seoDescription"):
        meta["description"] = str(frontmatter["seoDescription"])
    if frontmatter.get("ogImage"):
        og_image_url = normalize_local_asset_url(str(frontmatter["ogImage"]), markdown_file, raw_base_url)
        if is_external_url(og_image_url):
            meta["image"] = og_image_url
    if meta:
        draft_input["metaTags"] = meta

    return draft_input


def create_draft(draft_input: dict[str, Any], token: str) -> dict[str, Any]:
    mutation = """
    mutation CreateDraft($input: CreateDraftInput!) {
      createDraft(input: $input) {
        draft {
          id
          title
          slug
          updatedAt
          author { username }
        }
      }
    }
    """
    data = graphql_request(mutation, {"input": draft_input}, token)
    draft = (data.get("createDraft") or {}).get("draft")
    if not draft:
        raise RuntimeError("Hashnode did not return a draft: " + json.dumps(data, ensure_ascii=False))
    return draft


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a Hashnode draft from Markdown")
    parser.add_argument("markdown_file", type=Path)
    parser.add_argument("--publication-id", default=os.getenv("HASHNODE_PUBLICATION_ID"))
    parser.add_argument("--publication-host", default=os.getenv("HASHNODE_PUBLICATION_HOST"))
    parser.add_argument("--token", default=os.getenv("HASHNODE_API_TOKEN"))
    parser.add_argument("--raw-base-url", default=os.getenv("RAW_BASE_URL"))
    parser.add_argument("--dry-run", action="store_true", help="Print payload without calling Hashnode")
    args = parser.parse_args()

    if not args.markdown_file.exists():
        raise SystemExit(f"Markdown file not found: {args.markdown_file}")

    token = args.token
    publication_id = args.publication_id

    if not publication_id:
        if not args.publication_host:
            raise SystemExit("Need HASHNODE_PUBLICATION_ID or HASHNODE_PUBLICATION_HOST")
        if args.dry_run and not token:
            publication_id = "dry-run-publication-id"
        else:
            if not token:
                raise SystemExit("Need HASHNODE_API_TOKEN to resolve HASHNODE_PUBLICATION_HOST")
            publication_id = get_publication_id(args.publication_host, token)

    draft_input = build_draft_input(args.markdown_file, publication_id, args.raw_base_url)

    if args.dry_run:
        print(json.dumps({"input": draft_input}, ensure_ascii=False, indent=2))
        return 0

    if not token:
        raise SystemExit("Need HASHNODE_API_TOKEN")

    draft = create_draft(draft_input, token)
    print(json.dumps({"draft": draft}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
