import uuid, datetime
import os, csv
from utils.csv_utils import adicionar_registro

ARQUIVO_CSV = "data/alunos.csv"
FIELDNAMES= [
    "id_aluno", "nome", "idade", "email", "telefone",
    "cidade", "estado", "curso_interesse",
    "tipo_oportunidade", "escola_preferida", "data_registro"
]

def salvar_alunos(nome, email, telefone, cgm, idade, bairro, cidade, genero, etnia):
    existe = os.path.isfile(ARQUIVO_CSV)
    with open(ARQUIVO_CSV, mode='a', newline='', encoding= 'utf-8') as file:
        escritor = csv.writer(file)
        if not existe:
            escritor.writerow(['nome', 'email', 'telefone', 'cgm', 'idade', 'bairro', 'cidade', 'genero', 'etnia'])
        escritor.writerow([nome, email, telefone, cgm, idade, bairro, cidade, genero, etnia])

#garantir que o arquivo CSV esteja disponível ou corretamente estruturado
def ensure_csv():
    os.mkedirs(os.path.dirname(ARQUIVO_CSV), exist_ok = True)
    if not os.path.isfile(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def norm(s):
    return s.strip() if isinstance(s, str) else ''

def validar(payload):
    aluno      = norm(payload.get('aluno', ''))
    email      = norm(payload.get('email', ''))
    telefone   = norm(payload.get('telefone', ''))
    cgm        = norm(payload.get('cgm', ''))
    idade      = norm(payload.get('idade', ''))
    bairro     = norm(payload.get('bairro', '')) 
    cidade     = norm(payload.get('telefone', ''))
    genero     = norm(payload.get('genero', ''))
    etnia      = norm(payload.get('etnia', ''))

    adicionar_registro(ARQUIVO_CSV, aluno, FIELDNAMES)
    return {"mensagem": "Aluno cadastrado com sucesso!", "dados": aluno}, 201