#!/usr/bin/env python3
"""Controlled Hashnode publishing from Markdown.

Dependency-free helper for GitHub Actions and local use.

Supported actions:
  validate        Parse frontmatter and print the payload only.
  api-check       Resolve the publication and verify Hashnode API access.
  draft           Create a draft, or update an existing draft when draft ID exists.
  update-draft    Update an existing draft.
  publish-draft   Publish an existing draft.
  publish         Publish a new post directly.
  update-post     Update an existing published post.

This script never publishes unless action is explicitly `publish` or
`publish-draft`.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

HASHNODE_ENDPOINT = "https://gql.hashnode.com"
PAID_ACCESS_URL = "https://hashnode.com/changelog/2026-05-13-graphql-api-paid-access"


class HashnodeAPIError(RuntimeError):
    """Raised for actionable Hashnode API errors."""


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, str, str]:
    """Parse a small YAML-frontmatter subset used by this repository.

    Returns (data, body, raw_frontmatter, newline). This is intentionally not a
    full YAML parser so the workflow can run without dependencies.
    """
    newline = "\r\n" if "\r\n" in text[:200] else "\n"
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text, "", newline

    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", text, re.DOTALL)
    if not match:
        return {}, text, "", newline

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

    return data, body.lstrip("\r\n"), raw_fm, newline


def serialize_frontmatter_value(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, list):
        return "[" + ", ".join(json.dumps(str(v), ensure_ascii=False) for v in value) + "]"
    text = str(value)
    if not text:
        return ""
    if any(ch in text for ch in [":", "#", "[", "]", "{", "}", "\n", "\r"]) or text != text.strip():
        return json.dumps(text, ensure_ascii=False)
    return text


def upsert_frontmatter_fields(markdown_file: Path, updates: dict[str, str]) -> None:
    """Update or append simple top-level frontmatter fields."""
    original = markdown_file.read_text(encoding="utf-8")
    data, body, raw_fm, newline = parse_frontmatter(original)
    if not raw_fm:
        raw_fm = ""

    lines = raw_fm.splitlines()
    updated_keys: set[str] = set()
    out_lines: list[str] = []
    for line in lines:
        if ":" not in line or line.lstrip().startswith("#"):
            out_lines.append(line)
            continue
        key = line.split(":", 1)[0].strip()
        if key in updates:
            out_lines.append(f"{key}: {serialize_frontmatter_value(updates[key])}")
            updated_keys.add(key)
        else:
            out_lines.append(line)

    for key, value in updates.items():
        if key not in updated_keys:
            out_lines.append(f"{key}: {serialize_frontmatter_value(value)}")

    new_text = "---" + newline + newline.join(out_lines).rstrip() + newline + "---" + newline + newline + body
    markdown_file.write_text(new_text, encoding="utf-8")


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
    for name in names[:5]:
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or name.lower()
        tags.append({"name": name, "slug": slug})
    return tags


def truthy(value: Any) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


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
        candidate = (repo_root / url.lstrip("/")).resolve()
    else:
        abs_from_markdown = (markdown_dir / url).resolve()
        abs_from_root = (repo_root / url).resolve()
        candidate = abs_from_markdown if abs_from_markdown.exists() else abs_from_root

    try:
        rel = candidate.relative_to(repo_root).as_posix()
    except ValueError:
        return url
    return f"{raw_base_url}/{rel}"


def rewrite_relative_images(markdown: str, markdown_path: Path, raw_base_url: str | None) -> str:
    if not raw_base_url:
        return markdown

    def replace(match: re.Match[str]) -> str:
        alt = match.group(1)
        url_and_title = match.group(2).strip()
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


def explain_non_json_response(response: urllib.response.addinfourl, body: str) -> HashnodeAPIError:
    final_url = response.geturl()
    content_type = response.headers.get("content-type", "")
    parsed = urllib.parse.urlparse(final_url)
    body_start = re.sub(r"\s+", " ", body[:240]).strip()
    if "paid-access" in final_url or "GraphQL API is moving to a paid offering" in body:
        return HashnodeAPIError(
            "Hashnode API returned HTML instead of JSON. Likely cause: this publication "
            "does not have Hashnode Pro / GraphQL API access enabled. "
            f"Final URL: {final_url}. Upgrade/check billing: https://hashnode.com/settings/billing"
        )
    return HashnodeAPIError(
        "Hashnode API returned a non-JSON response. "
        f"Final URL: {parsed.netloc}{parsed.path}; Content-Type: {content_type}; Body: {body_start}"
    )


def graphql_request(query: str, variables: dict[str, Any], token: str) -> dict[str, Any]:
    req = urllib.request.Request(
        HASHNODE_ENDPOINT,
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            # Hashnode requires the raw PAT. No Bearer prefix.
            "Authorization": token,
            "User-Agent": "hashnode-controlled-action/2.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as response:
            raw = response.read().decode("utf-8", errors="replace")
            content_type = response.headers.get("content-type", "")
            if "json" not in content_type.lower():
                raise explain_non_json_response(response, raw)
            payload = json.loads(raw)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        if exc.code in {301, 302}:
            raise HashnodeAPIError(
                "Hashnode API redirected instead of returning JSON. Likely cause: "
                "GraphQL API access requires a Pro publication plan. "
                "Check https://hashnode.com/settings/billing"
            ) from exc
        raise HashnodeAPIError(f"Hashnode HTTP {exc.code}: {body}") from exc
    except json.JSONDecodeError as exc:
        raise HashnodeAPIError(f"Hashnode returned invalid JSON: {exc}") from exc

    if payload.get("errors"):
        raise HashnodeAPIError("Hashnode GraphQL errors: " + json.dumps(payload["errors"], ensure_ascii=False))
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
        raise HashnodeAPIError(f"Could not find Hashnode publication for host: {host}")
    print(f"Resolved publication: {publication.get('title')} ({publication.get('url')})", file=sys.stderr)
    return publication["id"]


def first_value(frontmatter: dict[str, Any], *keys: str) -> Any:
    for key in keys:
        value = frontmatter.get(key)
        if value not in (None, ""):
            return value
    return None


def build_post_input(markdown_file: Path, publication_id: str, raw_base_url: str | None) -> tuple[dict[str, Any], dict[str, Any]]:
    text = markdown_file.read_text(encoding="utf-8")
    frontmatter, body, _, _ = parse_frontmatter(text)
    body = rewrite_relative_images(body, markdown_file, raw_base_url)

    title = str(frontmatter.get("title") or "").strip()
    if not title:
        raise RuntimeError("Missing required frontmatter: title")

    post_input: dict[str, Any] = {
        "publicationId": publication_id,
        "title": title,
        "contentMarkdown": body,
    }

    subtitle = first_value(frontmatter, "subtitle", "description")
    if subtitle:
        post_input["subtitle"] = str(subtitle)
    if frontmatter.get("slug"):
        post_input["slug"] = str(frontmatter["slug"])
        post_input["settings"] = {"slugOverridden": True}
    canonical = first_value(frontmatter, "canonical", "canonical_url", "originalArticleURL")
    if canonical:
        post_input["originalArticleURL"] = str(canonical)
    if frontmatter.get("disableComments") is not None:
        post_input["disableComments"] = truthy(frontmatter["disableComments"])

    tags = normalize_tags(frontmatter.get("tags"))
    if tags:
        post_input["tags"] = tags

    cover = first_value(frontmatter, "cover", "cover_image", "ogImage")
    cover_url = None
    if cover:
        cover_url = normalize_local_asset_url(str(cover), markdown_file, raw_base_url)
        if is_external_url(cover_url):
            post_input["coverImageOptions"] = {"coverImageURL": cover_url}

    meta: dict[str, str] = {}
    if frontmatter.get("seoTitle"):
        meta["title"] = str(frontmatter["seoTitle"])
    if frontmatter.get("seoDescription"):
        meta["description"] = str(frontmatter["seoDescription"])
    og_image = first_value(frontmatter, "ogImage", "cover", "cover_image")
    if og_image:
        og_image_url = normalize_local_asset_url(str(og_image), markdown_file, raw_base_url)
        if is_external_url(og_image_url):
            meta["image"] = og_image_url
    if meta:
        post_input["metaTags"] = meta

    return post_input, frontmatter


def create_draft(post_input: dict[str, Any], token: str) -> dict[str, Any]:
    mutation = """
    mutation CreateDraft($input: CreateDraftInput!) {
      createDraft(input: $input) {
        draft { id title slug updatedAt author { username } }
      }
    }
    """
    data = graphql_request(mutation, {"input": post_input}, token)
    draft = (data.get("createDraft") or {}).get("draft")
    if not draft:
        raise HashnodeAPIError("Hashnode did not return a draft: " + json.dumps(data, ensure_ascii=False))
    return draft


def update_draft(draft_id: str, post_input: dict[str, Any], token: str) -> dict[str, Any]:
    mutation = """
    mutation UpdateDraft($input: UpdateDraftInput!) {
      updateDraft(input: $input) {
        draft { id title slug updatedAt author { username } }
      }
    }
    """
    update_input = {k: v for k, v in post_input.items() if k != "publicationId"}
    update_input["id"] = draft_id
    data = graphql_request(mutation, {"input": update_input}, token)
    draft = (data.get("updateDraft") or {}).get("draft")
    if not draft:
        raise HashnodeAPIError("Hashnode did not return an updated draft: " + json.dumps(data, ensure_ascii=False))
    return draft


def publish_draft(draft_id: str, token: str) -> dict[str, Any]:
    mutation = """
    mutation PublishDraft($input: PublishDraftInput!) {
      publishDraft(input: $input) {
        post { id title slug url publishedAt }
      }
    }
    """
    data = graphql_request(mutation, {"input": {"draftId": draft_id}}, token)
    post = (data.get("publishDraft") or {}).get("post")
    if not post:
        raise HashnodeAPIError("Hashnode did not return a published post: " + json.dumps(data, ensure_ascii=False))
    return post


def publish_post(post_input: dict[str, Any], token: str) -> dict[str, Any]:
    mutation = """
    mutation PublishPost($input: PublishPostInput!) {
      publishPost(input: $input) {
        post { id title slug url publishedAt }
      }
    }
    """
    data = graphql_request(mutation, {"input": post_input}, token)
    post = (data.get("publishPost") or {}).get("post")
    if not post:
        raise HashnodeAPIError("Hashnode did not return a published post: " + json.dumps(data, ensure_ascii=False))
    return post


def update_post(post_id: str, post_input: dict[str, Any], token: str) -> dict[str, Any]:
    mutation = """
    mutation UpdatePost($input: UpdatePostInput!) {
      updatePost(input: $input) {
        post { id title slug url updatedAt }
      }
    }
    """
    # UpdatePostInput is narrower than PublishPostInput in maintained Hashnode
    # MCP implementations. Do not send publicationId or publish-only fields.
    allowed_update_fields = {
        "title",
        "contentMarkdown",
        "subtitle",
        "tags",
        "coverImageOptions",
    }
    update_input = {k: v for k, v in post_input.items() if k in allowed_update_fields}
    update_input["id"] = post_id
    data = graphql_request(mutation, {"input": update_input}, token)
    post = (data.get("updatePost") or {}).get("post")
    if not post:
        raise HashnodeAPIError("Hashnode did not return an updated post: " + json.dumps(data, ensure_ascii=False))
    return post


def resolve_action(cli_action: str | None, frontmatter: dict[str, Any]) -> str:
    action = cli_action or str(first_value(frontmatter, "hashnode_action", "action") or "draft")
    action = action.strip().lower()
    aliases = {
        "create-draft": "draft",
        "create_draft": "draft",
        "publish_post": "publish",
        "publishpost": "publish",
        "publish_draft": "publish-draft",
        "publishdraft": "publish-draft",
        "update_draft": "update-draft",
        "updatedraft": "update-draft",
        "update_post": "update-post",
        "updatepost": "update-post",
        "check": "api-check",
    }
    action = aliases.get(action, action)
    allowed = {"validate", "api-check", "draft", "update-draft", "publish-draft", "publish", "update-post"}
    if action not in allowed:
        raise RuntimeError(f"Unsupported action '{action}'. Allowed: {', '.join(sorted(allowed))}")
    return action


def main() -> int:
    parser = argparse.ArgumentParser(description="Controlled Hashnode publishing from Markdown")
    parser.add_argument("markdown_file", type=Path)
    parser.add_argument("--action", choices=["validate", "api-check", "draft", "update-draft", "publish-draft", "publish", "update-post"])
    parser.add_argument("--publication-id", default=os.getenv("HASHNODE_PUBLICATION_ID"))
    parser.add_argument("--publication-host", default=os.getenv("HASHNODE_PUBLICATION_HOST"))
    parser.add_argument("--token", default=os.getenv("HASHNODE_API_TOKEN") or os.getenv("HASHNODE_TOKEN"))
    parser.add_argument("--raw-base-url", default=os.getenv("RAW_BASE_URL"))
    parser.add_argument("--draft-id", default=os.getenv("HASHNODE_DRAFT_ID"))
    parser.add_argument("--post-id", default=os.getenv("HASHNODE_POST_ID"))
    parser.add_argument("--dry-run", action="store_true", help="Print payload without calling Hashnode")
    parser.add_argument("--write-back", action="store_true", help="Write draft/post IDs back to markdown frontmatter")
    args = parser.parse_args()

    if not args.markdown_file.exists():
        raise SystemExit(f"Markdown file not found: {args.markdown_file}")

    token = args.token
    publication_id = args.publication_id

    raw_text = args.markdown_file.read_text(encoding="utf-8")
    frontmatter, _, _, _ = parse_frontmatter(raw_text)
    action = resolve_action(args.action, frontmatter)

    if not publication_id:
        if args.dry_run or action == "validate":
            publication_id = "dry-run-publication-id"
        else:
            if not args.publication_host:
                raise SystemExit("Need HASHNODE_PUBLICATION_ID or HASHNODE_PUBLICATION_HOST")
            if not token:
                raise SystemExit("Need HASHNODE_API_TOKEN to resolve HASHNODE_PUBLICATION_HOST")
            publication_id = get_publication_id(args.publication_host, token)

    post_input, frontmatter = build_post_input(args.markdown_file, publication_id, args.raw_base_url)
    draft_id = args.draft_id or first_value(frontmatter, "hashnode_draft_id", "draftId")
    post_id = args.post_id or first_value(frontmatter, "hashnode_article_id", "hashnode_post_id", "articleId", "postId")

    if action == "validate" or args.dry_run:
        print(json.dumps({"action": action, "input": post_input, "draftId": draft_id, "postId": post_id}, ensure_ascii=False, indent=2))
        return 0

    if not token:
        raise SystemExit("Need HASHNODE_API_TOKEN")

    if action == "api-check":
        print(json.dumps({"ok": True, "publicationId": publication_id}, ensure_ascii=False, indent=2))
        return 0

    updates: dict[str, str] = {}
    result: dict[str, Any]

    if action == "draft":
        if draft_id:
            result = {"draft": update_draft(str(draft_id), post_input, token), "operation": "update-draft"}
        else:
            draft = create_draft(post_input, token)
            updates["hashnode_draft_id"] = draft["id"]
            result = {"draft": draft, "operation": "create-draft"}
    elif action == "update-draft":
        if not draft_id:
            raise RuntimeError("Need hashnode_draft_id / draftId / --draft-id for update-draft")
        result = {"draft": update_draft(str(draft_id), post_input, token), "operation": "update-draft"}
    elif action == "publish-draft":
        if not draft_id:
            raise RuntimeError("Need hashnode_draft_id / draftId / --draft-id for publish-draft")
        post = publish_draft(str(draft_id), token)
        updates["hashnode_article_id"] = post["id"]
        result = {"post": post, "operation": "publish-draft"}
    elif action == "publish":
        post = publish_post(post_input, token)
        updates["hashnode_article_id"] = post["id"]
        result = {"post": post, "operation": "publish"}
    elif action == "update-post":
        if not post_id:
            raise RuntimeError("Need hashnode_article_id / articleId / --post-id for update-post")
        result = {"post": update_post(str(post_id), post_input, token), "operation": "update-post"}
    else:
        raise RuntimeError(f"Unhandled action: {action}")

    if args.write_back and updates:
        upsert_frontmatter_fields(args.markdown_file, updates)
        result["frontmatterUpdated"] = updates

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
