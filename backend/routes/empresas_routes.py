from flask import Blueprint, request, jsonify
from controllers.empresas_controller import cadastrar_empresa, validar, salvar, dados

empresas_bp = Blueprint("empresas", __name__)

@empresas_bp.route("/", methods=["POST"])
def post_empresa():
    """Rota POST para cadastrar empresa"""
    dados = request.json or {}
    resposta, status = cadastrar_empresa(dados)
    return jsonify(resposta), status

@empresas_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    payload = request.form if request else (request.get_json(silent=True) or {})
    erros, dados = validar(payload)
    if erros:
        return {'ok': False}, 400
    rid = salvar(dados)