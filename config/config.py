import os
from dotenv import load_dotenv


load_dotenv()

SUPER_JOB_KEY = os.getenv('SUPER_JOB_KEY')

FILE_FOR_WRITE = "./vacancy.json"

