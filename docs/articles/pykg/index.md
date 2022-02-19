---
$context:
  - $import: table
  - $import: provenance

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
  - release
  - source-stars
  - source-license
  - python-client
  - python-client-updated
  - python-client-stars
  - visualization

ordering: table:self

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

I have created this table to compare a few knowledge graph engines by a few subjectively chosen criteria. They might not be the ones that you would have chosen. For example: I do not believe the number of GitHub stars is the leading criterion to choose a software tool, but I do think their number can inform about how widely known and how well supported the solution is.

At the moment of this writing, I have not used the majority of the listed tools, and the table might contain errors. PRs are very welcome.

{{ render(local.kg_stores_comparison) }}
