# Knowly - Backend Server

A async FastAPI backend server with PostgreSQL database, featuring user authentication and RESTful API endpoints.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Docker and Docker Compose
- pip or poetry

### 1. Clone and Setup
```bash
cd server
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the server directory:
```env
DATABASE_URL=postgresql+asyncpg://postgres:example@localhost:5432/mydb
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXIRE_MINUTES=60
```

### 3. Start Database
```bash
docker-compose up -d
```
This starts:
- PostgreSQL 15 on port 5432
- Adminer (database admin tool) on port 8080

### 4. Run Database Migrations
```bash
alembic upgrade head
```

### 5. Start the Server
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Database Admin**: http://localhost:8080

## 🏗️ Codebase Structure

```
server/
├── app/
│   ├── api/                    # API endpoints and routers
│   │   ├── v1/                # API version 1
│   │   │   ├── auth.py        # Authentication endpoints
│   │   │   └── user.py        # User management endpoints
│   │   └── deps.py            # Dependency injection utilities
│   ├── core/                  # Core application configuration
│   │   ├── config.py          # Settings and environment config
│   │   └── security.py        # JWT token and password hashing
│   ├── crud/                  # Database CRUD operations
│   │   └── user.py            # User database operations
│   ├── db/                    # Database configuration
│   │   ├── base.py            # SQLAlchemy base models
│   │   └── session.py         # Database session management
│   ├── models/                # SQLAlchemy ORM models
│   │   └── user.py            # User database model
│   ├── schemas/               # Pydantic data validation schemas
│   │   └── user.py            # User request/response schemas
│   └── main.py                # FastAPI application entry point
├── alembic/                   # Database migration management
├── requirements.txt            # Python dependencies
├── docker-compose.yml          # Database and adminer services
└── README.md                  # This file
```

## 🛠️ Main Technologies

### **Backend Framework**
- **FastAPI** (v0.104.1) - Modern, fast web framework for building APIs with Python 3.8+
- **Uvicorn** (v0.30.6) - ASGI server for running FastAPI applications

### **Database & ORM**
- **PostgreSQL 15** - Robust, open-source relational database
- **SQLAlchemy 2.0** (v2.0.34) - Modern Python ORM with async support
- **Alembic** (v1.13.2) - Database migration tool for SQLAlchemy
- **asyncpg** (v0.29.0) - Fast PostgreSQL async driver

### **Authentication & Security**
- **python-jose** (v3.3.0) - JWT token implementation
- **passlib** (v1.7.4) - Password hashing with bcrypt
- **python-dotenv** (v1.0.1) - Environment variable management

### **Data Validation**
- **Pydantic** (v1.10.13) - Data validation using Python type annotations

## 🔐 API Endpoints

### Authentication (`/auth`)
- `POST /auth/register` - User registration
- `POST /auth/login` - User login (OAuth2 password flow)

### User Management (`/user`)
- User CRUD operations (defined in user.py)

## 🗄️ Database Schema

### Users Table
- `id` - Primary key (auto-increment)
- `username` - Unique username (50 chars)
- `email` - Unique email (255 chars)
- `hashed_password` - Bcrypt hashed password
- `is_active` - Account status boolean
- `created_at` - Timestamp of account creation

## 🚀 Development

### Running Tests
```bash
# Add pytest to requirements.txt first
pytest
```

### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Code Formatting
```bash
# Add black to requirements.txt first
black app/
```

## 🔧 Configuration

The application uses environment variables for configuration. Key settings:

- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - JWT signing secret
- `ALGORITHM` - JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time

## 🐳 Docker Services

- **PostgreSQL**: Main database running on port 5432
- **Adminer**: Web-based database administration tool on port 8080

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

