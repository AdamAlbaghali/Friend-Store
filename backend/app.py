#UPDATE FOR DEPLOYMENT
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
  app.run(debug=True, port=5001)

##first we run these two:
##export FLASK_APP=app.py
##export FLASK_ENV=development

## to check we have to run:
## echo $FLASK_APP  # Should output: app.py
## echo $FLASK_ENV  # Should output: development


## when running since we are using port 5001 we run: flask run --port=5001
