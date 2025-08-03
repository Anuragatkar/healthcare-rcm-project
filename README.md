🏥 Healthcare RCM ETL Pipeline
This project builds an end-to-end ETL (Extract, Transform, Load) pipeline to process and analyze healthcare Revenue Cycle Management (RCM) data from multiple hospitals. It integrates CSV and MySQL data sources, performs data cleaning and transformation, and loads the results into BigQuery for analytics.

🔧 Key Features
Extracts patient, provider, transaction, and claims data from CSV and MySQL

Cleans and standardizes data using pandas

Enriches datasets with CPT codes

Supports Slowly Changing Dimensions (SCD Type 2)

Loads final data into BigQuery using Google Cloud libraries

📁 Tech Stack
Python (pandas, mysql-connector, google-cloud-bigquery)

MySQL (local data source)

BigQuery (cloud warehouse)

.env for secure credential handling

