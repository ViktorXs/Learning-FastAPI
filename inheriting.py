from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int | None = -1
    first_name: str | None = "unknown first name"
    second_name: str | None = "unknown second name"
    joined: date | None = "unknown date"


user_data = [
    {
        "id": 2,
        "first_name": "Peter",
        "second_name": "Pan",
        "joined": "2020-1-30"
    },
    {
        "id": 3,
        "first_name": "Pantoffelpeter",
        "second_name": "",
        "joined": "1999-5-13"
    },
]

uber_user: User = User(id=1, first_name="Viktor", second_name="Maier", joined="2022-12-24")
first_user: User = User(**user_data[0])
second_user: User = User(**user_data[1])
unknown: User = User()

print()
print(uber_user)
print(uber_user.id)
print(uber_user.first_name)
print()
print(first_user)
print(first_user)
print()
print(second_user)
print(second_user)
print()
print(unknown)
