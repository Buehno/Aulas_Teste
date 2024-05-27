from flask import Flask, Request, redirect, render_template
#classe para cadastrar o candidato
class Candidate:
    def __init__(self, name , curse, test ,  coordenator):
        self.candidateName = name
        self.CurseCandidate = curse
        self.testName = test
        self.coordenatorCandidate =   coordenator
Candidateone = Candidate('João paulo', 'Analise e Desenvolvimento de Sistemas', 'Matematica Logica Aplicada ','Oswaldo')      

list = [Candidateone]
app = Flask(__name__)

app.secret_key = 'aulastestsfecaf'

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
    name =  Request.form['txtName']
    curse =  Request.form['txtCurse']
    coordenator =  Request.form['txtCoordenator']
    test =  Request.form['txtTest']
    newCandidate = Candidate(name,curse,test, coordenator)
    list.append(newCandidate)
    
    return redirect('/')

app.run(debug=True)