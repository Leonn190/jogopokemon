import random
import ataquesN
import ataquesS
import Evo2

def charizard(poke):
    
    Ataques_normais = [ataquesN.A]
    Ataques_especiais = [ataquesS.C]
    
    poke["nome"] = "charizard"
    poke["tipo"] = ["fogo"]
    poke["evolução"] = "n"
    poke["estágio"] = "Estágio 1"
   
    poke["vida"] += 10
    poke["def"] += 10
    poke["def SP"] += 10
    poke["velocidade"] = 2
    poke["custo"] = 2
    poke["XP"] = 3
    poke["XP atu"] = 0

    poke["ataque_normal"] = random.choice(Ataques_normais)
    poke["ataque_especial"] = random.choice(Ataques_especiais)

    return poke