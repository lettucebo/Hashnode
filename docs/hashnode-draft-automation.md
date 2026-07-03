# Controlled Hashnode publishing

This repository is currently a Hashnode markdown backup. The workflow at
`.github/workflows/hashnode-draft.yml` adds the other direction as an explicit,
manual control surface:

```text
Markdown in GitHub
    ↓ workflow_dispatch
validate / draft / publish-draft / publish / update
    ↓
Hashnode
```

The safe default is `draft`. Nothing is published unless the workflow input is
explicitly set to `publish-draft` or `publish`.

## Required Hashnode setup

Hashnode GraphQL API access now requires API access on the publication. If the
API returns a paid-access error or HTML instead of JSON, enable the required
plan/API access in the Hashnode dashboard first.

Create a Hashnode Personal Access Token from:

```text
https://hashnode.com/settings/developer
```

Then configure this repository.

### GitHub secrets

Required for all real Hashnode API calls:

```text
HASHNODE_API_TOKEN
```

Optional, but preferred because it avoids an extra API lookup:

```text
HASHNODE_PUBLICATION_ID
```

### GitHub variables

If `HASHNODE_PUBLICATION_ID` is not configured, set this repository variable:

```text
HASHNODE_PUBLICATION_HOST=blog.yu.money
```

`HASHNODE_PUBLICATION_HOST` is intentionally a variable, not a secret.

## Workflow actions

Run **Controlled Hashnode Publish** from GitHub Actions and choose one action:

| Action | What it does |
| --- | --- |
| `validate` | Parses the markdown and prints the Hashnode payload. Does not need a token. |
| `api-check` | Verifies token + publication API access. |
| `draft` | Creates a draft. If a draft ID already exists, updates that draft. |
| `update-draft` | Updates an existing draft. Requires `hashnode_draft_id` or workflow `draft_id`. |
| `publish-draft` | Publishes an existing draft. Requires `hashnode_draft_id` or workflow `draft_id`. |
| `publish` | Publishes a new post directly. Use carefully. |
| `update-post` | Updates an existing published post. Requires `hashnode_article_id` or workflow `post_id`. |

## Recommended flow

1. Commit the markdown file and any image assets.
2. Run `validate` first.
3. Run `draft` with `write_back=true`.
4. Review the draft in Hashnode.
5. Run `publish-draft` when ready.

## Markdown frontmatter

Supported fields:

```yaml
---
title: "Post title"
slug: post-slug
tags: hermes-agent, discord, ai-agent
cover: https://example.com/cover.png
ogImage: https://example.com/og.png
subtitle: Optional subtitle
canonical: https://original.example.com/article
seoTitle: Optional SEO title
seoDescription: Optional SEO description
hashnode_action: draft
hashnode_draft_id:
hashnode_article_id:
---
```

`title` is required.

The workflow can write these fields back when `write_back=true`:

```yaml
hashnode_draft_id: <created draft id>
hashnode_article_id: <published post id>
```

## Images

Hashnode needs public image URLs. If the article uses relative images like:

```markdown
![](assets/hermes-discord-flow.png)
```

this workflow rewrites them to GitHub raw URLs before sending the markdown to
Hashnode:

```text
https://raw.githubusercontent.com/<owner>/<repo>/<ref>/assets/hermes-discord-flow.png
```

For permanent production posts, using Hashnode CDN, Cloudinary, R2, or another
stable image host is still cleaner. GitHub raw URLs are good enough for a safe
first version of the automation.

## Local validate

From the repository root:

```bash
python3 scripts/hashnode_create_draft.py path/to/article.md \
  --action validate
```

This validates frontmatter and prints the Hashnode payload without calling
Hashnode.

## Local API check

```bash
export HASHNODE_API_TOKEN="..."
export HASHNODE_PUBLICATION_HOST="blog.yu.money"
python3 scripts/hashnode_create_draft.py path/to/article.md \
  --action api-check
```

If the publication does not have API access, the script prints an explicit
message pointing to Hashnode billing/API access instead of a raw JSON parse
error.

## Local draft / publish examples

Create or update a draft:

```bash
python3 scripts/hashnode_create_draft.py path/to/article.md \
  --action draft \
  --write-back
```

Publish an existing draft:

```bash
python3 scripts/hashnode_create_draft.py path/to/article.md \
  --action publish-draft \
  --draft-id <draft id> \
  --write-back
```

Publish directly:

```bash
python3 scripts/hashnode_create_draft.py path/to/article.md \
  --action publish
```
