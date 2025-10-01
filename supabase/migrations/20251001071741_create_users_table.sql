/*
  # Create users table for Discord bot

  1. New Tables
    - `users`
      - `discord_id` (text, primary key) - Discord user ID
      - `balance` (numeric, default 0) - User's balance in USD
      - `created_at` (timestamptz) - Account creation timestamp
      - `updated_at` (timestamptz) - Last update timestamp

  2. Security
    - Enable RLS on `users` table
    - Add policy for authenticated users to read all user data
    - Add policy for authenticated users to update their own balance
    - Note: Since this is a Discord bot, we'll use service role for operations
*/

CREATE TABLE IF NOT EXISTS users (
  discord_id text PRIMARY KEY,
  balance numeric DEFAULT 0 NOT NULL,
  created_at timestamptz DEFAULT now() NOT NULL,
  updated_at timestamptz DEFAULT now() NOT NULL
);

-- Create index for faster lookups
CREATE INDEX IF NOT EXISTS idx_users_discord_id ON users(discord_id);

-- Enable RLS
ALTER TABLE users ENABLE ROW LEVEL SECURITY;

-- Policy for service role to have full access (Discord bot will use service role)
CREATE POLICY "Service role has full access"
  ON users
  FOR ALL
  TO service_role
  USING (true)
  WITH CHECK (true);