import tkinter as tk
from tkinter import messagebox

from auth.register import registrar


def register_screen():

    win = tk.Tk()

    win.title("Cadastro")
    win.geometry("300x250")

    tk.Label(win, text="Usuario").pack(pady=5)

    user = tk.Entry(win)
    user.pack()

    tk.Label(win, text="Senha").pack(pady=5)

    senha = tk.Entry(win, show="*")
    senha.pack()

    def salvar():

        ok = registrar(user.get(), senha.get())

        if ok:

            messagebox.showinfo("Sucesso", "Conta criada")

            # IMPORT INTERNO
            from ui.login_ui import login_screen

            win.destroy()
            login_screen()

        else:

            messagebox.showerror("Erro", "Usuario já existe")

    tk.Button(
        win,
        text="Cadastrar",
        command=salvar
    ).pack(pady=15)

    win.mainloop()