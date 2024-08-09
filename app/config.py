import os

from dotenv import load_dotenv

load_dotenv()  # Извлекаем переменные окружения из файла .env

CONVERSION_API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASS = os.environ.get("MONGO_PASS")
MONGO_URL = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.diysdiz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

