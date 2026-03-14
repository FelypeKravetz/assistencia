from database.db import conectar


def cadastrar_referido(site_id,login,senha,senha_saque,tipo_saque,info_saque,deposito):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO referidos
    (site_id,login,senha,saque_senha_referido,tipo_saque_referido,saque_info_referido,deposito)
    VALUES (?,?,?,?,?,?,?)
    """,(
        site_id,
        login,
        senha,
        senha_saque,
        tipo_saque,
        info_saque,
        deposito
    ))

    conn.commit()
    conn.close()



def listar_referidos(site_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM referidos WHERE site_id=?",
        (site_id,)
    )

    dados = cursor.fetchall()

    conn.close()

    return dados



def obter_referido(ref_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM referidos WHERE id=?",
        (ref_id,)
    )

    dado = cursor.fetchone()

    conn.close()

    return dado



def atualizar_referido(ref_id,login,senha,senha_saque,tipo_saque,info_saque,deposito):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE referidos SET
    login=?,
    senha=?,
    saque_senha_referido=?,
    tipo_saque_referido=?,
    saque_info_referido=?,
    deposito=?
    WHERE id=?
    """,(
        login,
        senha,
        senha_saque,
        tipo_saque,
        info_saque,
        deposito,
        ref_id
    ))

    conn.commit()
    conn.close()



def excluir_referido(ref_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM referidos WHERE id=?",
        (ref_id,)
    )

    conn.commit()
    conn.close()