---
title: Retrieve auth token from an environment variable
$id: token-in-env
---

The recommended auth method at the moment is [API token auth](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/). In JIRA UI, you obtain a token and store it somehow in your environment variables (for example, in `~/.profile`).

I believe it important that a CLI tool can obtain token from environment variables. That:

* Makes configuration easier by eliminating the need of a special config file;
* Simplifies integration of the JIRA CLI tool into CI for various automation tasks.

I believe a proper tool should have this capability.
