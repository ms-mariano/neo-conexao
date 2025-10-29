from flask import Flask 
import csv
import os
from flask import request
from flask import render_template

app = Flask(__name__)

ARQUIVO_CSV = 'data/vagas.csv'

FIELDNAMES = ['id_vagas', 'titulo', 'descricao', 'empresa_id', 'cidade', 'remuneracao', 'requisitos', 'data_publicacao']
ALLOWED_TIPO = {'Jovem aprendiz', 'Estagio', 'Treinee','Emprego'}
ALLOWED_ESTADO = {'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO'}

def ensure_csv():
    os.makedirs (os.path.dirname (ARQUIVO_CSV), exist_ok = True)
    if not os.path.isfile (ARQUIVO_CSV):
        with open (ARQUIVO_CSV, 'w', newline='', encoding='utf-8')as f:
            writer = csv. DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
        
def norm(s):
    return s.strip() if isinstance(s, str) else ''

def validar(payload):
    id_vagas = norm(payload.get('id_vaga', ''))
    titulo = norm(payload.get('titulo', ''))
    descricao = norm(payload.get('descricao', ''))
    empresa_id = norm(payload.get('empresa_id', ''))
    cidade = norm(payload.get('cidade', ''))
    remuneracao = norm(payload.get('remuneracao', ''))
    requisitos = norm(payload.get('requisitos', ''))
    data_publicacao = norm(payload.get('data_publicacao', ''))
    tipo = norm(payload.get('tipo', ''))
    estado = norm(payload.get('estado', ''))

    dados = {
        'id_vaga': id_vagas, 'titulo':titulo, 'descricao': descricao, 'empresa_id':empresa_id, 'cidade': cidade, 'remuneracao':remuneracao, 'requisitos':requisitos, 'data_publicacao':data_publicacao, 'tipo': tipo, 'estado': estado
    }
    return dados

def salvar_vagas(id_vagas, titulo, descricao, empresa_id, cidade, remuneracao, requisitos, data_publicacao, tipo, estado):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow(['id_vagas', 'titulo', 'descricao', 'empresa_id', 'cidade', 'remuneracao', 'requisitos', 'data_publicacao', 'tipo', 'estado' ])
        escritor.writerow([id_vagas, titulo, descricao, empresa_id, cidade, remuneracao, requisitos, data_publicacao, tipo, estado])

def ler_vagas():
    dados = []
    if os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode = "r", encoding = 'utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados
    
if __name__=="__main__":
    app.run(debug=True)