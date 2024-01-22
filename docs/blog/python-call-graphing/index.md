---
title: Graph Python calls
alternatives:
  $id: call-graph-libraries
  table:columns:
    - table:self
    - last-updated
    - rejected-because
  table:class:
    $reverse:
      rdf:type:
        - rdfs:label: Python Call Graph
          schema:url: https://github.com/gak/pycallgraph/#python-call-graph
          last-updated: 2018-02-08
          rejected-because: Unmaintained
        - rdfs:label: pyan
          schema:url: https://github.com/davidfraser/pyan
          last-updated: 2021-02-15
          rejected-because: Unmaintained. Crashed for me.
          error-message: |
              File "/home/anatoly/.pyenv/versions/3.11.5/envs/datafold/lib/python3.11/site-packages/pyan/main.py", line 206, in main
                  v = CallGraphVisitor(filenames, logger, root=root)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              TypeError: CallGraphVisitor.__init__() got multiple values for argument 'root'
        - rdfs:label: PyCG
          schema:url: https://github.com/vitsalis/pycg
          last-updated: 2023-11-26
          rejected-because: Archived; also I cannot find how to generate graphical output.
        - rdfs:label: Callgraph
          schema:url: https://github.com/osteele/callgraph
          rejected-because: Is not a static analysis tool, requires decorators on functions.
        - rdfs:label: code2flow
          $id: code2flow
          last-updated: 2023-01-09
          schema:url: https://github.com/scottrogowski/code2flow
decision: code2flow
---

## Context

{{ render("call-graph-libraries") }}

## Decision

{{ render("code2flow") }}
