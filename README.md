# 📇 MEYU – Agenda de Contatos em Django

**MEYU** é uma aplicação web feita com Django que funciona como uma agenda de contatos simples, prática e moderna. É um projeto ideal para demonstrar conhecimentos em desenvolvimento backend com Python e Django, além do uso de templates, formulários e autenticação.

![Django](https://img.shields.io/badge/Django-4.x-green)   ![Python](https://img.shields.io/badge/Python-3.11-blue)   ![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

---

## 🚀 Funcionalidades

- 🔐 Sistema de autenticação (login/logout)
- 📄 Cadastro de contatos com nome, telefone, e-mail, imagem e categoria
- 🔎 Filtro e busca de contatos por nome
- ✏️ Edição e exclusão de contatos
- 🧾 Formulários personalizados com mensagens de erro
- 🧩 Organização de contatos por categorias
- 🖼 Upload de fotos para cada contato
- 🔒 Somente usuários autenticados acessam os dados

---

## 🧠 Tecnologias Utilizadas

- [Python 3.11+](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- HTML + CSS (via Templates Django)
- SQLite/PostgreeSQL (como banco de dados padrão)

---

## 📂 Estrutura do Projeto

Contact-Me-Agend/
```bash
├── AddressBook/ # Configurações do projeto Django
│ ├── settings.py
│ ├── urls.py
├── contacts/ # App principal da agenda
│ ├── models.py
│ ├── views/
│ │ └── contact_views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/
├── db.sqlite3 # Banco de dados local
├── manage.py
```
---

## ⚙️ Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/napolisiqueira/Contact-Me-Agend.git
cd Contact-Me-Agend
Crie um ambiente virtual:
```
2. Recomendação: Use o UV UltraViolet para fazer seu ambiente virtual ou Poetry.
```bash
uv init #para inicializar um projeto
uv venv #para criar o ambiente virtual
uv sync # para instalar as dependecias do pyproject.toml
```
3. Crie o ambiente virtual caso faça com o metodo padrão do python.
```bash
python -m venv .venv # crie um ambiente virtual
.venv\Scripts\activate # Ative no Windows:
source .venv/bin/activate # Ou no Linux/macOS:
```
4. Instale as dependências:
```bash
pip install -r requirements.txt  # ou use `uv pip install -r requirements.txt`
```
5. Rode as migrações:
```bash
python manage.py migrate
```
6. (Opcional) Crie um superusuário:
```
python manage.py createsuperuser
```
7. Inicio o servidor:
```
python manage.py runserver
```

## 📌 Próximas Melhorias
-  Paginação da lista de contatos

-  Upload de arquivos otimizado

-  Integração com API externa (WhatsApp, e-mail)

-  Melhorar responsividade com Bootstrap

-  Exportar contatos para CSV/PDF

-  Adicionar testes automatizados

---

### 👨‍💻 Autor
Desenvolvido por Felipe Napoli Siqueira
- 📫 napolisiqueira@gmail.com
- 🔗 github.com/napolisiqueira

---

### 📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.