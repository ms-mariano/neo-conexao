from flask import Blueprint, request, jsonify
from controllers.alunos_controller import cadastrar_aluno

alunos_bp = Blueprint("alunos", __name__)

@alunos_bp.route("/", methods=["POST"])
def post_aluno():
    """Rota POST para cadastrar aluno"""
    dados = request.json or {}
    resposta, status = cadastrar_aluno(dados)
    return jsonify(resposta), status

 @alunos_route.route("/cadastrar_form")
def cadastrar_form():
    nome = request.args.get("Nome")
    email = request.args.get("Email")
    telefone = request.args.get("telefone")
    cgm = request.args.get("CGM")
    idade = request.args.get("Idade")
    bairro = request.args.get("Bairro")
    cidade = request.args.get("Cidade")
    genero = request.args.get("Genero")
    etnia = request.args.get("Etnia")