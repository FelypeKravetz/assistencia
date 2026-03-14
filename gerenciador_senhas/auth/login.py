from database.db import conectar


def login(username,senha):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM usuarios WHERE username=? AND senha=?",
        (username,senha)
    )

    user = cursor.fetchone()

    conn.close()

    if user:
        return user[0]

    return None