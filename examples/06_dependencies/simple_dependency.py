from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
 
app = FastAPI(title="Simple Dependencies")
 
fake_items = [{"name": f"Item {i}"} for i in range(100)]
fake_users = [{"name": f"USer {i}"} for i in range(100)]
 
# @app.get("/items")
# def list_items(skip: int = 0, limit: int = 10):
#     return fake_items[skip : skip + limit]
 
# @app.get("/users")
# def list_users(skip: int = 0, limit: int = 10):
#     return fake_users[skip : skip + limit]
 
def pagination(skip: int = 0, limit: int = 10):
    """A reusable dependency that extracts pagination parameters"""
    return {"skip": skip, "limit": limit}
 
# Create a type alias for cleane signatures
# dict as defined above (pagination function return a dict)
Page = Annotated[dict, Depends(pagination)]
 
@app.get("/items")
def list_items(page: Page):
    return fake_items[page["skip"] : page["skip"] + page["limit"]]
 
fake_products = [{"name": f"Product {i}", "category": "electronics" if i % 2 == 0 else "clothing"} for i in range(100)]
 
@app.get("/products")
def list_products(page: Page, category: str | None = None):
    results = fake_products
    if category:
        results = [p for p in results if p["category"] == category]
    return results[page["skip"] : page["skip"] + page["limit"]]
 
@app.get("/search/{collection}")
def search(collection: str, page: Page, q: str):
    """
    Search a collection, by name with pagination.
    """
    collections = {
        "items": fake_items,
        "users": fake_users,
        "products": fake_products
    }
    if collection not in collections:
        raise HTTPException(status_code=404, detail=f"Unknown collection: {collection}")
    matches = [d for d in collections[collection] if q.lower() in d["name"].lower()]
 
    return matches[page["skip"] : page["skip"] + page["limit"]]