# Build a simple router class where you can do @app.route("/path") and it registers a callback.

from typing import Callable, Dict


class App:
    def __init__(self):
        self.routes: Dict[str, Callable] = {}

    def route(self, path: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.routes[path] = func
            return func
        return decorator

    def __call__(self, environ, start_response):
        path = environ.get("PATH_INFO", "/")
        handler = self.routes.get(path)
        
        if handler:
            status = "200 OK"
            body = handler().encode("utf-8")
        else:
            status = "404 Not Found"
            body = b"404 Not Found"
        
        headers = [("Content-Type", "text/plain")]
        start_response(status, headers)
        return [body]

    def run(self, host="127.0.0.1", port=8000):
        from wsgiref.simple_server import make_server
        print(f"Starting server on {host}:{port}")
        server = make_server(host, port, self)
        server.serve_forever()


app = App()


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/about")
def about():
    return "About page"


@app.route("/hello")
def hello():
    return "Hello!"


print("=== Registered routes ===")
for path in app.routes:
    print(f"  {path} -> {app.routes[path].__name__}")

print("\n=== Simulating requests ===")
class MockEnviron:
    def __init__(self, path):
        self._path = path
    
    def get(self, key, default=None):
        if key == "PATH_INFO":
            return self._path
        return default


def mock_start_response(status, headers):
    print(f"  Status: {status}")


for path in ["/", "/about", "/hello", "/missing"]:
    print(f"Request to {path}:")
    result = app(MockEnviron(path), mock_start_response)
    print(f"  Body: {b''.join(result).decode()}")
