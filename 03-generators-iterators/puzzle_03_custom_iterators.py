# QUESTION: What is the output of this code and why?

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1


c = Countdown(3)
print(f"Countdown(3): {list(c)}")

print()


class InfiniteCounter:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        return self.current


ic = InfiniteCounter(0)
print(f"First 5: {[next(ic) for _ in range(5)]}")
print(f"Next 5: {[next(ic) for _ in range(5)]}")
