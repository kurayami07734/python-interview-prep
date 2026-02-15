# QUESTION: What is the output of this code and why?

from fastapi import FastAPI, Depends

app = FastAPI()


def get_database_return():
    print("[RETURN] Opening database connection")
    db = {"connected": True}
    return db


def get_database_yield():
    print("[YIELD] Opening database connection")
    db = {"connected": True}
    yield db
    print("[YIELD] Closing database connection")


@app.get("/return")
def endpoint_return(db=Depends(get_database_return)):
    print(f"[ENDPOINT] Using db: {db}")
    return {"db": db}


@app.get("/yield")
def endpoint_yield(db=Depends(get_database_yield)):
    print(f"[ENDPOINT] Using db: {db}")
    return {"db": db}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
