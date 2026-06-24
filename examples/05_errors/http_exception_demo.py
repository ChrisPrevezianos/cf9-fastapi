from fastapi import FastAPI, HTTPException, status
 
app = FastAPI(title="HTTPException")
 
items = {'a':"Apple", "b":"Banana", "c":"Cherry"}
 
@app.get("/items/{key}")
def get_item(key: str):
    if key not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item {key} not found",
            headers={"X-Error": "item-missing"}
        )
    return {
        "key": key,
        "name": items[key]
    }