import pyrebase
import os
from dotenv import load_dotenv


load_dotenv()

config = {
    'apiKey': os.getenv('API_KEY'),
    'authDomain': os.getenv('STORAGE_BUCKET'),
    'databaseURL': os.getenv('DATABASE_URL'),
    'storageBucket': os.getenv('STORAGE_BUCKET'),
}

firebase = pyrebase.initialize_app(config)
