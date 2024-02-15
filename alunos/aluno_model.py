from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()
ma = Marshmallow()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    sexo = db.Column(db.String(10))
    data_nasc = db.Column(db.Date)
    mae = db.Column(db.String(100))
    mae_profissao = db.Column(db.String(100))
    pai = db.Column(db.String(100))
    pai_profissao = db.Column(db.String(100))
    naturalidade = db.Column(db.String(100))
    naturalidade_uf = db.Column(db.String(10))
    endereco_logradouro = db.Column(db.String(255))
    endereco_numero = db.Column(db.String(10))
    endereco_cep = db.Column(db.String(10))
    endereco_bairro = db.Column(db.String(100))
    endereco_cidade = db.Column(db.String(100))
    endereco_uf = db.Column(db.String(10))
    local_residencia = db.Column(db.String(100))
    cpf = db.Column(db.String(15))
    nacionalidade = db.Column(db.String(50))
    obs = db.Column(db.Text)
    racacor = db.Column(db.String(50))
    deficiencias = db.Column(db.Text)
    nivel_suporte = db.Column(db.String(50))
    codigo_cid = db.Column(db.String(10))
    data_diagnostico = db.Column(db.Date)
    descricao_deficiencia = db.Column(db.Text)
    necessidades_especificas = db.Column(db.Text)
    pasta_id = db.Column(db.Text)
    status = db.Column(db.String(20))
    data_inscricao = db.Column(db.DateTime)
    

class AlunoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Aluno
        load_instance = True  # Carregar instância do modelo
