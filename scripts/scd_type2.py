from datetime import datetime
import pandas as pd

def apply_scd_type2(table_name: str, new_data: pd.DataFrame) -> pd.DataFrame:
   
    now = datetime.utcnow()
    new_data["start_date"] = now
    new_data["end_date"] = pd.NaT
    new_data["is_active"] = True
    return new_data
