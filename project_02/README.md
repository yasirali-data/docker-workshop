# 🐍 Dockerized Data Pipeline

A simple Python data pipeline that runs inside Docker using `uv`.

The pipeline takes a day number as an argument, creates a Pandas DataFrame, and saves the result as a Parquet file.

## 🛠️ Technologies

- Python 3.13
- Pandas
- PyArrow
- uv
- Docker
- Parquet

## 🚀 Run the Project

Build the Docker image:

```bash
docker build -t project-02 .

Run the pipeline:
docker run --rm -v "$(pwd):/app" project-02 1

Change 1 to run the pipeline for another day:
docker run --rm -v "$(pwd):/app" project-02 5

This generates:
output_day_5.parquet

📌 What It Does
. Takes a day number as input
. Creates a Pandas DataFrame
. Displays the data
. Saves the result as a Parquet file

📁 Structure
project_02/
├── pipeline.py
├── Dockerfile
├── pyproject.toml
├── uv.lock
├── .python-version
├── src/
└── README.md

👨‍💻 Author
Yasir Ali