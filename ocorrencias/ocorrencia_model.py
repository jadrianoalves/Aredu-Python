from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()
ma = Marshmallow()

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer)
    nome = db.Column(db.String(100))

    # Relacionamento com Ocorrencia
    ocorrencia_id = db.Column(db.Integer, db.ForeignKey('ocorrencia.id'))
    ocorrencia = db.relationship('Ocorrencia', back_populates='alunos')

class Ocorrencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer)
    docente_id = db.Column(db.Integer)
    descricao = db.Column(db.String(100))
    registrado_por = db.Column(db.String(100))
    data_ocorrencia = db.Column(db.Date)
    hora_ocorrencia = db.Column(db.Time)
    data_registro = db.Column(db.Date)

    # Relacionamento com Aluno
    alunos = db.relationship('Aluno', back_populates='ocorrencia')

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class AlunoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Aluno
        load_instance = True

class OcorrenciaSchema(SQLAlchemyAutoSchema):
    alunos = ma.Nested(AlunoSchema, many=True)  # Adiciona a relação na schema
    class Meta:
        model = Ocorrencia
        load_instance = True
