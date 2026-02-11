import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM job_applications")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
