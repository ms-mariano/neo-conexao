import csv, os

def garantir_csv(caminho, campos):
    """Garante que o CSV existe e tem cabeçalho"""
    if not os.path.exists(caminho):
        with open(caminho, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()

def adicionar_registro(caminho, registro, campos):
    """Adiciona um registro novo ao CSV"""
    garantir_csv(caminho, campos)
    with open(caminho, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writerow(registro)