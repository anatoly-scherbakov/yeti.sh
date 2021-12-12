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
$included:
    - $id: rdflib
      title: rdflib
      octa:url: https://rdflib.dev/ 
---

{{ link(local.rdflib) }} <mark title="Opinion of the author">seems</mark> to be the de facto standard for knowledge graph management in Python. It is also easy to start with: in a few lines of code, one can create an in-memory graph, ingest data and query it.

This is how one may start building their KG oriented Python application, but applications require persistence and scalability - qualities found in mature knowledge graph database management systems.

{{ render(local.kg_stores_comparison) }}

