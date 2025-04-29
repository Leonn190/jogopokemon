import importlib
import random
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade

def padrao(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela)

DicionarioAtaques = {

    "Jato de Agua": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_de_Agua,
    "Jato Duplo": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_Duplo,

}

def SelecionaAtaques(O1,O2,O3=None,O4=None,O5=None,O6=None,O7=None,O8=None):
    Opçoes = [O1,O2,O3,O4,O5,O6,O7,O8]
    Seleçao = []
    for O in Opçoes:
        if O is not None:
            Seleçao.append(O)
    
    Sorteado = random.choice(Seleçao)
    return DicionarioAtaques[Sorteado]()