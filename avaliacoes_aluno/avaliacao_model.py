from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer)
    avaliacao_id = db.Column(db.Integer)
    disciplina_id = db.Column(db.Integer)
    docente_id = db.Column(db.Integer)
    aluno_nome = db.Column(db.String(100))
    nota = db.Column(db.Float(100))
    data_avaliacao = db.Column(db.Date)
    avaliacao = db.Column(db.Integer)
    periodo = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class Avaliacao(SQLAlchemyAutoSchema):
    class Meta:
        model = Avaliacao
        load_instance = True
