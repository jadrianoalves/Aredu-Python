from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()
ma = Marshmallow()

class Escola(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    situacao = db.Column(db.String(255))
    contato = db.Column(db.String(20))
    email = db.Column(db.String(255))
    endereco_logradouro = db.Column(db.String(255))
    endereco_numero = db.Column(db.String(10))
    endereco_complemento = db.Column(db.String(10))
    endereco_bairro = db.Column(db.String(100))
    endereco_cep = db.Column(db.String(100))
    endereco_cidade = db.Column(db.Integer)
    endereco_localidade = db.Column(db.String(100))
    localizacao_diferenciada = db.Column(db.String(100))
    pasta_id = db.Column(db.String(100))
    data_inscricao = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class EscolaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Escola
        load_instance = True


        