import random
from Visual.Sonoridade import tocar
import Visual.GeradoresVisuais as GV
from Geradores.GeradorPokemon import Pokemons_Todos
from Dados.itens import Pokebolas_Todas,Estadios_Todos,Amplificadores_Todos,Frutas_Todas,Outros_Todos, Poçoes_Todas
from Dados.Estadios import Estadios


Pokebolas_disponiveis = Pokebolas_Todas
Estadios_disponiveis = Estadios_Todos
Amplificadores_disponiveis = Amplificadores_Todos
Frutas_disponiveis = Frutas_Todas
Poçoes_disponiveis = Poçoes_Todas
Outros_disponiveis = Outros_Todos

Pokedex = Pokemons_Todos

Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "laranja", "cinza", "preta"]

class Baralho:
    def __init__(self):
        self.pokemons = []
        self.pokebolas = []
        self.frutas = []
        self.amplificadores = []
        self.estadios = []
        self.poçoes = []
        self.outros = []

        for pokebola in Pokebolas_disponiveis:
            for _ in range(pokebola["quantidade"]):
                self.pokebolas.append(pokebola)

        for fruta in Frutas_disponiveis:
            for _ in range(fruta["quantidade"]):
                self.frutas.append(fruta)

        for amplificador in Amplificadores_disponiveis:
            for _ in range(amplificador["quantidade"]):
                self.amplificadores.append(amplificador)

        for estadio in Estadios_disponiveis:
            for _ in range(estadio["quantidade"]):
                self.estadios.append(estadio)

        for poçao in Poçoes_disponiveis:
            for _ in range(poçao["quantidade"]):
                self.poçoes.append(poçao)

        for outro in Outros_disponiveis:
            for _ in range(outro["quantidade"]):
                self.outros.append(outro)
        
        self.baralho = self.pokebolas + self.amplificadores + self.frutas + self.poçoes + self.estadios + self.outros
        self.Comuns = []
        self.Incomuns = []
        self.Raros = []
        self.Lendarios = []

        for item in self.baralho:
            if item["raridade"] == "Comum":
                self.Comuns.append(item)
            elif item["raridade"] == "Incomum":
                self.Incomuns.append(item)
            elif item["raridade"] == "Raro":
                self.Raros.append(item)
            elif item["raridade"] == "Lendario":
                self.Lendarios.append(item)

    def devolve_item(self,item):
            if item["raridade"] == "Comum":
                self.Comuns.append(item)
            elif item["raridade"] == "Incomum":
                self.Incomuns.append(item)
            elif item["raridade"] == "Raro":
                self.Raros.append(item)
            elif item["raridade"] == "Lendario":
                self.Lendarios.append(item)

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

def Compra_Energia(player,custo=0):
    if player.ouro >= custo:
        tocar("Energia")
        player.ouro -= custo
        energia_sorteada = random.choice(Energias)
        player.energias[energia_sorteada] += 1
        energia_sorteada = random.choice(Energias)
        player.energias[energia_sorteada] += 1
    else:
        tocar("Bloq")
        GV.adicionar_mensagem("Sem ouro para comprar energias")
        

def caixa():
        while True:
            raridades = []
            # U = itens_disponiveis + pokebolas_disponiveis + amplificadores_disponiveis
            U = 2
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

def Gera_Baralho():
    return Baralho()

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
