import importlib
import random
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade

def Regular(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def Irregular(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta = I(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta)

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

DicionarioAtaques = {

    "Jato de Agua": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_de_Agua,
    "Jato Duplo": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_Duplo,
    "Bolhas": lambda: importlib.import_module("Dados.Ataques.Agua").Bolhas,
    "Controle do Oceano": lambda: importlib.import_module("Dados.Ataques.Agua").Controle_do_Oceano,
    "Splash": lambda: importlib.import_module("Dados.Ataques.Agua").Splash,
    "Vasculhar no Rio": lambda: importlib.import_module("Dados.Ataques.Agua").Vasculhar_no_Rio,
    "Golpe de Concha": lambda: importlib.import_module("Dados.Ataques.Agua").Golpe_de_Concha,
    "Gota Pesada": lambda: importlib.import_module("Dados.Ataques.Agua").Gota_Pesada,

    "Tapa": lambda: importlib.import_module("Dados.Ataques.Normal").Tapa,
    "Cabeçada": lambda: importlib.import_module("Dados.Ataques.Normal").Cabeçada,
    "Investida": lambda: importlib.import_module("Dados.Ataques.Normal").Investida,
    "Vasculhar": lambda: importlib.import_module("Dados.Ataques.Normal").Vasculhar,

    "Sopro do Dragao": lambda: importlib.import_module("Dados.Ataques.Dragao").Sopro_do_Dragao,

    "Faisca": lambda: importlib.import_module("Dados.Ataques.Eletrico").Faisca,
    "Energizar": lambda: importlib.import_module("Dados.Ataques.Eletrico").Energizar,
    "Eletrolise Hidrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Eletrolise_Hidrica,
    "Choque do Trovao": lambda: importlib.import_module("Dados.Ataques.Eletrico").Choque_do_Trovao,
    "Onda Eletrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Onda_Eletrica,

    "Queimar": lambda: importlib.import_module("Dados.Ataques.Fogo").Queimar,

    "Cristalizar": lambda: importlib.import_module("Dados.Ataques.Gelo").Cristalizar,

    "Mordida": lambda: importlib.import_module("Dados.Ataques.Inseto").Mordida,

    "Soco": lambda: importlib.import_module("Dados.Ataques.Lutador").Soco,
    "Chamar para Briga": lambda: importlib.import_module("Dados.Ataques.Lutador").Chamar_para_Briga,

    "Reforçar": lambda: importlib.import_module("Dados.Ataques.Metal").Reforçar,
    
    "Pedregulho": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedregulho,

    "Confusao": lambda: importlib.import_module("Dados.Ataques.Eletrico").Confusão,

    "Nas Sombras": lambda: importlib.import_module("Dados.Ataques.Sombrio").Nas_Sombras,

    "Voar": lambda: importlib.import_module("Dados.Ataques.Voador").Voar,

    "Envenenar": lambda: importlib.import_module("Dados.Ataques.Veneno").Envenenar,

    "Dreno": lambda: importlib.import_module("Dados.Ataques.Planta").Dreno,
    "Disparo de Semente": lambda: importlib.import_module("Dados.Ataques.Planta").Disparo_de_Semente,
    "Chicote de Vinha": lambda: importlib.import_module("Dados.Ataques.Planta").Chicote_de_Vinha,
    "Cura Natural": lambda: importlib.import_module("Dados.Ataques.Planta").Cura_Natural,
}

def SelecionaAtaques(O1,O2,O3=None,O4=None,O5=None,O6=None,O7=None,O8=None):
    Opçoes = [O1,O2,O3,O4,O5,O6,O7,O8]
    Seleçao = []
    for O in Opçoes:
        if O is not None:
            Seleçao.append(O)
    
    Sorteado = random.choice(Seleçao)
    return DicionarioAtaques[Sorteado]()