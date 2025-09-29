import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Criando a aplicação Flask
app = Flask(__name__)
CORS(app)

# Configurações básicas da aplicação
app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True

# URL do banco de dados (Render)
database_url = os.getenv(
    "DATABASE_URL",
    "postgresql://databaseapartamento_dyo1_user:nNN1iEvn0cNmqcDG4aHFxKhG8yZlOSw0@dpg-d3d0ss0gjchc739jp9o0-a.oregon-postgres.render.com/databaseapartamento_dyo1?sslmode=require"
)

# Garantir que a URL esteja no formato correto para SQLAlchemy
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criando o objeto de banco de dados
db = SQLAlchemy(app)
