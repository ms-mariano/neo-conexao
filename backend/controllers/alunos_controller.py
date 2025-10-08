from flask import Blueprint, request, jsonify
from utils.csv_utils import adicionar_registro
import uuid, datetime

# Blueprint para agrupar rotas relacionadas a alunos
alunos_bp = Blueprint("alunos", __name__)

CAMINHO = "data/alunos.csv"
CAMPOS = [
    "id_aluno", "nome", "idade", "email", "telefone",
    "cidade", "estado", "curso_interesse",
    "tipo_oportunidade", "escola_preferida", "data_registro"
]

# 🔹 Rota POST: /alunos/
@alunos_bp.route("/", methods=["POST"])
def cadastrar_aluno():
    """Cadastra um novo aluno no sistema."""
    dados = request.json or {}
    obrigatorios = ["nome", "idade", "email", "curso_interesse", "tipo_oportunidade"]

    faltando = [c for c in obrigatorios if c not in dados or not str(dados[c]).strip()]
    if faltando:
        return jsonify({"erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"}), 400

    aluno = {
        "id_aluno": str(uuid.uuid4()),
        "nome": dados["nome"].strip().title(),
        "idade": str(dados["idade"]).strip(),
        "email": dados["email"].strip().lower(),
        "telefone": dados.get("telefone", "").strip(),
        "cidade": dados.get("cidade", "").strip().title(),
        "estado": dados.get("estado", "").strip().upper(),
        "curso_interesse": dados["curso_interesse"].strip().title(),
        "tipo_oportunidade": dados["tipo_oportunidade"].strip().capitalize(),
        "escola_preferida": dados.get("escola_preferida", "").strip(),
        "data_registro": datetime.datetime.now().isoformat()
    }

    adicionar_registro(CAMINHO, aluno, CAMPOS)
    return jsonify({
        "mensagem": "Aluno cadastrado com sucesso!",
        "dados": aluno,
        "rota": "/alunos/"
    }), 201