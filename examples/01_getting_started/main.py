from fastapi import FastAPI
 
# Create the FastAPI application instance
app = FastAPI(
    title="Hello FastAPI",
    description="This is our first FastAPI project",
    version="1.0.0"
)
 
@app.get("/")
def read_root():
    """Return a simple greeting message: 'Hello FastAPI!'"""
    return {"message" : "Hello FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Read a single item by its ID.

    The type hint `int` tells FastAPI to:
    1. Validate that item_id is an integer
    2. Convert the string from the URL to an int
    3. Return 422 if validation fails (e.g. /items/abc)
    """
    return {
        "item_id": item_id, 
        "name": f"Item #{item_id}"
    }
