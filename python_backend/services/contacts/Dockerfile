
# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Install Poetry
RUN apt-get update \
    && apt-get install -y curl \
    && curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory in the container
WORKDIR /contacts

# Copy pyproject.toml and poetry.lock to the working directory
COPY pyproject.toml poetry.lock /contacts/

# Install dependencies
RUN poetry install --no-root

# Copy the rest of the application code to the working directory
COPY . /contacts

EXPOSE 8000

CMD ["sh", "-c", "poetry run python manage.py migrate && poetry run python manage.py runserver 0.0.0.0:8000"]