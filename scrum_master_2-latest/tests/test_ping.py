from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

uri = os.getenv("MONGO_URI")
print("DEBUG MONGO_URI =", uri)   # 👈 ADD THIS

client = MongoClient(
    uri,
    tls=True,
    tlsCAFile=certifi.where()
)

try:
    client.admin.command("ping")
    print("✅ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("❌ Connection failed:", e)

