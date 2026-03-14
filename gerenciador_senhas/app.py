from database.db import criar_banco
from ui.login_ui import login_screen


def main():

    criar_banco()

    login_screen()


if __name__ == "__main__":
    main()