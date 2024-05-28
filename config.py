import urllib.parse

SECRET_KEY = 'aulastestsfecaf'


# Codificar senha corretamente
senha = urllib.parse.quote_plus('Buh@1202')

SQLALCHEMY_DATABASE_URI = (
    'mysql+mysqlconnector://{usuario}:{senha}@{servidor}/{database}'.format(
        usuario='root',
        senha=senha,
        servidor='localhost',
        database='Exame_Candidates'
    )
)
SQLALCHEMY_TRACK_MODIFICATIONS = False