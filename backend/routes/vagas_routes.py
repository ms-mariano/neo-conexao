from flask import Blueprint, request, jsonify, render_template

escolas_bp = Blueprint("vagas", __name__)

@escolas_bp.route("/")
def index():
    return render_template("index.html")

@escolas_bp.route("/sobre")
def sobre():
    return render_template("sobre.html")

@escolas_bp.route("/listar_vagas")
def listar():
    escola = listar()
    resposta = "<h1>Lista de vagas</h1><ul>"
    for p in escola:
        resposta += f"<li>{p[' id_vagas']} ({p['titulo']}) - {p['descricao']} ({p['empresa_id']}) - {p['cidade']} ({p['remuneracao']}) - {p['requisitos']} ({p['data_publicacao']}) - {p['tipo']} ({p['estado']}) <li>"
        resposta += "</ul>"
        return resposta
    
@escolas_bp.route("/cadastrar_form_vagas")
def cadastrar():
    return