import sqlite3

conn = sqlite3.connect("emails.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM emails")

print(cursor.fetchone()[0])

conn.close()