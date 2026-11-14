---
exclude_from_blog: true
---

# An ontology inside a coding harness

Seven slides for the Semantic Backbone Council discussion on 22 October 2026.
The invoice-export example illustrates a proposed approach.

```sh
./j
make serve
```

Open <http://127.0.0.1:8767/index.html?full#idea>. Use the arrow keys to present,
or Escape for the overview. The deck includes local fonts and works offline
from `slides/index.html`.

Edit `templates/index.html.jinja`, `examples/invoice-export.yamlld`, and
`slides/styles.css`, then run `./j` again. The build generates both the deck and
`speaker-notes.md`. Speaker notes also live in each slide's hidden `aside`.

Requires Python 3, Jinja2, PyYAML, and Pygments. This follows the Shower Ribbon format and `j` /
Makefile workflow of `~/projects/streaming-demo`. Vendored Shower assets and
licenses remain under `slides/shower/`. The invoice vocabulary uses example.org
and serves only this presentation.

The build derives the visible excerpt from the canonical YAML-LD graph. The
complete example links a user story, an architecture decision, a dependency
constraint, and check definitions. The included Python fixture, boundary linter,
and tests run locally. The harness integration and recording of results against
source revisions remain proposals. Story and ADR excerpts illustrate document
frontmatter, with views generated from the canonical model.

```sh
python3 examples/check_architecture.py
python3 -m unittest discover -s examples -p test_invoice_export.py -v
```

The boundary linter handles static absolute imports in the mapped application
module. The fixture uses an in-memory repository and audit list.
