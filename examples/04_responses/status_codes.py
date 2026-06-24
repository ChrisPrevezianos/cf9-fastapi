from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI(title="Status Codes")

class Item(BaseModel):
    name: str
    price: float

items_db: dict[int, Item] = {}
counter = 0

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED,)
def create_item(item: Item):
    """Use status.HTTP_201_CREATED for new resources."""
    global counter
    counter += 1
    items_db[counter] = item
    return item