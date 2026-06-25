import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS emails(
    id TEXT PRIMARY KEY,
    sender TEXT,
    subject TEXT,
    body TEXT,
    date TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")