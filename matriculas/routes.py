from flask import Blueprint, jsonify, request
from matricula_service import *
from matricula_model import MatriculaSchema

matricula_schema = MatriculaSchema()
matricula_schema = MatriculaSchema(many=True)

matriculas_bp = Blueprint('matriculas', __name__)

@matriculas_bp.route('/matriculas', methods=['POST'])
def criar_matricula_endpoint():
    data = request.json
    matricula = criar_matricula(data)
    result = matricula_schema.dump(matricula)
    return jsonify(result), 201

@matriculas_bp.route('/matriculas', methods=['GET'])
def obter_matriculas_endpoint():
    matriculas = obter_todas_matriculas()
    result = matricula_schema.dump(matriculas)
    return jsonify(result)

@matriculas_bp.route('/matriculas/<int:matricula_id>', methods=['GET'])
def obter_matricula_por_id_endpoint(matricula_id):
    matricula = obter_matricula_por_id(matricula_id)
    if matricula:
        result = matricula_schema.dump(matricula)
        return jsonify(result)
    else:
        return jsonify({'message': 'Matrícula não encontrada'}), 404

@matriculas_bp.route('/matriculas/<int:matricula_id>', methods=['PUT'])
def atualizar_matricula_endpoint(matricula_id):
    dados_atualizados = request.json
    matricula = atualizar_matricula(matricula_id, dados_atualizados)
    if matricula:
        result = matricula_schema.dump(matricula)
        return jsonify(result)
    else:
        return jsonify({'message': 'Matrícula não encontrada'}), 404

@matriculas_bp.route('/matriculas/<int:matricula_id>', methods=['DELETE'])
def excluir_matricula_endpoint(matricula_id):
    resultado = excluir_matricula(matricula_id)
    if resultado:
        return jsonify({'message': 'Matrícula excluída com sucesso'})
    else:
        return jsonify({'message': 'Matrícula não encontrada'}), 404

