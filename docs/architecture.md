# MediTrust Architecture

## Batch flow
1. Hospital source systems generate patient and operational records.
2. Kafka receives event streams.
3. Spark performs distributed transformation and validation.
4. Airflow schedules and monitors pipelines.
5. Valid records are loaded to BigQuery.
6. Invalid records are routed to a data-quality issue store.
7. Spring Boot exposes operational APIs.
8. Dashboard consumers use quality and reliability metrics.

## Local MVP
The cloud warehouse is represented by PostgreSQL locally so the project can run without GCP credentials.

## BigQuery production extension
Recommended datasets:
- `meditrust_raw`
- `meditrust_clean`
- `meditrust_quality`
- `meditrust_analytics`

Recommended tables:
- `patients`
- `encounters`
- `prescriptions`
- `quality_issues`
- `pipeline_runs`
- `patient_duplicates`
