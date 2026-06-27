---
title: Evolution as multilevel learning (Vanchurin et al. 2022)
date: "2026-06-27"
description: Seven principles and ten evolutionary phenomena from Vanchurin, Wolf, Katsnelson & Koonin (PNAS 2022), formalized as linked data.
hide:
  - navigation

"@context":
  - https://json-ld.org/contexts/dollar-convenience.jsonld
  - rdfs: http://www.w3.org/2000/01/rdf-schema#
    schema: https://schema.org/
    dcterms: http://purl.org/dc/terms/
    prov: http://www.w3.org/ns/prov#
    dcterms:requires:
      "@type": "@id"
    prov:wasDerivedFrom:
      "@type": "@id"
    rdfs:isDefinedBy:
      "@type": "@id"

$id: https://doi.org/10.1073/pnas.2120037119
schema:name: Toward a theory of evolution as multilevel learning
$reverse:
  rdfs:isDefinedBy:
    - $id: _:P1
      rdfs:label: P1. Loss function
      rdfs:comment: In any evolving system, there exists a loss function of time-dependent variables that is minimized during evolution.

    - $id: _:P2
      rdfs:label: P2. Hierarchy of scales
      rdfs:comment: Evolving systems encompass multiple dynamical variables that change on different temporal scales (with different characteristic frequencies).

    - $id: _:P3
      rdfs:label: P3. Frequency gaps
      rdfs:comment: Dynamical variables are split among distinct levels of organization separated by sufficiently wide frequency gaps.

    - $id: _:P4
      rdfs:label: P4. Renormalizability
      rdfs:comment: Across the entire range of organization of evolving systems, a statistical description of faster-changing (higher-frequency) variables is feasible through the slower-changing (lower-frequency) variables.

    - $id: _:P5
      rdfs:label: P5. Extension
      rdfs:comment: Evolving systems have the capacity to recruit additional variables that can be utilized to sustain the system and the ability to exclude variables that could destabilize the system.

    - $id: _:P6
      rdfs:label: P6. Replication
      rdfs:comment: In evolving systems, replication and elimination of the corresponding information-processing units (IPUs) can take place on every level of organization.

    - $id: _:P7
      rdfs:label: P7. Information flow
      rdfs:comment: In evolving systems, slower-changing levels absorb information from faster-changing levels during learning and pass information down to the faster levels for prediction of the state of the environment and the system itself.

    - $id: _:E1
      rdfs:label: E1. IPUs
      rdfs:comment: Discrete information-processing units (self-vs. nonself-differentiation and discrimination) exist at all levels of organization.
      dcterms:requires:
        - _:P1
        - _:P2
        - _:P3
        - _:P4
        - _:P5
        - _:P6
        - _:P7

    - $id: _:E2
      rdfs:label: E2. Frustration
      rdfs:comment: Multidimensional and multiscale optimization problems generically lead to frustration from conflicting objectives at different scales.
      dcterms:requires: _:P2

    - $id: _:E3
      rdfs:label: E3. Multilevel hierarchy
      rdfs:comment: The hierarchy of multiple levels of organization is an intrinsic feature of evolving biological systems in structure and in the substrate evolutionary forces act upon.
      dcterms:requires: _:P4
      prov:wasDerivedFrom: _:E2

    - $id: _:E4
      rdfs:label: E4. Near optimality
      rdfs:comment: Stochastic optimization tends to rapidly find local optima and keeps the system in their vicinity, sustaining the loss function at a near-optimal level.
      dcterms:requires: _:P1

    - $id: _:E5
      rdfs:label: E5. Diversity of near-optimal solutions
      rdfs:comment: Solutions on loss-function landscapes span numerous local peaks of comparable heights.
      dcterms:requires:
        - _:P2
        - _:E2

    - $id: _:E6
      rdfs:label: E6. Separation of phenotype from genotype
      rdfs:comment: Dedicated digital information storage media are separated from mostly analog processing devices, with asymmetric information flow from genotype to phenotype.
      dcterms:requires:
        - _:P1
        - _:P2
        - _:P3
        - _:P4
        - _:P5
        - _:P6
        - _:P7

    - $id: _:E7
      rdfs:label: E7. Replication
      rdfs:comment: Copying and sharing genomic information are essential for long-term persistence of IPUs beyond individual lifetimes.
      dcterms:requires: _:P6
      prov:wasDerivedFrom: _:E6

    - $id: _:E8
      rdfs:label: E8. Natural selection
      rdfs:comment: Darwinian evolution arises when distinct IPUs depend on stored information and can copy and share it, producing differential reproduction of genotypes.
      dcterms:requires:
        - _:P1
        - _:P2
        - _:P3
        - _:P4
        - _:P5
        - _:P6
        - _:P7
        - _:E1
        - _:E6
        - _:E7

    - $id: _:E9
      rdfs:label: E9. Parasitism
      rdfs:comment: Parasites and host-parasite coevolution are ubiquitous across biological systems and indispensable for the evolution of life.
      dcterms:requires:
        - _:P5
        - _:P6
        - _:P7
        - _:E5

    - $id: _:E10
      rdfs:label: E10. Programmed death
      rdfs:comment: Programmed (to various degrees) death is an intrinsic feature of life.
      dcterms:requires:
        - _:P4
        - _:P5
        - _:P6
        - _:E8
