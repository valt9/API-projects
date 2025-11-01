import requests
import sqlite3
from datetime import datetime, timedelta


API_KEY = "f44ff8d296b85c97a40aeeff"
EXCHANGE_RATE_URL = "https://v6.exchangerate-api.com/v6/" 
DB_NAME = "exchange_rates.db"

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS rates (
            base TEXT,
            target TEXT,
            rate REAL,
            timestamp TEXT
        )
""")
conn.commit()

base = input("Enter base currency (e.g., USD, EUR, GBP,...)")
target = input("Enter target currency (e.g., USD, EUR, GBP,...)")

cur.execute("""
            SELECT rate, timestamp FROM rates
            WHERE base = ? AND target = ?
            ORDER BY timestamp DESC LIMIT 1"""
            , (base, target))
row = cur.fetchone()

use_db_rate = False
if row:
    rate, ts = row

if use_db_rate:
    print(f"latest exchange rate from DB ({ts}): 1 {base} = {rate} {target}")
else:
    url = f"{EXCHANGE_RATE_URL}{API_KEY}/pair/{base}/{target}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data.get("conversion_rate")
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur.execute("""
                    INSERT INTO rates (base, target, rate, timestamp)
                    VALUES (?, ?, ?, ?)"""
                    , (base, target, rate, ts))
        conn.commit()
        print(f"Grabbed from API: 1 {base} = {rate} {target} (at {ts})")
    else:
        print("Error fetching data from API:", response.status_code)
conn.close()