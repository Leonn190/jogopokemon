# Modelo de Gerador de pokemon
def pokemon():
    
    Nome = ""
    Tipo = ["",""]
    Evolução = [Evo1.]

    Status_base = {
        "Vida": ,   
        "Atk": ,
        "Atk SP" ,
        "Def": ,
        "Def SP": ,
        "Velocidade": ,
        "XP": ,
        "Custo": 
    }

    Ataques_normais = [ataquesN.,ataquesN.]
    Ataques_especiais = [ataquesS.,ataquesS.]

    return Gerador.Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução)

def ataque_n(atacante,alvo,player,inimigo):
    Dano = atacante["atk"] * 
    Tipo = ["",]
    mitigação = (100 / 100 + alvo["def"]) 
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)

def ataque_s(atacante,alvo,player,inimigo):
    Dano = atacante["atk SP"] * 
    Tipo = ["",]
    mitigação = 100 / (100 + alvo["def SP"]) 
    Dano_E = Dano * Funções.efetividade(Tipo,alvo["tipo"])
    
    dano_F = Dano_E * mitigação
    alvo["vida"] = round(alvo["vida"] - dano_F,2)
