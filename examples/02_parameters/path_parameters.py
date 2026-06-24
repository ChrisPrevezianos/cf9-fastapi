from fastapi import FastAPI
 
app = FastAPI(
    title="Pathh Parameters",
    description=(
        "Demonstrates how to validate and handle path parameters"
        "Includes standard integer parameters and catch all path parameters"
    ),
    version="1.0.0"
)
 
@app.get("/users/{user_id}",
         summary="Get a user by numeric ID",
         description=(
             "Accepts a user ID as a path parameter."
         ),
         tags=['users']
)
def get_user(user_id: int):
    """
    Return a user identifier received from the URL path.
    """
    return {
        "user_id": user_id,
        "kind": type(user_id).__name__
    }

@app.get("/files/{file_path:path}", tags=["files"])
def read_file(file_path: str):
    """
    Return the full file path captured from the URL.
    """
    return {
        "file_path": file_path
    }