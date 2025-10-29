import uuid, os, csv 
from datetime import datetime
from utils.csv_utils import adicionar_registro

ARQUIVO_CSV = "data/empresas.csv"
FIELDNAMES  = [
    'id_empresa', 'timestamp', 'nome', 'nome_fantasia', 'cnpj',
    'endereco', 'bairro', 'cidade', 'cep', 'estado', 'telefone', 'email',
    'area_atuacao'
]

def ensure_csv():
    os.makedirs(os.path.dirname (ARQUIVO_CSV), exist_ok = True)
    if not os.path.isfile (ARQUIVO_CSV):
        with open (ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv. DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def norm(s):
    return s.strip() if isinstance(s, str) else ''

def validar(payload):
    nome = norm(payload.get('nome', ''))
    nome_fantasia = norm(payload.get('nome_fantasia', ''))
    cnpj = norm(payload.get('cnpj', ''))
    endereco = norm(payload.get('endereco', ''))
    bairro = norm(payload.get('bairro', ''))
    cidade = norm(payload.get('cidade', ''))
    cep = norm(payload.get('cep', ''))
    telefone = norm(payload.get('telefone', ''))
    email = norm(payload.get('email', ''))
    area_atuacao = norm(payload.get('area_atuacao', ''))


    dados = {
        'nome': nome, 'nome_fantasia': nome_fantasia, 'cnpj': cnpj,
        'endereco': endereco, 'bairro': bairro, 'cidade': cidade,
         'cep': cep,  'telefone': telefone, 'email': email, 'area_atuacao': area_atuacao
    }
    return dados

def salvar(dados):
    ensure_csv()
    registro = dados.copy()
    registro['id_empresa'] = str(uuid.uuid4())
    registro['timestamp']  = datetime.now().isoformat(timespec='seconds')

    adicionar_registro(ARQUIVO_CSV, registro, FIELDNAMES)
    return {
        "mensagem": "Empresa cadastrada com sucesso!",
        "dados": dados
    }, 201
