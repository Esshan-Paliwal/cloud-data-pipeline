# Cloud Data Pipeline: Local CSV to Snowflake with Python ETL and Dashboard

This project implements a complete data pipeline that extracts movie rating data from a CSV file, performs data cleaning and validation using Python, and loads the curated dataset into Snowflake. The repository also includes automated testing using GitHub Actions, a Docker configuration for reproducible execution, and a Streamlit dashboard for basic analytics.

---

## 1. Architecture Overview

Pipeline flow:

Local CSV File → Python ETL → Cleaned DataFrame → Snowflake Table → Streamlit Dashboard

yaml
Copy code

Key components:
- ETL workflow (`src/etl.py`)
- Data cleaning logic (`src/cleaning.py`)
- Snowflake utility functions (`src/snowflake_utils.py`)
- Test suite (`tests/`)
- Continuous Integration workflow (`.github/workflows/`)
- Dashboard application (`dashboard/app.py`)

---

## 2. Features

- End-to-end ETL pipeline that loads structured data into Snowflake.
- Modular project structure suitable for production-oriented development.
- Automated unit testing using pytest.
- Continuous Integration configured through GitHub Actions.
- Optional Docker support for consistent runtime environments.
- Streamlit dashboard for exploratory data analysis.

---

## 3. Technology Stack

- Python 3.11+
- Pandas
- Snowflake Python Connector
- Pytest
- Docker
- Streamlit
- GitHub Actions

---

## 4. Setup Instructions

### 4.1 Clone the repository

```bash
git clone https://github.com/<your-username>/cloud-data-pipeline.git
cd cloud-data-pipeline
4.2 Create and activate a virtual environment
bash
Copy code
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
4.3 Configure environment variables
Create a .env file in the project root:

ini
Copy code
SNOW_ACCOUNT=sn47334.ap-south-1.aws
SNOW_USER=<your_snowflake_username>
SNOW_PASSWORD=<your_snowflake_password>
SNOW_DATABASE=MOVIES_DB
SNOW_SCHEMA=PUBLIC
SNOW_WAREHOUSE=COMPUTE_WH
SNOW_ROLE=ACCOUNTADMIN
5. Running the ETL Pipeline
Use the following command to run the ETL job:

bash
Copy code
python3 src/etl.py
Expected behavior:

The CSV file is loaded.

Data is cleaned and validated.

The output dataset is loaded into Snowflake.

A successful run prints:

nginx
Copy code
ETL completed successfully.
6. Testing and Continuous Integration
Run tests locally:

bash
Copy code
pytest -q
GitHub Actions automatically executes tests on every commit or pull request to maintain code quality.

7. Docker Support (Optional)
Build the Docker image:

bash
Copy code
docker build -t movie-etl .
Run the container:

bash
Copy code
docker run movie-etl
8. Streamlit Dashboard
The dashboard visualizes the loaded data from Snowflake, including distributions of ratings and basic aggregations.

Launch the dashboard:

bash
Copy code
streamlit run dashboard/app.py
9. Potential Enhancements
Add workflow scheduling using Airflow or Prefect.

Integrate with Amazon S3 for cloud-based file ingestion.

Add dbt for Snowflake transformations.

Deploy the Streamlit dashboard as a managed web application.

Implement incremental loads and auditing features.

10. Repository Structure
arduino
Copy code
cloud-data-pipeline/
│
├── src/
│   ├── etl.py
│   ├── cleaning.py
│   ├── snowflake_utils.py
│   └── config.py
│
├── tests/
│   └── test_cleaning.py
│
├── dashboard/
│   └── app.py
│
├── .github/workflows/
│   └── ci.yml
│
├── Dockerfile
├── requirements.txt
├── sample_movie_ratings.csv
└── README.md
End of documentation.
