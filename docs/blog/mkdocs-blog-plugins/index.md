---
exclude_from_blog: true
hide:
  - navigation

$id: mkdocs-blog-plugins

table:columns:
  - table:self
  - last-commit
  - $id: github:hasLatestRelease
    title: Latest Release
  - $id: github:stargazers_count
    title: Github Stars
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

table:rows:
  - $id: https://github.com/andyoakley/mkdocs-blog
    notes: Looks unmaintained ☹
    requires-nested-directories:
      ⇐: https://github.com/andyoakley/mkdocs-blog#content-layout
      =: true
    supports-frontmatter:
      ⇐: https://github.com/andyoakley/mkdocs-blog#content-layout
      =: false
  - $id: https://github.com/derJD/python-mkblog
    requires-nested-directories:
      ⇐: https://github.com/derJD/python-mkblog#python-mkblog
      =: false
    supports-frontmatter:
      ⇐: https://github.com/derJD/python-mkblog#python-mkblog
      =: true
  - $id: https://github.com/fmaida/mkdocs-blog-plugin
    requires-nested-directories:
      ⇐: https://github.com/fmaida/mkdocs-blog-plugin#how-can-i-add-new-articles-to-my-blog-section-
      =: true
    supports-frontmatter: false
  - $id: https://github.com/liang2kl/mkdocs-blogging-plugin
    notes: Uses front matter or Git log to retrieve date per blog entry.
    tags: true
    requires-nested-directories:
      ⇐: https://liang2kl.codes/mkdocs-blogging-plugin/#publish-with-github-pages
      =: false
    supports-frontmatter:
      ⇐: https://liang2kl.codes/mkdocs-blogging-plugin/#publish-with-github-pages
      =: true
    choice:
      =: true
      ⇐: https://yeti.sh/articles/
  - $id: https://github.com/vuquangtrong/mkdocs-material-blog
    tags: true
    notes: Is a theme, not a plugin.


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

{{ render('mkdocs-blog-plugins') }}
