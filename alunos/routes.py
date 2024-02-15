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
    obter_alunos_resumidos
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

@alunos_blueprint.route('/alunos/buscar', methods=['GET'])
def alunos_por_nome():
    termo_busca = request.args.get('nome')

    try:
        if termo_busca is None:
            raise ValueError("O parâmetro 'nome' é obrigatório")

        alunos_encontrados = buscar_alunos_por_nome(termo_busca)
        alunos_serializados = alunos_schema.dump(alunos_encontrados)
        return jsonify(alunos_serializados)
    except ValueError as e:
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

@alunos_blueprint.route('/alunos/indice', methods=['GET'])
def get_alunos_resumido():
    try:
        alunos_resumido = obter_alunos_resumidos()
        return jsonify(alunos_resumido)
   
    except ValueError as e:
        return jsonify({"message": str(e)}), 400