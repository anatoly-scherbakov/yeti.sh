---
title: Apology of the walrus operator
date: "2022-12-22"
description: Python walrus operator has been a source of controversy in the community. Let's list a few of its use cases.
hide:
    - navigation
    - toc
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

## List comprehensions

Transform the iterating value and filter by it.

```python
popular_repos = [
    name
    for repo in github_api_response
    if (name := repo['name']) and repo['stargazers_count'] > 100
]
```

## Antipatterns

* ≔ + λ

!!! warning "Linters?"
    What do we have on linters' front about walrus?

## Parallels

* `let` in Rust
* Monads?
