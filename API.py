from deepdiff import DeepDiff

estado_antigo = {
    "Jogador1": {"Vida": 100, "XP": 150},
    "Jogador2": {"Vida": 100, "XP": 150}
}

estado_novo = {
    "Jogador1": {"Vida": 90, "XP": 150},
    "Jogador2": {"Vida": 100, "XP": 160},
    "NovaChave": "valor novo"
}

diff = DeepDiff(estado_antigo, estado_novo, ignore_order=True)

print(diff)