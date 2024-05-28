from flask import render_template , redirect , request , session, flash, url_for 
from models import Candidates, Usuarios
from main import db, app


#rota para ir a tela inicial
@app.route('/')
def home():
    return render_template('Index.html',)
#rota para ir até a tela de cadastrar um candidato
@app.route("/Candidate")
def registerOne():
    return render_template('registerCandidate.html') 

@app.route('/Colect', methods = ['POST' , ])
def Add():
    name =  request.form['txtName']
    curse =  request.form['txtCurse']
    coordenator =  request.form['txtCoordenator']
    test =  request.form['txtTest']

    Candidate = Candidates.query.filter_by(candidateName = name).first()
    if Candidate:
        flash("Candidato ja esta Cadastrado!")
        return redirect("/")
    newcandidate = Candidates(candidateName = name, curseCandidate =  curse,  testName =  test, coordenatorCandidate =  coordenator )
    db.session.add(newcandidate)
    db.session.commit()
    return redirect('/')

app.run(debug=True)