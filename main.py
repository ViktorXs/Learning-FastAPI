from fastapi import FastAPI

app = FastAPI()

message = input("Wat ham sie dazu zusagen?: ")


@app.get("/")
async def root():
    return {
        "Message": message
    }


@app.get("/tada")
async def root():
    return {
        "Message": "Hello World from tada"
    }


@app.get("/tada/secret")
async def root():
    return {
        "Message": "Are there any easter eggs?"
    }
