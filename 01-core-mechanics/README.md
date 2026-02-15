# Core Mechanics

This module explores Python's fundamental behaviors that trip up many developers, even experienced ones.

## Topics Covered

### Mutable Default Arguments
Default arguments in Python are evaluated once at function definition, not at each call. This means mutable defaults persist across invocations, leading to surprising behavior. Always use `None` as the default and create fresh objects inside the function.

### Closures & Late Binding
Python closures capture variables by reference, not by value. When lambdas or nested functions reference loop variables, they see the final value, not the value at creation time. Use default arguments or `functools.partial` to capture current values.

### LEGB Scope
Python resolves names through four scopes: Local, Enclosing, Global, and Built-in. Understanding `global` and `nonlocal` is essential for modifying variables from outer scopes.

## Running the Puzzles

```bash
uv run python 01-core-mechanics/puzzle_01_mutable_defaults.py
uv run python 01-core-mechanics/puzzle_02_closure_late_binding.py
uv run python 01-core-mechanics/puzzle_03_leb_scope.py
```
