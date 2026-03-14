from database.db import conectar


def cadastrar_site(user_id,nome,url,tipo_login,login,senha,senha_saque,tipo_saque,saque_info):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO sites
    (user_id,nome,url,tipo_login,login,senha,senha_saque,tipo_saque,saque_info)
    VALUES (?,?,?,?,?,?,?,?,?)
    """,(
        user_id,
        nome,
        url,
        tipo_login,
        login,
        senha,
        senha_saque,
        tipo_saque,
        saque_info
    ))

    conn.commit()
    conn.close()



def listar_sites(user_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM sites WHERE user_id=?",
        (user_id,)
    )

    dados = cursor.fetchall()

    conn.close()

    return dados



def obter_site(site_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM sites WHERE id=?",
        (site_id,)
    )

    dado = cursor.fetchone()

    conn.close()

    return dado



def atualizar_site(site_id,nome,url,tipo_login,login,senha,senha_saque,tipo_saque,saque_info):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE sites SET
    nome=?,
    url=?,
    tipo_login=?,
    login=?,
    senha=?,
    senha_saque=?,
    tipo_saque=?,
    saque_info=?
    WHERE id=?
    """,(
        nome,
        url,
        tipo_login,
        login,
        senha,
        senha_saque,
        tipo_saque,
        saque_info,
        site_id
    ))

    conn.commit()
    conn.close()



def excluir_site(site_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM sites WHERE id=?",
        (site_id,)
    )

    conn.commit()
    conn.close()