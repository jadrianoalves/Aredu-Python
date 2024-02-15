from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Responsavel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    rg = db.Column(db.String(255))
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    profissao_id = db.Column(db.Integer)
    contatos = db.Column(db.String(100))
    email = db.Column(db.String(255))
    endereco_logradouro = db.Column(db.String(255))
    endereco_numero = db.Column(db.String(10))
    endereco_cep = db.Column(db.String(10))
    endereco_bairro = db.Column(db.String(100))
    endereco_cidade = db.Column(db.Integer)
    data_inscricao = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class ResponsavelSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Responsavel
        load_instance = True