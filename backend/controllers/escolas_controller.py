import uuid, datetime
from utils.csv_utils import adicionar_registro

CAMINHO = "data/escolas.csv"
CAMPOS = [
    "id_escola", "nome", "endereco", "cidade", "estado",
    "cep", "telefone", "email", "site", "cursos_oferecidos", "data_registro"
]

def cadastrar_escola(dados):
    obrigatorios = ["nome", "cidade", "estado", "email"]
    faltando = [c for c in obrigatorios if c not in dados or not str(dados[c]).strip()]
    if faltando:
        return {"erro": f"Campos obrigatórios ausentes: {', '.join(faltando)}"}, 400

    escola = {
        "id_escola": str(uuid.uuid4()),
        "nome": dados["nome"].strip().title(),
        "endereco": dados.get("endereco", "").strip(),
        "cidade": dados["cidade"].strip().title(),
        "estado": dados["estado"].strip().upper(),
        "cep": dados.get("cep", "").strip(),
        "telefone": dados.get("telefone", "").strip(),
        "email": dados["email"].strip().lower(),
        "site": dados.get("site", "").strip(),
        "cursos_oferecidos": dados.get("cursos_oferecidos", "").strip(),
        "data_registro": datetime.datetime.now().isoformat()
    }

    adicionar_registro(CAMINHO, escola, CAMPOS)
    return {"mensagem": "Escola cadastrada com sucesso!", "dados": escola}, 201