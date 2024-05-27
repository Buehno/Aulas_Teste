from flask import Flask, Request, redirect, render_template

app = Flask(__name__)

app.secret_key = 'aulastestsfecaf'
@app.route('/')
def telaInicial():
    return render_template('Index.html',)

app.run(debug=True)