from flask import Blueprint, request, jsonify
from controllers.alunos_controller import cadastrar_aluno

alunos_bp = Blueprint("alunos", __name__)

@alunos_bp.route("/", methods=["POST"])
def post_aluno():
    """Rota POST para cadastrar aluno"""
    dados = request.json or {}
    resposta, status = cadastrar_aluno(dados)
    return jsonify(resposta), status