from flask import Flask, render_template, request, redirect
import csv, os
from datetime import datetime

# ---------------------------------------------------------
# CONFIGURAÇÕES INICIAIS
# ---------------------------------------------------------
app = Flask(__name__)

DATA_PATH = "data"
os.makedirs(DATA_PATH, exist_ok=True)

# ---------------------------------------------------------
# FUNÇÕES AUXILIARES
# ---------------------------------------------------------
def inicializar_csv(nome_arquivo, cabecalho):
    """Cria o arquivo CSV se não existir."""
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    if not os.path.isfile(caminho):
        with open(caminho, "w", newline="", encoding="utf-8") as f:
            csv.DictWriter(f, fieldnames=cabecalho).writeheader()

def salvar_csv(nome_arquivo, dados, cabecalho):
    """Salva um novo registro no arquivo CSV."""
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    precisa_cabecalho = not os.path.isfile(caminho) or os.stat(caminho).st_size == 0
    with open(caminho, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=cabecalho)
        if precisa_cabecalho:
            writer.writeheader()
        writer.writerow(dados)

def ler_csv(nome_arquivo):
    """Lê o conteúdo de um arquivo CSV e retorna uma lista de dicionários."""
    caminho = os.path.join(DATA_PATH, nome_arquivo)
    if not os.path.isfile(caminho) or os.stat(caminho).st_size == 0:
        return []
    with open(caminho, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

# ---------------------------------------------------------
# INICIALIZA OS ARQUIVOS CSV
# ---------------------------------------------------------
inicializar_csv("alunos.csv", ["id", "nome", "email", "telefone", "cgm", "idade", "bairro", "cidade", "genero", "etnia"])
inicializar_csv("empresas.csv", ["id_empresa", "timestamp", "nome", "nome_fantasia", "cnpj", "endereco", "bairro", "cidade", "cep", "estado", "telefone", "email", "area_atuacao"])
inicializar_csv("vagas.csv", ["id_vagas", "titulo", "descricao", "empresa_id", "cidade", "remuneracao", "requisitos", "data_publicacao", "tipo", "estado"])
inicializar_csv("escolas.csv", ["id", "Nome_da_instituicao", "Tipo_de_instituicao", "INEP", "CNPJ", "Telefone", "Email", "endereco", "cidade", "estado", "cep", "Turno_de_funcionamento", "Nivel_de_escolaridade", "cursos_oferecidos"])
inicializar_csv("cursos.csv", ["nome", "descricao", "carga_horaria", "escola_id", "cidade", "estado", "requisitos", "modalidade"])
inicializar_csv("blog.csv", ["id", "id_autor", "texto"])
inicializar_csv("opiniao.csv" ["id", "id_blog", "id_autor", "texto"])
# ---------------------------------------------------------
# ROTAS PRINCIPAIS
# ---------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre.html")
def sobre():
    return render_template("sobre.html")

@app.route("/perfil.html")
def perfil():
    return render_template("perfil.html")

# ---------------------------------------------------------
# ROTA ALUNOS
# ---------------------------------------------------------
@app.route("/cadastrar_alunos", methods=["GET", "POST"])
def alunos():
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
    cabecalho = ["id_empresa", "timestamp", "nome", "nome_fantasia", "cnpj", "endereco", "bairro", "cidade", "cep", "estado", "telefone", "email", "area_atuacao"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id_empresa": str(novo_id),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nome": request.form["nome"],
            "nome_fantasia": request.form["nome_fantasia"],
            "cnpj": request.form["cnpj"],
            "endereco": request.form["endereco"],
            "bairro": request.form["bairro"],
            "cidade": request.form["cidade"],
            "cep": request.form["cep"],
            "estado": request.form["estado"],
            "telefone": request.form["telefone"],
            "email": request.form["email"],
            "area_atuacao": request.form.get("area_atuacao", "")
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/empresas")

    registros = ler_csv(arquivo)
    return render_template("industrias.html", registros=registros)

# ---------------------------------------------------------
# ROTA VAGAS
# ---------------------------------------------------------
@app.route("/cadastrar_form_vagas", methods=["GET", "POST"])
def vagas():
    arquivo = "vagas.csv"
    cabecalho = ["id_vagas", "titulo", "descricao", "empresa_id", "cidade", "remuneracao", "requisitos", "data_publicacao", "tipo", "estado"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id_vagas": str(novo_id),
            "titulo": request.form["titulo"],
            "descricao": request.form["descricao"],
            "empresa_id": request.form["empresa_id"],
            "cidade": request.form["cidade"],
            "remuneracao": request.form["remuneracao"],
            "requisitos": request.form["requisitos"],
            "data_publicacao": datetime.now().strftime("%Y-%m-%d"),
            "tipo": request.form["tipo"],
            "estado": request.form["estado"],
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/cadastrar_form_vagas")

    registros = ler_csv(arquivo)
    return render_template("cad_vagas.html", registros=registros)

# ---------------------------------------------------------
# ROTA ESCOLAS
# ---------------------------------------------------------
@app.route("/cadastrar_form_escola", methods=["GET", "POST"])
def escolas():
    arquivo = "escolas.csv"
    cabecalho = ["id", "Nome_da_instituicao", "Tipo_de_instituicao", "INEP", "CNPJ", "Telefone", "Email", "endereco", "cidade", "estado", "cep", "Turno_de_funcionamento", "Nivel_de_escolaridade", "cursos_oferecidos"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id": str(novo_id),
            "Nome_da_instituicao": request.form["Nome_da_instituicao"],
            "Tipo_de_instituicao": request.form["Tipo_de_instituicao"],
            "INEP": request.form["INEP"],
            "CNPJ": request.form["CNPJ"],
            "Telefone": request.form["Telefone"],
            "Email": request.form["Email"],
            "endereco": request.form["endereco"],
            "cidade": request.form["cidade"],
            "estado": request.form["estado"],
            "cep": request.form["cep"],
            "Turno_de_funcionamento": request.form["Turno_de_funcionamento"],
            "Nivel_de_escolaridade": request.form["Nivel_de_escolaridade"],
            "cursos_oferecidos": request.form["cursos_oferecidos"],
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/cadastrar_form_escola")

    registros = ler_csv(arquivo)
    return render_template("cad_escolas.html", registros=registros)

# ---------------------------------------------------------
# ROTA CURSOS
# ---------------------------------------------------------
@app.route("/cadastrar_form_cursos", methods=["GET", "POST"])
def cursos():
    arquivo = "cursos.csv"
    cabecalho = ["nome", "descricao", "carga_horaria", "escola_id", "cidade", "estado", "requisitos", "modalidade"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id": str(novo_id),
            "nome": request.form["nome"],
            "descricao": request.form["descricao"],
            "carga_horaria": request.form["carga_horaria"],
            "escola_id": request.form["escola_id"],
            "cidade": request.form["cidade"],
            "estado": request.form["estado"],
            "requisitos": request.form["requisitos"],
            "modalidade": request.form["modalidade"],
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/cadastrar_form_cursos")

    registros = ler_csv(arquivo)
    return render_template("cad_cursos.html", registros=registros)

# ---------------------------------------------------------
# ROTA BLOG
# ---------------------------------------------------------


# ---------------------------------------------------------
# ROTA CHAT
# ---------------------------------------------------------


# ---------------------------------------------------------
# EXECUÇÃO
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)