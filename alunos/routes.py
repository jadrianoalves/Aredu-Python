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

@alunos_blueprint.route('/alunos/search', methods=['GET'])
def alunos_por_nome():
    termo_busca = request.args.get('nome')
    campos = request.args.getlist('campos')  # Receber campos via query
    filtros = []

    try:
        if termo_busca is None:
            raise ValueError("O parâmetro 'nome' é obrigatório")

        # Construir lista de filtros
        for campo in request.args:
            if campo.startswith('filtro_'):
                campo_sem_prefixo = campo.replace('filtro_', '')
                operador, valor = request.args.get(campo).split(':')
                filtros.append((campo_sem_prefixo, operador, valor))

        # Modificado para utilizar o método obter_filtrado da camada de serviço
        alunos_encontrados = obter_filtrado(campos=campos, filtros=filtros)

        # Serializar os alunos encontrados
        alunos_serializados = []
        for aluno in alunos_encontrados:
            aluno_serializado = {}
            for campo in campos:
                aluno_serializado[campo] = aluno[campo]
            alunos_serializados.append(aluno_serializado)

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

