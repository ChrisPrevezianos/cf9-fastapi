import asyncio
from pathlib import Path
 
from fastapi import FastAPI, HTTPException
from fastapi.responses import (
    HTMLResponse,
    PlainTextResponse,
    RedirectResponse,
    FileResponse,
    StreamingResponse
)
 
app = FastAPI(title="Custom Reponse Types")
 
@app.get("/hello", response_class=PlainTextResponse)
def hello():
    """Retrun plain text instead of JSON"""
    return "Hello, CF9!"
 
@app.get("/home", response_class=HTMLResponse)
def home():
    html = """
    <html>
        <head><title>Home</title></head>
        <body>
            <h1>Welcome to FastAPI</h1>
            <p>This is an HTML response</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html)
 
 
@app.get("/greet/{name}", response_class=HTMLResponse)
def greet(name: str, title: str | None = None):
    display = f"{title} {name}" if title else name
    html = f"""
    <html>
        <head><title>Greeting</title></head>
        <body>
            <h1>Hello, {display}</h1>
            <p>This is an HTML response</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html)
 
 
@app.get("/go")
def go():
    """Redirect to the Swagger docs"""
    return RedirectResponse("/docs", status_code=307)
 
 
@app.get("/download/{filename}", response_class=FileResponse)
def download(filename: str):
    safe_name = Path(filename).name
    file_path = Path(__file__).parent / safe_name
    if not file_path.is_file():
        raise HTTPException(status_code=404, detail=f"File '{safe_name}' not found")
    return FileResponse(path=file_path, filename=safe_name)
 
@app.get("/stream")
def stream():
    """Stream data line by line (instant)"""
    def generate():
        for i in range(10):
            yield f"Line {i}\n"
    return StreamingResponse(generate(), media_type="text/plain")
 
@app.get("/countdown")
async def countdown():
    """Stream a live countdown - one number per second"""
    async def tick():
        for i in range(10, 0, -1):
            yield f"{i}...\n"
            await asyncio.sleep(1)
        yield "Booooooooooooooom!\n"
    return  StreamingResponse(tick(), media_type="text/plain")
