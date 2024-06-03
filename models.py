from main import db
class Usuarios(db.Model):
    __tablename__ = 'users'
    id_user = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name_user = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(50), nullable=False)
    passW = db.Column(db.String(20), nullable=False)
    def __repr__(self):
            return '<name %r>' %self.name

class Candidates(db.Model):
    id_candidate = db.Column(db.Integer, primary_key = True, autoincrement = True)
    candidateName  = db.Column(db.String(50), nullable =  False)
    curseCandidate = db.Column(db.String(50), nullable =  False)
    testName = db.Column(db.String(50), nullable =  False)
    coordenatorCandidate = db.Column(db.String(50), nullable =  False)
    def __repr__(self):
            return '<name %r>' %self.name

class exame(db.Model):
    id_exame = db.Column(db.Integer, primary_key = True, autoincrement = True)
    note =db.Column(db.String(50), nullable =  False)
    stats = db.Column(db.Boolean(), nullable =  False)
    def __repr__(self):
            return '<name %r>' %self.name
