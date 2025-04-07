import random
from prettytable import PrettyTable
import Gerador

Energias = ["fogo", "agua", "eletrico", "planta", "gelo", "lutador", "veneno", "terra", "voador", "psiquico", "inseto", "pedra", "fantasma", "dragao", "sombrio", "aço", "fada"]

def comprar(player,compras):
    for i in range(compras):
        while True:
            loja = input(f"{player[0]}, você deseja comprar em qual loja? loja de pokebolas, de itens ou de amplificadores ?").lower()
            if loja in ["loja de pokebolas", "pokebolas","1"]:
                tipo = "pokebola"
                break
            elif loja in ["loja de itens", "itens","2"]:
                tipo = "item"
                break
            elif loja in ["loja de amplificadores","amplificadores","3"]:
                tipo = "amplificador"
                break
            else:
                print("loja invalida, tente novamente")
        ganho = Gerador.ganhar_item(tipo)
        print (f"Você ganhou: {ganho['nome']}!")
        player[2].append(ganho)
    
    print (f"A compra foi realizada! seu inventário atual é:")
    for i in range(len(player[2])-1):
        print (f"{i+1} - {player[2][i+1]['nome']}") 

def ganhar_energia(player,numero):
    global Energias
    for i in range(numero):
        j = random.choice(Energias)
        player[3][j] = player[3][j] + 1
        print (f"{player[0]} ganhou 1 energia de {j}")

def efetividade(Tipo_do_ataque,Tipo_do_atacado):
    
    tabela_tipos = {
    "normal":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "veneno": 0, "terra": 0,
                  "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": -0.75, "dragao": 0, "sombrio": 0, "aco": 0, "fada": 0},

    "fogo":      {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": 0, "planta": 0.5, "gelo": 0.5, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psiquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "aco": 0.5, "fada": 0},

    "agua":      {"normal": 0, "fogo": 0.5, "agua": -0.25, "eletrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": 0.5, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0.5, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "aco": 0, "fada": 0},

    "eletrico":  {"normal": 0, "fogo": 0, "agua": 0.5, "eletrico": -0.25, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": -0.75, "voador": 0.5, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "aco": 0, "fada": 0},

    "planta":    {"normal": 0, "fogo": -0.25, "agua": 0.5, "eletrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": -0.25,
                  "terra": 0.5, "voador": -0.25, "psiquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragao": -0.25,
                  "sombrio": 0, "aco": -0.25, "fada": 0},

    "gelo":      {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": 0, "planta": 0.5, "gelo": -0.25, "lutador": 0, "veneno": 0,
                  "terra": 0.5, "voador": 0.5, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5, "sombrio": 0,
                  "aco": -0.25, "fada": 0},

    "lutador":   {"normal": 0.5, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0.5, "lutador": 0, "veneno": -0.25,
                  "terra": 0, "voador": -0.25, "psiquico": -0.25, "inseto": -0.25, "pedra": 0.5, "fantasma": -0.75, "dragao": 0,
                  "sombrio": 0.5, "aco": 0.5, "fada": -0.25},

    "veneno":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0.5, "gelo": 0, "lutador": 0, "veneno": -0.25,
                  "terra": -0.25, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": -0.25, "fantasma": -0.25, "dragao": 0,
                  "sombrio": 0, "aco": -0.75, "fada": 0.5},

    "terra":     {"normal": 0, "fogo": 0.5, "agua": 0, "eletrico": 0.5, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": 0.5,
                  "terra": 0, "voador": -0.75, "psiquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "aco": 0.5, "fada": 0},

    "voador":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": -0.25, "planta": 0.5, "gelo": 0, "lutador": 0.5, "veneno": 0,
                  "terra": 0, "voador": 0, "psiquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "aco": -0.25, "fada": 0},

    "psiquico":  {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "veneno": 0.5,
                  "terra": 0, "voador": 0, "psiquico": -0.25, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": -0.75, "aco": -0.25, "fada": 0},

    "inseto":    {"normal": 0, "fogo": -0.25, "agua": 0, "eletrico": 0, "planta": 0.5, "gelo": 0, "lutador": -0.25, "veneno": -0.25,
                  "terra": 0, "voador": -0.25, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": -0.25, "dragao": 0,
                  "sombrio": 0.5, "aco": -0.25, "fada": -0.25},

    "pedra":     {"normal": 0, "fogo": 0.5, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0.5, "lutador": -0.25, "veneno": 0,
                  "terra": -0.25, "voador": 0.5, "psiquico": 0, "inseto": 0.5, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "aco": -0.25, "fada": 0},

    "fantasma":  {"normal": -0.75, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragao": 0,
                  "sombrio": -0.25, "aco": 0, "fada": 0},

    "dragao":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5,
                  "sombrio": 0, "aco": -0.25, "fada": -0.75},

    "sombrio":   {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": -0.25, "veneno": 0,
                  "terra": 0, "voador": 0, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragao": 0,
                  "sombrio": -0.25, "aco": 0, "fada": -0.25},

    "aco":       {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": -0.25, "planta": 0, "gelo": 0.5, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "aco": -0.25, "fada": 0.5},

    "fada":      {"normal": 0, "fogo": -0.25, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "veneno": -0.25,
                  "terra": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5,
                  "sombrio": 0.5, "aço": -0.25, "fada": 0},
    }
    
    multiplicador = 1
    for i in range(len(Tipo_do_ataque)):
        for j in range(len(Tipo_do_atacado)):
            multiplicador = multiplicador + tabela_tipos[Tipo_do_ataque[i]][Tipo_do_atacado[j]]

    return multiplicador

def usar_item(item,player,inimigo):
    if item["classe"] in ["poçao","amplificador"]:
        tabela = PrettyTable()
        for i in range(len(player[1]) - 1):
            U = player[1][i + 1]
            tabela.title = f"Status dos pokemons de {player[0]}"
            tabela.field_names = ["num","nome","Vida", "ATK", "Sp ATK", "DEF", "Sp DEF", "VEL", "custo", "ataque normal", "ataque especial", "XP", "IV"]
            tabela.add_row([i+1,U.nome,U.Vida, U.Atk, U.Atk_sp, U.Def, U.Def_sp, U.vel, U.custo, U.ataque_normal["nome"], U.ataque_especial["nome"], U.xp_atu, U.IV])
            print (tabela)
            escolha = int(input(f"Escolha o numero do pokemon que voce vai utilizar o item {item['nome']}"))
            if item["classe"] in ["poçao"]:
                cura = item["cura"]
                player[2].remove(item)
                player[1][escolha].curar(cura)
                return
            elif item["classe"] in ["amplificador"]:
                tipo = item["aumento"]
                player[2].remove(item)
                player[1][escolha].amplificar(tipo,0.15,player[1][escolha])
                return
    elif item["classe"] in ["caixa","coletor"]:
        compras = item["compra"]
        if item["classe"] in ["caixa"]:
            player[2].remove(item)
            comprar(player,compras)
            return
        elif item["classe"] in ["coletor"]:
            player[2].remove(item)
            ganhar_energia(player,compras)
            return
    elif item["classe"] == "pokebola":
        print (f"{item["nome"]} deve ser usado apenas para capturar pokemons, item invalido!")
        return