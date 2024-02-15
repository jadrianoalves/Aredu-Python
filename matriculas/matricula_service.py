from matricula_model import db, Matricula

def criar_matricula(data):
    nova_matricula = Matricula(**data)
    db.session.add(nova_matricula)
    db.session.commit()
    return nova_matricula

def obter_todas_matriculas():
    return Matricula.query.all()

def obter_matricula_por_id(matricula_id):
    return Matricula.query.get(matricula_id)

def atualizar_matricula(matricula_id, novos_dados):
    matricula = Matricula.query.get(matricula_id)
    if matricula:
        for key, value in novos_dados.items():
            setattr(matricula, key, value)
        db.session.commit()
        return matricula
    else:
        return None

def excluir_matricula(matricula_id):
    matricula = Matricula.query.get(matricula_id)
    if matricula:
        db.session.delete(matricula)
        db.session.commit()
        return True
    else:
        return False
