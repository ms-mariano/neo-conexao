from flask import Flask, render_template, request, redirect, url_for
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
inicializar_csv("alunos.csv",   ["id", "nome", "email", "telefone", "cgm", "idade", "bairro", "cidade", "genero", "etnia"])
inicializar_csv("empresas.csv", ["id_empresa", "timestamp", "nome_empresa", "nome_fantasia", "cnpj", "endereco_completo", "rua", "bairro", "cidade", "cep", "estado", "telefone", "email", "area_atuacao"])
inicializar_csv("vagas.csv",    ["id_vagas", "titulo", "descricao", "nome_empresa", "telefone_empresa", "cidade", "estado", "bairro", "rua", "numero", "cep_vaga", "remuneracao", "carga_horaria", "requisitos", "data_publicacao", "tipo"])
inicializar_csv("escolas.csv",  ["id_escola", "Nome_da_instituicao", "Tipo_de_instituicao", "INEP", "CNPJ", "Telefone", "Email", "endereco_completo", "cidade", "estado", "cep", "Turno_de_funcionamento", "Nivel_de_escolaridade", "cursos_oferecidos"])
inicializar_csv("cursos.csv", ["id", "nome", "descricao", "carga_horaria", "Nome_da_instituicao", "requisitos", "modalidade"])
inicializar_csv("blog.csv",     ["id_post", "timestamp", "titulo", "autor", "conteudo"])
# ---------------------------------------------------------
# ROTAS PRINCIPAIS
# ---------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

# ---------------------------------------------------------
#ROTA CADASTRAR GERAL
# ---------------------------------------------------------
@app.route("/cadastrar")
def cadastrar():
      return render_template("cadastrar.html")

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
        return redirect("/")

    registros = ler_csv(arquivo)
    return render_template("cad_alunos.html", registros=registros)

