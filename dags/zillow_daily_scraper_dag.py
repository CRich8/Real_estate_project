import os
from zillow_scraper import zillow_scraper

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator


from google.cloud import storage
from datetime import date, timedelta

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'zillow_data_all')

def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    :param bucket: GCS bucket name
    :param object_name: target path & file-name
    :param local_file: source path & file-name
    :return:
    """
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)

    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)

today = date.today()
OUTPUT_FILE_TEMPLATE = AIRFLOW_HOME + f"/hoboken_{today}.csv"
CSV_FILE = f"hoboken_{today}.csv"
DATASET = "zillow_data_all"
TABLE_NAME = 'hoboken_raw_daily'
INPUT_FILETYPE = "csv"

schema2 = [
  {
    "name": "Date",
    "mode": "NULLABLE",
    "type": "DATE",
    "fields": []
  },
  {
    "name": "zpid",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "fields": []
  },
  {
    "name": "id",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "fields": []
  },
  {
    "name": "providerListingId",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "fields": []
  },
  {
    "name": "imgSrc",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "hasImage",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "detailUrl",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "statusType",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "statusText",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "countryCurrency",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "price",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "unformattedPrice",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "fields": []
  },
  {
    "name": "address",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "addressStreet",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "addressCity",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "addressState",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "addressZipcode",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "fields": []
  },
  {
    "name": "isUndisclosedAddress",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "beds",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "fields": []
  },
  {
    "name": "baths",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "fields": []
  },
  {
    "name": "area",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "fields": []
  },
  {
    "name": "latLong",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "isZillowOwned",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "variableData",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "badgeInfo",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "isSaved",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "isUserClaimingOwner",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "isUserConfirmedClaim",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "pgapt",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "sgapt",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "zestimate",
    "mode": "NULLABLE",
    "type": "INTEGER",
    "fields": []
  },
  {
    "name": "shouldShowZestimateAsPrice",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "has3DModel",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "hasVideo",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "isHomeRec",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "info2String",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "hasAdditionalAttributions",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "isFeaturedListing",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "availabilityDate",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "list",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "relaxed",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "brokerName",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "hasOpenHouse",
    "mode": "NULLABLE",
    "type": "BOOLEAN",
    "fields": []
  },
  {
    "name": "openHouseDescription",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "openHouseEndDate",
    "mode": "NULLABLE",
    "type": "TIMESTAMP",
    "fields": []
  },
  {
    "name": "openHouseStartDate",
    "mode": "NULLABLE",
    "type": "TIMESTAMP",
    "fields": []
  },
  {
    "name": "info3String",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "builderName",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "lotAreaString",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "isPropertyResultCDP",
    "mode": "NULLABLE",
    "type": "STRING",
    "fields": []
  },
  {
    "name": "best_deal",
    "mode": "NULLABLE",
    "type": "FLOAT",
    "fields": []
  }
]
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(0),
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(
    dag_id="zillow_daily_ingestion_dag",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['ZillowDaily'],
    schedule_interval="30 17 * * *",

) as dag:



    downlod_dataset_python_task = PythonOperator(
        task_id="download_daily_zillow_data_task",
        python_callable=zillow_scraper
    )
    local_to_gcs_task = PythonOperator(
        task_id="local_daily_zillow_data_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": f"daily_zillow_data/{CSV_FILE}",
            "local_file": f"{OUTPUT_FILE_TEMPLATE}",
        },
    )

    rm_task = BashOperator(
        task_id="rm_daily_zillow_data_task",
        bash_command=f"rm {OUTPUT_FILE_TEMPLATE}"
    )

    
    gcs_to_bigquery_task = GCSToBigQueryOperator(
        task_id="bq_daily_zillow_data_table_task",
        bucket = 'zillow_data_raw',
        source_objects=[f"daily_zillow_data/{CSV_FILE}"],
        destination_project_dataset_table=f"{DATASET}.{TABLE_NAME}",
        write_disposition="WRITE_APPEND",
        source_format='CSV',
        schema_fields = schema2,
        skip_leading_rows = 1
    )
    
    downlod_dataset_python_task >> local_to_gcs_task >> rm_task >> gcs_to_bigquery_task