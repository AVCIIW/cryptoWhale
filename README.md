# Discord Casino Bot

A Discord bot with gambling features including coinflip, airdrop, upgrader, and cryptocurrency deposit/withdrawal.

## Features

- Balance management
- LTC deposits and withdrawals
- Coinflip games
- Airdrops/giveaways
- Upgrader gambling game
- Tip system

## Setup

1. Install dependencies:
```bash
pip install discord-py-interactions cloudscraper supabase python-dotenv
```

2. Configure environment variables in `.env`:
```
VITE_SUPABASE_URL=your_supabase_url
VITE_SUPABASE_SUPABASE_ANON_KEY=your_supabase_key
```

3. Update bot token in `main.py` (line 14)

4. Run the bot:
```bash
python3 main.py
```

## Database

The bot uses Supabase for data persistence. All user balances are stored in the `users` table with the following schema:

- `discord_id` (text, primary key)
- `balance` (numeric)
- `created_at` (timestamptz)
- `updated_at` (timestamptz)

## Migration from JSON

All existing user data from `users.json` has been migrated to Supabase automatically.
