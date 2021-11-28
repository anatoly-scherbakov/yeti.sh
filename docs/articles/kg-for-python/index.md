---
title: Choosing a Knowledge Graph DB for a Python app
date: 2021-11-07
author: anatoly
hide:
    - navigation
source:
  - https://en.wikipedia.org/wiki/Comparison_of_triplestores
  - https://www.w3.org/2001/sw/wiki/ToolTable
  - http://www.michelepasin.org/blog/2011/02/24/survey-of-pythonic-tools-for-rdf-and-linked-data-programming/
---

When choosing a knowledge graph engine for {{ link(local.octadocs) }} I didn't over-think it and, at the time of writing, the knowledge graph is stored and managed in-memory on the basis of {{ link(local.rdflib) }}. That is usable, but for many other applications of knowledge graphs we *would* still want a real DBMS with persistence on disk, indices and stuff. Here I present a comparison of a few KG storage systems by criteria that I found important for my purposes.

!!! warning "Check this out"
    https://www.w3.org/RDF/ has a few examples and links

{{ render(local.kg_stores_comparison) }}
