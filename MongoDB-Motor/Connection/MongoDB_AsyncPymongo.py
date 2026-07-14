from pymongo import AsyncMongoClient
from dotenv import load_dotenv
import os
import certifi
load_dotenv()

USERNAME : str | None = os.getenv("UserName")
PASSWORD : str | None = os.getenv("Password")

url = f"mongodb+srv://{USERNAME}:{PASSWORD}@whatsapp-order-automati.kmyno73.mongodb.net/?appName=Whatsapp-Order-Automation"

client = AsyncMongoClient(url,tls=True,tlsCAFile=certifi.where())

db = client["blamestack"]