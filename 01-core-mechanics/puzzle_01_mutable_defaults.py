# QUESTION: What is the output of this code and why?

def append_to_list(value, result=[]):
    result.append(value)
    return result


print(append_to_list(1))
print(append_to_list(2))
print(append_to_list(3))

print()

def append_with_none(value, result=None):
    if result is None:
        result = []
    result.append(value)
    return result


print(append_with_none(1))
print(append_with_none(2))
print(append_with_none(3))
