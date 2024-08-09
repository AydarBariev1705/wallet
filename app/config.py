import os

from dotenv import load_dotenv

load_dotenv()  # Извлекаем переменные окружения из файла .env

DB = os.environ.get("DB")
CONVERSION_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_DATA = os.environ.get("MONGO_DATA")
MONGO_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@{MONGO_DATA}"

COMMISSION = 0.03
