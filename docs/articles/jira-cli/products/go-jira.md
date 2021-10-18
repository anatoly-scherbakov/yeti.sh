---
title: go-jira
$id: https://github.com/go-jira/jira
language: Go
token-in-env:
    is: true
    because: 'https://github.com/go-jira/jira'
    comment: For a less-secure option you can also provide the API token via a JIRA_API_TOKEN environment variable
fix-versions-support:
    is: false
    comment: The --override option can be used and custom commands with hard-coded JQL queries can be employed, but a normal shell option does not exist.
jql_builder:
    is: false
---

## How to install

```shell
wget -O ~/bin/jira https://github.com/go-jira/jira/releases/download/v1.0.27/jira-linux-amd64
chmod +x ~/bin/jira
```

## How to use

```shell
cat > ~/.jira.d/config.yml
endpoint: https://yeti-sh.atlassian.net
user: talk@yeti.sh   # replace this with yours
password-source: keyring
^D
```

- Create Jira API token
- Call `jira session`

You will be asked for the token and it will be persisted.

## Commands

### List issues

```shell
jira ls --assignee talk@yeti.sh
```

!!! warning "Did not work for me"
    The tool won't `ls` any of our relevant issues, see [Github issue here](https://github.com/go-jira/jira/issues/239).

### Create a new issue

```shell
jira create --project PROJ --issuetype=Task --override 'assignee=talk@yeti.sh' --override 'epic=PROJ-123' --override 'release=1.0.1 beta' --override 'summary=Add Thing.some_id column'
```

### Send issue to In Progress from Queued

```shell
jira transition --noedit 'DEVELOPMENT STARTED' PROJ-2575
```

### Send issue to Code Review from In Progress

```shell
jira transition --noedit 'Code Review' PROJ-2575
```

### How to add issue to an epic

```shell
jira epic add PROJ-126 PROJ-2663
```

### Link two issues

```shell
jira issuelink PROJ-2382 Blocks PROJ-2667
```

The order is reversed. In fact, 2667 will block 2382 in this example.
