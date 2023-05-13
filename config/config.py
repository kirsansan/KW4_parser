import os
from dotenv import load_dotenv


load_dotenv()
MY_APP_NAME = "K_ParserApp/1.0"

SUPER_JOB_ID = os.getenv('SUPER_JOB_ID')
SUPER_JOB_KEY = os.getenv('SUPER_JOB_KEY')

CODING_PAGE = 'utf-8'

FILE_FOR_WRITE_RAW_DATA = "../data/raw_data.json"
FILE_FOR_VACANCY_JSON = "../data/vacancy.json"
FILE_FOR_VACANCY_CSV = "../data/vacancy.csv"
DB_FOR_VACANCY = "postgree.bd"

MAIN_REQUEST_FOR_HH = "https://api.hh.ru/vacancies"
MAIN_REQUEST_FOR_SJ = "https://api.superjob.ru/2.0/vacancies"