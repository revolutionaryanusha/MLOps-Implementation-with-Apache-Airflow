# MLOps-Implementation-with-Apache-Airflow
Implement Apache Airflow to automate data extraction, transformation, and version-controlled storage.
# MLOps Implementation with Apache Airflow



## Tasks
1. **Data Extraction:**
   - Utilize dawn.com and BBC.com as data sources.
   - Extract links and article information from their homepages.

2. **Data Transformation:**
   - Preprocess the extracted text data for further analysis.

3. **Data Storage & Version Control:**
   - Store the processed data on Google Drive using DVC.

4. **Apache Airflow DAG Development:**
   - Write an Airflow DAG to automate the extraction, transformation, and storage process.


1. Airflow DAG script.
2. Documentation of preprocessing steps and DVC setup.
3. Brief report detailing workflow and challenges.

## Installation Instructions
1. Create a virtual environment and activate it.
    ```bash
    conda create -n mlops_airflow python=3.9 -y
    conda activate mlops_airflow
    ```

2. Install dependencies.
    ```bash
    pip install -r requirements.txt
    ```

3. Initialize Apache Airflow & DVC.
    ```bash
    export AIRFLOW_HOME=$(pwd)/airflow
    airflow db init
    airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

    dvc init
    ```

4. Configure DVC Remote.
    See `docs/dvc_setup.md` for details.

5. Start Apache Airflow.
    ```bash
    airflow webserver --port 8080
    airflow scheduler
    ```

6. Run the Airflow DAG `mlops_data_pipeline`.

