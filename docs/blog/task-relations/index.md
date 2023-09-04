---
title: Prefer task dependencies over subtasks
description: Subtasks, dependencies, their pro & contra in software projects
date: "2023-07-08"
exclude_from_blog: true
---

Planning a project means building a model of its future development, a model that will evolve as the project progresses. If the model is close enough then it should help us manage our efforts; but attempts to make it too close will mean we'll spend too much time on the model itself instead of putting the necessary effort into the real work.

Let's look into one particular aspect of software project management: relation between tasks.

## Subtasks & Supertasks

* `DEV-1`: Write a post about tasks in software projects
    * `DEV-2`: Come up with an example of a supertask with subtasks
    * `DEV-3`: Note about Jira sprints
    * `DEV-4`: Do something else
    * `DEV-5`: Publish the post

Supported by many Agile-oriented project management systems like Jira, Asana, Notion, or Linear, this helps decompose complex pieces of work into smaller pieces.

## Supertasks & Jira sprints

By the end of the sprint, you might have the following tasks structure:

* `DEV-1`: Write a post about tasks in software projects
    * ~~`DEV-2`: Come up with an example of a supertask with subtasks~~
    * ~~`DEV-3`: Note about Jira sprints~~
    * `DEV-4`: Do something else
    * `DEV-5`: Publish the post

As current sprint `SP1` expires, `DEV-1` will be moved to the next one (`SP2`), together with each subtask, — even the ones which were already completed.

This will:

* Distort the backlog for `SP2` sprint,
* corrupt the team velocity, if that metric is being tracked.

## Should a supertask have an associated pull request?

{{ render("supertask-roles") }}

If we're treating supertasks as containers then, theoretically, we can automatically close a supertask as soon as each of its subtasks is closed. In reality, however, I wouldn't be so bold:

* New circumstances reveal themselves, more work needs to be done
* Each developer has done their respective subtask, but results of their work suddenly do not integrate very well
* The feature as a whole has to be showcased to stakeholders and can be considered Done only when they approve

I personally would vote for supertasks-as-containers approach but, due to estimation difficulties and the tendency of Definition of Done to slip between the fingers, I do not feel this model well fits the reality.

Any alternatives?

## Task Dependencies

Instead of parent-to-child relations, we can keep all tasks on one level — and link them to each other with `blocks` relationships.

* No need for container tasks
* The end goal — the purple task — should contain any validation or verification work and has its own assignee who is not necessarily responsible for all of its dependencies

<div>{{ render("write-paper-about-task-relations") }}</div>

How does this approach compare against subtasks?

{{ render("subtasks-vs-dependencies") }}

## Dependencies support in project management software

{{ render("dependencies-software-support") }}
