---
title: JSON-RPC messages are annotated with LD contexts
description: "@context declarations allow to modify the message format within certain bounds without breaking compatibility."
---

{{ page.meta.description }}

## Communicating components

In certain circumstances, `terry` issues a command `terry.dev/create-task` which is expected to create a task with a title, description, type(s), and assignee. The task management plugin must create that task.

`terry-github` plugin is built specifically for `terry` and understands that command. Everything is fine.

Now what if we want to tie `terry` and a generic interfacing program for a task manager system? For instance, `jira-jsonrpc-ld` is a tool that accepts a different command: `ld.dev/create-task`, with different parameters.

Can we make these two tools friends?

Let's assume that we do not wish to change the source code of these tools. They need to be built from the beginning in a way which allows us to make them composable.

## Who is going to extend the hand?

The two tools must use a format that both of them can understand. We have choices.

```yaml
alternatives:
  - id: `terry` adapts its output
    title: `terry` changes its JSON-RPC message format so that `jira-jsonrpc-ld` can understand it.
    good: no
    because: This will mean that `terry` must receive a communication from `jira-jsonrpc-ld` to explain at least something about the format the latter can understand. This means the one-way communication that we've been looking at converts into a two-way communication, dramatically increasing the complexity of the system. Let's avoid that.
  - id: `jira-jsonrpc-ld` interprets `terry`'s output
    good: yes
  - id: `terry-to-jira` intermediate program is written and placed between the counterparts.
    good: so-so
    because: This is probably unavoidable in many situations but let's try to get along without such an effort whenever possible.
```

## How will `jira-jsonrpc-ld` adapt the incoming message?

The names of fields, their types and stuff — all of that is different for the two tools. I know two ways of coercing one into another without writing custom code in a general purpose language:

```yaml
alternatives:
    - id: json-ld-framing
    - id: rdf-and-owl
```

!!! warning "todo
    I have no evidence at this point to prefer one to the other. However, I do not know whether it is possible to coerce a document based on one ontology to another ontology with framing. With OWL, that's certainly possible but that requires more computing power. Further research is necessary.
