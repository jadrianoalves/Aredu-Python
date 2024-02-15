from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Frequencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer)
    disciplina_id = db.Column(db.Integer)
    docente_id = db.Column(db.Integer)
    registrado_por = db.Column(db.String(10))
    aulas_seguidas = db.Column(db.Integer)
    data_aula = db.Column(db.Date)
    data_registro = db.Column(db.Date)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class Frequencia(SQLAlchemyAutoSchema):
    class Meta:
        model = Frequencia
        load_instance = True