# ---------------------------------------------------------
# ROTA EMPRESAS
# ---------------------------------------------------------
@app.route("/cadastrar_empresas", methods=["GET", "POST"])
def empresas():
    arquivo = "empresas.csv"
    cabecalho = ["id_empresa", "timestamp", "nome_empresa", "nome_fantasia", "cnpj", "endereco_completo", "rua", "bairro", "cidade", "cep", "estado", "telefone", "email", "area_atuacao"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        
        rua_empresa = request.form["rua"]
        numero_empresa = request.form["numero"]
        bairro_empresa = request.form["bairro"]
        cidade_empresa = request.form["cidade"]
        estado_empresa = request.form["estado"]

        endereco_completo_empresa = f"{rua_empresa}, {numero_empresa}, {bairro_empresa} - {cidade_empresa}/{estado_empresa}"
        
        dados = {
            "id_empresa": str(novo_id),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "nome_empresa": request.form["nome_empresa"],
            "nome_fantasia": request.form["nome_fantasia"],
            "cnpj": request.form["cnpj"],
            "endereco_completo": endereco_completo_empresa,
            "rua": rua_empresa,
            "bairro": request.form["bairro"],
            "cidade": request.form["cidade"],
            "cep": request.form["cep"],
            "estado": request.form["estado"],
            "telefone": request.form["telefone"],
            "email": request.form["email"],   
            "area_atuacao": request.form["area_atuacao"] 
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/")

    registros = ler_csv(arquivo)
    return render_template("cad_empresas.html", registros=registros)
# ---------------------------------------------------------
# ROTA VAGAS
# ---------------------------------------------------------
@app.route("/cadastrar_vagas", methods=["GET", "POST"])
def cad_vagas():
    arquivo_vagas = "vagas.csv"
    arquivo_empresas = "empresas.csv"

    # Cabeçalho atualizado com os novos campos
    cabecalho = [
        "id_vagas", "titulo", "descricao", "nome_empresa", "telefone_empresa",
        "cidade", "estado", "bairro", "rua", "numero", "cep_vaga",
        "remuneracao", "carga_horaria", "requisitos", "data_publicacao", "tipo"
    ]

    if request.method == "POST":
        registros = ler_csv(arquivo_vagas)
        novo_id = len(registros) + 1

        # --- Busca o telefone da empresa ---
        empresas = ler_csv(arquivo_empresas)
        nome_empresa = request.form["nome_empresa"]
        telefone_empresa = ""
        for e in empresas:
            if e["nome_empresa"] == nome_empresa:
                telefone_empresa = e.get("telefone", "")
                break

        # --- Dados da vaga ---
        dados = {
            "id_vagas":         str(novo_id),
            "titulo":           request.form["titulo"],
            "descricao":        request.form["descricao"],
            "nome_empresa":     nome_empresa,
            "telefone_empresa": telefone_empresa,
            "cidade":           request.form["cidade"],
            "estado":           request.form["estado"],
            "bairro":           request.form.get("bairro", ""),
            "rua":              request.form.get("rua", ""),
            "numero":           request.form.get("numero", ""),
            "cep_vaga":         request.form["cep_vaga"],
            "remuneracao":      request.form["remuneracao"],
            "carga_horaria":    request.form["carga_horaria"],
            "requisitos":       request.form["requisitos"],
            "data_publicacao":  datetime.now().strftime("%d-%m-%Y"),
            "tipo":             request.form["tipo"],
        }

        salvar_csv(arquivo_vagas, dados, cabecalho)
        return redirect("/vagas")

    # Se for GET, apenas exibe o formulário
    registros_de_vagas = ler_csv(arquivo_vagas)
    lista_de_empresas = ler_csv(arquivo_empresas)

    return render_template(
        "cad_vagas.html",
        registros=registros_de_vagas,
        empresas=lista_de_empresas
    )


# ---------------------------------------------------------
# ROTA DIVULGAÇÃO DE VAGAS
# ---------------------------------------------------------
@app.route("/vagas")
def vagas():
    arquivo = "vagas.csv"
    
    # Lê os posts do CSV
    vagas = ler_csv(arquivo)
    
    # Invertemos a lista para que o post mais recente apareça primeiro.
    vagas = list(reversed(vagas)) 

    return render_template("div_vagas.html", vagas=vagas)

# ---------------------------------------------------------
# ROTA DETALHE DE VAGA
# ---------------------------------------------------------
@app.route("/vagas/<id_vagas>")
def detalhe_vaga(id_vagas):
    arquivo = "vagas.csv"
    vaga = ler_csv(arquivo)

    vaga_encontrada = None
    for v in vaga:
        if v["id_vagas"] == id_vagas:
            vaga_encontrada = v
            break

    if vaga_encontrada:
        return render_template("detalhe_vaga.html", vaga=vaga_encontrada)
    else:
        return "<h2>Vaga não encontrada</h2>", 404

# ---------------------------------------------------------
# ROTA ESCOLAS
# ---------------------------------------------------------
@app.route("/cadastrar_escola", methods=["GET", "POST"])
def escolas():
    arquivo = "escolas.csv"
    cabecalho = ["id_escola", "Nome_da_instituicao", "Tipo_de_instituicao", "INEP", "CNPJ", "Telefone", "Email", "endereco_completo", "rua", "numero", "bairro", "cidade", "estado", "cep", "Turno_de_funcionamento", "Nivel_de_escolaridade"]

    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        
        # --- Busca o telefone da escola ---
        escolas = ler_csv("escolas.csv")
        Nome_da_instituicao = request.form["Nome_da_instituicao"]
        Telefone = ""
        for e in escolas:
            if e["Nome_da_instituicao"] == Nome_da_instituicao:
                Telefone = e.get("Telefone", "")
                break
            
        rua_escola    = request.form["rua"]
        numero_escola = request.form["numero"]
        bairro_escola = request.form["bairro"]
        cidade_escola = request.form["cidade"]
        estado_escola = request.form["estado"]

        
        endereco_completo_escola = f"{rua_escola}, {numero_escola}, {bairro_escola} - {cidade_escola}/{estado_escola}"
        
        dados = {
            "id_escola":              str(novo_id),
            "Nome_da_instituicao":    request.form["Nome_da_instituicao"],
            "Tipo_de_instituicao":    request.form["Tipo_de_instituicao"],
            "INEP":                   request.form["INEP"],
            "CNPJ":                   request.form["CNPJ"],
            "Telefone":               request.form["Telefone"],
            "Email":                  request.form["Email"],
            "endereco_completo":      endereco_completo_escola,
            "rua":                    rua_escola,
            "numero":                 numero_escola,
            "bairro":                 bairro_escola,
            "cidade":                 cidade_escola,
            "estado":                 estado_escola,
            "Turno_de_funcionamento": request.form["Turno_de_funcionamento"],
            "Nivel_de_escolaridade":  request.form["Nivel_de_escolaridade"],
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/divulgacao_escolas")

    registros = ler_csv(arquivo)
    return render_template("cad_escolas.html", registros=registros)


# ---------------------------------------------------------
# ROTA CURSOS (FORMULÁRIO DE CADASTRO)
# ---------------------------------------------------------
@app.route("/cadastrar_cursos", methods=["GET", "POST"])
def cad_cursos():
    arquivo_cursos = "cursos.csv"
    arquivo_escolas = "escolas.csv"

    # Cabeçalho atualizado com os dados da instituição
    cabecalho = [
        "id", "nome", "descricao", "carga_horaria",
        "Nome_da_instituicao", "Telefone", "Email",
        "rua", "numero", "bairro", "cidade", "estado", "cep",
        "requisitos", "modalidade"
    ]

    if request.method == "POST":
        registros = ler_csv(arquivo_cursos)
        novo_id = len(registros) + 1

        # --- Busca os dados da escola selecionada ---
        escolas = ler_csv(arquivo_escolas)
        nome_escola = request.form["Nome_da_instituicao"]

        telefone_escola = ""
        email_escola = ""
        rua_escola = ""
        numero_escola = ""
        bairro_escola = ""
        cidade_escola = ""
        estado_escola = ""
        cep_escola = ""

        for e in escolas:
            if e["Nome_da_instituicao"] == nome_escola:
                telefone_escola = e.get("Telefone", "")
                email_escola = e.get("Email", "")
                rua_escola = e.get("rua", "")
                numero_escola = e.get("numero", "")
                bairro_escola = e.get("bairro", "")
                cidade_escola = e.get("cidade", "")
                estado_escola = e.get("estado", "")
                cep_escola = e.get("cep", "")
                break

        # --- Cria o registro do curso ---
        dados = {
            "id":                str(novo_id),
            "nome":              request.form["nome"],
            "descricao":         request.form["descricao"],
            "carga_horaria":     request.form["carga_horaria"],
            "Nome_da_instituicao": nome_escola,
            "Telefone":          telefone_escola,
            "Email":             email_escola,
            "rua":               rua_escola,
            "numero":            numero_escola,
            "bairro":            bairro_escola,
            "cidade":            cidade_escola,
            "estado":            estado_escola,
            "cep":               cep_escola,
            "requisitos":        request.form["requisitos"],
            "modalidade":        request.form["modalidade"],
        }

        salvar_csv(arquivo_cursos, dados, cabecalho)
        return redirect("/cursos")

    # Se for GET, apenas exibe o formulário
    registros_de_cursos = ler_csv(arquivo_cursos)
    lista_de_escolas = ler_csv(arquivo_escolas)

    return render_template(
        "cad_cursos.html",
        registros=registros_de_cursos,
        escolas=lista_de_escolas
    )

# ---------------------------------------------------------
# ROTA DIVULGAÇÃO DE CURSOS (A "PÁGINA GERAL")
# ---------------------------------------------------------
@app.route("/cursos")
def cursos():
    arquivo_cursos = "cursos.csv"
    arquivo_escolas = "escolas.csv"

    cursos = ler_csv(arquivo_cursos)
    escolas = ler_csv(arquivo_escolas)

    # --- Coleta filtros (se existirem) ---
    escola = request.args.get("escola", "").strip().lower()
    cidade = request.args.get("cidade", "").strip().lower()
    modalidade = request.args.get("modalidade", "").strip().lower()

    # --- Aplica filtros ---
    if escola:
        cursos = [c for c in cursos if c["Nome_da_instituicao"].lower() == escola]
    if cidade:
        cursos = [c for c in cursos if cidade in c["cidade"].lower()]
    if modalidade:
        cursos = [c for c in cursos if modalidade in c["modalidade"].lower()]

    cursos = list(reversed(cursos))

    return render_template(
        "div_cursos.html",
        cursos=cursos,
        escolas=escolas  # 👈 Passamos as escolas para o HTML
    )

# ---------------------------------------------------------
# ROTA DETALHE CURSOS
# ---------------------------------------------------------
@app.route("/cursos/<id>")
def detalhe_curso(id):
    arquivo = "cursos.csv"
    curso = ler_csv(arquivo)

    curso_encontrado = None
    for c in curso:
        if c["id"] == id:
            curso_encontrado = c
            break

    if curso_encontrado:
        return render_template("detalhe_cursos.html", curso=curso_encontrado)
    else:
        return "<h2>Curso não encontrado</h2>", 404
# ---------------------------------------------------------
# ROTA BLOG
# ---------------------------------------------------------
@app.route("/blog")
def blog():
    arquivo = "blog.csv"
    
    # Lê os posts do CSV
    posts = ler_csv(arquivo)
    
    # Invertemos a lista para que o post mais recente apareça primeiro.
    posts = list(reversed(posts)) 

    return render_template("blog.html", posts=posts)

# ---------------------------------------------------------
# ROTA PARA CRIAR NOVOS POSTS
# ---------------------------------------------------------
@app.route("/blog/novo", methods = ["GET", "POST"])
def novo_post():
    arquivo   = "blog.csv"
    cabecalho = ["id_post", "timestamp", "titulo", "autor", "conteudo"]

    if request.method == "POST":
        # Salva o novo post
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id_post":   str(novo_id),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "titulo":    request.form["titulo"],
            "autor":     request.form["autor"],
            "conteudo":  request.form["conteudo"], # Conteúdo vem da <textarea>
        }
        dados["conteudo"] = f"\"{dados['conteudo']}\""
        salvar_csv(arquivo, dados, cabecalho)
        
        # Redireciona de volta para a página principal do blog
        return redirect("/blog")

    # Se for GET, apenas mostra o formulário de criação
    return render_template("cad_post.html")
  
# ---------------------------------------------------------
# ROTA CHAT
# ---------------------------------------------------------
@app.route("/chat", methods=["GET", "POST"])
def chat():
    arquivo = "chat.csv"
    cabecalho = ["id_mensagem", "id_aluno", "id_escola", "remetente", "mensagem", "timestamp"]
    
    if request.method == "POST":
        registros = ler_csv(arquivo)
        novo_id = len(registros) + 1
        dados = {
            "id_mensagem": str(novo_id),
            "id_aluno": request.form["id_aluno"],
            "id_escola": request.form["id_escola"],
            "remetente": request.form["remetente"],
            "mensagem": request.form["mensagem"],
            "timestamp": datetime.now().strftime("%Y-%m-%d")
            
        }
        salvar_csv(arquivo, dados, cabecalho)
        return redirect("/chat")

    registros = ler_csv(arquivo)
    return render_template("chat.html", registros=registros)

# ---------------------------------------------------------
# ROTA DIVULGAÇÃO DE ESCOLAS
# ---------------------------------------------------------
@app.route("/divulgacao_escolas")
def div_escolas():
    arquivo = "escolas.csv"


    escolas = ler_csv(arquivo)
    escolas = list(reversed(escolas))

    return render_template("div_escolas.html", escolas=escolas) 

# ---------------------------------------------------------
# ROTA DETALHE DE ESCOLAS
# ---------------------------------------------------------
@app.route("/escolas/<id_escola>")
def detalhe_escolas(id_escola):
    arquivo = "escolas.csv"
    escolas = ler_csv(arquivo)

    escolas_encontrada = None
    for v in escolas:
        if v["id_escola"] == id_escola:
            escolas_encontrada = v
            break

    if escolas_encontrada:
        return render_template("detalhe_escolas.html", escolas=escolas_encontrada)
    else:
        return "<h2>Escolas não encontrada</h2>", 404


# ---------------------------------------------------------
# EXECUÇÃO
# ---------------------------------------------------------
if __name__ == "__main__":
        app.run(debug=True)