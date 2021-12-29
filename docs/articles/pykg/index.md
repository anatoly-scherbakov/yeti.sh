---
$context:
  $import: table

$id: kg_stores_comparison
title: Choosing a Knowledge Graph management system for a Python app
date: 2021-11-07
author: anatoly

hide:
    - navigation

class: KGStore
columns:
  - table:self
  - supports-rdflib
  - sparql-support
  - source
  - source-updated
  - source-stars
  - source-license
  - python-client
  - python-client-updated
  - python-client-stars
  - python-client-license
  - ui
ordering: octa:title

rdfs:seeAlso:
  - $id: https://en.wikipedia.org/wiki/Comparison_of_triplestores
    label: Comparison of triplestores / Wikipedia
  - $id: https://www.w3.org/2001/sw/wiki/ToolTable
    label: ToolTable / W3C
  - $id: http://www.michelepasin.org/blog/2011/02/24/survey-of-pythonic-tools-for-rdf-and-linked-data-programming/
    label: Survey of Pythonic tools for RDF and Linked Data programming / Michele Pasin

$included:
  - $id: rdflib
    title: rdflib
    octa:url: https://rdflib.dev/ 
---

{{ render(local.kg_stores_comparison) }}
