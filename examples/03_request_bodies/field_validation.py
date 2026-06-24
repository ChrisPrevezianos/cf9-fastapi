from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, Field
 
app = FastAPI(title="Field Validation")
 
class UserCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=20,
        pattern=r"^[a-z0-9_]+$",
        description="Lowercase letters, numbers and underscores only",
        examples=['john_doe']
    )
    email: EmailStr = Field(
        ...,
        description="A valid email address",
        examples=["me@example.com"]
    )
    age: int = Field(
        ...,
        ge=18,
        le=120,
        description="Must be between 18 and 120",
        examples=[20]
    )
    bio: str | None = Field(
        default=None,
        max_length=500,
        description="Optional short biography with a maximum of 500 characters",
        examples=["Python developer and coffee enthusiast."]
    )

@app.post("/users", summary="Create a user with validated fields", description="...", tags=["users"])
def create_user(user: UserCreate):
    return {
        "ok": True,
        "user": user.model_dump(),
    }