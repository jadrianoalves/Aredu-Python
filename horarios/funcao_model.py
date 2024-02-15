from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Horario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer)
    dia_semana = db.Column(db.String(255))
    disciplina = db.Column(db.String(255))
    aula = db.Column(db.Integer)
    aulas_seguidas = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class HorarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Horario
        load_instance = True