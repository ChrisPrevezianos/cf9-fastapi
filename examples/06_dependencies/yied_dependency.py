import time
from typing import Annotated
 
from fastapi import Depends, FastAPI
 
app = FastAPI(title="Yield Dependencies")
 
class FakeDatabase:
    def __init__(self):
        print("[DB] Openning connection")
        time.sleep(1)
        print("[DB] Connection opened")
   
    def query(self, sql: str):
        print(f"[DB] Running query: {sql}")
        time.sleep(1)
        print("[DB] Query completed")
        return f"Result of: {sql}"
   
    def close(self):
        print("[DB] Clossing connection...")
        time.sleep(1)
        print("[DB] Connection closed")
 
def get_db():
    print("\n" + "=" * 51)
    print("Step 1. SETUP - creating the resouce")
    print("=" * 51)
    db = FakeDatabase()
 
    try:
        print("\nStep 2. Yield - handling resource to the endpoint")
        print("=" * 51)
        yield db
    finally:
        print("\nStep 3. TEARDOWN - cleaning the resource")
        print("=" * 51)
        db.close()
        print("=" * 51)
   
 
@app.get("/data")
def read_data(db: Annotated[FakeDatabase, Depends(get_db)]):
    print("[ENDPOINT] Using db inside the endpoint")
    result = db.query("SELECT * FROM items")
    print("[ENDPOINT] Sending the response to client...")
    time.sleep(0.5)
    return {"result": result}