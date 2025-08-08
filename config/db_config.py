import os
from dotenv import load_dotenv 

load_dotenv()  
DB_CONFIG = {
    'hospital_a': {
        'host': 'localhost',
        'user': os.getenv("HOSP_A_USER"),
        'password': os.getenv("HOSP_A_PASS"),
        'database': 'hospital_a_db'
    },
    'hospital_b': {
        'host': 'localhost',
        'user': os.getenv("HOSP_B_USER"),
        'password': os.getenv("HOSP_B_PASS"),
        'database': 'hospital_b_db'
    }
}
