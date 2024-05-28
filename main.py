from flask import Flask, render_template , redirect , request , session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from views import *
#classe para cadastrar o candidato

app = Flask(__name__)

app.config.from_pyfile('config.py')

app.secret_key = 'aulastestsfecaf'
db = SQLAlchemy(app)
if __name__ == '__main__':
    app.run(debug=True)