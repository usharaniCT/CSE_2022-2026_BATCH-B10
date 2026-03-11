import sqlite3


def connect_db():
    conn = sqlite3.connect("database.db", check_same_thread=False)
    return conn


def create_tables():

    conn = connect_db()
    cur = conn.cursor()

    # USERS TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        email TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # HISTORY TABLE
    cur.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        image TEXT,
        result TEXT
    )
    """)
    cur.execute("""
CREATE TABLE IF NOT EXISTS history(
id INTEGER PRIMARY KEY AUTOINCREMENT,
email TEXT,
image TEXT,
result TEXT,
date TEXT,
time TEXT
)
""")

    conn.commit()
    conn.close()