---

Vanchurin, Wolf, Katsnelson & Koonin propose that biological evolution—including the origin of life—is multilevel learning: seven principles (P1–P7) that make a universe observable, and ten evolutionary phenomena (E1–E10) that follow from them. Primary source: [Toward a theory of evolution as multilevel learning](https://doi.org/10.1073/pnas.2120037119) (PNAS 2022, DOI [10.1073/pnas.2120037119](https://doi.org/10.1073/pnas.2120037119)). Local copy: [PDF](vanchurin-et-al-2022-toward-a-theory-of-evolution-as-multilevel-learning.pdf).

## Principles (P1–P7)

**P1. Loss function.** In any evolving system, there exists a loss function of time-dependent variables that is minimized during evolution.

**P2. Hierarchy of scales.** Evolving systems encompass multiple dynamical variables that change on different temporal scales (with different characteristic frequencies).

**P3. Frequency gaps.** Dynamical variables are split among distinct levels of organization separated by sufficiently wide frequency gaps.

**P4. Renormalizability.** Across the entire range of organization of evolving systems, a statistical description of faster-changing (higher-frequency) variables is feasible through the slower-changing (lower-frequency) variables.

**P5. Extension.** Evolving systems have the capacity to recruit additional variables that can be utilized to sustain the system and the ability to exclude variables that could destabilize the system.

**P6. Replication.** In evolving systems, replication and elimination of the corresponding information-processing units (IPUs) can take place on every level of organization.

**P7. Information flow.** In evolving systems, slower-changing levels absorb information from faster-changing levels during learning and pass information down to the faster levels for prediction of the state of the environment and the system itself.

## Evolutionary phenomena (E1–E10)

Phenomena E1–E7 are generic (learning systems generally); E8–E10 are biological.[^generic]

**E1. IPUs.** Discrete information-processing units (self-vs. nonself-differentiation and discrimination) exist at all levels of organization.

**E2. Frustration.** Multidimensional and multiscale optimization problems generically lead to frustration from conflicting objectives at different scales.

**E3. Multilevel hierarchy.** The hierarchy of multiple levels of organization is an intrinsic feature of evolving biological systems in structure and in the substrate evolutionary forces act upon.

**E4. Near optimality.** Stochastic optimization tends to rapidly find local optima and keeps the system in their vicinity, sustaining the loss function at a near-optimal level.

**E5. Diversity of near-optimal solutions.** Solutions on loss-function landscapes span numerous local peaks of comparable heights.

**E6. Separation of phenotype from genotype.** Dedicated digital information storage media are separated from mostly analog processing devices, with asymmetric information flow from genotype to phenotype.

**E7. Replication.** Copying and sharing genomic information are essential for long-term persistence of IPUs beyond individual lifetimes.

**E8. Natural selection.** Darwinian evolution arises when distinct IPUs depend on stored information and can copy and share it, producing differential reproduction of genotypes.

**E9. Parasitism.** Parasites and host-parasite coevolution are ubiquitous across biological systems and indispensable for the evolution of life.

**E10. Programmed death.** Programmed (to various degrees) death is an intrinsic feature of life.

## Relationship diagram

```mermaid
{{ (docs / 'blog/evolution-as-multilevel-learning/index.md') | as('mermaid') }}
```

## Principle → phenomenon links

| Phenomenon | Predicated on principles |
| --- | --- |
| E1 | P1, P2, P3, P4, P5, P6, P7 |
| E2 | P2 |
| E3 | P4 |
| E4 | P1 |
| E5 | P2 |
| E6 | P1, P2, P3, P4, P5, P6, P7 |
| E7 | P6 |
| E8 | P1, P2, P3, P4, P5, P6, P7 |
| E9 | P5, P6, P7 |
| E10 | P4, P5, P6 |

## Phenomenon → phenomenon links

| Phenomenon | Relationship | Related phenomenon |
| --- | --- | --- |
| E3 | consequence of | E2 |
| E5 | predicated on | E2 |
| E7 | consequence of | E6 |
| E8 | predicated on | E1, E6, E7 |
| E9 | predicated on | E5 |
| E10 | predicated on | E8 |

---

[^generic]: Phenomena E1–E7 are generic—they apply to all learning systems, including purely physical and prebiotic ones. Phenomena E8–E10 belong in the realm of biology; the onset of natural selection (E8) marks the origin of life.
