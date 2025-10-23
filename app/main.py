from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/add")
def add(a: int, b: int):
    return {"sum": a + b}
