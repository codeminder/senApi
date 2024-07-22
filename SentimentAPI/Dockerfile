FROM python:3.10-slim

# Copy the application files
COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy aiofiles jinja2 transformers torch

# Set environment variable to allow hot-reloading
ENV PYTHONUNBUFFERED=1

# Command to run the application in debug mode with hot-reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]