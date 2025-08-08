import pandas as pd

def clean_cpt_codes(cpt_df):  

    df = cpt_df.copy() 

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns] 

    df = df.rename(columns={     
        "cpt_codes": "procedure_code",
        "procedure_code_category": "category",
        "procedure_code_descriptions": "description"
    })

    df["procedure_code"] = pd.to_numeric(df["procedure_code"], errors="coerce").astype("Int64")


    return df 
