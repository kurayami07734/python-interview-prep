# QUESTION: What is the output of this code and why?

class A:
    def greet(self):
        return "A"


class B:
    def greet(self):
        return "B"


class C(A):
    def greet(self):
        return "C"


class D(B, C):
    pass


d = D()
print(f"D.greet(): {d.greet()}")
print(f"D.__mro__: {[cls.__name__ for cls in D.__mro__]}")
