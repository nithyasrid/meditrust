# MediTrust — Hospital Data Reliability & Patient Safety Platform

MediTrust is a production-inspired healthcare data reliability platform designed for both Data Engineering and Java Backend/SDE portfolios.

## Architecture

Hospital CSV/JSON data
        ↓
Kafka
        ↓
Spark validation/transformation
        ↓
PostgreSQL (local operational store) / BigQuery (cloud target)
        ↓
Spring Boot REST API
        ↓
Operational dashboard/API consumers

Airflow orchestrates ingestion and validation jobs.

## Core checks
- Duplicate patient detection
- Missing patient fields
- Invalid patient ID / date / age
- Invalid prescription values
- Data-quality scoring
- Pipeline/run monitoring

## Quick start

Requirements:
- Docker Desktop
- Java 17+ (only if running Spring Boot outside Docker)
- Python 3.11+ (only for local scripts)

1. Start infrastructure:
   `docker compose up -d postgres zookeeper kafka`

2. Start the backend:
   `cd services/patient-api`
   `mvn spring-boot:run`

3. Open:
   `http://localhost:8080`
   `http://localhost:8080/api/health`
   `http://localhost:8080/api/patients`
   `http://localhost:8080/api/quality/summary`

4. Run the sample Python data-quality pipeline:
   `python pipeline/data_quality.py`

The local MVP uses PostgreSQL so the project works without cloud credentials. The BigQuery adapter is included as the cloud extension point.
