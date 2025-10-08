from flask import Blueprint, request, jsonify
from controllers.escolas_controller import cadastrar_escola

escolas_bp = Blueprint("escolas", __name__)

@escolas_bp.route("/", methods=["POST"])
def post_escola():
    """Rota POST para cadastrar escola"""
    dados = request.json or {}
    resposta, status = cadastrar_escola(dados)
    return jsonify(resposta), status