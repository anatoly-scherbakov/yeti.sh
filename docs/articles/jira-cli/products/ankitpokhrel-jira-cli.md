---
$id: https://github.com/ankitpokhrel/jira-cli
title: ankitpokhrel/jira-cli
language: Go
token-in-env:
    is: true
    because: https://github.com/ankitpokhrel/jira-cli
    comment: Supports JIRA_API_TOKEN variable
fix-versions-support:
    $id: https://github.com/ankitpokhrel/jira-cli/discussions/161
    is: false
    comment: Code changes required for that
jql_builder:
    is: true
    comment: JQL query might be built from command line options and ~ character is used for negation.
exclude_from_blog: true
---

## Configuration

Configure the environment variable and run `jira init`.
