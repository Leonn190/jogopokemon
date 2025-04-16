import random

Pokebola = {
    "nome": "pokebola",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 1,
    "poder": 2
}

Gratball = {
    "nome": "greatball",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 2,
    "poder": 4
}

Ultraball = {
    "nome": "ultraball",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 3,
    "poder": 6
}

Masterball = {
    "nome": "masterball",
    "classe": "pokebola",
    "Descrição": "serve para capturar pokemons",
    "raridade": 5,
    "poder": 9
}

Poçao = {
    "nome": "poção",
    "classe": "poçao",
    "Descrição": "Cura 20 de HP dos pokemon",
    "raridade": 1,
    "cura": 20
} 

Super_Poçao = {
    "nome": "super poção",
    "classe": "poçao",
    "Descrição": "Cura 50 de HP dos pokemon",
    "raridade": 2,
    "cura": 50
} 

Hiper_Poçao = {
    "nome": "hiper poção",
    "classe": "poçao",
    "Descrição": "Cura 90 de HP dos pokemon",
    "raridade": 3,
    "cura": 90
} 

Mega_poção = {
    "nome": "mega poção",
    "classe": "poçao",
    "Descrição": "Cura 150 de HP dos pokemon",
    "raridade": 4,
    "cura": 150
} 

Caixa = {
    "nome": "caixa",
    "classe": "caixa",
    "Descrição": "serve para fazer 3 compras",
    "raridade": 2,
    "compra": 3
}

Caixote = {
    "nome": "caixote",
    "classe": "caixa",
    "Descrição": "serve para fazer 5 compras",
    "raridade": 4,
    "compra": 5
}

Coletor = {
    "nome": "coletor",
    "classe": "coletor",
    "Descrição": "serve para ganhar 3 energias",
    "raridade": 1,
    "compra": 3
}

Citrino = {
    "nome": "citrino",
    "classe": "amplificador",
    "Descrição": "aumenta a defesa dos pokemons",
    "raridade": 3,
    "aumento": "def"
}

Safira = {
    "nome": "safira",
    "classe": "amplificador",
    "Descrição": "aumenta a defesa especial dos pokemons",
    "raridade": 3,
    "aumento": "def SP"
}

Rubi = {
    "nome": "rubi",
    "classe": "amplificador",
    "Descrição": "aumenta a ataque dos pokemons",
    "raridade": 3,
    "aumento": "atk"
}

Ametista = {
    "nome": "ametista",
    "classe": "amplificador",
    "Descrição": "aumenta a ataque especial dos pokemons",
    "raridade": 3,
    "aumento": "atk SP"
}

Esmeralda = {
    "nome": "esmeralda",
    "classe": "amplificador",
    "Descrição": "aumenta 1 de XP dos pokemon",
    "raridade": 4,
    "aumento": "XP atu"
}

Removedor_de_estadio = {
    "nome": "Removedor",
    "classe": "estadio",
    "Descrição": "Leve a luta de volta ao basico e remova um estádio",
    "raridade": 2,
    "ST Code": 0
}

Mer_stadium = {
    "nome": "Estádio Mer",
    "classe": "estadio",
    "Descrição": "Leve a luta ao Estádio Mer",
    "raridade": 2,
    "ST Code": 1
}

Shivre_city = {
    "nome": "Cidade Shivre",
    "classe": "estadio",
    "Descrição": "Leve a luta para a cidade Shivre",
    "raridade": 3,
    "ST Code": 2
}

Auroma_park = {
    "nome": "Estádio Mer",
    "classe": "estadio",
    "Descrição": "Leve a luta ao parque Auroma",
    "raridade": 3,
    "ST Code": 3
}

Kalos_Stadium = {
    "nome": "Estádio Kalos",
    "classe": "estadio",
    "Descrição": "Leve a luta ao Estádio Kalos",
    "raridade": 4,
    "ST Code": 4
}

Skyloft = {
    "nome": "Skyloft",
    "classe": "estadio",
    "Descrição": "Leve a luta aos céus de Skyloft",
    "raridade": 3,
    "ST Code": 5
}

Porto_Molge = {
    "nome": "Porto Molge",
    "classe": "estadio",
    "Descrição": "Leve a luta ao Porto Molge",
    "raridade": 3,
    "ST Code": 6
}

itens_disponiveis = [Poçao,Super_Poçao,Hiper_Poçao,Mega_poção,Caixa,Caixote,Coletor]
pokebolas_disponiveis = [Pokebola,Gratball,Ultraball,Masterball]
amplificadores_disponiveis = [Citrino,Safira,Rubi,Ametista,Esmeralda]
Estadios_disponiveis = [Removedor_de_estadio,Mer_stadium,Shivre_city,Auroma_park,Kalos_Stadium,Skyloft,Porto_Molge]
        