from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Welcome to the demo app"}

@app.get("/new-endpoint")
def read_new_endpoint():
    return {"msg": "This is a new endpoint"}
