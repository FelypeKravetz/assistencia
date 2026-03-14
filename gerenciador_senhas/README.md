# Gerenciador de Sites e Referidos

Sistema desktop desenvolvido em **Python + Tkinter + SQLite** para gerenciar:

* Sites cadastrados
* Dados de login
* Informações de saque
* Contas referidas vinculadas a cada site

O sistema permite organizar credenciais e contas relacionadas a diferentes plataformas de forma simples e segura.

---

# Funcionalidades

## Autenticação

* Cadastro de usuário
* Login seguro
* Logout

## Gerenciamento de Sites

* Cadastrar novo site
* Editar site
* Excluir site
* Visualizar lista de sites
* Armazenar:

  * Nome do site
  * URL
  * Tipo de login
  * Login
  * Senha
  * Senha de saque
  * Tipo de saque
  * Informação de saque

Tipos de login disponíveis:

* CPF
* Email
* Celular
* Usuário

Tipos de saque disponíveis:

* CPF
* Email
* Celular
* Chave Aleatória

---

## Gerenciamento de Referidos

Cada site pode possuir múltiplos referidos.

Funções disponíveis:

* Cadastrar referido
* Editar referido
* Excluir referido
* Visualizar detalhes

Dados armazenados:

* Login
* Senha
* Senha de saque
* Tipo de saque
* Informação de saque
* Valor de depósito

---

# Estrutura do Projeto

```
gerenciador_senhas/

app.py
config.py

database/
    db.py

auth/
    login.py
    register.py

managers/
    sites_manager.py
    referidos_manager.py

ui/
    login_ui.py
    register_ui.py
    dashboard_ui.py
```

---

# Tecnologias Utilizadas

* Python 3
* Tkinter (interface gráfica)
* SQLite3 (banco de dados local)

---

# Banco de Dados

## Tabela usuarios

| Campo   | Tipo    |
| ------- | ------- |
| id      | INTEGER |
| usuario | TEXT    |
| senha   | TEXT    |

---

## Tabela sites

| Campo       | Tipo    |
| ----------- | ------- |
| id          | INTEGER |
| user_id     | INTEGER |
| nome        | TEXT    |
| url         | TEXT    |
| tipo_login  | TEXT    |
| login       | TEXT    |
| senha       | TEXT    |
| senha_saque | TEXT    |
| tipo_saque  | TEXT    |
| saque_info  | TEXT    |

---

## Tabela referidos

| Campo                | Tipo    |
| -------------------- | ------- |
| id                   | INTEGER |
| site_id              | INTEGER |
| login                | TEXT    |
| senha                | TEXT    |
| saque_senha_referido | TEXT    |
| tipo_saque_referido  | TEXT    |
| saque_info_referido  | TEXT    |
| deposito             | REAL    |

---

# Como Executar

1. Clone ou baixe o projeto

```
git clone projeto
```

2. Acesse a pasta

```
cd gerenciador_senhas
```

3. Execute o sistema

```
python app.py
```

---

# Interface

O sistema possui:

* Tema escuro
* Dashboard com lista de sites
* Tela de gerenciamento de referidos
* Janelas para cadastro e edição de dados

---

# Melhorias Futuras

* Busca de sites
* Mostrar / ocultar senha
* Copiar login e senha
* Relatório de depósitos
* Exportação de dados
* Backup automático do banco
* Interface mais moderna

---

# Licença

Projeto de uso educacional e pessoal.
