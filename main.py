from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from uuid import uuid4, UUID
app = FastAPI()


db: List[User] = [
    User(id=UUID("968ea255-ff90-4be6-b6c5-e82a2f9ddf19"),
         first_name="Aditya",
         last_name="Pawar",
         gender=Gender.male,
         role=[Role.student]),

    User(id=UUID("ea80bb0c-bcf9-4b15-92c4-fb6c08420795"),
         first_name="Alex",
         last_name="Jones",
         gender=Gender.female,
         role=[Role.admin, Role.student]
         )
]


@app.get("/")
def root():
    return {"Hello": "Aditya"}


@app.get("/api/v1/users/")
def fetch_users():
    return db


@app.post("/api/v1/users/")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}
