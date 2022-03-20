---
title: alisaifee/jira-cli
$id: https://github.com/alisaifee/jira-cli
language: Python
token-in-env:
    is: false
    because: 'https://jira-cli.readthedocs.io/en/master/intro.html#installation'
    comment: There is no mention of environment variables support.
fix-versions-support:
    is: true
    comment: --fix-version option :)
jql_builder:
    is: false
exclude_from_blog: true
---

## How to auth?

Run `jira-cli configure`, choose `basic_auth` and provide your email and your API token obtainable at your Jira account settings.

## Command line examples

### Creating a new task

...does not work :(

```shell
jira-cli new \
  --type=Story \
  --project=PROJ \
  --assign='talk@yeti.sh' \
  --priority=High \
  'Initialize data-lake-downloader project' --description 'Start a new project from project-template.'
```
⇒
```
The issue type selected is invalid.
```

!!! error "Further investigation halted"
    I had no luck bringing this tool online.
