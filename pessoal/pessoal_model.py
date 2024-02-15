from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Pessoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    profissional_id = db.Column(db.Integer)
    funcao = db.Column(db.String(100))
    inicio_atividade = db.Column(db.Date)
    fim_atividade = db.Column(db.Date)
    pasta_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class PessoalSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pessoal
        load_instance = True