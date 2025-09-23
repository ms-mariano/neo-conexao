from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

ARQUIVO_CSV ='escolas.csv'

def salvar_escola(Nome_da_instituiçao, Tipo_de_instituiçao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow([ 'Nome_da_instituiçao', 'Tipo_de_instituiçao', 'INEP', 'CNPJ', 'Telefone', 'Email', 'Localidade', 'Turno_de_funcionamento', 'Nivel_de_escolaridade'])
        escritor.writerow([Nome_da_instituiçao, Tipo_de_instituiçao, INEP, CNPJ, Telefone, Email, Localidade, Turno_de_funcionamento, Nivel_de_escolaridade])

def ler_cadastro():
    dados = []
    if os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode="r", encoding='utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados

@app.route("/")
def index ():
    return render_template("index.html")

@app.route("/")
def sobre():
    return render_template("sobre.html")

