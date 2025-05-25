import random
import pygame
from Visual.Sonoridade import tocar
import Visual.GeradoresVisuais as GV
from Geradores.GeradorPokemon import Pokemons_Todos
from Dados.itens import Pokebolas_Todas,Estadios_Todos,Amplificadores_Todos,Frutas_Todas,Outros_Todos, Poçoes_Todas, dicionario_itens
from Dados.Estadios import Estadios
from Dados.Treinadores import Treinadores_Todos


Pokebolas_disponiveis  = Pokebolas_Todas
Estadios_disponiveis = Estadios_Todos
Amplificadores_disponiveis = Amplificadores_Todos
Frutas_disponiveis = Frutas_Todas
Poçoes_disponiveis = Poçoes_Todas
Outros_disponiveis = Outros_Todos

Pokedex = Pokemons_Todos

Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "laranja", "preta"]

class Baralho:
    def __init__(self,Deck1,Deck2,Dados=False):
        
        if Dados is False:
            self.Comuns = []
            self.Incomuns = []
            self.Raros = []
            self.Lendarios = []

            self.PokeComuns = []
            self.PokeIncomuns = []
            self.PokeRaros = []
            self.PokeEpicos = []
            self.PokeMiticos = []
            self.PokeLendarios = []

            for item in Deck1["itens"] + Deck2["itens"]:
                if item["raridade"] == "Comum":
                    self.Comuns.append(item)
                elif item["raridade"] == "Incomum":
                    self.Incomuns.append(item)
                elif item["raridade"] == "Raro":
                    self.Raros.append(item)
                elif item["raridade"] == "Lendario":
                    self.Lendarios.append(item)
            
            for pokemon in Deck1["pokemons"] + Deck2["pokemons"]:
                if pokemon != 0:
                    if pokemon["raridade"] == "Comum":
                        self.PokeComuns.append(pokemon)
                    elif pokemon["raridade"] == "Incomum":
                        self.PokeIncomuns.append(pokemon)
                    elif pokemon["raridade"] == "Raro":
                        self.PokeRaros.append(pokemon)
                    elif pokemon["raridade"] == "Epico":
                        self.PokeEpicos.append(pokemon)
                    elif pokemon["raridade"] == "Mitico":
                        self.PokeMiticos.append(pokemon)
                    elif pokemon["raridade"] == "Lendario":
                        self.PokeLendarios.append(pokemon)
        else:
            self.Comuns = Dados["Comuns"]
            self.Incomuns = Dados["Incomuns"]
            self.Raros = Dados["Raros"]
            self.Lendarios = Dados["Lendarios"]
            self.PokeComuns = Dados["PokeComuns"]
            self.PokeIncomuns = Dados["PokeIncomuns"]
            self.PokeRaros = Dados["PokeRaros"]
            self.PokeEpicos = Dados["PokeEpicos"]
            self.PokeMiticos = Dados["PokeMiticos"]
            self.PokeLendarios = Dados["PokeLendarios"]

    def Tira_item(self,item):
        if item["raridade"] == "Comum":
            self.Comuns.remove(item)
        elif item["raridade"] == "Incomum":
            self.Incomuns.remove(item)
        elif item["raridade"] == "Raro":
            self.Raros.remove(item)
        elif item["raridade"] == "Lendario":
            self.Lendarios.remove(item)

    def devolve_item(self,item):
            if item["raridade"] == "Comum":
                self.Comuns.append(item)
            elif item["raridade"] == "Incomum":
                self.Incomuns.append(item)
            elif item["raridade"] == "Raro":
                self.Raros.append(item)
            elif item["raridade"] == "Lendario":
                self.Lendarios.append(item)
    
    def devolve_pokemon(self,pokemon):
        if pokemon["raridade"] == "Comum":
            self.PokeComuns.append(pokemon)
        elif pokemon["raridade"] == "Incomum":
            self.PokeIncomuns.append(pokemon)
        elif pokemon["raridade"] == "Raro":
            self.PokeRaros.append(pokemon)
        elif pokemon["raridade"] == "Epico":
            self.PokeEpicos.append(pokemon)
        elif pokemon["raridade"] == "Mitico":
            self.PokeMiticos.append(pokemon)
        elif pokemon["raridade"] == "Lendario":
            self.PokeLendarios.append(pokemon)

    def ToDic(self):
        return {
            "Comuns": self.Comuns,
            "Incomuns": self.Incomuns,
            "Raros": self.Raros,
            "Lendarios": self.Lendarios,
            "PokeComuns": self.PokeComuns,
            "PokeIncomuns": self.PokeIncomuns,
            "PokeRaros": self.PokeRaros,
            "PokeEpicos": self.PokeEpicos,
            "PokeMiticos": self.PokeMiticos,
            "PokeLendarios": self.PokeLendarios,
        }

def GeraBaralhoClone(dados):
    Baralho(None,None,dados)

