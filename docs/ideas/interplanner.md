---
title: interplanner
---

## Target audience

* Linked Data community,
* Tech-savvy individuals,
* Companies,
* Individuals from the general audience,
* Government agencies,
* the humanity as a whole.

## Problem

When you have a plan, normally the reality never goes exactly as planned. Every kind of random things happen, disrupting the plans of individuals, companies, governments, and the whole of mankind. Planning is extremely difficult to get right.

However, it is still very much necessary for survival on all levels: from an individual to the whole species.

We have huge problems which can't be solved without such a level of planning:

* improve education on a global scale,
* solve the shortage of energy,
* prevent pandemics proactively,
* solve the global climate change,
* from producing waste, go to a closed-cycle economically viable manufacturing system,
* evolve to become an interplanetary species,
* …

These issues will define it whether we survive — or we die out.

In order to make planning useful, our plans need to satisfy the following criteria.

* the planning system of an individual, organization, or the whole human race must include multiple different scenarios of what might happen;
* there must be scenarios on multiple levels: short-term, mid-term, long-term;
* every scenario must be assigned a probability, at least relative and crude, of its coming into existence;
* the scenarios, especially short term ones, must be revised constantly.

We do not have a system that does that, at least, semi-automatically.

## Essence

`interplanner` is a headless planning maintenance system that operates over an `iolanta`-capable semantic graph. That permits to use `iolanta` oracles to retrieve data from sources, and to upload the results of planning to the graph whatever medium it might use.

* Inputs of `interplanner` are semantic data from any kind of source:
    * time tracking records,
    * existing short-term plans manually managed by the person in a tool like Todoist,
    * oracles of neural network systems,
    * financial statements, cost and income estimates,
    * projected events and their frames (min time … max time),
    * wikidata, dbpedia, github, any other information source supported by `iolanta` ecosystem.
* `interplanner` outputs an RDF dataset which encodes (typically very many) scenarios:
    * every scenario is a sequence of events, each tied to time,
    * events might be accompanied by financial information, links to external resources, whatever else,
    * each scenario might be ranked.

!!! info
    Perhaps rename this tool to `scenarist` or `scriptwriter`?

## How is this done?

Judging from the input data, `interplanner` will do the following stages.

1. *Combinatorial explosion.* Given the input data and the time frame to plan for, it will first deduce every scenario that is possible given the input data. This stage will give us a huge number of scenarios.
2. *Selection.* Exclude the scenarios which are impossible.
    * exclude events which are of too low probability over the time span we are planning for,
    * if a scenario contains mutually exclusive events then skip it,
    * if this scenario is conflicting with a plan of another level, skip it,
    * etc.
3. **Optimization.** Rank every scenario according to the optimization function the user has requested.
    * That might be time spent on certain tasks,
    * or achievement of certain goals,
    * or whatever.

As a result of an `interplanner` run we get a semantic graph of scenarios from which we can choose those that we like. Multiple such incarnations can be used in a hierarchical manner. You can't recalculate the global plan for the whole of humanity every day, it's too large; but you can recalculate small pieces of it here and there, and use their integrated results as inputs for the master strategy.

## Vocabulary examples

`interplanner` will very heavily rely upon other systems. For example,
- accounting/financial systems to understand what we can afford,
- legal data to know how much time a person can work and which days are holidays or days off.

In general, something like this can be imagined:

- `requiresTime` to define how long an event or task takes to be completed,
- `hasPreRequisite` to define relationships between tasks,
- `hasProbabililty` defines how possible an event is,
- …

## State of the art

* `Design methods` by G. K. Jones
* Existing Optimization systems, if any
* Discrete optimization methods and strategies

## Evolution

* Octadocs?
    * Can this be an application of Octadocs? How can it be used to improve software project documentation in view of how companies plan their work with task trackers?
    * I do not know at this point.
* iolanta
    * first this will probably be a personal tool,
    * and then it can be expanded to be able to upload scenarios to IPFS and render them from there.
* …
