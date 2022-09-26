from fastapi import FastAPI

app = FastAPI()
items = dict()
users = dict()
current_user = dict({0: "Viktor"})
site_owner = dict({0: "Max Mustermann"})


# Just routes
# @app.get("/")
# def root():
#     return {"Message": "Hello World"}
#
#
# @app.get("/input")
# async def root():
#     text = input("Gib ein, was du willst: ")
#     return text


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.put("/put_item/{item_key},{item_value}")
async def read_items(item_key: str, item_value: int):
    items.update({item_key: item_value})
    return [items]


# fixed paths should be declared before path operations
# fixed
@app.get("/users/me")
async def get_user_me():
    return [current_user]


# path params
@app.get("/users/{user_id},{user_value}")
async def get_users(user_id: int, user_value: str):
    users.update({user_id: user_value})
    return [users]


@app.get("/imprint/owner")
async def get_site_owner():
    return site_owner


@app.get("/imprint/{site_owner_id},{site_owner_name}")
async def get_site_owner(site_owner_id: int, site_owner_name: str):
    site_owner.update({site_owner_id: site_owner_name})
    return site_owner

