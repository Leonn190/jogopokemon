import random

def Gerador(Nome,Status_base,Ataques_normais,Ataques_especiais,Tipo,Evolução):
    
    Var_minuscula = (-5, 5)
    Var_baixa = (-10, 10)
    Var_media = (-20, 20)
    Var_alta = (-30, 30)

    if Status_base["Vida"] <= 50:
        Var_V = Var_minuscula
    elif Status_base["Vida"] <= 200:
        Var_V = Var_baixa
    elif Status_base["Vida"] <= 400:
        Var_V = Var_media
    else:
        Var_V = Var_alta
    Variacao = random.randint(*Var_V)
    vida = Status_base["Vida"] + Variacao

    if Status_base["Atk"] <= 20:
        Var_A = Var_minuscula
    elif Status_base["Atk"] <= 80:
        Var_A = Var_baixa
    else:
        Var_A = Var_media
    Variacao = random.randint(*Var_A)
    Atk = Status_base["Atk"] + Variacao

    if Status_base["Atk SP"] <= 20:
        Var_AS = Var_minuscula
    elif Status_base["Atk SP"] <= 80:
        Var_AS = Var_baixa
    else:
        Var_AS = Var_media
    Variacao = random.randint(*Var_AS)
    Atk_SP = Status_base["Atk SP"] + Variacao

    if Status_base["Def"] <= 20:
        Var_D = Var_minuscula
    elif Status_base["Def"] <= 80:
        Var_D = Var_baixa
    else:
        Var_D = Var_media
    Variacao = random.randint(*Var_D)
    Def = Status_base["Def"] + Variacao

    if Status_base["Def SP"] <= 20:
        Var_DS = Var_minuscula
    elif Status_base["Def SP"] <= 80:
        Var_DS = Var_baixa
    else:
        Var_DS = Var_media
    Variacao = random.randint(*Var_DS)
    Def_SP = Status_base["Def SP"] + Variacao
    
    def calc_iv(base, valor_final, intervalo):
        min_val, max_val = intervalo
        if max_val == min_val:
            return 0
        return ((valor_final - (base + min_val)) / (max_val - min_val)) * 100

    IVV = calc_iv(Status_base["Vida"], vida, Var_V)
    IVA = calc_iv(Status_base["Atk"], Atk, Var_A)
    IVAS = calc_iv(Status_base["Atk SP"], Atk_SP, Var_AS)
    IVD = calc_iv(Status_base["Def"], Def, Var_D)
    IVDS = calc_iv(Status_base["Def SP"], Def_SP, Var_DS)

    IV = round((IVV+IVA+IVAS+IVD+IVDS) / 5,2)

    return {
        "nome": Nome,
        "tipo": Tipo,
        "vida": vida,
        "estagio": "Basico",
        "atk": Atk,
        "atk SP": Atk_SP,
        "def": Def,
        "def SP": Def_SP,
        "velocidade": Status_base["Velocidade"],
        "XP": Status_base["XP"],
        "custo": Status_base["Custo"],
        "ataque normal": random.choice(Ataques_normais),
        "ataque especial": random.choice(Ataques_especiais),
        "evolução": Evolução,
        "XP atu": 0,
        "IV": f"{IV}%"
    }

