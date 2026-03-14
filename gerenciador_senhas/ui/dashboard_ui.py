import tkinter as tk
from tkinter import ttk,messagebox

from managers.sites_manager import *
from managers.referidos_manager import *


# -------------------------------
# DASHBOARD
# -------------------------------

def dashboard(user_id):

    win = tk.Tk()
    win.title("Gerenciador de Sites")
    win.geometry("900x500")
    win.configure(bg="#1e1e1e")

    # -------------------------
    # TITULO
    # -------------------------

    titulo = tk.Label(
        win,
        text="Gerenciador de Sites",
        bg="#1e1e1e",
        fg="white",
        font=("Arial",16,"bold")
    )

    titulo.pack(pady=10)


    # -------------------------
    # TABELA
    # -------------------------

    tabela = ttk.Treeview(
        win,
        columns=("id","nome","login"),
        show="headings",
        height=15
    )

    tabela.heading("id",text="ID")
    tabela.heading("nome",text="Site")
    tabela.heading("login",text="Login")

    tabela.column("id",width=50)
    tabela.column("nome",width=200)
    tabela.column("login",width=200)

    tabela.pack(fill="both",expand=True,padx=20,pady=10)


    atualizar_sites(tabela,user_id)


    tabela.bind(
        "<Double-1>",
        lambda e:abrir_site(tabela)
    )


    # -------------------------
    # BOTOES
    # -------------------------

    botoes = tk.Frame(win,bg="#1e1e1e")
    botoes.pack(pady=10)


    btn_novo = ttk.Button(
        botoes,
        text="➕ Novo Site",
        command=lambda:cadastrar_site_ui(user_id,tabela)
    )

    btn_novo.grid(row=0,column=0,padx=5)


    btn_editar = ttk.Button(
        botoes,
        text="✏ Editar Site",
        command=lambda:editar_site(tabela,user_id)
    )

    btn_editar.grid(row=0,column=1,padx=5)


    btn_excluir = ttk.Button(
        botoes,
        text="🗑 Excluir Site",
        command=lambda:remover_site_ui(tabela,user_id)
    )

    btn_excluir.grid(row=0,column=2,padx=5)


    btn_logout = ttk.Button(
        botoes,
        text="Logout",
        command=win.destroy
    )

    btn_logout.grid(row=0,column=3,padx=5)


    win.mainloop()

# -------------------------------
# ATUALIZAR SITES
# -------------------------------

def atualizar_sites(tabela,user_id):

    for item in tabela.get_children():
        tabela.delete(item)

    sites = listar_sites(user_id)

    for s in sites:

        tabela.insert(
            "",
            "end",
            values=(
                s[0],  # id
                s[2],  # nome
                s[5]   # login
            )
        )

# -------------------------------
# CADASTRAR SITE
# -------------------------------

def cadastrar_site_ui(user_id,tabela):

    win = tk.Toplevel()
    win.title("Novo Site")
    win.geometry("300x420")

    labels = [
        "Nome",
        "URL",
        "Tipo Login",
        "Login",
        "Senha",
        "Senha Saque",
        "Tipo Saque",
        "Info Saque"
    ]

    campos = {}

    for l in labels:

        tk.Label(win,text=l).pack()

        if l == "Tipo Login":

            e = ttk.Combobox(
                win,
                values=["CPF","Email","Celular","Usuario"]
            )

        elif l == "Tipo Saque":

            e = ttk.Combobox(
                win,
                values=[
                    "CPF",
                    "Email",
                    "Celular",
                    "Chave Aleatoria"
                ]
            )

        else:

            e = tk.Entry(win)

        e.pack()

        campos[l] = e


    def salvar():

        cadastrar_site(
            user_id,
            campos["Nome"].get(),
            campos["URL"].get(),
            campos["Tipo Login"].get(),
            campos["Login"].get(),
            campos["Senha"].get(),
            campos["Senha Saque"].get(),
            campos["Tipo Saque"].get(),
            campos["Info Saque"].get()
        )

        atualizar_sites(tabela,user_id)

        win.destroy()


    ttk.Button(
        win,
        text="Salvar",
        command=salvar
    ).pack(pady=10)



