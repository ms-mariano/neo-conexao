from flask import Flask, render_template, request, redirect
import csv, os
from datetime import datetime

app = Flask(__name__)

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

# ---------------------------------------------------------
# Funções auxiliares
# ---------------------------------------------------------
def inicializar_csv(nome_arquivo, cabecalho):
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    if not os.path.isfile(caminho):
        with open(caminho, mode="w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=cabecalho).writeheader()

def salvar_csv(nome_arquivo, dados, cabecalho):
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    precisa_cabecalho = not os.path.isfile(caminho) or os.stat(caminho).st_size == 0
    with open(caminho, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cabecalho)
        if precisa_cabecalho:
            writer.writeheader()
        writer.writerow(dados)

def ler_csv(nome_arquivo):
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    if not os.path.isfile(caminho) or os.stat(caminho).st_size == 0:
        return []
    with open(caminho, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ---------------------------------------------------------
# Inicializa os CSVs
# ---------------------------------------------------------
inicializar_csv("alunos.csv", ["id", "nome", "email", "telefone", "cgm", "idade", "bairro", "cidade", "genero", "etnia"])

# ---------------------------------------------------------
# ROTA PRINCIPAL
# ---------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# ---------------------------------------------------------
# ROTA SOBRE
# ---------------------------------------------------------
@app.route("/sobre")
def index():
    return render_template("sobre.html")
if __name__ == '__main__':
    app.run(debug=True)

# ---------------------------------------------------------
# ROTA ALUNOS
# ---------------------------------------------------------
@app.route("/cadastrar_alunos", methods=["GET", "POST"])
def industrias():
    arquivo = "alunos.csv"
    cabecalho = ["id", "nome", "email", "telefone", "cgm", "idade", "bairro", "cidade", "genero", "etnia"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id": str(novo_id),
            "nome": request.form["nome"],
            "email": request.form["email"],
            "telefone": request.form["telefone"],
            "cgm": request.form["cgm"],
            "idade": request.form["idade"],
            "bairro": request.form["bairro"],
            "cidade": request.form["cidade"],
            "genero": request.form["genero"],
            "etnia": request.form["etnia"]
            
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/cadastrar_alunos")

    registros = ler_csv(arquivo)
    return render_template("cad_alunos.html", registros=registros)


# ---------------------------------------------------------
# ROTA EMPRESAS
# ---------------------------------------------------------
@app.route("/empresas", methods=["GET", "POST"])
def empresas():
    arquivo = "empresas.csv"
    cabecalho = ["id_empresa", "timestamp", "nome", "nome_fantasia", "cnpj",
    "endereco", "bairro", "cidade", "cep", "estado", "telefone", "email",
    "area_atuacao"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id_empresa": str(novo_id),
            "timestamp": request.form["timestamp"],
            "nome": request.form["nome"],
            "nome_fantasia": request.form["nome_fantasia"],
            "cnpj": request.form["cnpj"],
            "endereço": request.form["endereço"],
            "bairro": request.form["bairro"],
            "cidade": request.form["cidade"],
            "cep": request.form["cep"],
            "estado": request.form["cep"],
            "telefone": request.form["telefone"],
            "email": request.form["email"]
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/industrias")

    registros = ler_csv(arquivo)
    return render_template("industrias.html", registros=registros)

# ---------------------------------------------------------
# ROTA VAGAS
# ---------------------------------------------------------
@app.route("/cadastrar_form_vagas", methods=["GET", "POST"])
def industrias():
    arquivo = "vagas.csv"
    cabecalho = ["id_vagas", "titulo", "descricao", "empresa_id", "cidade", "remuneracao", "requisitos", "data_publicacao", "tipo", "estado"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            id_vagas = request.form["cep"],
            titulo : request.form["cep"],
            descricao : request.form["cep"],
            empresa_id : request.form["cep"],
            cidade : request.form["cep"],
            remuneracao : request.form["cep"],
            requisitos = norm(payload.get('requisitos', ''))
            data_publicacao = norm(payload.get('data_publicacao', ''))
            tipo = norm(payload.get('tipo', ''))
            estado = norm(payload.get('estado', ''))
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/cadastrar_form_vagas")

    registros = ler_csv(arquivo)
    return render_template("cad_vagas.html", registros=registros)


# ---------------------------------------------------------
# ROTA ESCOLAS
# ---------------------------------------------------------
@app.route("/cadastrar_form_escola", methods=["GET", "POST"])
def industrias():
    arquivo = "escolas.csv"
    cabecalho = ["Nome_da_instituicao", "Tipo_de_instituicao", "INEP", "CNPJ", "Telefone", "Email", "endereco", "cidade", "estado", "cep", "Turno_de_funcionamento", "Nivel_de_escolaridade", "cursos_oferecidos"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id": str(novo_id),
            "Nome_da_instituicao": request.form["Nome_da_instituicao"],
            "Tipo_de_instituicao":request.form["Tipo_de_instituicao"],
            "INEP"     : request.form["INEP"],
            "CNPJ"     : request.form["CNPJ"],
            "Telefone" : request.form["Telefone"],
            "Email"    : request.form["Email"],
            "endereco" : request.form["endereco"],
            "cidade"   : request.form["cidade"],
            "estado"   : request.form["estado"],
            "cep"      : request.form["cep"],
            "Turno_de_funcionamento" : request.form["Turno_de_funcionamento"],
            "Nivel_de_escolaridade"  : request.form["Nivel_de_escolaridade"],
            "cursos_oferecidos"      : request.form["cursos_oferecidos"],
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/cadastrar_form_escola")

    registros = ler_csv(arquivo)
    return render_template("cad_escolas.html", registros=registros)