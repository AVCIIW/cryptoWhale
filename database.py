import os
import json
import urllib.request
import urllib.parse

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    with open('.env', 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

SUPABASE_URL = os.environ.get("VITE_SUPABASE_URL")
SUPABASE_KEY = os.environ.get("VITE_SUPABASE_SUPABASE_ANON_KEY")

def _make_request(url, method="GET", data=None):
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

    req = urllib.request.Request(url, headers=headers, method=method)

    if data:
        req.data = json.dumps(data).encode('utf-8')

    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        return None

def getbalance(discord_id: str) -> float:
    url = f"{SUPABASE_URL}/rest/v1/users?discord_id=eq.{discord_id}&select=balance"
    data = _make_request(url)

    if data and len(data) > 0:
        return float(data[0]["balance"])
    return 0.0

def register(discord_id: str) -> str:
    url = f"{SUPABASE_URL}/rest/v1/users"
    data = {"discord_id": str(discord_id), "balance": 0}
    _make_request(url, method="POST", data=data)
    return "Done"

def add(discord_id: str, amount: float):
    current_balance = getbalance(discord_id)
    new_balance = round(current_balance + amount, 2)

    url = f"{SUPABASE_URL}/rest/v1/users?discord_id=eq.{discord_id}"
    data = {"balance": new_balance}
    _make_request(url, method="PATCH", data=data)

def remove(discord_id: str, amount: float):
    current_balance = getbalance(discord_id)
    new_balance = round(current_balance - amount, 2)

    url = f"{SUPABASE_URL}/rest/v1/users?discord_id=eq.{discord_id}"
    data = {"balance": new_balance}
    _make_request(url, method="PATCH", data=data)

def isregistered(discord_id: str) -> bool:
    url = f"{SUPABASE_URL}/rest/v1/users?discord_id=eq.{discord_id}&select=discord_id"
    data = _make_request(url)
    return data and len(data) > 0
