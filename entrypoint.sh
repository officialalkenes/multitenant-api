#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Set the Django settings module environment variable
export DJANGO_SETTINGS_MODULE=core.settings

# Function to wait for the PostgreSQL database to be ready
wait_for_db() {
    echo "Waiting for PostgreSQL to be ready at $DB_HOST:$DB_PORT..."
    while ! nc -z $DB_HOST $DB_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL is ready."
}

# Collect static files
collect_static() {
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
}

# Apply database migrations
apply_migrations() {
    echo "Applying database migrations..."
    python manage.py migrate --noinput
}

# Start the Gunicorn server
start_server() {
    echo "Starting Gunicorn server..."
    gunicorn core.wsgi:application --bind 0.0.0.0:8000
}

# Execute functions
wait_for_db
collect_static
apply_migrations
start_server
