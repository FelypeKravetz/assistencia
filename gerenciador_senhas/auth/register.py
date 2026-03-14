from database.db import conectar


def registrar(username,senha):

    conn = conectar()
    cursor = conn.cursor()

    try:

        cursor.execute(
            "INSERT INTO usuarios(username,senha) VALUES (?,?)",
            (username,senha)
        )

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()