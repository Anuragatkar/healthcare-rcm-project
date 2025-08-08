import pandas as pd
import os

def extract_hospital_csvs(hospital_name): 
   
    base_path = f"data/{hospital_name}"
    
    table_files = {                         
        "patients": "patients.csv",
        "providers": "providers.csv",
        "departments": "departments.csv",
        "transactions": "transactions.csv",
        "claims": "claims.csv",
        "encounters": "encounters.csv"
    }

    dataframes = {}           

    for table, filename in table_files.items(): 
        full_path = os.path.join(base_path, filename) 
        try:
            df = pd.read_csv(full_path)
            dataframes[table] = df        
            print(f"Loaded {filename} from {hospital_name}")
        except FileNotFoundError:
            print(f"Missing file: {full_path}")
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    return dataframes


def extract_cpt_codes():

    path = "data/reference/cpt_codes.csv"
    try:
        df = pd.read_csv(path)
        print("Loaded CPT codes from reference folder")
        return df   
    except Exception as e:
        print(f"Error loading CPT codes: {e}")
        return None
