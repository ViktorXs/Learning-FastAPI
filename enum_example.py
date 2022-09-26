# predefined values
from fastapi import FastAPI
from enum import Enum


class GetMessage(str, Enum):
    message1 = "FastAPI"
    message2 = "Python"
    message3 = "Coding"


app = FastAPI()


@app.get("/messages/{value}")
async def get_model(value: GetMessage):
    if value is GetMessage.message1:
        return {"value": value, "message": "Fast API rules!"}
    if value is GetMessage.message2:
        return {"value": value, "message": "Python rules a lot"}

    return {"value": value, "message": "Coding FTW!"}
