# QUESTION: What is the output of this code and why?

funcs = [lambda x: x * i for i in range(3)]

for f in funcs:
    print(f(2), end=" ")

print()

funcs_correct = [lambda x, i=i: x * i for i in range(3)]

for f in funcs_correct:
    print(f(2), end=" ")
