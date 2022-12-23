---
title: Apology of the walrus operator
date: 2022-12-22
description: Python walrus operator has been a source of controversy in the community. Let's list a few of its use cases.
---

{{ page.meta.description }}

## Conditions

```python
if (status := subsystem.Something().status).is_success():
    return status
```

## `pytest`

Provide an informative assertion error message in `pytest`.

```python
def test_something():
    assert (
        response := requests.get(...)
    ).json() == {'foo': 'bar'}, response.text
```

## Antipatterns

* ≔ + λ

!!! warning "Linters?"
    What do we have on linters' front about walrus?

## Parallels

* `let` in Rust
* Monads?
