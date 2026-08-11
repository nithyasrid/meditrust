from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="meditrust_data_quality",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    validate = BashOperator(
        task_id="validate_patient_data",
        bash_command="python /opt/airflow/pipeline/data_quality.py"
    )

    validate
