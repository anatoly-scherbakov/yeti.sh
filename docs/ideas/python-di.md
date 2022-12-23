---
title: Python Dependency Injection
---

## Target audience

Python software developers.

## Essence

```python
from depend import Depends

class OrientDB:
    def query(self, text: str):
        ...
    
    ...


def retrieve_settings_from_graph(orient_db: OrientDB = Depends(OrientDB)) -> Settings:
    orient_db.query(...)


def reply_to_user_request(
    settings: Settings = Depends(retrieve_settings_from_graph),
):
    ...
```

In this snippet, `Depends()` should magically resolve to the `OrientDB` instance in runtime, or it calls `retrieve_settings_from_graph` function. 

Moreover, if multiple instances of dependable objects are used they will be only instantiated once during the runtime of the process because the library maintains a registry of cached dependencies.


## State of the art

### Existing DI libraries for Python

!!! error "TODO"
    A survey of alternatives is necessary here. Maybe such a library does already exist?

* `proofit404/dependencies`
* `python-inject`
* https://github.com/Neoteroi/rodi
* https://github.com/ets-labs/python-dependency-injector
* https://github.com/bobthemighty/punq

### Similar things

* pytest fixtures are very similar.

### More concerns

* What if we provide just string path to the object instead of importing it, in certain cases?
* Can DI be used to redefine configuration options or parameters in installed Jeeves plugins?

## Implementation details

* Can be probably done using `__new__` or something.
* The repository of objects is essentially a global registry, I do not know whether that is a good thing. A question to research.
