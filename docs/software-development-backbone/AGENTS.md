# Presentation guidance

- Keep the seven-slide code-example sequence unless the user asks to change the scope.
- Edit `templates/index.html.jinja`, `slides/styles.css`, and `examples/`, then
  run `./j`. The HTML deck and speaker notes are generated from the same source.
- Preserve Shower Ribbon, local fonts, offline assets, and the `j` / Makefile
  workflow inherited from `~/projects/streaming-demo`.
- Keep one running example. Label illustrative models and proposed harness
  behavior clearly. Distinguish ontology statements from executable checks.
- Always use YAML-LD for linked-data examples.
- Keep source references at the bottom right, outside titles.
- Retain code highlighting and verify executable snippets when adding them.
- Use Mermaid for diagrams and retain editable `.mmd` sources.
- Split dense content instead of shrinking it. Remove captions that only
  narrate the visible example.
- Validate rendered slides in Chromium through Playwright MCP after changes.
