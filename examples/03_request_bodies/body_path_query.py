from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI(title="Body + Path + Query")
 
class Item(BaseModel):
    name: str
    price: float
    is_stock: bool = True
 
# PUT / /items/7?notify=true
 
@app.put("/items/{item_id}")
def update_item(
    item_id: int,           # path parameter
    item: Item,             # JSON body (Pydantic model)
    notify: bool = False    # query parameter
):
    return {
        "item_id": item_id,
        "item": item,
        "notify": notify
    }