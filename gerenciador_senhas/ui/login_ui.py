import tkinter as tk
from tkinter import messagebox

from auth.login import login
from ui.dashboard_ui import dashboard


def login_screen():

    win = tk.Tk()
    win.title("Login")
    win.geometry("300x250")

    tk.Label(win, text="Usuario").pack(pady=5)

    user = tk.Entry(win)
    user.pack()

    tk.Label(win, text="Senha").pack(pady=5)

    senha = tk.Entry(win, show="*")
    senha.pack()

    def entrar():

        uid = login(user.get(), senha.get())

        if uid:

            win.destroy()
            dashboard(uid)

        else:

            messagebox.showerror("Erro", "Login inválido")

    def abrir_cadastro():

        from ui.register_ui import register_screen

        win.destroy()
        register_screen()

    tk.Button(
        win,
        text="Entrar",
        command=entrar
    ).pack(pady=10)

    tk.Button(
        win,
        text="Cadastrar",
        command=abrir_cadastro
    ).pack()

    win.mainloop()