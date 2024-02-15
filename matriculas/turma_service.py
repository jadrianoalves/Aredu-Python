from matricula_model import db, Turma

def obter_matriculas_por_turma(turma_id):
    turma = Turma.query.get(turma_id)
    if turma:
        return turma.matriculas
    else:
        return None