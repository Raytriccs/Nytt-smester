import mysql.connector

def init_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="rayaanyasar",
        password="Rayaan2007!",  # passordet du satte
        database="cvdb"
    )
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS cv (
            id INT AUTO_INCREMENT PRIMARY KEY,
            navn VARCHAR(100),
            epost VARCHAR(100),
            telefon VARCHAR(20),
            utdanning TEXT,
            erfaring TEXT,
            ferdigheter TEXT
        )
    """)

    conn.commit()
    conn.close()

def save_cv(navn, epost, telefon, utdanning, erfaring, ferdigheter):
    conn = mysql.connector.connect(
        host="localhost",
        user="rayaanyasar",
        password="Rayaan2007!",
        database="cvdb"
    )
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cv (navn, epost, telefon, utdanning, erfaring, ferdigheter)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (navn, epost, telefon, utdanning, erfaring, ferdigheter))

    conn.commit()
    conn.close()












