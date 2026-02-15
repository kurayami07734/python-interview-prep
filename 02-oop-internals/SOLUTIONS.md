# OOP Internals - Solutions

## Puzzle 1: MRO - Diamond Inheritance (`puzzle_01_mro_diamond.py`)

**Output:**
```
D.greet(): B
D.__mro__: ['D', 'B', 'C', 'A', 'object']
```

**Explanation:**

Python uses C3 Linearization for Method Resolution Order (MRO). For `class D(B, C)`:
1. Start with D
2. Merge parent MROs respecting inheritance order
3. B comes before C, so B's MRO takes precedence

The MRO for `D(B, C)` is: D → B → C → A → object

Since B appears before C in `D(B, C)`, B's `greet()` is called.

**Key Takeaway:** Python's C3 linearization ensures:
1. Subclasses come before parents
2. Order in `__bases__` is preserved
3. Each class appears only once

**References:**
- [Python Docs - Method Resolution Order](https://docs.python.org/3/howtop/mro.html)
- [PEP 253 - Subclassing Types](https://peps.python.org/pep-0253/)

---

## Puzzle 2: Class vs Instance Variables (`puzzle_02_class_vs_instance.py`)

**Output:**
```
c1: Counter(count=1)
c2: Counter(count=1)
c3: Counter(count=1)
Counter.count: 0

c1: CounterFixed(count=1)
c2: CounterFixed(count=2)
c3: CounterFixed(count=3)
CounterFixed.count: 3
```

**Explanation:**

In the first example, `self.count += 1` creates an *instance attribute* that shadows the class attribute. Each instance has its own `count=1`.

The fix explicitly uses `CounterFixed.count` to modify the class attribute.

**Key Takeaway:** 
- `self.attr += 1` creates instance attribute if it doesn't exist
- Use `ClassName.attr` to modify class attributes
- Mutable class attributes are shared across all instances

**References:**
- [Python Docs - Class and Instance Variables](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)

---

## Puzzle 3: `__new__` vs `__init__` (`puzzle_03_new_vs_init.py`)

**Output:**
```
Creating new instance
Initializing instance
Returning existing instance
Initializing instance
Returning existing instance
Initializing instance
s1 is s2: True
s2 is s3: True
```

**Explanation:**

- `__new__` creates and returns the instance
- `__init__` initializes the instance

In a Singleton pattern, `__new__` returns the same instance each time. Note that `__init__` still runs on every call (even when returning an existing instance).

To prevent re-initialization, check if the instance already exists in `__init__`.

**Key Takeaway:**
- `__new__` is for object creation (factory logic)
- `__init__` is for object initialization
- Always call `super().__new__()` in `__new__`

**References:**
- [Python Docs - __new__](https://docs.python.org/3/reference/datamodel.html#object.__new__)
- [Python Docs - __init__](https://docs.python.org/3/reference/datamodel.html#object.__init__)
