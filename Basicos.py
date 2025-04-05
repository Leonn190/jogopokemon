import ataquesN
import ataquesS
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

    Ataques_normais = [ataquesN.A]
    Ataques_especiais = [ataquesS.C,ataquesS.D]

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

    Ataques_normais = [ataquesN.A,ataquesN.B]
    Ataques_especiais = [ataquesS.D]

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

    Ataques_normais = [ataquesN.A,ataquesN.B]
    Ataques_especiais = [ataquesS.C]

    return Funções.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)