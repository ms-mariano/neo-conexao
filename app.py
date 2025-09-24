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
    nome = request.args.get("nome")
    email = request.args.get("email")
    telefone = request.args.get("telefone")
    cgm = request.args.get("cgm")
    idade = request.args.get("idade")
    bairro = request.args.get("bairro")
    cidade = request.args.get("cidade")
    genero = request.args.get("genero")
    etnia = request.args.get("etnia")

    salvar_alunos(nome, email, telefone, cgm, idade, bairro, cidade, genero, etnia)

    return f"Aluno cadastrado com sucesso: {nome} ({email}) {telefone} {cgm} {idade} - {cidade} ({bairro}) {genero} {etnia}"

if __name__=="__main__":
    app.run(debug=True)