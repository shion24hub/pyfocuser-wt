import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_LEVEL = os.getenv("ACCESS_LEVEL")
MY_ACCOUNT_ID = os.getenv("MY_ACCOUNT_ID")
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")