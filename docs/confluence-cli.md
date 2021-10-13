---
title: Choose a Confluence CLI
choices:
  https://marketplace.atlassian.com/apps/284/confluence-command-line-interface-cli?hosting=cloud&tab=overview:
    label: Confluence Command Line Interface (CLI)
    author: Bob Swift Atlassian Apps
    pricing:
      - trial: 30 days
      - rate: $5/mo
    contra: I do not have rights to install this app on our Confluence Cloud.
  https://github.com/proctorlabs/confluence-cli:
    label: proctorlabs/confluence-cli
    author: proctorlabs
    programming-language: Go
    pro: There is a ready-to-use Docker command.
    contra:
      - Repo is archived and unsupported.
      - There are forks but none of them shows independent development.
  https://github.com/jsinglet/confluence-command-line:
    label: jsinglet/confluence-command-line
    programming-language: Python
    contra:
      - The only supported command is `create-skeleton`, which can help me but not entirely,
      - The tool is unmaintained since 2018.
decision:
    chosen: null
    because: None of these suffice. Going to use Python API.
---

