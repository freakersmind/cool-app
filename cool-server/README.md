# Setup development environment

## Prerequisites

* Python 3.7 or newer

## Creating Python Virtual Environment

*nix:
```sh
python3 -m venv env
source env/bin/activate
```

Windows:
```sh
py -3 -m venv env
env\scripts\activate
```

Note: Python Virtual Environment is typically created only once but you need run ```activate``` script every time you launch a new terminal.


## Install dependencies

This needs to be done only once.

```sh
pip install -r requirements-dev.txt
```

# Run locally

*nix:
```sh
chmod +x run_locally
./run_locally
```

Windows (with Git Unix tools in PATH):
```sh
sh run_locally
```

The Flask server is launched and the endpoint is listened in port 5000.

Try with a browser: http://localhost:5000/eservice. It should return:
```json
[
    "1",
    "2",
    "3"
]
```


# Build and Deploy

```sh
sam build
sam deploy
```


# Running as Docker container

```sh
docker-compose -f docker-compose.yml -f docker-compose.local.yml up --build --force-recreate
```
