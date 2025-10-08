from flask import Blueprint, request, jsonify
from utils.csv_utils import adicionar_registro
import uuid, datetime

empresas_bp = Blueprint("empresas", __name__)

CAMINHO = "data/empresas.csv"
CAMPOS = [
    "id_empresa", "nome_fantasia", "razao_social", "cnpj",
    "endereco", "cidade", "estado", "telefone", "email",
    "area_atuacao", "site", "data_registro"
]

# 🔹 Rota POST: /empresas/
@empresas_bp.route("/", methods=["POST"])
def cadastrar_empresa():
    """Cadastra uma nova empresa no sistema."""
    dados = request.json or {}
    obrigatorios = ["nome_fantasia", "cnpj", "email", "cidade", "estado"]

    faltando = [c for c in obrigatorios if c not in dados or not str(dados[c]).strip()]
    if faltando:
        return jsonify({"erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"}), 400

    empresa = {
        "id_empresa": str(uuid.uuid4()),
        "nome_fantasia": dados["nome_fantasia"].strip().title(),
        "razao_social": dados.get("razao_social", "").strip().title(),
        "cnpj": dados["cnpj"].strip(),
        "endereco": dados.get("endereco", "").strip(),
        "cidade": dados["cidade"].strip().title(),
        "estado": dados["estado"].strip().upper(),
        "telefone": dados.get("telefone", "").strip(),
        "email": dados["email"].strip().lower(),
        "area_atuacao": dados.get("area_atuacao", "").strip().capitalize(),
        "site": dados.get("site", "").strip(),
        "data_registro": datetime.datetime.now().isoformat()
    }

    adicionar_registro(CAMINHO, empresa, CAMPOS)
    return jsonify({
        "mensagem": "Empresa cadastrada com sucesso!",
        "dados": empresa,
        "rota": "/empresas/"
    }), 201
