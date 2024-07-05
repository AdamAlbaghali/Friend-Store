from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

print(f"Current working directory: {os.getcwd()}")
print(f"Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

import routes

with app.app_context():
  db.create_all()

if __name__ == "__main__":
  app.run(debug=True)

