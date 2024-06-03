from flask import render_template , redirect , request , session, flash, url_for 
from models import Candidates, Usuarios
from main import db, app


#rota para ir a tela inicial
@app.route('/')
def home():
    if 'User_Only' not in session or session['User_Only'] == None:
        return redirect('Login')
    lista = Candidates.query.order_by(Candidates.id_candidate)
    return render_template('Index.html', Candidate = lista )
#rota para ir até a tela de cadastrar um candidato
@app.route("/Candidate")
def registerOne():
    if 'User_Only' not in session or session['User_Only'] == None:
        return redirect('Login')
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
        return redirect(url_for('home'))
    newcandidate = Candidates(candidateName = name, curseCandidate =  curse,  testName =  test, coordenatorCandidate =  coordenator )
    db.session.add(newcandidate)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/Login')
def Login():
    return render_template('login.html')
@app.route('/autenticate', methods=['POST',])
def Autenticate():
    usuario =  Usuarios.query.filter_by(mail =  request.form['txtLogin']).first()
    if usuario:
        if  request.form['txtSenha'] == usuario.passW:
            session['User_Only'] = usuario.name_user
            flash("Usuario Logado")
            return redirect(url_for('home'))
        else:
            flash('senha Incorreta!')
            return redirect(url_for('Login'))
    else:
        flash("Usuario/Senha Incorreta!")
        return render_template('login.html')
    
@app.route("/out")
def  out ():
    session['User_Only'] = None
    return redirect(url_for('Login'))

app.run(debug=True)