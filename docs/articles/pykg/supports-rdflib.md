---
$context:
    $import: prov
$id: supports-rdflib
title: RDFLib support
$included:
  - $id: rdflib-native-driver
    =: true
    comment: There is a native storage backend for RDFLib, which (theoretically) promises better performance.
  - $id: rdflib-incompatible
    =: false
    comment: The system is principally incompatible with RDFLib.
  - $id: rdflib-via-sparql
    label: SPARQL
    comment: The database exposes a SPARQL endpoint, which can be used to communicate with it from within RDFLib. This method is versatile (compare with SQL access to relational databases) but somewhat limited because RDFLib <code>SPARQLStore</code> and its descendant <code>SPARQLUpdateStore</code> do not support blank nodes.
    rdfs:seeAlso:
      - octa:url: https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.plugins.stores.html#rdflib.plugins.stores.sparqlstore.SPARQLUpdateStore
        label: SPARQLUpdateStore (read-write access)
        position: 2
      - octa:url: https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.plugins.stores.html#rdflib.plugins.stores.sparqlstore.SPARQLStore
        label: SPARQLStore (read only)
        position: 1
exclude_from_blog: true
---

<img src="https://rdflib.dev/images/RDFlib-250.png" style="float: left" />

{{ link(local.rdflib) }} <mark title="Opinion of the author">seems</mark> to be the de facto standard for knowledge graph management in Python. It is also easy to start with: in a few lines of code, one can create an in-memory graph, ingest data and query it.

This is how one may start building their KG oriented Python application, but applications require persistence and scalability - qualities found in mature knowledge graph database management systems.

If a KGMS provides a backend for a `rdflib` the developer can easily migrate from a naive in-memory rdflib solution to a solution backed by the KGMS.

{{ render(local['supports-rdflib']) }}
