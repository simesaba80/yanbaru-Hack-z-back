FROM python:3.12.6-alpine3.20
# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN apk add --no-cache python3 py3-pip \
    && pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false \
    &&poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY ./backend/ /app

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "uvicorn", "main:app", "--port", "8000", "--reload", "--host", "0.0.0.0"]