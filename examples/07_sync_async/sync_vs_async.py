import asyncio
import time
from fastapi import FastAPI

app = FastAPI(title="Sync vs Async")

@app.get("/sync")
def sync_endpoint():
    time.sleep(0.1)
    return {"style": "sync"}

@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(0.1)
    return {"style": "async"}