from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

from ETL.scrape_coinmarketcap import scrape_task
from ETL.transform_crypto import transform_task
from ETL.store_crypto import store_task


# Default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 13),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# Define the DAG
with DAG('crypto_pipeline', default_args=default_args,
         schedule='@hourly',  catchup=False) as dag:

    Extract = PythonOperator(
        task_id = "ExtractCrypto",
        python_callable = scrape_task
    )

    Transform = PythonOperator(
        task_id = "TransformCrypto",
        python_callable = transform_task,
        provide_context=True
    )
    
    Load = PythonOperator(
        task_id = "LoadCrypto",
        python_callable = store_task,
        provide_context=True
    )
    

    # Set the task dependencies using the TaskFlow API
    Extract >> Transform >> Load