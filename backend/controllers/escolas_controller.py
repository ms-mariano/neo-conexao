from flask import Flask 
import csv, uuid
import os
from datetime import datetime

app = Flask(__name__)

ARQUIVO_CSV = 'data/escolas.csv'
FIELDNAMES  = ['Nome_da_instituicao', 'INEP', 'CNPJ', 'Telefone', 'Email', 'endereco', 'cidade', 'cep', 'cursos_oferecidos']
ALLOWED_TIPO_DE_INSTITUICAO = {'Escolas particulares', 'Escolas publicas', 'Escolas técnicas'}
ALLOWED_ESTADO = {'AC','AL','AM','AP','BA','CE','DF','ES','GO','MA','MG','MS','MT','PA','PB','PE','PI','PR','RJ','RN','RO','RR','RS','SC','SE','SP','TO'}
ALLOWED_TURNO_DE_FUNCIONAMENTO = {'Matutino', 'Vespertino', 'Noturno', 'Integral'}
ALLOWED_NIVEL_DE_ESCOLARIDADE  = {'Ens. Fundamental II', 'Ens. Medio', 'Ens. Fundamental II e Ens. Medio'}

def ensure_csv():
    os.makedirs (os.path.dirname (ARQUIVO_CSV), exist_ok = True)
    if not os.path.isfile (ARQUIVO_CSV):
        with open (ARQUIVO_CSV, 'w', newline='', encoding='utf-8')as f:
            writer = csv. DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def norm(s):
    return s.strip() if isinstance(s, str) else ''

def validar(payload):
    Nome_da_instituicao = norm(payload.get('Nome_da_instituicao', ''))
    Tipo_de_instituicao = norm(payload.get('Tipo_de_instituicao', ''))
    INEP     = norm(payload.get('INEP', ''))
    CNPJ     = norm(payload.get('CNPJ', ''))
    Telefone = norm(payload.get('Telefone', ''))
    Email    = norm(payload.get('Email', ''))
    endereco = norm(payload.get('endereco', ''))
    cidade   = norm(payload.get('cidade', ''))
    estado   = norm(payload.get('estado', ''))
    cep      = norm(payload.get('cep', ''))
    Turno_de_funcionamento = norm(payload.get('Turno_de_funcionamento', ''))
    Nivel_de_escolaridade  = norm(payload.get('Nivel_de_escolaridade', ''))
    cursos_oferecidos      = norm(payload.get('cursos_oferecidos', ''))

    dados = {
        'Nome_da_instituicao': Nome_da_instituicao, 'Tipo_de_instituicao': Tipo_de_instituicao, 'INEP': INEP, 'CNPJ': CNPJ, 'Telefone':Telefone,'Email':Email, 'endereco':endereco, 'cidade':cidade, 'estado':estado, 'cep':cep,'Turno_de_funcionamento':Turno_de_funcionamento, 'Nivel_de_escolaridade':Nivel_de_escolaridade, 'cursos_oferecidos':cursos_oferecidos
    }
    return dados

def salvar(dados):
    ensure_csv()
    registro = dados.copy()
    registro['id_escola'] = str(uuid.uuid4())
    registro['timestamp']  = datetime.now().isoformat(timespec='seconds')

def salvar_escola(Nome_da_instituicao, Tipo_de_instituicao, INEP, CNPJ, Telefone, Email, endereco, cidade, estado, cep, Turno_de_funcionamento, Nivel_de_escolaridade, cursos_oferecidos):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding='utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow([ 'Nome_da_instituicao', 'Tipo_de_instituicao', 'INEP', 'CNPJ', 'Telefone', 'Email', 'endereco', 'cidade', 'estado', 'cep', 'Turno_de_funcionamento', 'Nivel_de_escolaridade', 'cursos_oferecidos'])
        escritor.writerow([Nome_da_instituicao, Tipo_de_instituicao, INEP, CNPJ, Telefone, Email, endereco, cidade, estado, cep, Turno_de_funcionamento, Nivel_de_escolaridade, cursos_oferecidos])

def ler_escola():
    dados = []
    if os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, mode = "r", encoding = 'utf-8') as file:
            leitor = csv.DictReader(file)
            for linha in leitor:
                dados.append(linha)
    return dados
    
if __name__=="__main__":
    app.run(debug=True)
