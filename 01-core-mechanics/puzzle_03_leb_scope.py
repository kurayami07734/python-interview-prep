# QUESTION: What is the output of this code and why?

x = "global"


def outer():
    x = "outer"

    def inner():
        x = "inner"
        print(f"Inner: {x}")

    def inner_nonlocal():
        nonlocal x
        x = "inner_nonlocal"
        print(f"Inner nonlocal: {x}")

    def inner_global():
        global x
        x = "inner_global"
        print(f"Inner global: {x}")

    inner()
    print(f"Outer after inner: {x}")

    inner_nonlocal()
    print(f"Outer after nonlocal: {x}")

    inner_global()
    print(f"Outer after global: {x}")


outer()
print(f"Global after outer: {x}")
