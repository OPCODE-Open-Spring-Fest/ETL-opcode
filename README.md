# 📘 ETL Problems – Open Source Learning Project

Welcome to **ETL Problems**, an open-source project designed for learning, experimenting, and contributing to real-world data engineering workflows.

This repository contains a **deliberately broken ETL pipeline** that mimics issues data engineers face daily. The goal is for contributors to **identify, fix, and enhance** the pipeline — while learning best practices in **data extraction, transformation, and loading**.

---

## 🚀 What’s Inside?
The pipeline follows a simple **ETL flow**:

1. **Extract** → Reads data from a CSV file (with encoding fallback).
2. **Transform** → Cleans, deduplicates, and prepares the dataset.
3. **Load** → Stores processed data into an SQLite database (with idempotency).

---

## ⚠️ Find and Fix Issues

These bugs are intentionally introduced and marked in the code with  
`# TODO (Find & Fix): ...`  
Contributors should search for these comments and fix the issues.

### Examples:
- Unused imports
- Incorrect default values
- Wrong file extension checks
- Missing error handling
- Print statements instead of logging
- Missing idempotency in database load
- No duplicate removal in transform
- Missing actual logic in extract/transform/load steps

---

## 🎯 Ways to Contribute

- Fix bugs marked with `# TODO (Find & Fix): ...`
- Improve error handling and logging
- Add tests and validation
- Enhance documentation
- Add new features (scrapers, data quality checks, visualizations)

---

## 🛠 Setup Instructions

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/etl-problems.git
cd etl-problems
pip install -r requirements.txt
python main.py
```

---

## 🧪 Testing

Unit tests can be added in the `tests/` folder.  
Run them with:

```bash
pytest tests/
```

---

## 💡 Tips for Contributors

- Search for `# TODO (Find & Fix): ...` in the codebase.
- Check the [Issues](https://github.com/<your-username>/etl-problems/issues) for tasks and guidance.
- If you find a new bug, open an issue and suggest a fix.
- All contributions, big or small, are welcome!

---

## 📬 Questions?

Open an issue or start a discussion in the repo. Happy hacking!