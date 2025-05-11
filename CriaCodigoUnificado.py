import os

# Caminho da pasta onde estão os arquivos .py
pasta_origem = "Dados/Gen1"  # 🔁 Substitua pelo caminho da sua pasta
arquivo_saida = "codigo_unificado_P.py"

# Obtém todos os arquivos .py na pasta (exceto o próprio arquivo de saída)
arquivos = sorted([f for f in os.listdir(pasta_origem) if f.endswith(".py") and f != arquivo_saida])

with open(arquivo_saida, "w", encoding="utf-8") as saida:
    for nome in arquivos:
        caminho_arquivo = os.path.join(pasta_origem, nome)
        with open(caminho_arquivo, "r", encoding="utf-8") as entrada:
            saida.write(f"# === Início de {nome} ===\n")
            saida.write(entrada.read() + "\n\n")
            saida.write(f"# === Fim de {nome} ===\n\n")

print(f"{len(arquivos)} arquivos combinados em '{arquivo_saida}'.")