import os
import requests
from dotenv import load_dotenv

load_dotenv()

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("MICROSOFT_APP_ID")
CLIENT_SECRET = os.getenv("MICROSOFT_APP_PASSWORD")

if not TENANT_ID or not CLIENT_ID or not CLIENT_SECRET:
    raise RuntimeError("Missing Azure environment variables")

token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

data = {
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "scope": "https://graph.microsoft.com/.default",
    "grant_type": "client_credentials"
}

response = requests.post(token_url, data=data)

if response.status_code == 200:
    token = response.json().get("access_token")
    print("✅ Microsoft Entra ID authentication SUCCESS")
    print("Token received (length):", len(token))
else:
    print("❌ Authentication FAILED")
    print(response.status_code)
    print(response.text)
