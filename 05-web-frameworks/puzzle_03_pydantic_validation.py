# QUESTION: What is the output of this code and why?

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str = Field(min_length=1)
    age: int = Field(ge=0)


print("=== String to int coercion ===")
try:
    user1 = User(id="1", name="Alice", age=25)
    print(f"Created user: {user1}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

print("\n=== Passing dict to model ===")
data = {"id": 2, "name": "Bob", "age": 30}
user2 = User(**data)
print(f"Created user from dict: {user2}")

print("\n=== Invalid data ===")
try:
    user3 = User(id=3, name="", age=-5)
    print(f"Created user: {user3}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

print("\n=== Extra fields (default behavior) ===")
try:
    user4 = User(id=4, name="Carol", age=20, extra_field="ignored")
    print(f"Created user: {user4}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")

print("\n=== Strict mode ===")


class StrictUser(BaseModel):
    model_config = {"strict": True}

    id: int
    name: str
    age: int


try:
    user5 = StrictUser(id="5", name="Dave", age=35)
    print(f"Created user: {user5}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
