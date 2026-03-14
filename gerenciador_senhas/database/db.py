import sqlite3
from config import DB_NAME


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_banco():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        senha TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sites(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        nome TEXT,
        url TEXT,
        tipo_login TEXT,
        login TEXT,
        senha TEXT,
        senha_saque TEXT,
        tipo_saque TEXT,
        saque_info TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS referidos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        site_id INTEGER,
        login TEXT,
        senha TEXT,
        saque_senha_referido TEXT,
        tipo_saque_referido TEXT,
        saque_info_referido TEXT,
        deposito REAL,
        data TEXT
    )
    """)

    conn.commit()
    conn.close()