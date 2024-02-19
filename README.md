# Payload Inspector

Tool used to point tools at to help with payload capturing.

## Problem 
I want to build an API endpoint that accepts a vendor's webhook, they didn't provide a schema.

## Solution
Have them send to this endpoint and check the `app/logs` dir.


# Installing with Poetry
1. `poetry install --no-root`

# Installing with pip
1. `venv of your choice`
2. `pip install -r requirements.txt`

# Running
1. `uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload` or `python app/main.py` (hardcoded 0.0.0.0:8000)
2. Point webhook or do an api call to `<host_ip>:<chosen port>/payload` example; `192.168.1.20:8000/payload`