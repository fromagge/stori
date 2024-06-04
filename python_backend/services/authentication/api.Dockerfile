# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install Poetry
RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /authentication

# Copy pyproject.toml and poetry.lock to the working directory
COPY pyproject.toml poetry.lock /authentication/

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the working directory
COPY . /authentication

EXPOSE 5001

# Define environment variable
ENV FLASK_APP=run.py

CMD ["sh", "-c", "poetry run alembic upgrade head && poetry run flask run --host=0.0.0.0"]
