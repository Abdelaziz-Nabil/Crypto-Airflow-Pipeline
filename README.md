# Crypto Airflow Pipeline

A real-time cryptocurrency data pipeline built with Apache Airflow to extract, transform, and load (ETL) crypto prices from the CoinGecko API into a SQLite database.

## Features
- **Real-Time Data Extraction**: Fetches cryptocurrency prices from the CoinGecko API.
- **ETL Workflow**: Transforms and loads data into a SQLite database.
- **Docker Integration**: Easy setup using Docker and Docker Compose.
- **Automated Scheduling**: Runs daily to keep data up-to-date.

## Prerequisites
- Docker and Docker Compose
- Python 3.8+
- [CoinGecko API Key](https://www.coingecko.com/en/api) (optional for higher rate limits)

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Abdelaziz-Nabil/Crypto-Airflow-Pipeline.git
cd Crypto-Airflow-Pipeline
```

### 2. Configure Environment Variables
Create a .env file:

```bash
AIRFLOW_IMAGE_NAME=apache/airflow:2.10.4
AIRFLOW_UID=50000
```

### 3. Build and Start Containers
```bash
docker-compose up --build
```


### 4. Access Airflow UI
Open http://localhost:8080 and log in with:
```
Username: airflow
Password: airflow
```

### 5. Trigger the DAG
Navigate to the crypto_pipeline DAG.

Click Trigger DAG.

### Project Structure
```
.
├── dags/                   # Airflow DAGs
    └── ETL                  
├── config/                 # Custom config
├── data/                   # Database storage
├── logs/                   # logs files
├── docker-compose.yml      # Docker setup
└── .env                    # Environment variables
```
