import random
import F_ataquesN
import F_ataquesS
import Evo2

def charmeleon(poke):
    
    Ataques_normais = [F_ataquesN.A]
    Ataques_especiais = [F_ataquesS.C]
    
    poke["nome"] = "charmeleon"
    poke["tipo"] = ["fogo"]
    poke["evolução"] = Evo2.charizard
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

def ivysaur(poke):
    
    Ataques_normais = [F_ataquesN.A]
    Ataques_especiais = [F_ataquesS.C]
    
    poke["nome"] = "ivysaur"
    poke["tipo"] = ["planta","venenoso"]
    poke["evolução"] = Evo2.charizard
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

def wartortle(poke):
    
    Ataques_normais = [F_ataquesN.A]
    Ataques_especiais = [F_ataquesS.C]
    
    poke["nome"] = "charmeleon"
    poke["tipo"] = ["agua"]
    poke["evolução"] = Evo2.charizard
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
