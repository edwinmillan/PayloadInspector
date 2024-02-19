import json
import pendulum
from pathlib import Path
from fastapi import FastAPI, HTTPException

app = FastAPI()

log_dir = Path(__file__).resolve().parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)


@app.post("/payload")
async def print_payload(payload: dict):
    try:
        timestamp = pendulum.now().int_timestamp
        filename = f"payload_{timestamp}.json"
        filepath = log_dir / filename
        with open(filepath, "w") as file:
            json.dump(payload, file, indent=4)

        print(payload)
        return {"message": f"Payload received: {filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
