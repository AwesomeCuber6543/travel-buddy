from fastapi import FastAPI
from app.schemas.auth import UserLogin


app = FastAPI()

@app.post("/login")
def login(user_login: UserLogin):
    print(user_login.email)
    print(user_login.password)


@app.post("/register")
def register(user_register: UserRegister):
    pass
