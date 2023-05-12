import os
from dotenv import load_dotenv


load_dotenv()

SUPER_JOB_KEY = os.getenv('SUPER_JOB_KEY')

FILE_FOR_WRITE_RAW_DATA = "./raw_data.json"
CODING_PAGE = 'utf-8'
FILE_FOR_VACANCY_JSON = "./vacancy.json"
FILE_FOR_VACANCY_CSV = "./vacancy.csv"
DB_FOR_VACANCY = "postgree.bd"

