# Morphle Assignment — Flask /htop Endpoint

[![last commit](https://img.shields.io/github/last-commit/5h4d0wn1k/morphleassignment)](https://github.com/5h4d0wn1k/morphleassignment)

A minimal Flask application that exposes a single `/htop` web endpoint showing
live server system information: your name, the OS username, current time in the
Asia/Kolkata (IST) timezone, and the real `top -bn1` process output — packaged
for one-command deployment with Docker.

## Why

This is a deliberately small, single-purpose Flask service: a classic
"system-info over HTTP" exercise that combines a simple web framework, the
`top` command at the OS level, and timezone-aware formatting. It is useful as a
straightforward demonstration of building a Dockerized Flask microservice, and
as a lightweight remote system-information probe when run inside a
containerized environment where `procps` provides the `top` binary.

## Features

- **`/htop` endpoint** — returns a styled HTML page with the configured full
  name, the OS username (`os.getenv('USER')`), server time rendered in IST,
  and the full output of `top -bn1`.
- **Timezone-aware timestamps** — converts to `Asia/Kolkata` via `pytz` with
  date, time, timezone, and UTC offset.
- **Dockerized** — `Dockerfile` installs `procps` so `top` works in the
  container; `docker-compose.yml` maps host port `5000`.
- **Graceful error handling** — any exception is logged and returned with HTTP
  500 instead of a silent crash.

## Quickstart

### Run with Docker (recommended)

```bash
docker build -t morphleassignment .
docker run -p 5000:5000 morphleassignment
```

Open `http://localhost:5000/htop`.

### Run with Python

```bash
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000/htop`. The app listens on `0.0.0.0:5000`.

## Project structure

```
app.py              Flask application with the /htop endpoint
Dockerfile          Python 3.9-slim image with procps
docker-compose.yml  Single-service compose config (port 5000)
requirements.txt    Flask, Werkzeug, and pytz
```

## Contributing

Keep the scope: one endpoint, minimal dependencies, reproducible containers.
Pull requests that add features beyond the `/htop` contract should update this
README.

## License

This repository does not currently ship a `LICENSE` file; confirm terms with
the owner before reuse.