# Steam Market Watcher (Python)

## Quick Start
```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run
python -m steam_market.cli   # or: python steam_market/cli.py
```

## Project Structure
```
.
├─ steam_market/            # package
│  ├─ __init__.py
│  ├─ cli.py                # CLI entry
│  └─ core.py               # main logic
├─ README.md
├─ LICENSE
├─ requirements.txt
└─ .gitignore
```

## 📝 License
Released under the **MIT License** © 2025 Bogdan Yatsenko.

📦 About the migration
This repository was migrated as part of my Portfolio Refresh. Originally developed locally; during migration I added README, .env.example, Docker/CI, and minor improvements.
