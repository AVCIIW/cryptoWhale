import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url: str = os.environ.get("VITE_SUPABASE_URL")
key: str = os.environ.get("VITE_SUPABASE_SUPABASE_ANON_KEY")
supabase: Client = create_client(url, key)

def getbalance(discord_id: str) -> float:
    response = supabase.table("users").select("balance").eq("discord_id", str(discord_id)).maybe_single().execute()
    if response.data:
        return float(response.data["balance"])
    return 0.0

def register(discord_id: str) -> str:
    data = {"discord_id": str(discord_id), "balance": 0}
    supabase.table("users").upsert(data).execute()
    return "Done"

def add(discord_id: str, amount: float):
    current_balance = getbalance(discord_id)
    new_balance = round(current_balance + amount, 2)
    supabase.table("users").update({"balance": new_balance, "updated_at": "now()"}).eq("discord_id", str(discord_id)).execute()

def remove(discord_id: str, amount: float):
    current_balance = getbalance(discord_id)
    new_balance = round(current_balance - amount, 2)
    supabase.table("users").update({"balance": new_balance, "updated_at": "now()"}).eq("discord_id", str(discord_id)).execute()

def isregistered(discord_id: str) -> bool:
    response = supabase.table("users").select("discord_id").eq("discord_id", str(discord_id)).maybe_single().execute()
    return response.data is not None
