# OOP Internals

This module explores Python's object-oriented programming internals—how classes actually work under the hood.

## Topics Covered

### MRO (Method Resolution Order)
Python uses C3 linearization to determine the order in which base classes are searched when resolving methods. This becomes critical in diamond inheritance scenarios. The MRO can be viewed via `ClassName.__mro__`.

### Class vs Instance Variables
The distinction between class and instance attributes is subtle but important. Using `self.attr += 1` creates an instance attribute that shadows the class attribute. Mutable class attributes are shared across all instances.

### `__new__` vs `__init__`
`__new__` handles object creation (returning an instance), while `__init__` handles initialization. For implementing singletons, factories, or immutable objects, understanding this distinction is crucial.

## Running the Puzzles

```bash
uv run python 02-oop-internals/puzzle_01_mro_diamond.py
uv run python 02-oop-internals/puzzle_02_class_vs_instance.py
uv run python 02-oop-internals/puzzle_03_new_vs_init.py
```
