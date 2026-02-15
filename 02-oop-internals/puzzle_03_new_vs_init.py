# QUESTION: What is the output of this code and why?

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Creating new instance")
        else:
            print("Returning existing instance")
        return cls._instance

    def __init__(self):
        print("Initializing instance")


s1 = Singleton()
s2 = Singleton()
s3 = Singleton()

print(f"s1 is s2: {s1 is s2}")
print(f"s2 is s3: {s2 is s3}")
