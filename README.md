# Multi-Tenant API for SaaS in Django

This project provides a robust foundation for building a multi-tenant Software as a Service (SaaS) platform using Django. It supports tenant isolation, scalable architecture, and an intuitive design to accelerate your SaaS development process.

## Features

- **Multi-tenancy Support**: Per-tenant database schema (Schema Isolation).
- **Scalable API Design**: RESTful API with Django REST Framework (DRF).
- **Authentication and Authorization**: JWT-based authentication with support for roles and permissions.
- **Customizable Tenants**: Add tenant-specific configurations and branding.
- **Admin Panel**: A powerful admin interface for managing tenants and their data.
- **Extensible Framework**: Easily extend and customize for your use case.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.9+
- Django 5.0+
- PostgreSQL 13+
- Docker and Docker Compose

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/officialalkenes/multitenant-api.git
cd multitenant-api
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `env\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.in
```

### 4. Configure Environment Variables

Copy the example `.env.example` file to `.env` and configure the variables.

```bash
cp .env.example .env
```

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## Multi-Tenancy Implementation

This project uses the `django-tenants` library for multi-tenancy. By default, it is configured for schema-based multi-tenancy.

### Tenant Management Commands

<!-- - **Create a Tenant**:

  ```bash
  python manage.py create_tenant
  ```

- **Migrate Tenant Schema**:

  ```bash
  python manage.py migrate_schemas
  ``` -->

## API Documentation

API documentation is available via Swagger and Redoc.

- Swagger: `http://127.0.0.1:8000/swagger/`
- Redoc: `http://127.0.0.1:8000/redoc/`

## Docker Setup

### Build and Run Containers

```bash
docker-compose up --build
```

### Stop Containers

```bash
docker-compose down
```

## Folder Structure

```
multitenant-api-django/
├── tenants/                # Tenant-specific apps and configurations
├── core/                   # Core app for common logic and utilities
├── api/                    # API endpoints and views
├── templates/              # HTML templates for web views
├── static/                 # Static files
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
└── docker-compose.yml      # Docker Compose file
```

## Testing

Run the test suite with:

```bash
python manage.py test
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature name'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

<!-- ## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

--- -->

Happy coding!
