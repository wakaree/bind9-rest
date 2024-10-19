FROM python:3.12.7-slim
ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app

# Prepare system
RUN set +x \
 && apt update \
 && apt upgrade -y \
 && apt install -y --no-install-recommends curl gcc build-essential \
 && apt-get purge --auto-remove -y curl \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install project dependencies
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml /app/
RUN uv sync --no-dev

# Prepare entrypoint
ADD . /app/
RUN chmod +x scripts/*
ENTRYPOINT ["docker-entrypoint.sh"]
