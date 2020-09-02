from airflow import DAG
from airflow.hooks.base_hook import BaseHook
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.helpers import chain

import datetime as dt
import sys

sys.path.append('/usr/local/airflow/dags/efs')
# Need to set project name to `cityparcel`
from cityparcel.scripts.scrape import scrape_parcel_api

# Connection to Database and API
DATABASE_CONN = BaseHook.get_connection('redb_postgres')
DATABASE_NAME = DATABASE_CONN.schema

default_args = {
    'owner': 'redb',
    'start_date': dt.datetime.now(),
    'concurrency': 1,
    'retries': 0,
    'catchup': False
}

dag = DAG(
    dag_id='CityParcel_API_Scrape',
    default_args=default_args,
    schedule_interval='@monthly'
    )

scrape_city_api = PythonOperator(
    task_id='scrape_city_api',
    python_callable=scrape_parcel_api,
    dag = dag
)

scrape_city_api