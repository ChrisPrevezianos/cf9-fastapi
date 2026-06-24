from fastapi import FastAPI
from enum import Enum
 
app = FastAPI(
    title="Enum Path Parameterss",
    description=(
        "Demostrates how to validate path parameters using Enum"
        "Only specific roles are accepted"
        ),
    version="1.0.1"
)
 
class Role(str, Enum):
    """
    Enum representing the ony valid user roles accepted by the endpoint.
 
    Why inherit from `str` and `Enum`?
    - `Enum` gives us a fixed set of allowed values.
    - `str` makes enum members behave like strin gin many contexts
       which is especially useful for JSON rerialization and FastAPI docs.
   
    Allowed values:
    - admin
    - editor
    - viewer
    """
    admin = "admin"
    editor = "editor"
    viewer = "viewer"
 
@app.get("/users/{role}",
         summary="List users by role",
         description="Accepts only a valid role from Role Enum"
)
def list_users(role: Role):
    return {
        "role" : role,
        "message": f"Listing all {role.value}s"
    }