# -------------------------------
# EDITAR SITE
# -------------------------------

def editar_site(tabela,user_id):

    item = tabela.selection()

    if not item:
        return

    site_id = tabela.item(item)["values"][0]

    site = obter_site(site_id)

    win = tk.Toplevel()
    win.title("Editar Site")
    win.geometry("300x420")

    labels = [
        "Nome",
        "URL",
        "Tipo Login",
        "Login",
        "Senha",
        "Senha Saque",
        "Tipo Saque",
        "Info Saque"
    ]

    valores = [
        site[2],
        site[3],
        site[4],
        site[5],
        site[6],
        site[7],
        site[8],
        site[9]
    ]

    campos = {}

    for i,l in enumerate(labels):

        tk.Label(win,text=l).pack()

        if l == "Tipo Login":

            e = ttk.Combobox(
                win,
                values=["CPF","Email","Celular","Usuario"]
            )

        elif l == "Tipo Saque":

            e = ttk.Combobox(
                win,
                values=[
                    "CPF",
                    "Email",
                    "Celular",
                    "Chave Aleatoria"
                ]
            )

        else:

            e = tk.Entry(win)

        e.insert(0,valores[i])

        e.pack()

        campos[l] = e


    def salvar():

        atualizar_site(
            site_id,
            campos["Nome"].get(),
            campos["URL"].get(),
            campos["Tipo Login"].get(),
            campos["Login"].get(),
            campos["Senha"].get(),
            campos["Senha Saque"].get(),
            campos["Tipo Saque"].get(),
            campos["Info Saque"].get()
        )

        atualizar_sites(tabela,user_id)

        win.destroy()


    ttk.Button(
        win,
        text="Atualizar",
        command=salvar
    ).pack(pady=10)

# -------------------------------
# EXCLUIR SITE
# -------------------------------

def remover_site_ui(tabela,user_id):

    item = tabela.selection()

    if not item:
        return

    site_id = tabela.item(item)["values"][0]

    excluir_site(site_id)

    atualizar_sites(tabela,user_id)



# -------------------------------
# ABRIR SITE
# -------------------------------

def abrir_site(tabela):

    item = tabela.selection()

    if not item:
        return

    site_id = tabela.item(item)["values"][0]

    win = tk.Toplevel()
    win.title("Referidos")
    win.geometry("800x400")


    tabela_ref = ttk.Treeview(
        win,
        columns=("id","login","deposito"),
        show="headings"
    )

    tabela_ref.heading("id",text="ID")
    tabela_ref.heading("login",text="Login")
    tabela_ref.heading("deposito",text="Deposito")

    tabela_ref.pack(fill="both",expand=True)


    atualizar_refs(tabela_ref,site_id)


    tabela_ref.bind(
        "<Double-1>",
        lambda e:ver_ref(tabela_ref)
    )


    frame = tk.Frame(win)
    frame.pack(pady=5)


    ttk.Button(
        frame,
        text="Novo Referido",
        command=lambda:novo_ref(site_id,tabela_ref)
    ).pack(side="left",padx=5)


    ttk.Button(
        frame,
        text="Editar Referido",
        command=lambda:editar_ref(tabela_ref,site_id)
    ).pack(side="left",padx=5)


    ttk.Button(
        frame,
        text="Excluir Referido",
        command=lambda:excluir_ref(tabela_ref,site_id)
    ).pack(side="left",padx=5)



# -------------------------------
# ATUALIZAR REFERIDOS
# -------------------------------

def atualizar_refs(tabela,site_id):

    for i in tabela.get_children():
        tabela.delete(i)

    refs = listar_referidos(site_id)

    for r in refs:

        tabela.insert(
            "",
            "end",
            values=(
                r[0],
                r[2],
                r[7]
            )
        )

# -------------------------------
# NOVO REFERIDO
# -------------------------------

