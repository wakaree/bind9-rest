# bind9-rest

## System dependencies
- Python 3.12+
- Docker
- docker-compose
- make
- uv

## Deployment
> Before you start, make sure to rename `.env.dist` to `.env` and configure it!

### Via [Docker](https://www.docker.com/)
- Rename `docker-compose.example.yml` to `docker-compose.yml`
- Run `make app-build` command then `make app-run` to start the app

### Via Systemd service
- Run database migrations with `make migrate` command
- Fill `User` and `WorkingDirectory` fields in `systemd/bind9-rest.example.service` ([» Read more](https://gist.github.com/comhad/de830d6d1b7ae1f165b925492e79eac8)
- Move `systemd/bind9-restt.example.service` to `/etc/systemd/system` directory
- Run `systemctl start bind9-rest` command to start the app
- If you want to start the app on system boot, run `systemctl enable bind9-rest` command

## Development
### Setup environment
- Create virtual environment: `python -m venv .venv`
- Activate virtual environment: `source .venv/bin/activate`
- Install uv: `pip install uv`
- Run `uv sync` to load dependencies
