# QUESTION: What is the output of this code and why?

class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def __repr__(self):
        return f"Counter(count={self.count})"


c1 = Counter()
c2 = Counter()
c3 = Counter()

print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c3: {c3}")
print(f"Counter.count: {Counter.count}")

print()


class CounterFixed:
    count = 0

    def __init__(self):
        CounterFixed.count += 1

    def __repr__(self):
        return f"CounterFixed(count={CounterFixed.count})"


c1 = CounterFixed()
c2 = CounterFixed()
c3 = CounterFixed()

print(f"c1: {c1}")
print(f"c2: {c2}")
print(f"c3: {c3}")
print(f"CounterFixed.count: {CounterFixed.count}")
