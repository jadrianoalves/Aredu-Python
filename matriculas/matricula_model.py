from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Matricula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ano_letivo = db.Column(db.String(4))
    aluno_id = db.Column(db.Integer)
    aluno_nome = db.Column(db.String(255))
    turma_id = db.Column(db.Integer)
    turma_nome = db.Column(db.String(255))
    turma_turno = db.Column(db.String(10))
    responsavel_nome = db.Column(db.String(255))
    responsavel_id = db.Column(db.Integer)
    responsavel_parentesco = db.Column(db.String(50))
    data_matricula = db.Column(db.Date)
    escola_origem = db.Column(db.String(255))
    fardamento = db.Column(db.String(1))
    transporte = db.Column(db.String(3))
    tipo = db.Column(db.String(50))
    observacoes = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50))
    pasta_aluno_id = db.Column(db.String(36))
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)


class MatriculaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Matricula
        load_instance = True  # Carregar instância do modelo