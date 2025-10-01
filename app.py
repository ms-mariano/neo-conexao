from flask import Flask 
import csv
import os
from flask import request
from flask import render_template

app = Flask(__name__)

ARQUIVO_CSV ='escolas.csv'

#Escolas

def salvar_escola(Nome_da_instituicao, Tipo_de_instituicao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow([ 'Nome_da_instituicao', 'Tipo_de_instituicao', 'INEP', 'CNPJ', 'Telefone', 'Email', 'Localidade', 'Turno_de_funcionamento', 'Nivel_de_escolaridade'])
        escritor.writerow([Nome_da_instituicao, Tipo_de_instituicao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade])

def ler_escola():
    dados = []
    if os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode="r", encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/listar_escola")
def listar():
    escola = ler_escola()
    resposta = "<h1>Lista de escolas</h1><ul>"
    for p in escola:
        resposta += f"<li>{p['Nome_da_instituicao']} ({p['Tipo_de_instituicao']}) - {p['INEP']} ({p['CNPJ']}) - {p['Telefone']} ({p['Email']}) - {p['Localidade']} ({p['Turno_de_funcionamento']}) - {p['Nivel_de_escolaridade']}<li>"
        resposta += "</ul>"
        return resposta
    
@app.route("/cadastrar_form_escola")
def cadastrar_form_escola():
    Nome_da_instituicao = request.args.get("Nome_da_instituicao")
    Tipo_de_instituicao = request.args.get("Tipo_de_instituicao")
    INEP = request.args.get("INEP")
    CNPJ = request.args.get("CNPJ")
    Telefone = request.args.get("Telefone")
    Email = request.args.get("Email")
    Localidade = request.args.get("Localidade")
    Turno_de_funcionamento = request.args.get("Turno_de_funcionamento")
    Nivel_de_escolaridade = request.args.get("Nivel_de_escolaridade")
    
    salvar_escola(Nome_da_instituicao, Tipo_de_instituicao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade)
    return f"Escola cadastrada com sucesso: {Nome_da_instituicao} ({Tipo_de_instituicao}) - {INEP} ({CNPJ}) - {Telefone} ({Email}) - {Localidade} ({Turno_de_funcionamento}) - {Nivel_de_escolaridade}"

#Alunos

def salvar_alunos(nome, email, telefone, cgm, idade, bairro, cidade, genero, etnia):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding= 'utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow(['nome', 'email', 'telefone', 'cgm', 'idade', 'bairro', 'cidade', 'genero', 'etnia'])
        escritor.writerow([nome, email, telefone, cgm, idade, bairro, cidade, genero, etnia])


def ler_problemas():
    dados = []
    if os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode='r', encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados

@app.route("/cadastrar_form")
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

    salvar_alunos(nome, email, telefone, cgm, idade, bairro, cidade, genero, etnia)

    return f"Aluno cadastrado com sucesso: {nome} ({email}) {telefone} {cgm} {idade} - {cidade} ({bairro}) {genero} {etnia}"

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

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

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


if __name__=="__main__":
    app.run(debug=True)