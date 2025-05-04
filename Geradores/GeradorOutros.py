import random
from Visual.Sonoridade import tocar
import Visual.GeradoresVisuais as GV
from Geradores.GeradorPokemon import Pokemons_Todos
from Dados.itens import pokebolas_Todas,Estadios_Todos,amplificadores_Todos,itens_Todos
from Dados.Estadios import Estadios


pokebolas_disponiveis = pokebolas_Todas
Estadios_disponiveis = Estadios_Todos
amplificadores_disponiveis = amplificadores_Todos
itens_disponiveis = itens_Todos
Pokedex = Pokemons_Todos

Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "laranja", "cinza", "preta"]

def spawn_do_centro(centro):
    pokemons_possiveis = Pokedex.copy()
    if 0 in pokemons_possiveis:
        pokemons_possiveis.remove(0)


    if len(centro) < 9:
        if random.choice(["s", "n"]) == "s":
            # Cria uma lista ponderada com base na raridade (quanto menor a raridade, mais comum)
            raridades = []
            for pokemon in pokemons_possiveis:
                raridades.extend([pokemon] * (11 - pokemon["raridade"]))

            # Seleciona um Pokémon aleatório com base na raridade
            pokemon_apareceu = random.choice(raridades)
            centro.append(pokemon_apareceu)

            GV.adicionar_mensagem(f"Um {pokemon_apareceu['nome']} selvagem apareceu no centro!")

    return centro

def gera_item(tipo,player,custo=0,Turno=10):
    U = None
    if player.ouro >= custo:
        if tipo == "energia":
            player.ouro -= custo
            energia_sorteada = random.choice(Energias)
            player.energias[energia_sorteada] += 1
            energia_sorteada = random.choice(Energias)
            player.energias[energia_sorteada] += 1
        
        else:
            raridades = []
            if tipo == "pokebola":
                if len(player.Captura) < 9:
                    U = pokebolas_disponiveis
                else:
                    tocar("Bloq")
                    GV.adicionar_mensagem("Seu inventário está cheio")
            else:
                if len(player.inventario) < 10:
                    if tipo == "item":
                        U = itens_disponiveis
                    elif tipo == "amplificador":
                        if Turno > 3:
                            U = amplificadores_disponiveis
                    elif tipo == "estadio":
                        if Turno > 5:
                            U = Estadios_disponiveis
                else:
                    tocar("Bloq")
                    GV.adicionar_mensagem("Seu inventário está cheio")
    
            if U is not None:
                for i in range(len(U)):
                    for j in range(6 - U[i]["raridade"]):
                        raridades.append(U[i])
                player.ouro -= custo
                item = random.choice(raridades)
                tocar("Compra")
                GV.adicionar_mensagem(f"Você comprou um item: {item["nome"]}")
                if tipo == "pokebola":
                    player.Captura.append(item)
                else:
                    player.inventario.append(item)
            else:
                tocar("Bloq")
    else:
        tocar("Bloq")
        GV.adicionar_mensagem("Você não tem ouro o suficiente")

def caixa():
        while True:
            raridades = []
            U = itens_disponiveis + pokebolas_disponiveis + amplificadores_disponiveis
            for i in range(len(U)):
                        for j in range(6 - U[i]["raridade"]):
                            raridades.append(U[i])
            item = random.choice(raridades)
            if item["classe"] != "caixa":
                break
            
        return item

def coletor():
    energia_sorteada = random.choice(Energias)
    return energia_sorteada

def Gera_Mapa(i):
    return Mapa(Estadios[i])

class Mapa:
    def __init__(self, Info):
        self.tempo = Info["Tempo"]
        self.area = Info["zona"]
        self.cores = Info["cores"]
        self.PlojaI = Info["LojaItens"]
        self.PlojaP = Info["LojaPokebolas"]
        self.PlojaE = Info["LojaEnergias"]
        self.PlojaA = Info["LojaAmplificadores"]
        self.pLojaT = Info["LojaTreEst"]
        self.Musica = Info["Code Musica"]
        self.Fundo = Info["Code Tela"]
        self.Metros = Info["Metros"]

    def MudarEstagio(self,i):
        
        Info = Estadios[i]

        self.tempo = Info["Tempo"]
        self.area = Info["zona"]
        self.cores = Info["cores"]
        self.PlojaI = Info["LojaItens"]
        self.PlojaP = Info["LojaPokebolas"]
        self.PlojaE = Info["LojaEnergias"]
        self.PlojaA = Info["LojaAmplificadores"]
        self.pLojaT = Info["LojaTreEst"]
        self.Musica = Info["Code Musica"]
        self.Fundo = Info["Code Tela"]
        self.Metros = Info["Metros"]
