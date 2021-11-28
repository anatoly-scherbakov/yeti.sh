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

{{ link(local.rdflib) }} seems to be a de facto standard for knowledge graph management in Python. It is also the easiest method to try playing with KGs in that language: in a few lines of code, you can create a graph in memory.

That will cease to be an acceptable method when you need on-disk persistence, especially for large datasets.

Here, we will try to compare a few knowledge graph engines suitable for use in open source Python projects.

{{ render(local.kg_stores_comparison) }}
