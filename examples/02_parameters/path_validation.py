from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI(
    title="Path Validation",
    description=(
        "Demonstrates validation and documentation metadata for path"
        "parameters using FastAPI's Path(...)."
    ),
    version="1.0.2",
)


@app.get("/items/{item_id}", tags=["items"])
def get_item(
    item_id: Annotated[int, Path(
        ge=1,
        le=100,
        description="The ID of the item to retrieve",
        examples=[42]
)]):
    
    return {
        "item_id": item_id,
        "kind": type(item_id).__name__
    }