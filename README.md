# CQRS Demo Project

A Django-based demonstration of the Command Query Responsibility Segregation (CQRS) pattern, implemented with a product management system.

## Features

- RESTful API for product management
- PostgreSQL database integration
- Docker containerization
- CQRS pattern implementation
- Product inventory tracking

## Prerequisites

- Docker
- Docker Compose

## Tech Stack

- Django 4.2.7
- Django REST Framework 3.14.0
- PostgreSQL 15
- Python 3.x

## Project Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd cqrs_demo
```

2. Start the Docker containers:
```bash
docker-compose up -d
```

3. Run migrations:
```bash
docker-compose exec web python manage.py migrate
```

## Database Configuration

The project uses PostgreSQL with the following default configuration:
- Database: cqrs_demo
- User: postgres
- Password: postgres
- Host: db
- Port: 5432

These settings can be modified in the `docker-compose.yml` file.

## API Endpoints

The application runs on `http://localhost:9000` and provides the following endpoints:

- `/api/` - API root endpoint
- Product management endpoints (detailed documentation coming soon)

## Development

To run the development server:
```bash
docker-compose up
```

To create new migrations:
```bash
docker-compose exec web python manage.py makemigrations
```

To apply migrations:
```bash
docker-compose exec web python manage.py migrate
```

## Project Structure

```
cqrs_demo/
├── cqrs_demo/          # Project settings
├── products/           # Products app
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose configuration
├── manage.py          # Django management script
└── requirements.txt   # Python dependencies
```

## CQRS Pattern Overview

CQRS (Command Query Responsibility Segregation) is an architectural pattern that separates read and write operations for a data store. This separation can maximize performance, scalability, and security.

### Key Concepts

1. **Commands**
   - Write operations that modify state
   - Examples: CreateProduct, UpdateStock, DeleteProduct
   - Can be queued and processed asynchronously
   - Return no data, only success/failure

2. **Queries**
   - Read operations that return data
   - Examples: GetProduct, ListProducts, GetProductStock
   - Always return data but never modify state
   - Can be optimized for specific use cases

### Benefits

- **Scalability**: Read and write workloads can be scaled independently
- **Performance**: Query models can be optimized for specific use cases
- **Security**: Better control over which operations can modify data
- **Flexibility**: Different data models for reading and writing

### Implementation in This Project

Our CQRS implementation separates operations as follows:

**Commands (Write Operations)**
- Create new products
- Update product details
- Modify stock levels

**Queries (Read Operations)**
- Get product details
- List all products
- Search products
- Check stock availability

### Data Flow

```
┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│   Command    │────>│   Command   │────>│    Write     │
│   Request    │     │   Handler   │     │    Model     │
└──────────────┘     └─────────────┘     └──────────────┘
                                               │
                                               │
                                               ▼
┌──────────────┐     ┌─────────────┐     ┌──────────────┐
│    Query     │<────│    Query    │<────│    Read      │
│   Response   │     │   Handler   │     │    Model     │
└──────────────┘     └─────────────┘     └──────────────┘
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
