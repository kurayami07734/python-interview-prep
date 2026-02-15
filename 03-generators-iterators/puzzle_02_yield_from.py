# QUESTION: What is the output of this code and why?

def sub_generator():
    yield from [1, 2, 3]


def delegating_generator():
    yield from sub_generator()
    yield from [4, 5, 6]


gen = delegating_generator()
print(f"List from generator: {list(gen)}")

print()


def generator_with_return():
    def sub1():
        yield 1
        yield 2
        return "sub1 done"

    def sub2():
        yield 3
        yield 4

    def main():
        result = yield from sub1()
        print(f"Received from sub1: {result}")
        yield from sub2()

    gen = main()
    print(f"List: {list(gen)}")


generator_with_return()
