---
title: Terry
target-audience: software-developers
---

## Problem

While coding, a developer sometimes notices an issue, something that has to be addessed in the future but isn't strictly related to the developer's current task at hand. The developer might:

- ignore the issue;
- decide to get to it later, immediately forget, and never return;
- write it down somewhere on a scratch of paper which will subsequently be found by the developer's cat and made away with;
- write a TODO comment which will never be tracked and remembered of;
- make a ticket in the project's task management system.

The last is the best thing to do in the long term, but it forces the developer to switch context, and breaks concentration.

## Approach

There has been an idea to combine the last two alternatives and write a specially formed TODO or FIXME comments. For instance:

```python
# fixme:
#   title: Rename do_something function to reflect what it is really doing
#   assignee: me
#   priority: low
def do_something():
    ...
```

An automatic system will then parse this comment and create an issue in the project's task management system itself. Such a comment is known as **a puzzle**. The idea is named Puzzle Driven Development (PDD) and is apparently proposed by Egor Bugaenko.

## Previous art

- See `state-of-the-art.yaml`.

!!! warning "Todo"
    Visualize that.

## Todo

I believe Bugaenko's `zerocrat` is a complex solution that does multiple things. I'd want to create a very simple tool for the same exact purpose and a more modular one, supporting different task management systems.

The tool might be named `terry` after Terry Gilliam, who played [Bridge Keeper](https://villains.fandom.com/wiki/Bridge_Keeper) in Monty Python and the Holy Grail, an antagonist who asked people hard questions. Or puzzles. Just as what we're doing here.

So the workflow is like this: you write a `FIXME` or `TODO` comment just as described above; that comment is formatted as YAML. When you run `terry` CLI tool against your code base (as a pre-commit hook, for example), it will search for such comments and *resolve* them. Meaning, the comment will be changed and will now look like this:

```python
# fixme:
#   id: https://github.com/vasya/pupkin/issues/15
#   title: Rename do_something function to reflect what it is really doing
#   assignee: me
#   priority: low
def do_something():
    ...
```

A GitHub issue has been created from this comment. Now the comment is considered *resolved*. You can proceed with committing this to the repo.

## How this helps

In the spirit of PDD, this allows to keep tasks/issues small and therefore more manageable. This prevents changes of focus, works with multiple programming and markup languages, is open source, very small, and works very fast even on humongous code bases due to massive parallelism.

## Implementation

* Perhaps such a thing already exist?
    - [] Research
* Language:
    - Python
        - (+) There are great YAML libraries
        - (+) Faster to develop
        - (+) Easier to create a plugin system
        - (-) Harder to do parallelism
        - (-) Harder to make it fast
    - Rust
        - (+) Much better parallelism and faster to run
        - (+) More personally educational for the author
        - (-) Slower to develop
        - (?) Is there a library like Python YAML libraries which preserve exact formatting of the document while editing it?
        - (?) Plugin system based on what?
            - JSON-RPC!
* Can one do this at all BTW?
    * Patent [is abandoned](https://patents.google.com/patent/US20120023476A1/en), so yes.
* How do we build integrations with task management systems?
    - Plainly as plugins with standardized API
    - Or somehow via a semantic interaction layer, if that makes sense
        How does it make sense? I have no idea ATM
* How do we integrate with different programming & markup languages?
    - Extract the relevant piece of code,
    - Make account of the function, class, module where the comment is located,
    - Format all this beautifully and insert into the newly created ticket
* Do we care about changes?
    - For example, when we update the puzzle comment, do we then go and update the ticket?
    - How do we make sure we don't overwrite whatever humans have already written there?

## Extensions

* Datadog
    * specify measurement units for metrics
    * create alerts
* Calendars
    * Schedule meetings?
* Octadocs
    * Ingest information into the graph *(hey this might prove interesting as an integration method actually)*
        * **This might shift the whole focus of the tool**
        * This might mean we will use `pytkdocs` to parse stuff
            * but then how to write back??
