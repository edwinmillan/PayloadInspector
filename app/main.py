import json
import time
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

log_dir = Path(__file__).resolve().parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)


@app.get("/")
@app.post("/")
async def read_root(request: Request):
    method = request.method
    additional_message = ""
    if method == "GET":
        additional_message = " GET Detected: Use POST"
    raise HTTPException(
        status_code=400,
        detail=f"Did you mean to POST to '/payload'?{additional_message}",
    )


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
    import asyncio

    async def main():
        config = uvicorn.Config("main:app", port=8000, log_level="info", reload=True)
        server = uvicorn.Server(config)
        await server.serve()

    asyncio.run(main())
