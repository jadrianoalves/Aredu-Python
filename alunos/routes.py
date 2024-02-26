from flask import Blueprint, request, jsonify
from aluno_model import Aluno, AlunoSchema, db
from aluno_service import (
    adicionar_aluno,
    obter_todos_alunos,
    obter_aluno_por_id,
    atualizar_aluno,
    excluir_aluno,
    buscar_alunos_por_nome,
    atualizar_parcialmente_aluno,
    obter_filtrado
)

alunos_blueprint = Blueprint('alunos', __name__)
aluno_schema = AlunoSchema()
alunos_schema = AlunoSchema(many=True)

@alunos_blueprint.route('/alunos', methods=['POST'])
def add_aluno():
    try:
        data = request.json
        novo_aluno = adicionar_aluno(data)
        aluno_serializado = aluno_schema.dump(novo_aluno)
        return jsonify(aluno_serializado)
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    todos_alunos = obter_todos_alunos()
    alunos_serializados = alunos_schema.dump(todos_alunos)
    return jsonify(alunos_serializados)

@alunos_blueprint.route('/alunos/<id>', methods=['GET'])
def get_aluno(id):
    aluno = obter_aluno_por_id(id)

    if not aluno:
        return jsonify({"message": "Aluno não encontrado"}), 404

    aluno_serializado = aluno_schema.dump(aluno)
    return jsonify(aluno_serializado)

@alunos_blueprint.route('/alunos/<id>', methods=['PUT'])
def update_aluno(id):
    aluno = obter_aluno_por_id(id)
    
    if not aluno:
        return jsonify({"message": "Aluno não encontrado"}), 404

    try:
        data = request.json
        aluno_atualizado = atualizar_aluno(aluno, data)
        aluno_serializado = aluno_schema.dump(aluno_atualizado)
        return jsonify(aluno_serializado)
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

@alunos_blueprint.route('/alunos/<id>', methods=['DELETE'])
def delete_aluno(id):
    aluno = obter_aluno_por_id(id)

    if not aluno:
        return jsonify({"message": "Aluno não encontrado"}), 404

    try:
        aluno_excluido = excluir_aluno(aluno)
        aluno_serializado = aluno_schema.dump(aluno_excluido)
        return jsonify(aluno_serializado)
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@alunos_blueprint.route('/alunos/search', methods=['POST'])
def buscar_alunos():
    data = request.json  # Receber dados JSON do corpo da solicitação

    campos = data.get('campos', [])
    filtro = data.get('filtro', None)  # Mudança aqui para receber um único filtro

    try:
        if filtro is not None and len(filtro) == 3:  # Verificar se o filtro está no formato correto
            alunos_filtrados = obter_filtrado(campos=campos, filtro=filtro)
        else:
            alunos_filtrados = obter_filtrado(campos=campos)  # Chamada sem filtro

        return jsonify(alunos_filtrados)
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    

@alunos_blueprint.route('/alunos/<id>', methods=['PATCH'])
def partial_update_aluno(id):
    aluno = obter_aluno_por_id(id)

    if not aluno:
        return jsonify({"message": "Aluno não encontrado"}), 404

    try:
        data = request.json
        aluno_atualizado = atualizar_parcialmente_aluno(aluno, data)
        aluno_serializado = aluno_schema.dump(aluno_atualizado)
        return jsonify(aluno_serializado)
    except ValueError as e:
        return jsonify({"message": str(e)}), 400

