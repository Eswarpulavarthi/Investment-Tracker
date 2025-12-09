# 📊 Investment Tracker

> **Smart portfolio management made simple.** Track your investments, analyze returns, and optimize your asset allocation with beautiful visualizations and data-driven insights.

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active%20Development-yellow.svg)](#)

---

## 🎯 Problem Statement

Indian investors often juggle multiple investment vehicles—stocks, mutual funds, PPF, fixed deposits, and gold bonds—across different apps and spreadsheets. Without a unified view:
- 📉 Portfolio performance is hard to track
- 📊 Asset allocation remains unclear
- 💡 Investment insights are buried in data
- ⏰ Rebalancing decisions become guesswork

**Investment Tracker** solves this by providing a single, intuitive dashboard to monitor and optimize your entire portfolio.

---

## ✨ Features

### Core Functionality
- ✅ **Portfolio Overview**: List all holdings with quantity, buy price, current value, and profit/loss
- 📈 **Performance Analytics**: Calculate absolute returns, XIRR, and time-weighted performance
- 🎨 **Asset Allocation**: Visual breakdown by category (stocks, mutual funds, fixed deposits, etc.)
- 🎯 **Investment Goals**: Set targets and track progress toward financial milestones
- 📊 **Interactive Dashboards**: Beautiful charts and summaries for quick insights

### Coming Soon 🚀
- Real-time price updates via APIs
- Goal-based rebalancing recommendations
- Tax-loss harvesting alerts
- Sector and instrument diversification analysis
- Export to CSV and PDF reports

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Python 3.9+ |
| **Data** | SQLite / PostgreSQL |
| **Frontend** | Web-based (FastAPI + React) |
| **Visualization** | Plotly / Matplotlib |
| **Deployment** | Docker, AWS/Heroku (planned) |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip or conda

### Installation

```bash
# Clone the repository
git clone https://github.com/Eswarpulavarthi/Investment-Tracker.git
cd Investment-Tracker

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage (CLI)

```bash
# Add a new investment
python src/main.py add-investment --type stock --name "RELIANCE" --qty 10 --buy-price 2500

# View portfolio summary
python src/main.py portfolio --summary

# Generate allocation report
python src/main.py analyze --allocation

# Set investment goal
python src/main.py goal --name "Corpus by 2030" --target 50_00_000 --deadline 2030
```

### Web Interface (Coming Soon)

```bash
# Start the web server
python src/app.py

# Open http://localhost:5000 in your browser
```

---

## 📂 Project Structure

```
Investment-Tracker/
├── src/
│   ├── main.py                 # CLI entry point
│   ├── app.py                  # Web app entry point
│   ├── tracker.py              # Core portfolio logic
│   ├── models/
│   │   ├── investment.py       # Investment data model
│   │   └── portfolio.py        # Portfolio aggregation
│   ├── analytics/
│   │   ├── returns.py          # Return calculations (absolute, XIRR)
│   │   ├── allocation.py       # Asset allocation analysis
│   │   └── goals.py            # Goal tracking
│   ├── utils/
│   │   ├── database.py         # DB operations
│   │   └── config.py           # Configuration
│   └── visualization/
│       ├── charts.py           # Chart generation
│       └── dashboard.py        # Dashboard layouts
├── tests/
│   ├── test_tracker.py
│   ├── test_analytics.py
│   └── test_models.py
├── data/
│   ├── sample_portfolio.json   # Demo data
│   └── schema.sql              # Database schema
├── docs/
│   ├── ARCHITECTURE.md         # System design
│   ├── CONTRIBUTING.md         # Contribution guide
│   └── USER_GUIDE.md           # User documentation
├── requirements.txt            # Python dependencies
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📊 Sample Output

### Portfolio Summary
```
╔════════════════════════════════════════════╗
║           PORTFOLIO OVERVIEW                ║
╠════════════════════════════════════════════╣
║ Total Investment:        ₹5,00,000         ║
║ Current Value:           ₹6,75,000         ║
║ Absolute Gain/Loss:      ₹1,75,000 (+35%)  ║
║ Invested Qty:            12 holdings       ║
╚════════════════════════════════════════════╝

TOP GAINERS
─────────────────────────────────────────────
1. INFY Mutual Fund         +45%  | ₹2,40,000
2. HDFC Bank Stock          +38%  | ₹1,80,000
3. Axis Bank Stock          +28%  | ₹1,20,000
```

### Asset Allocation
```
Asset Class Distribution
├─ Stocks (45%)          ▓▓▓▓▓▓▓▓░░
├─ Mutual Funds (35%)    ▓▓▓▓▓▓░░░░
├─ Fixed Deposits (15%)  ▓▓░░░░░░░░
└─ Gold Bonds (5%)       ▓░░░░░░░░░
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m 'Add your feature'`
4. **Push** to the branch: `git push origin feature/your-feature`
5. **Open** a Pull Request

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for detailed guidelines.

---

## 🗺️ Roadmap

### Phase 1: MVP (Current)
- [ ] Core portfolio tracking (CLI)
- [ ] Basic analytics (returns, allocation)
- [ ] SQLite database integration
- [ ] Unit tests

### Phase 2: Web Interface
- [ ] FastAPI backend
- [ ] React dashboard
- [ ] Real-time price updates
- [ ] User authentication

### Phase 3: Advanced Features
- [ ] Goal-based rebalancing
- [ ] Tax optimization
- [ ] Integration with broker APIs
- [ ] PDF report generation

### Phase 4: Production
- [ ] Docker containerization
- [ ] Cloud deployment (AWS)
- [ ] Mobile app
- [ ] Multi-user support

---

## 📚 Documentation

- [Architecture Guide](docs/ARCHITECTURE.md) – System design and data flow
- [User Guide](docs/USER_GUIDE.md) – Detailed usage instructions
- [API Reference](docs/API.md) – CLI and REST API endpoints
- [Contributing Guidelines](docs/CONTRIBUTING.md) – How to contribute

---

## 💡 Why This Project?

This project combines my passion for **cloud engineering**, **full-stack development**, and **personal finance**. It demonstrates:
- **Python backend development** with clean architecture
- **Data visualization** and analytics
- **Test-driven development**
- **DevOps practices** (Docker, CI/CD)
- **Cloud deployment** (AWS/Heroku)

It's perfect for building your portfolio as a cloud engineer or full-stack developer.

---

## 📝 License

MIT License – See [LICENSE](LICENSE) for details.

---

## 🙌 Support & Feedback

Found a bug? Have an idea? Feel free to:
- 🐛 [Open an issue](https://github.com/Eswarpulavarthi/Investment-Tracker/issues)
- 💬 Start a [discussion](https://github.com/Eswarpulavarthi/Investment-Tracker/discussions)
- ⭐ Star this repo if you found it useful!

---

**Made with ❤️ by [Eswarpulavarthi](https://github.com/Eswarpulavarthi)**

*Last updated: December 2025*
