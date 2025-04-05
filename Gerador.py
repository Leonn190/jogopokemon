import random

def Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução):
    
    Var_nula = [0]
    Var_baixa = [10,0,0,-10]
    Var_media = [20,10,0,0,0,-10,-20]
    Var_alta = [30,20,10,0,0,0,0,-10,-20,-30]

    Var_V =  Var_nula
    if Status_base["Vida"] <= 200:
        Var_V = Var_baixa
        Variacao = random.choice(Var_V)
    elif Status_base["Vida"] <= 400:
        Var_V = Var_media
        Variacao = random.choice(Var_V)
    elif Status_base["Vida"] > 400:
        Var_V = Var_alta
        Variacao = random.choice(Var_V)
    vida = Status_base["Vida"] + Variacao
    
    Var_D = Var_nula
    if Status_base["Def"] <= 20:
        Variacao = Var_nula[0]
    elif Status_base["Def"] <= 80:
        Var_D = Var_media
        Variacao = random.choice(Var_D)
    elif Status_base["Def"] > 80:
        Var_D = Var_baixa
        Variacao = random.choice(Var_D)
    Def = Status_base["Def"] + Variacao

    Var_DS = Var_nula
    if Status_base["Def SP"] <= 20:
        Variacao = Var_nula[0]
    elif Status_base["Def SP"] <= 80:
        Var_DS = Var_media
        Variacao = random.choice(Var_DS)
    elif Status_base["Def SP"] > 80:
        Var_DS = Var_baixa
        Variacao = random.choice(Var_DS)
    Def_SP = Status_base["Def SP"] + Variacao

    if max(Var_D) == min(Var_D):
        Var_D.append (1)

    if max(Var_DS) == min(Var_DS):
        Var_DS.append (1)

    IVV = ((vida - (Status_base["Vida"] + min(Var_V))) / (max(Var_V) - min(Var_V))) * 100
    IVD = ((Def - (Status_base["Def"] + min(Var_D))) / (max(Var_D) - min(Var_D))) * 100
    IVDS = ((Def_SP - (Status_base["Def SP"] + min(Var_DS))) / (max(Var_DS) - min(Var_DS))) * 100

    IV = round(IVV + IVD + IVDS / 3,2)

    return {
        "nome": Nome,
        "tipo": Tipo,
        "vida": vida,
        "estagio": "Basico",
        "def": Def,
        "def SP": Def_SP,
        "velocidade": Status_base["Velocidade"],
        "XP": Status_base["XP"],
        "custo": Status_base["Custo"],
        "ataque normal": random.choice(Ataques_normais),
        "ataque especial": random.choice(Ataques_especiais),
        "evolução": Evolução,
        "XP Atu": 0,
        "IV": f"{IV}%"
    }
