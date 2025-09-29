import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.config['HOST'] = '0.0.0.0'
app.config['PORT'] = 8000
app.config['DEBUG'] = True


app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
    "DATABASE_URL",
    "postgresql://databaseapartamento_dyo1_user:nNN1iEvn0cNmqcDG4aHFxKhG8yZlOSw0@dpg-d3d0ss0gjchc739jp9o0-a.oregon-postgres.render.com/databaseapartamento_dyo1"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)