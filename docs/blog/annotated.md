---
title: "Annotated[]"
description: "Annotated[] type arrived at Python 3.6 as per PEP 527. It is now getting more use cases."
hide:
    - toc
---

# The power of `Annotated[]` is being unleashed

`Annotated[]` type arrived at Python 3.6 as per [PEP 527](https://peps.python.org/pep-0526/). It is now getting more use cases.

## What is it anyway?

From `mypy` point of view, `Annotated[T, foo, bar, baz, ...]` is strictly equivalent to `T`, its first argument. The remaining arguments can be any Python objects. For instance,

```python
greeting: Annotated[str, 5, ..., [], 'boombadam', float]
```

is valid.

## Why to use it?

To attach additional metadata to type annotations in Python. Even though `mypy` does not care for said metadata, other libraries might make use of it.

## Use Cases

This table is a snapshot of things how they are at the moment of writing this post. Things are going to change.

<table>
    <thead>
        <tr>
            <th>Library declaring the annotation</th>
            <th>Annotation</th>
            <th>Library using the annotation</th>
            <th>Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="6">
                <a href="https://github.com/annotated-types/annotated-types">
                    <code>annotated-types</code>
                </a>
            </td>
            <td>
                <a href="https://docs.pydantic.dev/latest/why/#type-hints">
                    <code>Gt</code> <code>Lt</code> <code>Ge</code> <code>Le</code>
                </a>
                <code>Interval</code>
            </td>
            <td rowspan="9">
                <code>pydantic</code>
            </td>
            <td>&gt; &lt; ⩾ ⩽ and generic interval validators</td>
        </tr>
        <tr>
            <td>
                <code>MinLen</code>
                <code>MaxLen</code>
                <code>Len</code>
            </td>
            <td>Sequence length validators</td>
        </tr>
        <tr>
            <td>
                <code>Timezone</code>
            </td>
            <td>Validate timezone for a datetime value</td>
        </tr>
        <tr>
            <td>
                <code>Predicate</code>
            </td>
            <td>Validate value satisfies a given predicate</td>
        </tr>
        <tr>
            <td>
                <code>GroupedMetadata<code>
            </td>
            <td>Combine multiple annotations into one</td>
        </tr>
        <tr>
            <td>
                <code>…<code>
            </td>
            <td>…</td>
        </tr>
        <tr>
            <td rowspan="3">
                <code>pydantic</code>
            </td>
            <td>
                <a href="https://docs.pydantic.dev/latest/usage/strict_mode/#strict-mode-with-annotated-strict">
                    <code>Strict</code>
                </a>
            </td>
            <td>Validate the value in strict mode</td>
        </tr>
        <tr>
            <td>
                <a href="https://docs.pydantic.dev/latest/usage/types/custom/#composing-types-via-annotated">
                    <code>Field</code>
                </a>
            </td>
            <td>Specify Pydantic validation rules</td>
        </tr>
        <tr>
            <td>
                <code>…<code>
            </td>
            <td>…</td>
        </tr>
        <tr>
            <td>
                <a href="https://github.com/python/typing_extensions/pull/277">
                    <code>typing-extensions</code>
                </a>
            </td>
            <td rowspan="2">
                <code>doc</code>
            </td>
            <td rowspan="2">
                <a href="https://github.com/mkdocstrings/mkdocstrings">
                    mkdocstrings
                </a>
            </td>
            <td rowspan="2">Document a variable, function parameter, or class field</td>
        </tr>
        <tr>
            <td>
                <a href="https://peps.python.org/pep-0727/">
                    <code>typing</code>
                </a>,
                starting at Python 3.13 <em>(if PEP 727 passes)</em>
            </td>
        </tr>
        <tr>
            <td rowspan="4">
                <a href="https://fastapi.tiangolo.com">
                    FastAPI
                </a>
            </td>
            <td>
                <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/?h=annotated#import-query-and-annotated">
                    <code>Query</code>
                </a>
            </td>
            <td rowspan="4">
                FastAPI
            </td>
            <td>Designate this as a query parameter</td>
        </tr>
        <tr>
            <td>
                <a href="https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/?h=annotated#better-with-annotated">
                    <code>Path</code>
                </a>
            </td>
            <td>Designate as a path parameter</td>
        </tr>
        <tr>
            <td>
                <a href="https://fastapi.tiangolo.com/tutorial/extra-data-types/?h=annotated#example">
                    <code>Body</code>
                </a>
            </td>
            <td>Designate as a body parameter</td>
        </tr>
        <tr>
            <td>
                <a href="https://fastapi.tiangolo.com/tutorial/dependencies/?h=annotated#share-annotated-dependencies">
                    <code>Depends</code>
                </a>
            </td>
            <td>Inject a dependency</td>
        </tr>
        <tr>
            <td>
                <a href="https://typer.tiangolo.com">
                    Typer
                </a>
            </td>
            <td>
                <a href="https://typer.tiangolo.com/tutorial/parameter-types/number/">
                    <code>Argument</code>
                    <code>Option</code>
                </a>
            </td>
            <td>
                Typer
            </td>
            <td>
                Designate function parameter as CLI option or argument.
            </td>
        </tr>
    </tbody>
</table>

## Documenting function arguments

One of the cases above I would want to attract your attention to is `doc()` annotation, proposed by [PEP 727](https://peps.python.org/pep-0727/) and best illustrated by an example:

```python
from typing import Annotated, doc


def create_user(
    lastname: Annotated[str, doc("The **last name** of the newly created user")],
    firstname: Annotated[str | None, doc("The user's **first name**")] = None,
) -> Annotated[User, doc("The created user after saving in the database")]:
    """
    Create a new user in the system, it needs the database connection to be already
    initialized.
    """
```

This is another way to document function parameters, in addition to two existing methods:

* in the docstring,
* and via inline comments.

Let's compare those approaches.

!!! info "Scope"
    I am intentionally leaving out other applications of `doc()` — annotation of variables and class fields. I believe that function signature annotations are much more often met in real code than the other use cases and thus will be most substantial to the overall developer experience.

<table>
    <thead>
        <tr>
            <th></th>
            <th>Docstrings</th>
            <th>Inline comments</th>
            <th><code>doc()</code></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <th>Standardized?</th>
            <td>🟡 Google, numpy, and a few more styles exist</td>
            <td>🔴 No</td>
            <td>🟢 Yes, by PEP 727</td>
        </tr>
        <tr>
            <th>Looking at parameter definition, how easy it is to locate its description?</th>
            <td>🟡 One has to scroll to the docstring and find it there</td>
            <td>🟢 Right in place</td>
            <td>🟢 Right in place</td>
        </tr>
        <tr>
            <th>How verbose is function signature?</th>
            <td>🟢 Not verbose</td>
            <td>🔴 Significantly more verbose</td>
            <td>🟡 A bit more verbose</td>
        </tr>
        <tr>
            <th>How verbose is the docstring?</th>
            <td>🔴 Verbose</td>
            <td>🟢 Not verbose</td>
            <td>🟢 Not verbose</td>
        </tr>
        <tr>
            <th>How hard is it to extract parameter documentation programmatically?</th>
            <td>
                🔴 Very hard<br/>
                <small>Support multiple standards and recognize which is used</small>
            </td>
            <td>
                🟡 Moderately hard<br/>
                <small>Forces to extract docs from Python AST</small>
            </td>
            <td>
                🟢 Very easy<br/>
                <small><code>something.__annotations__</code> gets the job done</small>
            </td>
        </tr>
    </tbody>
</table>

## More ideas for annotations

If you have a hammer ⇒ everything around looks like a nail.

<table>
    <tbody>
        <tr>
            <td><code>Annotated[dict, MutatedArgument('Accumulator to store cached `Badabazinga` instances.')]</code></td>
            <td>If argument of a function is mutated in the function, convey that information for documentation and linters. By default functions should not do that; but if they do — this should be very clearly evident.</td>
        </tr>
        <tr>
            <td><code>Annotated[str, TODO('Use an `Enum` instead of a plain string.', ticket='PRJ-123')]</code></td>
            <td>Make `TODO` and `FIXME` markers more semantic and integrate them into project docs. IDE might show this hint every time the user hovers over the annotated value, even at a completely different place in the code.</td>
        </tr>
    </tbody>
</table>

Do you have anything in mind? Feel free to [submit a PR](https://github.com/anatoly-scherbakov/yeti.sh).

## Conclusion

I do not care for increased verbosity that the reliance on `Annotated[]` introduces to type annotations for parameters, fields, and variables, as long as

* repetition is avoided,
* and the annotations provide both proteine- and silicon-based developers with semantically rich information about the code they are reading.

I believe advantages are quite evident.
