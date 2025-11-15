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

### Local Setup

Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/etl-problems.git
cd etl-problems
pip install -r app/requirements.txt
python -m app.main
```

### Running with Docker

Containerize the ETL pipeline for a consistent, isolated development environment across all machines.

**Prerequisites:** Docker and Docker Compose must be installed on your system.

**Quick Start:**

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/etl-problems.git
cd etl-problems
```

2. Run the pipeline in a container:
```bash
docker-compose up
```

This command will:
- Build the Docker image from the provided `Dockerfile`
- Start the ETL pipeline in an isolated container
- Mount your local code directory as a volume, so changes you make to the code are immediately reflected in the container

**Rebuilding the Image:**

If you update dependencies in `requirements.txt`, rebuild the image:
```bash
docker-compose up --build
```

**Interactive Mode:**

To run commands interactively inside the container:
```bash
docker-compose run etl bash
```

Then inside the container, you can run:
```bash
python -m app.main
python -m pytest tests/
```

**Stopping the Container:**

```bash
docker-compose down
```

**Benefits:**
- 🎯 **Consistency**: Same environment for all developers (Python 3.10, all dependencies)
- 📦 **Isolation**: No conflicts with local Python installations
- 🚀 **Reproducibility**: Works the same on Windows, macOS, and Linux
- 🔧 **Hot Reload**: Code changes are immediately reflected without rebuilding
- 🧪 **Testing**: Run tests in an isolated environment

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