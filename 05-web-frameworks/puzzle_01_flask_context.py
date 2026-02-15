# QUESTION: What is the output of this code and why?

from flask import Flask, g

app = Flask(__name__)


@app.before_request
def before_request():
    g.user = "Alice"
    print(f"Set g.user = {g.user}")


@app.route("/")
def index():
    return f"Hello, {g.user}!"


@app.route("/manual")
def manual():
    try:
        return f"User: {g.user}"
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"


if __name__ == "__main__":
    with app.test_client() as client:
        print("=== Test normal request ===")
        response = client.get("/")
        print(f"Response: {response.data.decode()}")

        print("\n=== Test manual access ===")
        try:
            print(f"g.user = {g.user}")
        except Exception as e:
            print(f"Error accessing g outside request: {type(e).__name__}: {e}")
