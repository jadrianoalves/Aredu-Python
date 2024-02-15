# routes.py
from flask import Blueprint, request, jsonify
from responsavel_service import *
from responsavel_model import ResponsavelSchema

responsavel_schema = ResponsavelSchema()
responsavel_schema = ResponsavelSchema(many=True)

responsavel_bp = Blueprint('responsavel_bp', __name__)

@responsavel_bp.route('/responsaveis', methods=['GET'])
def get_all():
    responsaveis = get_all_responsaveis()
    result = responsavel_schema.dump(responsaveis)
    return jsonify(result), 200

@responsavel_bp.route('/responsaveis/<int:responsavel_id>', methods=['GET'])
def get_by_id(responsavel_id):
    responsavel = get_responsavel(responsavel_id)
    if responsavel:
        # Usar o esquema do Marshmallow para serializar
        result = responsavel_schema.dump(responsavel)
        return jsonify(result), 200
    return jsonify({'message': 'Responsavel not found'}), 404

@responsavel_bp.route('/responsaveis', methods=['POST'])
def create():
    data = request.get_json()
    new_responsavel = create_responsavel(data)
    # Usar o esquema do Marshmallow para serializar
    result = responsavel_schema.dump(new_responsavel)
    return jsonify(result), 201

@responsavel_bp.route('/responsaveis/<int:responsavel_id>', methods=['PUT'])
def update(responsavel_id):
    data = request.get_json()
    updated_responsavel = update_responsavel(responsavel_id, data)
    # Usar o esquema do Marshmallow para serializar
    result = responsavel_schema.dump(updated_responsavel)
    return jsonify(result), 200

@responsavel_bp.route('/responsaveis/<int:responsavel_id>', methods=['DELETE'])
def delete(responsavel_id):
    delete_responsavel(responsavel_id)
    return jsonify({'message': 'Responsavel deleted'}), 200
