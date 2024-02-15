from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Direcao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    profissional_id = db.Column(db.Integer)
    funcao = db.Column(db.String(100))
    inicio_atividade = db.Column(db.Date)
    fim_atividade = db.Column(db.Date)
    status = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class Direcao(SQLAlchemyAutoSchema):
    class Meta:
        model = Direcao
        load_instance = True
