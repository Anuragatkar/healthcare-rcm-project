
CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.dim_patients_a` (
  patient_id STRING,
  first_name STRING,
  last_name STRING,
  middle_name STRING,
  ssn STRING,
  phone_number STRING,
  gender STRING,
  dob DATE,
  address STRING,
  modified_date DATE,
  start_date TIMESTAMP,
  end_date TIMESTAMP,
  is_active BOOLEAN
);

CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.dim_patients_b` (
  patient_id STRING,
  first_name STRING,
  last_name STRING,
  middle_name STRING,
  ssn STRING,
  phone_number STRING,
  gender STRING,
  dob DATE,
  address STRING,
  modified_date DATE,
  start_date TIMESTAMP,
  end_date TIMESTAMP,
  is_active BOOLEAN
);
CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.dim_providers_a` (
  provider_id STRING,
  first_name STRING,
  last_name STRING,
  specialization STRING,
  dept_id STRING,
  npi INT64
);

CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.dim_providers_b` (
  provider_id STRING,
  first_name STRING,
  last_name STRING,
  specialization STRING,
  dept_id STRING,
  npi INT64
);


CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.dim_departments_a` (
  dept_id STRING,
  name STRING
);

CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.dim_departments_b` (
  dept_id STRING,
  name STRING
);


CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.fact_encounters_a` (
  encounter_id STRING,
  patient_id STRING,
  encounter_date DATE,
  encounter_type STRING,
  provider_id STRING,
  department_id STRING,
  procedure_code INT64,
  procedure_description STRING,
  inserted_date DATE,
  modified_date DATE
);

CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.fact_encounters_b` (
  encounter_id STRING,
  patient_id STRING,
  encounter_date DATE,
  encounter_type STRING,
  provider_id STRING,
  department_id STRING,
  procedure_code INT64,
  procedure_description STRING,
  inserted_date DATE,
  modified_date DATE
);


CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.fact_transactions_a` (
  transaction_id STRING,
  encounter_id STRING,
  patient_id STRING,
  provider_id STRING,
  dept_id STRING,
  visit_date DATE,
  service_date DATE,
  paid_date DATE,
  visit_type STRING,
  amount FLOAT64,
  amount_type STRING,
  paid_amount FLOAT64,
  claim_id STRING,
  payor_id STRING,
  procedure_code INT64,
  procedure_description STRING,
  icd_code STRING,
  line_of_business STRING,
  medicaid_id STRING,
  medicare_id STRING,
  insert_date DATE,
  modified_date DATE
);

CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.fact_transactions_b` (
  transaction_id STRING,
  encounter_id STRING,
  patient_id STRING,
  provider_id STRING,
  dept_id STRING,
  visit_date DATE,
  service_date DATE,
  paid_date DATE,
  visit_type STRING,
  amount FLOAT64,
  amount_type STRING,
  paid_amount FLOAT64,
  claim_id STRING,
  payor_id STRING,
  procedure_code INT64,
  procedure_description STRING,
  icd_code STRING,
  line_of_business STRING,
  medicaid_id STRING,
  medicare_id STRING,
  insert_date DATE,
  modified_date DATE
);


CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.fact_claims_a` (
  claim_id STRING,
  transaction_id STRING,
  patient_id STRING,
  encounter_id STRING,
  provider_id STRING,
  dept_id STRING,
  service_date DATE,
  claim_date DATE,
  payor_id STRING,
  claim_amount FLOAT64,
  paid_amount FLOAT64,
  claim_status STRING,
  payor_type STRING,
  deductible FLOAT64,
  coinsurance FLOAT64,
  copay FLOAT64,
  insert_date DATE,
  modified_date DATE
);

CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.fact_claims_b` (
  claim_id STRING,
  transaction_id STRING,
  patient_id STRING,
  encounter_id STRING,
  provider_id STRING,
  dept_id STRING,
  service_date DATE,
  claim_date DATE,
  payor_id STRING,
  claim_amount FLOAT64,
  paid_amount FLOAT64,
  claim_status STRING,
  payor_type STRING,
  deductible FLOAT64,
  coinsurance FLOAT64,
  copay FLOAT64,
  insert_date DATE,
  modified_date DATE
);


CREATE TABLE IF NOT EXISTS `plasma-datum-467517-d6.healthcare_rcm.ref_cpt_codes` (
  procedure_code INT64,
  category STRING,
  description STRING
);
