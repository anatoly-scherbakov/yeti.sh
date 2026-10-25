# Speaker notes

Five minutes of presentation, then discussion.

## User story

About 50 seconds. The proposal is a coding harness that can query the relationships between familiar development artifacts. This story names a user outcome: an accountant wants CSV invoices to reconcile payments. Acceptance criteria make that outcome checkable.

The document excerpt combines Markdown prose with YAML-LD frontmatter. Its links point to the finance role and audit requirement. The full canonical graph includes the prose and all criteria too. The build generates these views from that one graph. Precise project relations use an illustrative vocabulary, while names, descriptions, and document state reuse Schema.org terms.

## ADR as linked data

About 50 seconds. This is an excerpt illustrating how an ADR could carry linked data. It represents a fictional decided choice, not a decision adopted for this presentation project. The complete example also records the alternative of direct database-adapter access.

The rationale stays readable as Markdown. Frontmatter connects the decision to the boundary it establishes. This borrows from my ADR and semantify workflows: model the decision's meaning and relationships, alongside the prose explaining why it was made.

## Use a repository interface for invoice access

The previous slide shows the machine-readable relationships. This is the same decision's readable body: chosen action, rationale, and considered alternative. Both views come from the canonical example. Spend about 20 seconds here and 30 on the frontmatter slide.

## Architecture as a queryable model

About 45 seconds. The ADR establishes an explicit dependency constraint. ApplicationLayer maps to invoice_demo.application and InfrastructureLayer maps to invoice_demo.infrastructure. The canonical graph stores these module prefixes as well.

The runnable export function imports the InvoiceRepository protocol from the domain module. Tests supply an in-memory implementation from the infrastructure module. This makes the dependency direction visible in both the model and the code.

## A linter checks the boundary

About 45 seconds. This is the core comparison function from the runnable linter. The omitted runner reads the source and forbidden target from the YAML-LD graph, resolves the corresponding application file, and parses its imports through Python's AST.

The imports helper handles absolute import and from-import forms. Relative imports explicitly fail in this small fixture. The check covers static imports in the mapped application module. Dynamic imports and whole-project architectural conformance would require a broader linter. A separate rejection check verifies both a direct forbidden module and a descendant module fail this rule.

## Tests check the story

About 50 seconds. These are two actual test methods. The omitted setUp method creates a repository containing two invoices and an empty audit list for each test. The CSV test selects invoice two and checks the parsed output. The authorization test rejects a guest. A third method in the same file checks the audit event.

Run python3 -m unittest discover -s examples -p test_invoice_export.py -v from the project root. All three tests exercise the included Python fixture. These are local demonstration results, not a claim that a production export system or an ontology-driven harness is complete.

## The harness connects these artifacts

About 40 seconds, then discussion. The individual checks run today. The proposed harness would retrieve their relationships from the graph, use them when planning a change, then execute the checks.

A link to a check definition does not assert that it passed. The harness would need to record the command, source revision, and observed result separately. That integration and result model remain proposed.

We could compare an agent using ordinary instructions and tests with one receiving this graph as additional context. Does it find and respect the relevant requirements? Who maintains the links when code moves or an ADR changes? Those costs belong in the experiment too.
