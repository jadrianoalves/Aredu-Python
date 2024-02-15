from datetime import datetime
from responsavel_model import db, Responsavel

def create_responsavel(data):
    new_responsavel = Responsavel(**data)
    db.session.add(new_responsavel)
    db.session.commit()
    return new_responsavel

def get_responsavel(responsavel_id):
    return Responsavel.query.get(responsavel_id)

def get_all_responsaveis():
    return Responsavel.query.all()

def update_responsavel(responsavel_id, data):
    responsavel = Responsavel.query.get(responsavel_id)
    for key, value in data.items():
        setattr(responsavel, key, value)
    db.session.commit()
    return responsavel

def delete_responsavel(responsavel_id):
    responsavel = Responsavel.query.get(responsavel_id)
    db.session.delete(responsavel)
    db.session.commit()
