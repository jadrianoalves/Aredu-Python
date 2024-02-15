# routes.py
from flask import Blueprint, request, jsonify
from escola_service import *
from escola_model import EscolaSchema

escola_schema = EscolaSchema()
escolas_schema = EscolaSchema(many=True)

escola_bp = Blueprint('escola_bp', __name__)

@escola_bp.route('/escolas', methods=['GET'])
def get_all():
    escolas = get_all_escolas()
    result = escolas_schema.dump(escolas)
    return jsonify(result), 200

@escola_bp.route('/escolas/<int:escola_id>', methods=['GET'])
def get_escola_by_id(escola_id):
    escola = get_escola(escola_id)
    if escola:
        # Usar o esquema do Marshmallow para serializar
        result = escola_schema.dump(escola)
        return jsonify(result), 200
    return jsonify({'message': 'escola not found'}), 404

@escola_bp.route('/escolas', methods=['POST'])
def create_escola():
    data = request.get_json()
    new_escola = create_escola(data)
    # Usar o esquema do Marshmallow para serializar
    result = escola_schema.dump(new_escola)
    return jsonify(result), 201

@escola_bp.route('/escolas/<int:escola_id>', methods=['PUT'])
def update_escola(escola_id):
    data = request.get_json()
    updated_escola = update_escola(escola_id, data)
    # Usar o esquema do Marshmallow para serializar
    result = escola_schema.dump(updated_escola)
    return jsonify(result), 200

@escola_bp.route('/escolas/<int:escola_id>', methods=['DELETE'])
def delete_escola(escola_id):
    delete_escola(escola_id)
    return jsonify({'message': 'escola deleted'}), 200
