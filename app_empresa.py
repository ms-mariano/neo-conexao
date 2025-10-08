#empresa

def salvar_empresas(nome_da_empresa, nome_fantasia, CNPJ, Telefone, Email, CEP, area_de_atuacao, endereco, Cidade, Bairro, Estado):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow([ 'nome_da_empresa', 'nome_fantasia', 'CNPJ', 'Telefone', 'Email', 'CEP', 'area_de_atuacao', 'endereco', 'Cidade', 'Bairro', 'Estado'])
        escritor.writerow([nome_da_empresa, nome_fantasia, CNPJ, Telefone, Email, CEP, area_de_atuacao, endereco, Cidade, Bairro, Estado])

def ler_empresas():
    dados = []
    if os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode="r", encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados

@app.route("/listar_empresas")
def listar():
    empresas = ler_empresas()
    resposta = "<h1>Lista de empresas</h1><ul>"
    for p in empresas:
        resposta += f"<li>{p['nome_da_empresa']} ({p['nome_fantasia']}) - {p['CNPJ']} ({p['Telefone']}) - {p['Email']} ({p['CEP']}) - {p['area_de_atuacao']} ({p['endereco']}) -  {p['Cidade']} ({p['Bairro']}) -{p['Estado']}<li>"
        resposta += "</ul>"
        return resposta
    
@app.route("/cadastrar_form_empresas")
def cadastrar_form_empresas():
    nome_da_empresa = request.args.get("Nome da empresa")
    nome_fantasia = request.args.get("Nome fantasia")
    CNPJ = request.args.get("CNPJ")
    Telefone = request.args.get("Telefone")
    Email = request.args.get("Email")
    CEP = request.args.get("CEP")
    area_de_atuacao = request.args.get("Área de atuação")
    endereco = request.args.get("Endereço")
    Bairro = request.args.get("Bairro")
    Estado = request.args.get("Estado")
    
    salvar_empresas(nome_da_empresa, nome_fantasia, CNPJ, Telefone, Email, CEP, area_de_atuacao, endereco, Cidade, Bairro, Estado)
    return f"empresas cadastrada com sucesso: {nome_da_empresa} ({nome_fantasia}) - ({CNPJ}) - {Telefone} ({Email}) - {CEP} ({area_de_atuacao}) - {endereco} - {Cidade} ({Bairro}) - {Estado}"

