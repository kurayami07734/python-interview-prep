# Core Mechanics

This module explores Python's fundamental behaviors that trip up many developers.

## Puzzles

### 1. Mutable Default Arguments (`puzzle_01_mutable_defaults.py`)

**Question:** What happens when you use a mutable object as a default argument?

**Answer:**
```
[1]
[1, 2]
[1, 2, 3]

[1]
[2]
[3]
```

**Explanation:**

The first function uses `result=[]` as a default argument. In Python, default arguments are evaluated once at function definition time and shared across all calls. Each call appends to the same list.

The second function creates a new list each time by checking `if result is None`.

**Key Takeaway:** Never use mutable objects as default arguments. Use `None` instead.

**References:**
- [PEP 309 - Partial Function Application](https://peps.python.org/pep-0309/)
- [Python Docs - Default Argument Values](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)

---

### 2. Closure & Late Binding (`puzzle_02_closure_late_binding.py`)

**Question:** Why do all lambdas return the same value?

**Answer:**
```
4 4 4 
0 2 4
```

**Explanation:**

In the first list comprehension, all lambdas capture the *variable* `i`, not its *value*. By the time the lambdas are executed, the loop has finished and `i` equals 2. All lambdas reference the same `i`.

The fix (second example) uses default arguments: `lambda x, i=i: x * i` captures the current value of `i` at each iteration.

**Key Takeaway:** Closures in Python capture variables by reference, not by value. Use default arguments or `functools.partial` to capture values.

**References:**
- [Python Docs - Compound Statements (for)](https://docs.python.org/3/reference/compound_stmts.html#for)
- [PEP 289 - List Comprehensions](https://peps.python.org/pep-0289/)

---

### 3. LEGB Scope (`puzzle_03_leb_scope.py`)

**Question:** How do `global` and `nonlocal` affect variable resolution?

**Answer:**
```
Inner: inner
Outer after inner: outer

Inner nonlocal: inner_nonlocal
Outer after nonlocal: inner_nonlocal

Inner global: inner_global
Outer after nonlocal: inner_nonlocal
Global after outer: inner_global
```

**Explanation:**

Python follows the LEGB rule: Local → Enclosing → Global → Built-in.

- `global` modifies the module-level variable
- `nonlocal` modifies the variable in the nearest enclosing scope (excluding global)

Notice that `global` inside `inner()` doesn't affect the `outer()` function's `x` - it only affects the global scope.

**References:**
- [Python Docs - Scoping and Namespaces](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces)
- [PEP 3104 - Access to Names in Outer Scopes](https://peps.python.org/pep-3104/)
