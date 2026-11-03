FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.6 /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    PATH="/code/.venv/bin:$PATH"

WORKDIR /code

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

COPY . /code

ENV SECRET_KEY="pIxGEKUKWaMsIbCyGxwwvpqrxyX8taWHpI3ajJ8Z6QHNaKWPMT"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
