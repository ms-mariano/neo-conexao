from flask import Blueprint, request, jsonify
from controllers.escolas_controller  import cadastrar_escola

escolas_bp = Blueprint("escolas", __name__)

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
        resposta += f"<li>{p['Nome_da_instituicao']} ({p['Tipo_de_instituicao']}) - {p['INEP']} ({p['CNPJ']}) - {p['Telefone']} ({p['Email']}) - {p['endereco']} ({p['cidade']}) - {p['estado']} ({p['cep']}) - {p['Turno_de_funcionamento']} ({p['Nivel_de_escolaridade']})- {p['cursos_oferecidos']}<li>"
        resposta += "</ul>"
        return resposta
    
@app.route("/cadastrar_form_escola")