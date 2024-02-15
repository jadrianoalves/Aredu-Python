from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class ProfissionalSala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer)
    nome = db.Column(db.String(100))
    profissional_id = db.Column(db.String(100))
    funcao = db.Column(db.String(100))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
class ProfissionalSala(SQLAlchemyAutoSchema):
    class Meta:
        model = ProfissionalSala
        load_instance = True
