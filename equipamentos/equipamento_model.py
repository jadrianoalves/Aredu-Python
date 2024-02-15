from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Equipamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(255))
    modelo = db.Column(db.String(255))
    marca = db.Column(db.String(20))
    data_aquisicao = db.Column(db.Date)
    estado = db.Column(db.String(255))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class EquipamentoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Equipamento
        load_instance = True


        