# Payload Inspector

Tool used to point tools at to help with payload capturing.

## Problem 
I want to build an API endpoint that accepts a vendor's webhook, they didn't provide a schema.

## Solution
Have them send to this endpoint and check the `app/logs` dir.


# Installing with Poetry
1. `poetry install`

# Installing with pip
1. `venv of your choice`
2. `pip install -r requirements.txt`

# Running
1. Change info in `hypercorn_config.toml` as needed.
2. `hypercorn -c .\hypercorn_config.toml app.main:app` 
3. Point webhook or do an api call to `<host_ip>:<chosen port>/payload` example; `192.168.1.20:8000/payload`