# The power of `Annotated[]` is being unleashed

I have been thinking of putting additional meta data into Annotated[]. It would seem that this topic is being researched by the community.

There is a very recent [PEP 727 Documentation Metadata in Typing](https://peps.python.org/pep-0727/)

```python
from typing import Annotated, TypedDict, NotRequired, doc


class User(TypedDict):
    firstname: Annotated[str, doc("The user's first name")]
    lastname: Annotated[str, doc("The user's last name")]
```

It is scheduled for 3.13 if it is even being accepted, but [there is already a PR](https://github.com/python/typing_extensions/pull/277) for `typing-extensions` library. Author of this PEP is the author of FastAPI, so I expect at least FastAPI is going to support this.

There is also [annotated-types](https://github.com/annotated-types/annotated-types/) library.

```python
from typing import Annotated
from annotated_types import Gt, Len, Predicate

class MyClass:
    age: Annotated[int, Gt(18)]                         # Valid: 19, 20, ...
                                                        # Invalid: 17, 18, "19", 19.0, ...
    factors: list[Annotated[int, Predicate(is_prime)]]  # Valid: 2, 3, 5, 7, 11, ...
                                                        # Invalid: 4, 8, -2, 5.0, "prime", ...

    my_list: Annotated[list[int], Len(0, 10)]           # Valid: [], [10, 20, 30, 40, 50]
                                                        # Invalid: (1, 2), ["abc"], [0] * 20
```

It only provides the types, with no introspection neither validation. But, this is a prerequisite for pydantic v2, which does understand and use these types.
