from D_ataquesN import A
from D_ataquesN import B
from D_ataquesS import C
from D_ataquesS import D
import Evo1
import Funções

def gerador_charmander():
    
    Nome = "Charmander"
    Tipo = ["fogo"]
    Evolução = Evo1.charmeleon

    Status_base = {
        "Vida": 100,
        "Atk": 20,
        "Atk SP": 20,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [A]
    Ataques_especiais = [C,D]

    return Funções.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)
    
def gerador_bulbasaur():
    
    Nome = "Bulbasaur"
    Tipo = ["planta","veneno"]
    Evolução = Evo1.ivysaur

    Status_base = {
        "Vida": 100,
        "Atk": 20,
        "Atk SP": 20,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [A,B]
    Ataques_especiais = [D]

    return Funções.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)

def gerador_squirtle():

    Nome = "Squirtle"
    Tipo = ["agua"]
    Evolução = Evo1.wartortle

    Status_base = {
        "Vida": 100,
        "Atk": 20,
        "Atk SP": 20,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [A,B]
    Ataques_especiais = [C]

    return Funções.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)