from pathlib import Path
from fastapi import BackgroundTasks, FastAPI
 
app = FastAPI(title="Background Tasks")
 
LOG_FILE = Path("background_log.txt")
 
def write_log(message: str):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
    print(f" [BG] Logged: {message}")
 
@app.post("/send-email")
def send_email(to: str, bg: BackgroundTasks):
    bg.add_task(write_log, f"Email sent to {to}")
    return {
        "status": "queued",
        "to":to
    }