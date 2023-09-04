---
exclude_from_blog: true

$id: terminal-recorders
title: Terminal recorder

# FIXME:
#   title: Boolean facet does not work for this table.

table:columns:
  - table:self
  - $id: output-format
    title: Output Format
  - $id: scripting
    title: Scripting
  - $id: runs-commands
    title: Runs Commands
  - $id: archived
    title: "Archived @ GitHub"

table:rows:
  - $id: https://github.com/faressoft/terminalizer
    output-format: svg
    scripting: no
  - $id: https://github.com/neatsoftware/term-sheets
    comment: This is essentially a presentation tool, it does not run commands itself. Instead, it playbacks a script.
    output-format:
      - svg
      - gif
    runs-commands: no
    scripting: yes
  - $id: https://github.com/nbedos/termtosvg
    archived: true
  - $id: https://github.com/marionebl/svg-term-cli
    comment: asciinema → svg
  - $id: https://asciinema.org
    language: python
  - $id: https://github.com/ovh/ovh-ttyrec
  - $id: https://github.com/mjording/ttyrec
  - $id: https://github.com/slowli/term-transcript/cli
    language: rust
    supports-animation: no
    scripting: yes
    runs-commands: yes
  - $id: https://github.com/sloria/doitlive
    format: null
  - $id: https://github.com/pawamoy/shelldemo
  - $id: https://github.com/ines/termynal
    scripting: yes
    supports-animation: yes
    runs-commands: no
    language: js

table:order-by:
  - table:self

---

{{ render('terminal-recorders') }}
