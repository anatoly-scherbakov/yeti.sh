---
id: plugin-communication
title: Communicate with plugins via stdin & stdout
description: The main `terry` executable will communicate with language-specific and scheduler-specific plugins sending text-based messages to their stdin and reading analogous messages from their stdout.
---

{{ page.meta.description }}

## Context

At the moment of writing this document, it isn't yet clear in what programming language to write `terry`. Anyway, I believe it to be important to ensure that plugins for `terry` must be language agnostic.

## Decision

```yaml
criteria:
  language-agnostic:
    title: Language Agnostic
  ease-of-debug:
    title: Debuggability

alternatives:
  - title: socket-based communication
    language-agnostic: yes
    ease-of-debug: 3
  - title: stdin/stdout communication
    language-agnostic: yes
    ease-of-debug: 1
```
