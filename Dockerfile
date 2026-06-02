# image
FROM python:3.13-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# environment variables
ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Working directory
WORKDIR /app

# Dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync -v --frozen --no-install-project

# virtual environment to the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Run app
CMD python -m src.main