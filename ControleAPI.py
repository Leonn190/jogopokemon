import requests

API_BASE = "https://apipokemon-i9bb.onrender.com"

def main():
    print("O que você deseja fazer?")
    print("1 - Consultar partida(s)")
    print("2 - Limpar partida(s)")
    acao = input("Digite o número da ação: ")

    if acao not in ["1", "2"]:
        print("❌ Ação inválida.")
        return

    entrada = input("Digite o número da partida (0 para todas): ")

    if acao == "1":
        consultar(entrada)
    elif acao == "2":
        limpar(entrada)

def consultar(entrada):
    if entrada == "0":
        try:
            resposta = requests.get(f"{API_BASE}/estado_partidas")
            if resposta.status_code == 200:
                print("\n📋 Lista de partidas:")
                print(resposta.json())
            else:
                print("❌ Erro ao consultar todas as partidas:", resposta.text)
        except Exception as e:
            print("Erro de conexão:", e)
    else:
        nome_partida = f"partida{entrada}"
        try:
            resposta = requests.get(f"{API_BASE}/estado_partida", json={"partida": nome_partida})
            if resposta.status_code == 200:
                print(f"\n🔎 Estado da {nome_partida}:")
                print(resposta.json())
            else:
                print(f"❌ Erro ao consultar {nome_partida}:", resposta.text)
        except Exception as e:
            print("Erro de conexão:", e)

def limpar(entrada):
    if entrada == "0":
        try:
            resposta = requests.post(f"{API_BASE}/limpa_partidas")
            if resposta.status_code == 200:
                print("✅ Todas as partidas foram resetadas com sucesso.")
            else:
                print("❌ Erro ao limpar todas as partidas:", resposta.text)
        except Exception as e:
            print("Erro de conexão:", e)
    else:
        nome_partida = f"partida{entrada}"
        try:
            resposta = requests.post(f"{API_BASE}/limpa_partida", json={"partida": nome_partida})
            if resposta.status_code == 200:
                print(f"✅ {nome_partida} foi resetada com sucesso.")
            else:
                print(f"❌ Erro ao limpar {nome_partida}:", resposta.text)
        except Exception as e:
            print("Erro de conexão:", e)

# Executa
main()
