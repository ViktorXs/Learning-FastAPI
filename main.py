from fastapi import FastAPI

app = FastAPI()
items = set()

# message = input("Wat haben sie dazu zu sagen?: ")

@app.get("/")
def root():
    return {"Message": "Hello World"}


# @app.get("/special")
# def root():
#     return {"Message": message}


@app.get("/input")
def root():
    text = input("Gib ein, was du willst: ")
    return text


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    """declaring type. item_id is an int"""
    return {"item_id": item_id}


@app.put("/put_item/{item_id}")
async def read_item(item_id: int):
    items.add(item_id)
    return {"items": items}
