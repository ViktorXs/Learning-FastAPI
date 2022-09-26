from fastapi import FastAPI

app = FastAPI()

message = input("Wat ham sie dazu zusagen?: ")


@app.get("/")
def root():
    return {"Message": "Hello World"}


@app.get("/special")
def root():
    return {"Message": message}


@app.get("/input")
def root():
    text = input("Gib ein, was du willst: ")
    return text
