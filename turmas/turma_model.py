from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    escola_id = db.Column(db.Integer)
    nome = db.Column(db.String(255), nullable=False)
    ano_letivo = db.Column(db.Integer, nullable=False)
    turno = db.Column(db.String(10), nullable=False)
    modalidade = db.Column(db.String(255))
    serie = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class TurmaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Turma
        load_instance = True