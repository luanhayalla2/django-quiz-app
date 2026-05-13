# 🎓 Django Quiz App

Uma aplicação web desenvolvida em Django para criação, gerenciamento e resolução de quizzes. Este projeto foi configurado e aprimorado como parte da atividade prática de testes e validação de software.

## 🚀 Funcionalidades Principais

O sistema foi validado e atualizado para garantir o funcionamento das seguintes áreas:

*   **Autenticação de Usuários**: Login seguro e funcionalidade de Logout.
*   **Cadastro (Registro)**: Criação de novas contas de usuário pela interface pública.
*   **Acesso Administrativo**: Painel de administração (`/admin`) exclusivo para superusuários gerenciarem quizzes, perguntas e usuários.
*   **Navegação e Interface**: Interface de usuário moderna (UI premium) e navegação contínua entre as páginas (Home, Login, Register, Quizzes).
*   **Resolução de Quizzes**: Seleção e resposta de questionários armazenados no banco de dados.

## 🛠️ Tecnologias Utilizadas

*   **Backend**: Python 3.x, Django 4.2+
*   **Banco de Dados**: SQLite (configurado localmente para desenvolvimento/testes)
*   **Frontend**: HTML5, CSS3 (Custom Premium UI), Google Fonts (Inter)
*   **Gerenciamento de Dependências**: Pip e Virtualenv

## 📋 Pré-requisitos

Para executar o projeto localmente, você precisará de:

*   Python 3.8 ou superior instalado.
*   Gerenciador de pacotes `pip`.
*   Acesso ao terminal (PowerShell, CMD, ou Bash).

## ⚙️ Como Configurar e Executar

Siga os passos abaixo para preparar o ambiente de testes e executar o servidor local:

### 1. Clonar o Repositório

```bash
git clone <url-do-repositorio>
cd django-quiz-app-main/src
```

### 2. Criar e Ativar o Ambiente Virtual

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente (Windows)
.\venv\Scripts\activate

# Ativar o ambiente (Linux/Mac)
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
# ou instale os pacotes base essenciais caso haja conflito:
pip install django python-dotenv whitenoise django-environ
```

### 4. Executar as Migrações do Banco de Dados

O projeto utiliza SQLite para testes locais. Antes de rodar as migrações, certifique-se de ter apagado os arquivos `.py` (exceto `__init__.py`) da pasta `src/quizzes/migrations/` se houver conflitos com PostgreSQL.

```bash
python manage.py makemigrations quizzes
python manage.py migrate
```

### 5. Carregar Dados de Exemplo (Opcional)

Carregue o arquivo de configuração (fixture) para popular o banco de dados com quizzes iniciais:

```bash
python manage.py loaddata seed_data
```

### 6. Criar Superusuário (Acesso Administrativo)

Crie uma conta de administrador para gerenciar o sistema:

```bash
python manage.py createsuperuser
# Siga as instruções no terminal para definir usuário, e-mail e senha.
```

### 7. Executar o Servidor Local

```bash
python manage.py runserver
```

Acesse o sistema no seu navegador:
*   **Página Inicial**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
*   **Painel Admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 🧪 Evidências de Teste

Durante a validação, as seguintes evidências foram geradas:

1.  **Servidor em Execução**: Print do terminal confirmando o Django rodando sem erros.
2.  **Interface de Usuário**: Prints da tela inicial, fluxos de login e cadastro.
3.  **Acesso Administrativo**: Validação do painel de controle do superusuário logado.

*Este projeto foi revisado e mantido para atender aos critérios da Atividade Prática.*
