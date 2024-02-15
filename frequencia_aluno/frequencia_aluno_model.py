from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Frequencia_Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    frequencia_id = db.Column(db.Integer)
    disciplina_id = db.Column(db.Integer)
    data_aula = db.Column(db.DateTime)
    aluno_id = db.Column(db.Integer)
    aluno_nome = db.Column(db.Text)
    presente = db.Column(db.Integer)
    ausente = db.Column(db.Integer)
    justificado = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class Frequencia_Aluno(SQLAlchemyAutoSchema):
    class Meta:
        model = Frequencia_Aluno
        load_instance = True
