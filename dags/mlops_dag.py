from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
import os
import shutil

# Define default arguments for the DAG
default_args = {
    "owner": "admin",
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

# DAG definition
with DAG(
    dag_id="mlops_data_pipeline",
    default_args=default_args,
    description="A DAG to implement MLOps with Apache Airflow",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
) as dag:

    def data_extraction():
        import subprocess
        subprocess.run(["python", "data_extraction.py"], check=True)

    def preprocess_data():
        import pandas as pd

        df = pd.read_csv("data/articles.csv")
        df.dropna(subset=["title", "description"], inplace=True)
        df = df[df["title"].str.strip().astype(bool) & df["description"].str.strip().astype(bool)]
        df.to_csv("data/processed_articles.csv", index=False)

    def dvc_push():
        os.system("dvc add data/processed_articles.csv")
        os.system("dvc push")
        shutil.copy("data/processed_articles.csv.dvc", "repo/data/")
        os.system("git add repo/data/processed_articles.csv.dvc")
        os.system("git commit -m 'Add new processed data version'")
        os.system("git push origin main")

    task_data_extraction = PythonOperator(
        task_id="data_extraction",
        python_callable=data_extraction,
    )

    task_preprocess_data = PythonOperator(
        task_id="preprocess_data",
        python_callable=preprocess_data,
    )

    task_dvc_push = PythonOperator(
        task_id="dvc_push",
        python_callable=dvc_push,
    )

    # Define the task dependencies
    task_data_extraction >> task_preprocess_data >> task_dvc_push
