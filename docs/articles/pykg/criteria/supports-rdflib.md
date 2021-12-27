---
$id: supports-rdflib
title: RDFLib support
---

{{ link(local.rdflib) }} <mark title="Opinion of the author">seems</mark> to be the de facto standard for knowledge graph management in Python. It is also easy to start with: in a few lines of code, one can create an in-memory graph, ingest data and query it.

This is how one may start building their KG oriented Python application, but applications require persistence and scalability - qualities found in mature knowledge graph database management systems.

If a knowledge graph management system provides a backend for rdflib this provides a fast migration path from a rdflib in-memory prototype to a production system. That's why it is one of the criteria for this comparison.
