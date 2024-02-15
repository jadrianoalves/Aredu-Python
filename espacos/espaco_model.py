from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Espaco(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    escola_id = db.Column(db.Integer)
    tipo = db.Column(db.String(255))
    quantidade = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class EspacoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Espaco
        load_instance = True


        