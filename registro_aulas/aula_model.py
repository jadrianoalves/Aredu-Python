from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Aula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer)
    disciplina_id = db.Column(db.Integer)
    docente_id = db.Column(db.Integer)
    descricao = db.Column(db.String(100))
    registrado_por = db.Column(db.String(10))
    aulas_seguidas = db.Column(db.Integer)
    data_avaliacao = db.Column(db.Date)
    data_registro = db.Column(db.Date)
    conteudo = db.Column(db.String(100))
    metodologia = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class Aula(SQLAlchemyAutoSchema):
    class Meta:
        model = Aula
        load_instance = True
