from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Demo App")


class EchoRequest(BaseModel):
    message: str


class GreetRequest(BaseModel):
    name: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def index():
    return {"app": "demo-app", "version": "1.0"}


@app.post("/echo")
def echo(req: EchoRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="message cannot be empty")
    return {"echo": req.message}


@app.post("/greet")
def greet(req: GreetRequest):
    if not req.name.strip():
        raise HTTPException(status_code=400, detail="name cannot be empty")
    return {"greeting": f"Hello, {req.name}!"}
