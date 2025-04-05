import ataquesN
import ataquesS
import Evo1
import Gerador

def gerador_charmander():
    
    Nome = "Charmander"
    Tipo = ["fogo"]
    Evolução = [Evo1.charmeleon]

    Status_base = {
        "Vida": 100,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [ataquesN.golpe_de_fogo]
    Ataques_especiais = [ataquesS.fogo_puro,ataquesS.defesa_flamejante]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)
    
def gerador_bulbasaur():
    
    Nome = "Bulbasaur"
    Tipo = ["planta","veneno"]
    Evolução = [Evo1.ivysaur]

    Status_base = {
        "Vida": 100,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [ataquesN.golpe_de_fogo,ataquesN.disparo_quente]
    Ataques_especiais = [ataquesS.fogo_puro]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)

def gerador_squirtle():

    Nome = "Squirtle"
    Tipo = ["agua"]
    Evolução = [Evo1.wartorle]

    Status_base = {
        "Vida": 100,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [ataquesN.golpe_de_fogo,ataquesN.disparo_quente]
    Ataques_especiais = [ataquesS.fogo_puro]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)

def pokemon():
    
    Nome = ""
    Tipo = ["",""]
    Evolução = [Evo1.]

    Status_base = {
        "Vida": ,
        "Def": ,
        "Def SP": ,
        "Velocidade": ,
        "XP": ,
        "Custo": 
    }

    Ataques_normais = [ataquesN.,ataquesN.]
    Ataques_especiais = [ataquesS.,ataquesS.]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)