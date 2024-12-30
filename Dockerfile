# Use the official Python image as the base image
FROM python:3.12-slim-bullseye

# Set build-time arguments for the project
ARG DJANGO_SECRET_KEY
ARG DJANGO_DEBUG=0
ARG PROJ_NAME="core"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY} \
    DJANGO_DEBUG=${DJANGO_DEBUG} \
    PATH=/opt/venv/bin:$PATH

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        libpq-dev \
        libjpeg-dev \
        libcairo2 \
        netcat \
        && rm -rf /var/lib/apt/lists/*

# Create and activate a virtual environment
RUN python -m venv /opt/venv

# Upgrade pip
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entire project into the container
COPY . .

# Ensure the entrypoint script is executable
RUN chmod +x /app/entrypoint.sh

# Expose the port the app runs on
EXPOSE 8000

# Set the default command to run the entrypoint script
CMD ["/app/entrypoint.sh"]
