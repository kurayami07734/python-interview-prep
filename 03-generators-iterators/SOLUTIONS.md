# Generators & Iterators - Solutions

## Puzzle 1: Yield Basics (`puzzle_01_yield_basics.py`)

**Output:**
```
Created generator, type: <class 'generator'>

--- First iteration ---
Starting generator
Yielding 0
next(gen): 0

--- Second iteration ---
Yielding 1
next(gen): 1

--- Third iteration ---
Yielding 2
next(gen): 2

--- Fourth iteration ---
Generator finished
StopIteration raised!
```

**Explanation:**

Generators are lazy iterators. Code doesn't run until `next()` is called:
1. Creating a generator doesn't execute any code
2. Each `next()` runs until `yield`, pausing at that point
3. After the generator finishes, `StopIteration` is raised

The generator object maintains internal state (local variables, execution pointer).

**Key Takeaway:** Generators are iterators that produce values on-demand, enabling memory-efficient processing of large sequences.

**References:**
- [Python Docs - Generators](https://docs.python.org/3/howto/generators.html)
- [PEP 255 - Simple Generators](https://peps.python.org/pep-0255/)

---

## Puzzle 2: Yield From (`puzzle_02_yield_from.py`)

**Output:**
```
List from generator: [1, 2, 3, 4, 5, 6]

Received from sub1: sub1 done
List: [1, 2, 3, 4]
```

**Explanation:**

`yield from` creates a bidirectional channel between the delegating generator and the sub-generator:
- Values flow from sub-generator to caller
- Exceptions propagate in both directions
- The `return` value from the sub-generator becomes the value of `yield from`

In the second example, `"sub1 done"` is the return value of `sub1()`.

**Key Takeaway:** `yield from` enables generator delegation, simplifying coroutine implementations.

**References:**
- [PEP 380 - Syntax for Delegating to a Subgenerator](https://peps.python.org/pep-0380/)

---

## Puzzle 3: Custom Iterators (`puzzle_03_custom_iterators.py`)

**Output:**
```
Countdown(3): [3, 2, 1]

First 5: [1, 2, 3, 4, 5]
Next 5: [6, 7, 8, 9, 10]
```

**Explanation:**

An iterator must implement:
- `__iter__()`: returns the iterator (usually `self`)
- `__next__()`: returns next value or raises `StopIteration`

The `Countdown` class is both iterable and iterator (same class for `__iter__` and `__next__`).

The `InfiniteCounter` demonstrates a non-terminating iterator - it has no `StopIteration`.

**Key Takeaway:** 
- Iterators produce values one at a time
- Iterables can be used in `for` loops via `iter()`
- Be careful with infinite iterators

**References:**
- [Python Docs - Iterator Types](https://docs.python.org/3/library/stdtypes.html#iterator-types)
