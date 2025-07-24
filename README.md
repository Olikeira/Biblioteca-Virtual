<h1 align="center">
  📚 Biblioteca Online com Flask e Firebase
</h1>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img alt="Firebase" src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black"/>
  <img alt="Bootstrap" src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
</p>

<p align="center">
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-funcionalidades">Funcionalidades</a> •
  <a href="#-demonstração-visual">Demonstração</a> •
  <a href="#️-pilha-de-tecnologias">Tecnologias</a> •
  <a href="#-configuração-e-execução">Execução</a> •
  <a href="#-autor">Autor</a>
</p>

## 📖 Sobre o Projeto

Aplicação web full-stack que simula o funcionamento de uma biblioteca online. O projeto utiliza **Flask** (Python) para o backend, responsável por servir as páginas, e integra-se com o **Firebase** para gerenciar a autenticação de usuários e o banco de dados em tempo real.

## 🚀 Funcionalidades

* **Autenticação de Usuários:** Sistema completo de login e cadastro utilizando o *Firebase Authentication*.
* **Rotas Protegidas:** Acesso à página principal da biblioteca (`home.html`) somente para usuários autenticados.
* **Validação de Formulários:** Validações em tempo real nos formulários de login e registro para melhorar a experiência do usuário.
* **Interface Reativa:** Uso de JavaScript para interagir com o backend e o Firebase sem a necessidade de recarregar a página.
* **(WIP) Gestão de Livros:** Estrutura pronta para implementar funcionalidades de listagem, busca e empréstimo de livros, utilizando o *Cloud Firestore* ou *Realtime Database*.

## 📸 Demonstração Visual

<p align="center">
  <img width="750" alt="Tela de Login da Biblioteca Online" src="https://github.com/user-attachments/assets/442d6128-dfac-4c02-827d-224fc356c998" />
</p>

## 🛠️ Pilha de Tecnologias

* **Backend:**
    * **Python 3**
    * **Flask** (para o servidor web e roteamento)
* **Frontend:**
    * HTML5
    * CSS3 (com **Bootstrap** para componentização e responsividade)
    * JavaScript (Vanilla)
* **Banco de Dados e Autenticação:**
    * **Firebase Authentication**
    * **Cloud Firestore** / **Realtime Database** (como banco de dados NoSQL)

## ⚙️ Configuração e Execução

Para executar este projeto localmente, siga os passos abaixo.

### 1. Configuração do Firebase
Você precisará de um projeto no Firebase para obter as credenciais de cliente.

1.  Acesse o [Console do Firebase](https://console.firebase.google.com/).
2.  Crie um novo projeto.
3.  No painel do seu projeto, vá para a seção **Authentication** > **Sign-in method** e ative o provedor "E-mail/Senha".
4.  Ainda no painel, clique no ícone de engrenagem > **Configurações do projeto**.
5.  Na aba "Geral", role para baixo até "Seus apps" e crie um novo **Aplicativo da Web** (ícone `</>`).
6.  Copie o objeto de configuração `firebaseConfig`.
7.  Cole esse objeto de configuração dentro do seu arquivo `static/firebase-init.js`.

### 2. Configuração do Ambiente Local

> **Nota Importante:** Seu projeto precisa de um arquivo `requirements.txt` para que outras pessoas possam instalar as dependências. Para gerá-lo, ative seu ambiente virtual e execute: `pip freeze > requirements.txt`. Depois, adicione-o ao seu repositório.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Olikeira/biblioteca-online-projeto-DB-e-Firebase.git](https://github.com/Olikeira/biblioteca-online-projeto-DB-e-Firebase.git)
    cd biblioteca-online-projeto-DB-e-Firebase
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS / Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Este comando funcionará depois que você criar o arquivo `requirements.txt`. No mínimo, ele deve conter `Flask`)*.

4.  **Execute a aplicação:**
    ```bash
    flask run
    ```
    *(Ou, dependendo da configuração: `python main.py`)*

5.  Acesse `http://127.0.0.1:5000` no seu navegador.

## 📂 Estrutura do Projeto
```
.
├── main.py             # Arquivo principal da aplicação Flask
├── static/             # Arquivos estáticos (CSS, JS)
│   ├── BS.css          # Estilos do Bootstrap
│   ├── *.js            # Scripts de cada página
│   └── *.css           # Estilos customizados
└── templates/          # Moldes HTML renderizados pelo Flask
    ├── indexprojeto.html # Página de login
    ├── register.html   # Página de cadastro
    └── home.html       # Página principal (usuários logados)
```

## 👨‍💻 Autor

**Lucas de Oliveira Pereira**

* LinkedIn: [`lucas-de-oliveira-pereira-741936272`](https://www.linkedin.com/in/lucas-de-oliveira-pereira-741936272/)
* GitHub: [`Olikeira`](https://github.com/Olikeira)