def spawn_do_centro(centro,Baralho,turnos):

    if turnos < 4:
        raridades = { "Comum": 45, "Incomum": 40, "Raro": 13, "Epico": 2, "Mitico": 0, "Lendario": 0 }

    elif turnos < 8:
        raridades = { "Comum": 35, "Incomum": 35, "Raro": 20, "Epico": 7, "Mitico": 3, "Lendario": 0 }

    elif turnos < 15:
        raridades = { "Comum": 28, "Incomum": 28, "Raro": 25, "Epico": 12, "Mitico": 5, "Lendario": 2}
    
    else:
        raridades = { "Comum": 18, "Incomum": 20, "Raro": 22, "Epico": 20, "Mitico": 13, "Lendario": 7}


    baralhos_por_raridade = {
        "Comum": Baralho.PokeComuns,
        "Incomum": Baralho.PokeIncomuns,
        "Raro": Baralho.PokeRaros,
        "Epico": Baralho.PokeEpicos,
        "Mitico": Baralho.PokeMiticos,
        "Lendario": Baralho.PokeLendarios
    }
    
    def spawn(centro,i):
        raridade_escolhida = random.choices(
                population=["Comum", "Incomum", "Raro", "Epico", "Mitico", "Lendario"],
                weights=[raridades["Comum"], raridades["Incomum"], raridades["Raro"], raridades["Epico"], raridades["Mitico"], raridades["Lendario"]],
                k=1
            )[0]
        
        BaralhoEscolhido = baralhos_por_raridade[raridade_escolhida]
        if BaralhoEscolhido == []:
            return
        centro[i] = random.choice(BaralhoEscolhido)
        GV.adicionar_mensagem(f"Um {centro[i]["nome"]} selvagem apareceu")
        BaralhoEscolhido.remove(centro[i])
    
    def despawn(centro,i):
        GV.adicionar_mensagem(f"Um {centro[i]["nome"]} selvagem desapareceu")
        Baralho.devolve_pokemon(centro[i])
        centro[i] = None

    for i,slot in enumerate(centro):
        if slot is not None:
            if random.choice([1,2,3,4]) == 1:
                despawn(centro,i)
                break

    pokemonsSpawn = 0
    for i,slot in enumerate(centro):
        if pokemonsSpawn == 2:
            break
        if slot is None:
            if random.choice([1,2,3]) == 1:
                spawn(centro,i)
                pokemonsSpawn += 1

    return centro

def Compra_Energia(player,custo=0):
    if player.ouro >= custo:
        tocar("Energia")
        energia_sorteada = None

        for i in range(30):
            energia_sorteada = random.choice(Energias)
            if player.energias[energia_sorteada] < player.energiasMax:
                break

        if energia_sorteada is not None:
            player.energias[energia_sorteada] += 1


        for i in range(30):
            energia_sorteada = random.choice(Energias)
            if player.energias[energia_sorteada] < player.energiasMax:
                break

        if energia_sorteada is not None:
            player.energias[energia_sorteada] += 1

    else:
        tocar("Bloq")
        GV.adicionar_mensagem("Sem ouro para comprar energias")

def Gera_item(Lista,Baralho):
    item = random.choice(Lista)
    Baralho.tira_item(item)
    return item

def item_extra(player,item):
    ItemExtra = dicionario_itens[item]
    ItemExtra["extra"] = True
    player.inventario.append(ItemExtra)

def coletor(player):
    for i in range(30):
        energia_sorteada = random.choice(Energias)
        if player.energias[energia_sorteada] < player.energiasMax:
            break
    if energia_sorteada is not None:
        player.energias[energia_sorteada] += 1

def Gera_Baralho(Deck1,Deck2):
    return Baralho(Deck1,Deck2)

def Gera_Mapa(i):
    return Mapa(i)

class Mapa:
    def __init__(self, i):

        Info = Estadios[i]
        self.i = i
        self.terreno = Info["Code Tabuleiro"]
        self.Musica = Info["Code Musica"]
        self.Fundo = Info["Code Tela"]
        self.Metros = Info["Metros"]
        self.mudança = False
        self.Peças = []
        self.Ocupadas = []

    def MudarEstagio(self,i):
        
        Info = Estadios[i]
        self.i = i
        self.terreno = Info["zona"]
        self.Musica = Info["Code Musica"]
        self.Fundo = Info["Code Tela"]
        self.Metros = Info["Metros"]
        self.mudança = True
        self.Ocupadas = []

    def Verifica(self, player, inimigo): 
        self.Ocupadas = []
        self.mudança = False

        for Peça in self.Peças:
            if Peça.pokemon.local is None:
                self.Peças.remove(Peça)

        for pokemon in player.pokemons + inimigo.pokemons:
            if pokemon.local is not None:
                pokemon.atualizar_rect()
                self.Ocupadas.append(pokemon.rect)

    def ToDic(self):
        return {
            "Code": self.i
    }