def novo_ref(site_id,tabela):

    win = tk.Toplevel()
    win.title("Novo Referido")

    labels = [
        "Login",
        "Senha",
        "Senha Saque",
        "Tipo Saque",
        "Info Saque",
        "Deposito"
    ]

    campos = {}

    for l in labels:

        tk.Label(win,text=l).pack()

        if l == "Tipo Saque":

            e = ttk.Combobox(
                win,
                values=[
                    "CPF",
                    "Email",
                    "Celular",
                    "Chave Aleatoria"
                ]
            )

        else:

            e = tk.Entry(win)

        e.pack()

        campos[l] = e


    def salvar():

        cadastrar_referido(
            site_id,
            campos["Login"].get(),
            campos["Senha"].get(),
            campos["Senha Saque"].get(),
            campos["Tipo Saque"].get(),
            campos["Info Saque"].get(),
            campos["Deposito"].get()
        )

        atualizar_refs(tabela,site_id)

        win.destroy()


    ttk.Button(win,text="Salvar",command=salvar).pack(pady=10)



# -------------------------------
# VER REFERIDO
# -------------------------------

def ver_ref(tabela):

    item = tabela.selection()

    if not item:
        return

    ref_id = tabela.item(item)["values"][0]

    ref = obter_referido(ref_id)

    txt = f"""
Login: {ref[2]}
Senha: {ref[3]}

Senha Saque: {ref[4]}
Tipo Saque: {ref[5]}
Info Saque: {ref[6]}

Deposito: {ref[7]}
"""

    messagebox.showinfo("Detalhes",txt)



# -------------------------------
# EDITAR REFERIDO
# -------------------------------

def editar_ref(tabela,site_id):

    item = tabela.selection()

    if not item:
        return

    ref_id = tabela.item(item)["values"][0]

    ref = obter_referido(ref_id)

    win = tk.Toplevel()
    win.title("Editar Referido")

    labels = [
        "Login",
        "Senha",
        "Senha Saque",
        "Tipo Saque",
        "Info Saque",
        "Deposito"
    ]

    valores = ref[2:8]

    campos = {}

    for i,l in enumerate(labels):

        tk.Label(win,text=l).pack()

        if l == "Tipo Saque":

            e = ttk.Combobox(
                win,
                values=[
                    "CPF",
                    "Email",
                    "Celular",
                    "Chave Aleatoria"
                ]
            )

        else:

            e = tk.Entry(win)

        e.insert(0,valores[i])

        e.pack()

        campos[l] = e


    def salvar():

        atualizar_referido(
            ref_id,
            campos["Login"].get(),
            campos["Senha"].get(),
            campos["Senha Saque"].get(),
            campos["Tipo Saque"].get(),
            campos["Info Saque"].get(),
            campos["Deposito"].get()
        )

        atualizar_refs(tabela,site_id)

        win.destroy()


    ttk.Button(win,text="Atualizar",command=salvar).pack(pady=10)



# -------------------------------
# EXCLUIR REFERIDO
# -------------------------------

def excluir_ref(tabela,site_id):

    item = tabela.selection()

    if not item:
        return

    ref_id = tabela.item(item)["values"][0]

    excluir_referido(ref_id)

    atualizar_refs(tabela,site_id)

def novo_ref(site_id,tabela):

    win = tk.Toplevel()
    win.title("Cadastrar Referido")
    win.geometry("300x350")

    labels = [
        "Login",
        "Senha",
        "Senha Saque",
        "Tipo Saque",
        "Info Saque",
        "Deposito"
    ]

    campos = {}

    for l in labels:

        tk.Label(win,text=l).pack(pady=3)

        if l == "Tipo Saque":

            e = ttk.Combobox(
                win,
                values=[
                    "CPF",
                    "Email",
                    "Celular",
                    "Chave Aleatoria"
                ]
            )

        else:

            e = tk.Entry(win)

        e.pack()

        campos[l] = e


    def salvar():

        cadastrar_referido(
            site_id,
            campos["Login"].get(),
            campos["Senha"].get(),
            campos["Senha Saque"].get(),
            campos["Tipo Saque"].get(),
            campos["Info Saque"].get(),
            campos["Deposito"].get()
        )

        atualizar_refs(tabela,site_id)

        win.destroy()

    ttk.Button(
        frame,
        text="➕ Cadastrar Referido",
        command=lambda: novo_ref(site_id, tabela_ref)
    ).pack(side="left", padx=5)