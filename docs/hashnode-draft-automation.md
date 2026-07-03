# Hashnode draft automation

This repository is currently a Hashnode markdown backup. The workflow at
`.github/workflows/hashnode-draft.yml` adds the other direction as an explicit,
manual action:

```text
Markdown in GitHub
    ↓ workflow_dispatch
Hashnode draft
```

It does **not** publish posts automatically. It only creates a draft so the
article can be reviewed in Hashnode before publishing.

## Required Hashnode setup

Hashnode GraphQL API access now requires API access on the publication. If the
API returns a paid-access error, enable the required plan/API access in the
Hashnode dashboard first.

Create a Hashnode Personal Access Token from:

```text
https://hashnode.com/settings/developer
```

Then configure this repository:

### GitHub secrets

Required:

```text
HASHNODE_API_TOKEN
```

One of these is also required:

```text
HASHNODE_PUBLICATION_ID
```

or configure this repository variable instead:

```text
HASHNODE_PUBLICATION_HOST=blog.yu.money
```

`HASHNODE_PUBLICATION_ID` is preferred because it avoids an extra API lookup.
`HASHNODE_PUBLICATION_HOST` is more convenient when setting things up the first
time.

## How to create a draft

1. Commit the markdown file and any image assets to this repository.
2. Open GitHub Actions.
3. Run **Create Hashnode Draft**.
4. Enter the markdown file path, for example:

```text
posts/hermes-agent-discord-gateway.md
```

or, if the file is at the repo root:

```text
hermes-agent-discord-gateway.md
```

The workflow prints the created draft metadata in the logs.

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
---
```

`title` is required.

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

## Local dry-run

From the repository root:

```bash
python scripts/hashnode_create_draft.py path/to/article.md \
  --publication-host blog.yu.money \
  --dry-run
```

This validates frontmatter and prints the GraphQL payload without calling
Hashnode.

## Local real draft creation

```bash
export HASHNODE_API_TOKEN="..."
export HASHNODE_PUBLICATION_HOST="blog.yu.money"
python scripts/hashnode_create_draft.py path/to/article.md
```

Again, this creates a draft only. It does not publish.
