# 🏥 Healthcare RCM (Revenue Cycle Management) BigQuery Project

## 📌 Overview
This project simulates a **Healthcare Revenue Cycle Management (RCM)** data pipeline for two hospitals.  
It uses **Python (ETL)** + **Google BigQuery** to process, clean, and load data for analytics.

The pipeline extracts data from CSVs, transforms it into a consistent format, handles **Slowly Changing Dimensions (SCD Type 2)** for patient data, and loads it into BigQuery for analytics and dashboards.

---

## 🎯 Goals of the Project
- Create a **reusable ETL pipeline** for healthcare datasets.
- Standardize data across different hospital systems.
- Implement **SCD Type 2** to track historical changes in patient data.
- Store clean and processed data in **BigQuery fact & dimension tables**.
- Allow for easy KPI reporting, dashboards, and analytics.

---

## ⚙️ Tech Stack
- **Python** – Data extraction, transformation, loading.
- **Pandas** – Data cleaning & manipulation.
- **Google BigQuery** – Cloud data warehouse for analytics.
- **.env & Service Keys** – Secure credentials management.
- **SQL** – Creating tables & running analytics queries.

## 📂 Project Structure
Healthcare_RCM_Project/
│── config/ # Database and GCP configurations
│── scripts/ # All ETL scripts
│ ├── extract.py # Extracts CSV data
│ ├── transform.py # Cleans & standardizes data
│ ├── transform_cpt.py # Cleans CPT (procedure code) data
│ ├── load.py # Loads data to BigQuery
│ ├── scd_type2.py # SCD Type 2 historical tracking
│── sql/ # SQL scripts for BigQuery table creation
│── main.py # Runs the full ETL pipeline
│── requirements.txt # Python dependencies
│── .env # Environment variables (Project ID, Keys)
│── README.md # Project documentation 


---

## 🔄 ETL Pipeline Flow
1. **Extract**  
   - Reads hospital data CSVs (patients, providers, departments, encounters, transactions, claims).  
   - Reads CPT codes file.

2. **Transform**  
   - Renames columns for consistency across hospitals.  
   - Merges CPT descriptions into encounter and transaction data.  
   - Removes duplicates.  
   - Adds SCD Type 2 columns (`start_date`, `end_date`, `is_active`).

3. **Load**  
   - Loads processed data into **BigQuery fact tables**.  
   - Fact tables store transaction-level data.  
   - Dimension tables store reference data like patients, providers, departments.

---

## 🗄 Fact vs Dimension Tables
- **Fact Tables** – Store actual measurable events (e.g., transactions, claims).  
- **Dimension Tables** – Store descriptive/reference information (e.g., patient details, provider details).

Example:
| Table Type   | Example Data |
|--------------|--------------|
| Fact         | Amount paid in a transaction |
| Dimension    | Patient's name, gender, DOB |

---

## 📊 Example Queries
**1️⃣ Total Revenue by Hospital**
```sql
SELECT 
  'Hospital A' AS hospital,
  ROUND(SUM(paid_amount), 2) AS total_revenue
FROM `project_id.healthcare_rcm.fact_transactions_a`
UNION ALL
SELECT 
  'Hospital B' AS hospital,
  ROUND(SUM(paid_amount), 2) AS total_revenue
FROM `project_id.healthcare_rcm.fact_transactions_b`;
```
📌 Future Improvements
Automate dashboard creation using Looker Studio.
Add real-time streaming data ingestion.
Enhance data quality checks.
