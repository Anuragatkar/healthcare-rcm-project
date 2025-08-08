import pandas as pd

def clean_patients(df, hospital):
    
    if hospital == "hospital_a":
        df_cleaned = df.rename(columns={
            "PatientID": "patient_id",
            "FirstName": "first_name",
            "LastName": "last_name",
            "MiddleName": "middle_name",
            "SSN": "ssn",
            "PhoneNumber": "phone_number",
            "Gender": "gender",
            "DOB": "dob",
            "Address": "address",
            "ModifiedDate": "modified_date"
        })
    else: 
        df_cleaned = df.rename(columns={
            "ID": "patient_id",
            "F_Name": "first_name",
            "L_Name": "last_name",
            "M_Name": "middle_name",
            "SSN": "ssn",
            "PhoneNumber": "phone_number",
            "Gender": "gender",
            "DOB": "dob",
            "Address": "address",
            "ModifiedDate": "modified_date"
        })

    df_cleaned["hospital"] = hospital
    df_cleaned = df_cleaned.drop_duplicates(subset=["patient_id"])
    return df_cleaned


def clean_providers(df):
    df = df.rename(columns={
        "ProviderID": "provider_id",
        "FirstName": "first_name",
        "LastName": "last_name",
        "Specialization": "specialization",
        "DeptID": "dept_id",
        "NPI": "npi"
    })
    df = df.drop_duplicates(subset=["provider_id"])
    return df


def clean_departments(df):
    df = df.rename(columns={
        "DeptID": "dept_id",
        "Name": "name"
    })
    df = df.drop_duplicates(subset=["dept_id"])
    return df


def clean_encounters(df):
    df = df.rename(columns={
        "EncounterID": "encounter_id",
        "PatientID": "patient_id",
        "EncounterDate": "encounter_date",
        "EncounterType": "encounter_type",
        "ProviderID": "provider_id",
        "DepartmentID": "dept_id",
        "ProcedureCode": "procedure_code",
        "InsertedDate": "inserted_date",
        "ModifiedDate": "modified_date"
    })
    df = df.drop_duplicates(subset=["encounter_id"])
    return df


def clean_transactions(df):
    df = df.rename(columns={
        "TransactionID": "transaction_id",
        "EncounterID": "encounter_id",
        "PatientID": "patient_id",
        "ProviderID": "provider_id",
        "DeptID": "dept_id",
        "VisitDate": "visit_date",
        "ServiceDate": "service_date",
        "PaidDate": "paid_date",
        "VisitType": "visit_type",
        "Amount": "amount",
        "AmountType": "amount_type",
        "PaidAmount": "paid_amount",
        "ClaimID": "claim_id",
        "PayorID": "payor_id",
        "ProcedureCode": "procedure_code",
        "ICDCode": "icd_code",
        "LineOfBusiness": "line_of_business",
        "MedicaidID": "medicaid_id",
        "MedicareID": "medicare_id",
        "InsertDate": "insert_date",
        "ModifiedDate": "modified_date"
    })
    df = df.drop_duplicates(subset=["transaction_id"])
    return df


def clean_claims(df):
    df = df.rename(columns={
        "ClaimID": "claim_id",
        "TransactionID": "transaction_id",
        "PatientID": "patient_id",
        "EncounterID": "encounter_id",
        "ProviderID": "provider_id",
        "DeptID": "dept_id",
        "ServiceDate": "service_date",
        "ClaimDate": "claim_date",
        "PayorID": "payor_id",
        "ClaimAmount": "claim_amount",
        "PaidAmount": "paid_amount",
        "ClaimStatus": "claim_status",
        "PayorType": "payor_type",
        "Deductible": "deductible",
        "Coinsurance": "coinsurance",
        "Copay": "copay",
        "InsertDate": "insert_date",
        "ModifiedDate": "modified_date"
    })
    df = df.drop_duplicates(subset=["claim_id"])
    return df


def enrich_with_cpt(df, cpt_df):

    return df.merge(cpt_df, how="left", on="procedure_code")


def transform_all(hospital_data, cpt_df, hospital_name):
    return {
        "patients": clean_patients(hospital_data["patients"], hospital_name),
        "providers": clean_providers(hospital_data["providers"]),
        "departments": clean_departments(hospital_data["departments"]),
        "encounters": enrich_with_cpt(clean_encounters(hospital_data["encounters"]), cpt_df),
        "transactions": enrich_with_cpt(clean_transactions(hospital_data["transactions"]), cpt_df),
        "claims": clean_claims(hospital_data["claims"])
    }
