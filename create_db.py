import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# ---------------- USERS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS USERS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    USERNAME TEXT UNIQUE NOT NULL,
    PASSWORD TEXT NOT NULL
)
""")


# ---------------- JOB APPLICATIONS TABLE ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS JOB_APPLICATIONS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    COMPANY_NAME TEXT NOT NULL,
    JOB_ROLE TEXT NOT NULL,
    APPLIED_DATE DATE NOT NULL,
    STATUS TEXT NOT NULL,
    USER_ID INTEGER NOT NULL,
    FOREIGN KEY (USER_ID) REFERENCES USERS(ID)
)
""")

conn.commit()
conn.close()

print("✅ Database reset and table ready!")
