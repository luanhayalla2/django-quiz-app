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

## 🧪 Testes Automatizados (Pytest)

O projeto conta com uma suíte de testes robusta e automatizada integrada com o **Pytest** e o **pytest-django**, garantindo proteção contra regressões e validação contínua de rotas críticas:

### Como Executar os Testes:
```bash
# Executar todos os testes no ambiente virtual
pytest
```

### Funcionalidades Testadas:
* **Acessibilidade do Login:** Verifica se a rota `/accounts/login/` está ativa (HTTP 200) e exibe os elementos corretos da interface.
* **Fluxos de Redirecionamento:** Valida se o login e o logout redirecionam com segurança o usuário de volta à página inicial (`LOGIN_REDIRECT_URL` e `LOGOUT_REDIRECT_URL`).
* **Visualização e Validação do Quiz:** Testes unitários e de integração para a listagem e submissão de respostas de quizzes.

---

## 🎨 Ajustes Finos de Layout e Usabilidade Recentes

### 1. Botão de Retorno (Back Button)
Adicionado um botão elegante e responsivo **"← Back to Quizzes"** no topo da tela de resolução de perguntas (`display.html`), facilitando a navegação de volta para a lista geral de quizzes a qualquer momento.

### 2. Resolução do Bug de Redirecionamento 404
Correção de um bug de fluxo de autenticação onde o Django redirecionava por padrão para `/accounts/profile/` (gerando um erro 404). O fluxo foi padronizado para a home page (`/`) e coberto por testes.

### 3. Correção de Formato do Banco de Dados (seed_data.json)
Resolução de um bug visual onde as datas e opções de múltipla escolha se dividiam caractere por caractere verticalmente. Os dados agora carregam como uma estrutura JSON nativa válida (`choices`), renderizando em caixas organizadas e fáceis de ler.

### 4. Perguntas Atualizadas para a Última Versão do Python
O banco de dados de exemplo foi atualizado de forma dinâmica para incluir as versões estáveis mais recentes do Python (3.12 e 3.13) na pergunta de trivia correspondente.

---

## 📋 Relatório Completo de Evidências

Todo o histórico de comandos executados, logs do terminal, arquivos de testes e capturas de tela estão catalogados no documento oficial:
> 📂 **Acesse aqui:** [evidencias_django_quiz.md](file:///C:/Users/aluno/.gemini/antigravity/brain/4364d40d-9c59-48a4-b595-6dec5ba9c9ae/evidencias_django_quiz.md)

