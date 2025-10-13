from flask import Blueprint, request, jsonify
from controllers.empresas_controller import cadastrar_empresa

empresas_bp = Blueprint("empresas", __name__)

@empresas_bp.route("/", methods=["POST"])
def post_empresa():
    """Rota POST para cadastrar empresa"""
    dados = request.json or {}
    resposta, status = cadastrar_empresa(dados)
    return jsonify(resposta), status