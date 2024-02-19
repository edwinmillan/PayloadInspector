import json
import time
from pathlib import Path
from fastapi import FastAPI, HTTPException

app = FastAPI()

log_dir = Path(__file__).resolve().parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)


@app.post("/payload")
async def print_payload(payload: dict):
    try:
        timestamp = int(time.time())
        filename = f"payload_{timestamp}.json"
        filepath = log_dir / filename
        with open(filepath, "w") as file:
            json.dump(payload, file, indent=4)

        print(payload)
        return {"message": f"Payload received: {filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, log_level="info", reload=True)