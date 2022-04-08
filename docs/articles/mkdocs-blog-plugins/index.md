---
$context:
  - $import: table
  - $import: github

hide:
  - navigation

$type: table:Table
table:class:
  $id: MkdocsBlogPlugin
  title: Plugin
columns:
  - table:self
  - last-commit
  - github:hasLatestRelease
  - github:stargazers_count
  - $id: requires-nested-directories
    rdfs:comment: "Requires nested directory structure, like: 2022/03/page.md"
    title: Requires Nested Dirs
    rdfs:domain: MkdocsBlogPlugin
  - $id: supports-frontmatter
    title: Supports Frontmatter
    rdfs:comment: Supports providing the blog entry date in Markdown YAML front matter.
    rdfs:domain: MkdocsBlogPlugin
  - $id: tags
    title: 🏷️ Tags
    rdfs:comment: Supports tagging blog posts
    rdfs:domain: MkdocsBlogPlugin
  - $id: notes
    title: 💬 Notes
  - $id: choice
    title: ✔️ My Choice

$included:
  - $id: github:pushed_at
    rdfs:subPropertyOf:
      $id: last-commit
      rdfs:comment: Last commit on the main branch
      title: Last Commit
      iolanta:hasDefaultFacet:
        $id: python://octadocs.facets.DateLiteral

title: MkDocs plugins for blogging
description: "MkDocs was designed to manage software project documentation, but in fact it is a very wide purpose static site generator. Can you use it to write your personal blog? Yes, most assuredly. Here are a few plugins for that."
---

{{ page.meta.description }}
