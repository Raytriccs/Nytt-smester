import sqlite3

def init_db():
    conn = sqlite3.connect("cv_database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cv (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            navn TEXT,
            epost TEXT,
            telefon TEXT,
            utdanning TEXT,
            erfaring TEXT,
            ferdigheter TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_cv(navn, epost, telefon, utdanning, erfaring, ferdigheter):
    conn = sqlite3.connect("cv_database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cv (navn, epost, telefon, utdanning, erfaring, ferdigheter)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (navn, epost, telefon, utdanning, erfaring, ferdigheter))

    conn.commit()
    conn.close()












