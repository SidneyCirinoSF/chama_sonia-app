# 🎫 Sistema de Tickets (Django)

Um sistema simples de gerenciamento de tickets desenvolvido com
**Django**, utilizando uma arquitetura modular com dois apps principais:

-   **user** → gerenciamento de usuários\
-   **ticket** → criação e controle de tickets

O objetivo deste projeto é fornecer uma base sólida para CRUDs,
autenticação, relacionamento entre modelos e uma estrutura escalável
para aplicações Django.

------------------------------------------------------------------------

## 🚀 Tecnologias utilizadas

-   **Python 3.13**
-   **Django**
-   **SQLite (desenvolvimento)**
-   **Virtualenv**
-   **Padrão MVC/MVT do Django**

------------------------------------------------------------------------

## 📁 Estrutura do projeto

A estrutura do projeto segue o padrão recomendado pelo Django:

    chama_sonia/
    │ manage.py
    │ requirements.txt
    │ db.sqlite3 (ignorado no git)
    │
    ├── chama_sonia/    # Configurações principais do projeto
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    │
    ├── user/           # App de usuários
    │   ├── models.py
    │   ├── admin.py
    │   ├── views.py
    │   └── migrations/
    │
    └── ticket/         # App de tickets
        ├── models.py
        ├── admin.py
        ├── views.py
        └── migrations/

------------------------------------------------------------------------

## 📦 Instalação e uso

### 1️⃣ Clone o repositório

``` bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2️⃣ Crie e ative o ambiente virtual

``` bash
python -m venv venv
```

**Windows**

``` bash
venv\Scripts\activate
```

**Mac/Linux**

``` bash
source venv/bin/activate
```

### 3️⃣ Instale as dependências

``` bash
pip install -r requirements.txt
```

### 4️⃣ Execute as migrações do banco

``` bash
python manage.py migrate
```

### 5️⃣ Crie um superusuário

``` bash
python manage.py createsuperuser
```

### 6️⃣ Inicie o servidor

``` bash
python manage.py runserver
```

Acesse em:\
👉 http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🧩 Funcionalidades implementadas

-   Cadastro de usuários\
-   Login e autenticação\
-   CRUD de tickets\
-   Organização modular com apps independentes\
-   Painel administrativo completo (Django Admin)

------------------------------------------------------------------------

## 🛡️ Segurança e boas práticas

O repositório inclui um `.gitignore` personalizado contendo:

-   Ambiente virtual\
-   Banco de dados local\
-   Arquivos sensíveis e temporários\
-   Caches e pyc\
-   Pastas de IDE

------------------------------------------------------------------------

