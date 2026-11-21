---
title: Semantic Backbones Crosswalk
description: A crosswalk of semantic backbone modeling constructs.
date: "2026-11-15"
hide:
  - toc
  - navigation
---

# Semantic Backbones <small>:material-walk: Crosswalk</small>

!!! definition "Definition: Semantic backbone"

    A semantic backbone is a shared foundation that defines concepts & relationships, connects them to data, & makes their meaning available across systems.

    ⇐ [Semantic Backbone Council's principles](https://semanticbackbone.ai/principles/ "Derived from")
    {: style="text-align: right;" }

A row suggests a correspondence between constructs that serve similar modeling purposes; it does not assert semantic equivalence.


<table markdown="1">
<thead markdown="1">
<tr markdown="1">
<th markdown="1" scope="col"></th>
<th markdown="1" scope="col">[:simple-netflix: Netflix UDA](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)</th>
<th markdown="1" scope="col">[:simple-palantir: Palantir](https://www.palantir.com/docs/foundry/ontologies)</th>
<th markdown="1" scope="col">[:simple-nvidia: NVIDIA Auto Ontology](https://developer.nvidia.com/topics/ai/agent-knowledge-foundation)</th>
</tr>
</thead>
<tbody markdown="1">
<tr markdown="1">
<td markdown="1">Syntax</td>
<td markdown="1">[RDF](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl)</td>
<td markdown="1">[Foundry UI](https://www.palantir.com/docs/foundry/ontology-manager/overview)<br>[:simple-typescript: TypeScript](https://www.palantir.com/docs/foundry/superrepo/core-concepts#ontology-as-code)</td>
<td markdown="1">[Auto Ontology UI](https://github.com/NVIDIA/auto-ontology)<br>[:simple-yaml: Native YAML<br>Apache Ossie YAML](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/SKILL.md)</td>
</tr>
<tr markdown="1">
<td markdown="1">License</td>
<td markdown="1">[Proprietary](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)</td>
<td markdown="1">[Commercial](https://www.palantir.com/explore/platforms/foundry/ontology/)</td>
<td markdown="1">[Apache 2.0](https://github.com/NVIDIA/auto-ontology/blob/main/LICENSE)</td>
</tr>
</tbody>
<tbody markdown="1">
<tr markdown="1">
<th markdown="1" colspan="4" scope="rowgroup">Entities &amp; relationships</th>
</tr>
<tr markdown="1">
<td markdown="1">Business entity type</td>
<td markdown="1">[`upper:DirectClass`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L30)</td>
<td markdown="1">[Object type](https://www.palantir.com/docs/foundry/object-link-types/object-types-overview)</td>
<td markdown="1">[Term](https://github.com/NVIDIA/auto-ontology/blob/main/auto_ontology/server/models.py#L490-L505)</td>
</tr>
<tr markdown="1">
<td markdown="1">Shared entity contract</td>
<td markdown="1">[:material-help-circle-outline:](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d "A shared entity contract is not established in the UDA overview")</td>
<td markdown="1">[Interface](https://www.palantir.com/docs/foundry/interfaces/interface-overview)</td>
<td markdown="1">[:material-help-circle-outline:](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/references/modeling.md "A shared entity contract is not established in the modeling guide")</td>
</tr>
<tr markdown="1">
<td markdown="1">Attribute</td>
<td markdown="1">[`upper:Attribute`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L39)</td>
<td markdown="1">[Property](https://www.palantir.com/docs/foundry/object-link-types/properties-overview)</td>
<td markdown="1">[Column attribute](https://github.com/NVIDIA/auto-ontology/blob/main/auto_ontology/server/models.py#L561-L579)</td>
</tr>
<tr markdown="1">
<td markdown="1">Relationship</td>
<td markdown="1">[`upper:Relationship`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L56)</td>
<td markdown="1">[Link type](https://www.palantir.com/docs/foundry/object-link-types/link-types-overview)</td>
<td markdown="1">[Relationships between tables](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/references/modeling.md#relationship-contract)</td>
</tr>
<tr markdown="1">
<td markdown="1">Entity identity</td>
<td markdown="1">[`upper:keyedOn`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L31)</td>
<td markdown="1">[Primary key property](https://www.palantir.com/docs/foundry/object-link-types/create-object-type#configure-the-primary-key-and-title-key)</td>
<td markdown="1">[Source database keys](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/references/modeling.md#start-with-the-question-contract)</td>
</tr>
<tr markdown="1">
<td markdown="1">Attach a property to an entity type</td>
<td markdown="1">[`upper:property`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L32)</td>
<td markdown="1">[Property on an object type](https://www.palantir.com/docs/foundry/object-link-types/properties-overview)</td>
<td markdown="1">[Column attributes mapped to a term](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/references/write-api.md#column-attributes)</td>
</tr>
<tr markdown="1">
<td markdown="1">Property value type</td>
<td markdown="1">[`upper:datatype`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L40)</td>
<td markdown="1">[Property base type](https://www.palantir.com/docs/foundry/object-link-types/base-types)</td>
<td markdown="1">[Column attribute datatype](https://github.com/NVIDIA/auto-ontology/blob/main/auto_ontology/server/models.py#L571-L572)</td>
</tr>
<tr markdown="1">
<td markdown="1">Relationship cardinality</td>
<td markdown="1">[`upper:minCount`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L58-L59)<br>[`upper:maxCount`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L58-L59)</td>
<td markdown="1">[Link type cardinality](https://www.palantir.com/docs/foundry/object-link-types/link-type-metadata)</td>
<td markdown="1">[Expected multiplicity in the modeling contract](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/references/modeling.md#relationship-contract)</td>
</tr>
<tr markdown="1">
<td markdown="1">Enumerated values</td>
<td markdown="1">[`upper:Enumeration`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L81-L92)<br>[`upper:EnumValue`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L81-L92)</td>
<td markdown="1">[Enumeration value type constraint](https://www.palantir.com/docs/foundry/object-link-types/value-type-constraints)</td>
<td markdown="1">[Sample values](https://github.com/NVIDIA/auto-ontology/blob/main/auto_ontology/server/models.py#L574); no enumeration constraint found in the public API</td>
</tr>
<tr markdown="1">
<td markdown="1">Display name for an entity</td>
<td markdown="1">[`upper:label`](https://github.com/Netflix-Skunkworks/uda/blob/9627a97fcd972a41ec910be3f928ea7692d38714/uda-intro-blog/onepiece.ttl#L29-L35) labels model terms; the example does not specify instance display names</td>
<td markdown="1">[Title key property](https://www.palantir.com/docs/foundry/object-link-types/create-object-type#configure-the-primary-key-and-title-key)</td>
<td markdown="1">[:material-help-circle-outline:](https://nvidia.github.io/auto-ontology/ "No instance display-name convention found in the public API")</td>
</tr>
</tbody>
<tbody markdown="1">
<tr markdown="1">
<th markdown="1" colspan="4" scope="rowgroup">Data &amp; operations</th>
</tr>
<tr markdown="1">
<td markdown="1">Link to source data</td>
<td markdown="1">[Data container representations<br>Mappings](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)</td>
<td markdown="1">[Object type backing data sources](https://www.palantir.com/docs/foundry/object-link-types/create-object-type)</td>
<td markdown="1">[Terms mapped to columns](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/references/write-api.md#column-attributes)</td>
</tr>
<tr markdown="1">
<td markdown="1">Change an entity</td>
<td markdown="1">[:material-help-circle-outline:](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d "An instance change mechanism is not established in the UDA overview")</td>
<td markdown="1">[Action type](https://www.palantir.com/docs/foundry/action-types/overview)</td>
<td markdown="1">[:material-help-circle-outline:](https://nvidia.github.io/auto-ontology/ "An instance change operation is not established in the public API")</td>
</tr>
<tr markdown="1">
<td markdown="1">Business logic</td>
<td markdown="1">[:material-help-circle-outline:](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d "Executable business logic is not established in the UDA overview")</td>
<td markdown="1">[Functions](https://www.palantir.com/docs/foundry/functions/overview)</td>
<td markdown="1">[SQL attributes](https://github.com/NVIDIA/auto-ontology#how-it-works)</td>
</tr>
<tr markdown="1">
<td markdown="1">Agent access</td>
<td markdown="1">[Observability agents<br>Upper integration planned](https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf)</td>
<td markdown="1">[Ontology MCP](https://www.palantir.com/docs/foundry/dev-toolchain/overview#ontology-mcp)</td>
<td markdown="1">[MCP<br>CLI<br>API](https://github.com/NVIDIA/auto-ontology#auto-ontology)</td>
</tr>
<tr markdown="1">
<td markdown="1">Security</td>
<td markdown="1">[:material-help-circle-outline:](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d "Access controls are not established in the UDA overview")</td>
<td markdown="1">[Ontology permissions](https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions)</td>
<td markdown="1">[Role-based access control](https://github.com/NVIDIA/auto-ontology#key-features)</td>
</tr>
<tr markdown="1">
<td markdown="1">Model exchange</td>
<td markdown="1">[:material-help-circle-outline:](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d "Ontology model import or export is not established in the UDA overview")</td>
<td markdown="1">[:material-help-circle-outline:](https://www.palantir.com/docs/foundry/ontology/overview "Ontology model exchange is not established in the cited overview")</td>
<td markdown="1">[Native YAML<br>Apache Ossie YAML](https://github.com/NVIDIA/auto-ontology/blob/main/skills/nvidia-ontology-management/references/write-api.md#model-interchange)</td>
</tr>
</tbody>
<tbody markdown="1">
<tr markdown="1">
<th markdown="1" colspan="4" scope="rowgroup">Generated artifacts</th>
</tr>
<tr markdown="1">
<td markdown="1">Schemas</td>
<td markdown="1">[:simple-graphql: GraphQL](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)<br>[:simple-apacheavro: Avro](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)</td>
<td markdown="1">[:material-help-circle-outline:](https://www.palantir.com/docs/foundry/dev-toolchain "Schema generation not established in the cited documentation")</td>
<td markdown="1">[:material-help-circle-outline:](https://github.com/NVIDIA/auto-ontology "Schema generation not established in the cited documentation")</td>
</tr>
<tr markdown="1">
<td markdown="1">Code or SDKs</td>
<td markdown="1">[:fontawesome-brands-java: Java API](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)</td>
<!-- vale Vale.Terms = NO -->
<td markdown="1">[:simple-python: Python](https://www.palantir.com/docs/foundry/ontology-sdk/python-osdk)<br>[:fontawesome-brands-java: Java](https://www.palantir.com/docs/foundry/ontology-sdk/java-osdk)<br>[:simple-typescript: TypeScript](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk)</td>
<!-- vale Vale.Terms = YES -->
<td markdown="1">[:material-help-circle-outline:](https://github.com/NVIDIA/auto-ontology "SDK generation not established in the cited documentation")</td>
</tr>
<tr markdown="1">
<td markdown="1">Data containers</td>
<td markdown="1">[Iceberg tables<br>Data Mesh sources](https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d)</td>
<td markdown="1">[:material-help-circle-outline:](https://www.palantir.com/docs/foundry/object-link-types/create-object-type "Data container generation not established in the cited documentation")</td>
<td markdown="1">[:material-help-circle-outline:](https://github.com/NVIDIA/auto-ontology "Data container generation not established in the cited documentation")</td>
</tr>
</tbody>
</table>

