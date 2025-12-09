# Investment Tracker - Architecture Guide

## System Overview

Investment Tracker is a modular, full-stack application designed for managing and analyzing investment portfolios. It follows a clean architecture pattern with clear separation of concerns.

## Architecture Layers

### 1. **Presentation Layer** (CLI & Web)
- **CLI**: Click-based command-line interface for power users
- **Web**: React frontend with FastAPI backend (Phase 2)
- Handles user input and displays results

### 2. **Business Logic Layer**
- Portfolio management (add, remove, update investments)
- Analytics engines (returns, allocation, goals)
- Data validation and calculations

### 3. **Data Access Layer**
- SQLAlchemy ORM for database operations
- Portfolio data models
- Transaction history

### 4. **Database Layer**
- SQLite for development
- PostgreSQL for production
- Normalized schema for investments and portfolios

## Module Breakdown

```
src/
├── main.py                 # CLI entry point
├── app.py                  # Web app (FastAPI)
├── tracker.py              # Core portfolio logic
├── models/
│   ├── investment.py       # Investment data model
│   └── portfolio.py        # Portfolio aggregation
├── analytics/
│   ├── returns.py          # Return calculations (XIRR, absolute)
│   ├── allocation.py       # Asset allocation analysis
│   └── goals.py            # Goal tracking logic
├── utils/
│   ├── database.py         # ORM and DB operations
│   └── config.py           # Configuration management
└── visualization/
    ├── charts.py           # Plotly/Matplotlib charts
    └── dashboard.py        # Dashboard layouts
```

## Data Flow

```
User Input (CLI/Web)
    ↓
Validation (Input validators)
    ↓
Business Logic (Analytics engines)
    ↓
Data Access (SQLAlchemy models)
    ↓
Database (SQLite/PostgreSQL)
    ↓
Visualization (Charts & outputs)
```

## Key Design Patterns

1. **MVC Pattern**: Clear separation between models, controllers (Click commands), and views
2. **Repository Pattern**: Database access through abstraction
3. **Factory Pattern**: Investment object creation
4. **Observer Pattern**: Goal progress tracking

## Technology Stack

| Component | Technology |
|-----------|------------|
| CLI | Click 8.1+ |
| Web Framework | FastAPI 0.109+ |
| Database | SQLAlchemy 2.0+ |
| Data Processing | Pandas 2.1+ |
| Visualization | Plotly 5.18+, Matplotlib 3.8+ |
| Frontend | React (Phase 2) |
| Testing | Pytest 7.4+ |
| Code Quality | Black, Flake8, Pylint |

## Database Schema (MVP)

### Investments Table
```sql
CREATE TABLE investments (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    name VARCHAR(100),
    type VARCHAR(50),  -- stock, mutual_fund, fd, gold_bond
    quantity FLOAT,
    buy_price DECIMAL(10, 2),
    current_price DECIMAL(10, 2),
    purchase_date DATE,
    notes TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

## Scalability Considerations

### Current (MVP)
- Single-user SQLite database
- CLI-based interface
- Manual portfolio updates

### Phase 2
- Multi-user support with authentication
- PostgreSQL for concurrency
- Real-time price API integration
- Web dashboard with responsive design

### Phase 3+
- Microservices architecture
- Message queue for async processing
- caching layer (Redis)
- Mobile app (React Native)

## Development Workflow

1. **Local Development**: SQLite + CLI
2. **Testing**: Pytest with mocked database
3. **Staging**: PostgreSQL + FastAPI + React
4. **Production**: Containerized (Docker) on cloud (AWS/Heroku)

## API Design (Phase 2)

### REST Endpoints
- `POST /api/investments` - Add investment
- `GET /api/investments` - List investments
- `PUT /api/investments/{id}` - Update investment
- `DELETE /api/investments/{id}` - Remove investment
- `GET /api/portfolio/summary` - Get summary
- `GET /api/analytics/allocation` - Asset allocation
- `GET /api/goals` - List goals

## Security Considerations

- Input validation on all endpoints
- SQL injection prevention via ORM
- Password hashing for user authentication (Phase 2)
- HTTPS for web interface
- Encryption for sensitive data at rest

## Performance

- Database indexing on frequently queried columns
- Caching of computed analytics
- Pagination for large datasets
- Lazy loading of related data

## Future Enhancements

1. **Real-time Updates**: WebSocket integration
2. **AI-Powered Insights**: ML models for portfolio recommendations
3 **Multi-currency Support**: Handle different currencies
4. **Tax Optimization**: Automated tax-loss harvesting suggestions
5. **Social Features**: Portfolio sharing and benchmarking
