# QUESTION: What is the output of this code and why?

def generator_range(n):
    print("Starting generator")
    i = 0
    while i < n:
        print(f"Yielding {i}")
        yield i
        i += 1
    print("Generator finished")


gen = generator_range(3)
print(f"Created generator, type: {type(gen)}")

print("\n--- First iteration ---")
print(f"next(gen): {next(gen)}")

print("\n--- Second iteration ---")
print(f"next(gen): {next(gen)}")

print("\n--- Third iteration ---")
print(f"next(gen): {next(gen)}")

print("\n--- Fourth iteration ---")
try:
    print(f"next(gen): {next(gen)}")
except StopIteration:
    print("StopIteration raised!")
