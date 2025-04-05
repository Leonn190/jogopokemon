import ataques
import Gerador

def gerador_charmander():
    Nome = "Charmander"
    Tipo = ["fogo"]

    Status_base = {
        "Vida": 100,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [ataques.golpe_de_fogo]
    Ataques_especiais = [ataques.fogo_puro,ataques.defesa_flamejante]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo)
    
def gerador_bulbasauro():
    Nome = "Bulbasauro"

    Status_base = {
        "Vida": 100,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [ataques.golpe_de_fogo,ataques.disparo_quente]
    Ataques_especiais = [ataques.fogo_puro]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais)

def gerador_squirtle():
    Nome = "Squirtle"

    Status_base = {
        "Vida": 100,
        "Def": 10,
        "Def SP": 10,
        "Velocidade": 3,
        "XP": 3,
        "Custo": 1
    }

    Ataques_normais = [ataques.golpe_de_fogo,ataques.disparo_quente]
    Ataques_especiais = [ataques.fogo_puro]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais)

