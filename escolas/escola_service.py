from datetime import datetime
from escola_model import db, Escola
import os
import hashlib
import uuid


def criar_pasta(nome_base, base_dir='./documentos/'):
    
    id_unico = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nome_pasta = f'{nome_base}_{timestamp}_{id_unico}'
    pasta_entidade = os.path.join(base_dir, nome_pasta)

    try:
        # Crie a pasta se não existir
        os.makedirs(pasta_entidade, exist_ok=True)
        return nome_pasta
    except Exception as e:
        # Capture e imprima a exceção para diagnóstico
        print(f"Erro ao criar a pasta: {e}")
        return None


def create_escola(data):
    new_escola = Escola(**data)
    db.session.add(new_escola)
    nome_pasta = criar_pasta('escola', new_escola.id)
    new_escola.pasta_id = nome_pasta
    db.session.commit()
    return new_escola

def get_escola(escola_id):
    return Escola.query.get(escola_id)

def get_all_escolas():
    return Escola.query.all()

def update_escola(escola_id, data):
    escola = Escola.query.get(escola_id)
    for key, value in data.items():
        setattr(escola, key, value)
    db.session.commit()
    return escola

def delete_escola(escola_id):
    escola = Escola.query.get(escola_id)
    db.session.delete(escola)
    db.session.commit()
