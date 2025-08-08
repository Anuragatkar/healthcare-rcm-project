import pandas as pd
from google.cloud import bigquery

def load_to_bigquery(df, table_id, write_disposition="WRITE_APPEND"):
    
    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        write_disposition=write_disposition,
        autodetect=True,
    )

    job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    job.result() 

    print(f"Loaded data to {table_id} ({len(df)} rows)")
