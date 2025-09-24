from flask import Flask
import csv
import os
from flask import request
from flask import render_template

app = Flask(__name__)

ARQUIVO_CSV = 'alunos.csv'

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

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/cadastrar")
def cadastrar():
    salvar_alunos("Maria", "123@email.com", "44 12345-6789", "1234567890", "15", "Jardim Olímpico", "Maringá", "Feminino", "Parda")
    return "Aluno cadastrado com sucesso!"

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
   
if __name__ == "__main__":
    app.run(debug=True)
