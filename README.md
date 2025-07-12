<body>
    <div class="container">
        <h1>📇 MEYU – Agenda de Contatos em Django</h1>
        <p><strong>MEYU</strong> é uma aplicação web feita com Django que funciona como uma agenda de contatos simples, prática e moderna. É um projeto ideal para demonstrar conhecimentos em desenvolvimento backend com Python e Django, além do uso de templates, formulários e autenticação.</p>
        <p>
            <img src="https://img.shields.io/badge/Django-4.x-green" alt="Django 4.x" class="badge">
            <img src="https://img.shields.io/badge/Python-3.11-blue" alt="Python 3.11" class="badge">
            <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow" alt="Status: Em desenvolvimento" class="badge">
        </p>

  <h2>🚀 Funcionalidades</h2>
  <ul>
      <li>🔐 Sistema de autenticação (login/logout)</li>
      <li>📄 Cadastro de contatos com nome, telefone, e-mail, imagem e categoria</li>
      <li>🔎 Filtro e busca de contatos por nome</li>
      <li>✏️ Edição e exclusão de contatos</li>
      <li>🧾 Formulários personalizados com mensagens de erro</li>
      <li>🧩 Organização de contatos por categorias</li>
      <li>🖼 Upload de fotos para cada contato</li>
      <li>🔒 Somente usuários autenticados acessam os dados</li>
  </ul>

  <h2>🧠 Tecnologias Utilizadas</h2>
  <ul>
      <li><a href="https://www.python.org/">Python 3.11+</a></li>
      <li><a href="https://www.djangoproject.com/">Django</a></li>
      <li>HTML + CSS (via Templates Django)</li>
      <li>SQLite/PostgreSQL (como banco de dados padrão)</li>
  </ul>

  <h2>📂 Estrutura do Projeto</h2>
  <pre><code>Contact-Me-Agend/
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
</code></pre>

  <h2>⚙️ Como Executar Localmente</h2>
  <ol>
      <li><strong>Clone o repositório</strong>:
          <pre><code>git clone https://github.com/napolisiqueira/Contact-Me-Agend.git
cd Contact-Me-Agend</code></pre>
            </li>
            <li><strong>Crie um ambiente virtual</strong>:
                <p>Recomendação: Use o UV UltraViolet para fazer seu ambiente virtual ou Poetry.</p>
                <pre><code>uv init # para inicializar um projeto
uv venv # para criar o ambiente virtual
uv sync # para instalar as dependências do pyproject.toml</code></pre>
                <p>Ou, com o método padrão do Python:</p>
                <pre><code>python -m venv .venv # crie um ambiente virtual
.venv\Scripts\activate # Ative no Windows
source .venv/bin/activate # Ou no Linux/macOS</code></pre>
            </li>
            <li><strong>Instale as dependências</strong>:
                <pre><code>pip install -r requirements.txt  # ou use `uv pip install -r requirements.txt`</code></pre>
            </li>
            <li><strong>Rode as migrações</strong>:
                <pre><code>python manage.py migrate</code></pre>
            </li>
            <li><strong>(Opcional) Crie um superusuário</strong>:
                <pre><code>python manage.py createsuperuser</code></pre>
            </li>
            <li><strong>Inicie o servidor</strong>:
                <pre><code>python manage.py runserver</code></pre>
            </li>
        </ol>

  <h2>👨‍💻 Autor</h2>
  <p>Desenvolvido por Felipe Napoli Siqueira</p>
  <ul>
      <li>📫 <a href="mailto:napolisiqueira@gmail.com">napolisiqueira@gmail.com</a></li>
      <li>🔗 <a href="https://github.com/napolisiqueira">github.com/napolisiqueira</a></li>
  </ul>

</div>
</body>
</html>
