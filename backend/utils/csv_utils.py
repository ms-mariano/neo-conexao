import csv, os

def garantir_csv(ARQUIVO_CSV, FIELDNAMES):
    """Garante que o CSV existe e tem cabeçalho"""
    if not os.path.exists(ARQUIVO_CSV):
        with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()

def adicionar_registro(ARQUIVO_CSV, registro, FIELDNAMES):
    """Adiciona um registro novo ao CSV"""
    garantir_csv(ARQUIVO_CSV, FIELDNAMES)
    with open(ARQUIVO_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow(registro)