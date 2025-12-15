# Cloud Data Pipeline: Local CSV → Python ETL → Snowflake → Dashboard

This project implements an end-to-end cloud data pipeline using:

- Python (ETL)
- Snowflake (Cloud Data Warehouse)
- GitHub Actions (CI for tests)
- Docker (reproducible environment)
- Streamlit (Analytics Dashboard)

The pipeline loads movie rating data from a CSV file, cleans it, and loads it into Snowflake for analytics and reporting.

---

## 1. Architecture Overview

Local CSV → Python ETL → Clean DataFrame → Snowflake Table → Streamlit Dashboard

yaml
Copy code

### Components:
- **ETL Layer**: `src/etl.py`
- **Cleaning Functions**: `src/cleaning.py`
- **Snowflake Utility Functions**: `src/snowflake_utils.py`
- **Tests**: `tests/`
- **CI Pipeline**: GitHub Actions workflow
- **Dashboard**: `dashboard/app.py`

---

## 2. Features

### ✔ End-to-end working ETL  
Reads CSV → cleans → loads into Snowflake table.

### ✔ Modular & scalable project structure  
Industry-style `src/`, `tests/`, `configs/`.

### ✔ Snowflake warehouse + database integration  
Automatically selects the correct warehouse, database, and schema.

### ✔ GitHub Actions CI  
Runs tests on every push.

### ✔ Docker Support  
Reproducible environment.

### ✔ Streamlit Dashboard  
Visualizes movie rating data stored in Snowflake.

---

## 3. Tech Stack

- Python 3.11+
- Pandas
- Snowflake Python Connector
- pytest
- Docker
- Streamlit

---

## 4. Setup Instructions

### 4.1 Clone the repository

```bash
git clone https://github.com/<your-username>/cloud-data-pipeline.git
cd cloud-data-pipeline
4.2 Create virtual environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
4.3 Create .env file
ini
Copy code
SNOW_ACCOUNT=sn47334.ap-south-1.aws
SNOW_USER=<your-username>
SNOW_PASSWORD=<your-password>
SNOW_DATABASE=MOVIES_DB
SNOW_SCHEMA=PUBLIC
SNOW_WAREHOUSE=COMPUTE_WH
SNOW_ROLE=ACCOUNTADMIN

5. Running the ETL Pipeline
bash
Copy code
python3 src/etl.py
Expected output:

vbnet
Copy code
ETL: Starting pipeline...
Cleaning data...
Loading into Snowflake...
ETL completed successfully.
6. Running Tests (GitHub Actions)
Locally:

bash
Copy code
pytest -q
CI automatically runs tests on GitHub for every push/PR.

7. Docker (Optional)
Build:

bash
Copy code
docker build -t movie-etl .
Run:

bash
Copy code
docker run movie-etl
8. Streamlit Dashboard
Run dashboard locally:
bash
Copy code
streamlit run dashboard/app.py
Dashboard features:

Data preview

Rating distribution

Top movies by rating count

9. Future Improvements
Add Airflow / Prefect orchestration

Add S3 ingestion

Add dbt transformation layer

Deploy Streamlit dashboard online

Add user-level analytics

End of README
