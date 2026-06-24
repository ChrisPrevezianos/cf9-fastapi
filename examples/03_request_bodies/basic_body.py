from fastapi import FastAPI
from pydantic import BaseModel, Field
 
app = FastAPI(title="Request Bodies - Basics")
 
class Item(BaseModel):
    """A Pydantic model that validates incoming JSON"""
    name: str
    price: float
    in_stock: bool = True
    tags: list[str] = Field(default_factory=list)
 
items: list[Item] = []
 
@app.post("/items")
def create_item(item: Item):
    """
    Any Pydantic model used as an argument i read from the JSON body.
    FastAPI vaidates the data and returns 422 if it's invalid.
    """
    items.append(item)
    return {
        "ok": True,
        "item": item
    }

@app.get("/items")
def get_items():
    """Return all items."""
    return {"items": items}