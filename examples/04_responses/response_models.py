from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
 
app = FastAPI(title="Response Models")
 
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
 
class UserOut(BaseModel):
    username: str
    email: EmailStr
 
user_db: list[dict] = []
 
@app.post("/users", response_model=UserOut)
def create_user(user: UserIn):
    user_db.append(user)
    return user
