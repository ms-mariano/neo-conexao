from flask import Flask 
import csv
import os
from flask import request
from flask import render_template

app = Flask(__name__)

ARQUIVO_CSV ='escolas.csv'

def salvar_escola(Nome_da_instituiçao, Tipo_de_instituiçao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow([ 'Nome_da_instituiçao', 'Tipo_de_instituiçao', 'INEP', 'CNPJ', 'Telefone', 'Email', 'Localidade', 'Turno_de_funcionamento', 'Nivel_de_escolaridade'])
        escritor.writerow([Nome_da_instituiçao, Tipo_de_instituiçao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade])

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

@app.route("/")
def sobre():
    return render_template("sobre.html")

@app.route("/cadastrar_escola")
def cadastrar():
    salvar_escola("CEEP","publico", "41129857", "78.146.230/0001-50", "(41) 3284-6820", "ceep@ceep.net.br", "Curitiba", "Manha", "ensino medio")
    return "Escola cadastrada com sucesso!"

@app.route("/listar_escola")
def listar():
    escola = ler_escola()
    resposta = "<h1>Lista de escolas</h1><ul>"
    for p in escola:
        resposta += f"<li>{p['Nome_da_instituiçao']} ({p['Tipo_de_instituiçao']}) - {p['INEP']} ({p['CNPJ']}) - {p['Telefone']} ({p['Email']}) - {p['Localidade']} ({p['Turno_de_funcionamento']}) - {p['Nivel_de_escolaridade']}<li>"
        resposta += "</ul>"
        return resposta
    
@app.route("/cadastrar_form_escola")
def cadastrar_form_escola():
    Nome_da_instituiçao = request.args.get(" Nome_da_instituiçao")
    Tipo_de_instituiçao = request.args.get("Tipo_de_instituiçao")
    INEP = request.args.get("INEP")
    CNPJ = request.args.get("CNPJ")
    Telefone = request.args.get("Telefone")
    Email = request.args.get("Email")
    Localidade = request.args.get("Localidade")
    Turno_de_funcionamento = request.args.get("Turno_de_funcionamento")
    Nivel_de_escolaridade = request.args.get("Nivel_de_escolaridade ")
    
    salvar_escola(Nome_da_instituiçao, Tipo_de_instituiçao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade)
    
    return f"Escola cadastrada com sucesso: {Nome_da_instituiçao} ({Tipo_de_instituiçao}) - {INEP} ({CNPJ}) - {Telefone} ({Email}) - {Localidade} ({Turno_de_funcionamento}) - {Nivel_de_escolaridade}"


if __name__=="__main__":
    app.run(debug=True)