def efetividade(Tipo_do_ataque,Tipo_do_atacado):
    
    tabela_tipos = {
    "normal":    {"normal": 0, "fogo": 0, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "veneno": 0, "terra": 0,
                  "voador": 0, "psíquico": 0, "inseto": 0, "pedra": 0, "fantasma": -0.75, "dragão": 0, "sombrio": 0, "aço": 0, "fada": 0},

    "fogo":      {"normal": 0, "fogo": -0.25, "água": -0.25, "elétrico": 0, "planta": 0.5, "gelo": 0.5, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psíquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragão": -0.25, "sombrio": 0,
                  "aço": 0.5, "fada": 0},

    "água":      {"normal": 0, "fogo": 0.5, "água": -0.25, "elétrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": 0.5, "voador": 0, "psíquico": 0, "inseto": 0, "pedra": 0.5, "fantasma": 0, "dragão": -0.25, "sombrio": 0,
                  "aço": 0, "fada": 0},

    "elétrico":  {"normal": 0, "fogo": 0, "água": 0.5, "elétrico": -0.25, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": -0.75, "voador": 0.5, "psíquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragão": -0.25, "sombrio": 0,
                  "aço": 0, "fada": 0},

    "planta":    {"normal": 0, "fogo": -0.25, "água": 0.5, "elétrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": -0.25,
                  "terra": 0.5, "voador": -0.25, "psíquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragão": -0.25,
                  "sombrio": 0, "aço": -0.25, "fada": 0},

    "gelo":      {"normal": 0, "fogo": -0.25, "água": -0.25, "elétrico": 0, "planta": 0.5, "gelo": -0.25, "lutador": 0, "veneno": 0,
                  "terra": 0.5, "voador": 0.5, "psíquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragão": 0.5, "sombrio": 0,
                  "aço": -0.25, "fada": 0},

    "lutador":   {"normal": 0.5, "fogo": 0, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0.5, "lutador": 0, "veneno": -0.25,
                  "terra": 0, "voador": -0.25, "psíquico": -0.25, "inseto": -0.25, "pedra": 0.5, "fantasma": -0.75, "dragão": 0,
                  "sombrio": 0.5, "aço": 0.5, "fada": -0.25},

    "veneno":    {"normal": 0, "fogo": 0, "água": 0, "elétrico": 0, "planta": 0.5, "gelo": 0, "lutador": 0, "veneno": -0.25,
                  "terra": -0.25, "voador": 0, "psíquico": 0, "inseto": 0, "pedra": -0.25, "fantasma": -0.25, "dragão": 0,
                  "sombrio": 0, "aço": -0.75, "fada": 0.5},

    "terra":     {"normal": 0, "fogo": 0.5, "água": 0, "elétrico": 0.5, "planta": -0.25, "gelo": 0, "lutador": 0, "veneno": 0.5,
                  "terra": 0, "voador": -0.75, "psíquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragão": 0,
                  "sombrio": 0, "aço": 0.5, "fada": 0},

    "voador":    {"normal": 0, "fogo": 0, "água": 0, "elétrico": -0.25, "planta": 0.5, "gelo": 0, "lutador": 0.5, "veneno": 0,
                  "terra": 0, "voador": 0, "psíquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragão": 0,
                  "sombrio": 0, "aço": -0.25, "fada": 0},

    "psíquico":  {"normal": 0, "fogo": 0, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "veneno": 0.5,
                  "terra": 0, "voador": 0, "psíquico": -0.25, "inseto": 0, "pedra": 0, "fantasma": 0, "dragão": 0,
                  "sombrio": -0.75, "aço": -0.25, "fada": 0},

    "inseto":    {"normal": 0, "fogo": -0.25, "água": 0, "elétrico": 0, "planta": 0.5, "gelo": 0, "lutador": -0.25, "veneno": -0.25,
                  "terra": 0, "voador": -0.25, "psíquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": -0.25, "dragão": 0,
                  "sombrio": 0.5, "aço": -0.25, "fada": -0.25},

    "pedra":     {"normal": 0, "fogo": 0.5, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0.5, "lutador": -0.25, "veneno": 0,
                  "terra": -0.25, "voador": 0.5, "psíquico": 0, "inseto": 0.5, "pedra": 0, "fantasma": 0, "dragão": 0,
                  "sombrio": 0, "aço": -0.25, "fada": 0},

    "fantasma":  {"normal": -0.75, "fogo": 0, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psíquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragão": 0,
                  "sombrio": -0.25, "aço": 0, "fada": 0},

    "dragão":    {"normal": 0, "fogo": 0, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psíquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragão": 0.5,
                  "sombrio": 0, "aço": -0.25, "fada": -0.75},

    "sombrio":   {"normal": 0, "fogo": 0, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0, "lutador": -0.25, "veneno": 0,
                  "terra": 0, "voador": 0, "psíquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragão": 0,
                  "sombrio": -0.25, "aço": 0, "fada": -0.25},

    "aço":       {"normal": 0, "fogo": -0.25, "água": -0.25, "elétrico": -0.25, "planta": 0, "gelo": 0.5, "lutador": 0, "veneno": 0,
                  "terra": 0, "voador": 0, "psíquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragão": 0,
                  "sombrio": 0, "aço": -0.25, "fada": 0.5},

    "fada":      {"normal": 0, "fogo": -0.25, "água": 0, "elétrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "veneno": -0.25,
                  "terra": 0, "voador": 0, "psíquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragão": 0.5,
                  "sombrio": 0.5, "aço": -0.25, "fada": 0},
    }
    
    multiplicador = 1
    for i in range(len(Tipo_do_ataque)):
        for j in range(len(Tipo_do_atacado)):
            multiplicador = multiplicador + tabela_tipos[Tipo_do_ataque[i]][Tipo_do_atacado[j]]

    return multiplicador
