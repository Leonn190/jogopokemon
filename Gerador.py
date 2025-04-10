import random
import Funções
from itens import pokebolas_disponiveis,itens_disponiveis,amplificadores_disponiveis
from Basicos import Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo

class Jogador:
    def __init__(self, informaçoes):
        self.nome = informaçoes[0]
        self.pokemons = [informaçoes[1]]
        self.inventário = [0,]



class Pokemon:
    def __init__(self, pokemon):
        self.nome = pokemon["nome"]
        self.tipo = pokemon["tipo"]
        self.raridade = pokemon["raridade"]
        self.dificuldade = pokemon["dificuldade"]
        self.VidaMax = pokemon["vida"]
        self.Vida = pokemon["vida"]
        self.Estagio = pokemon["estagio"]
        self.Atk = pokemon["atk"]
        self.Atk_sp = pokemon["atk SP"]
        self.Def = pokemon["def"]
        self.Def_sp = pokemon["def SP"]
        self.vel = pokemon["velocidade"]
        self.xp_total = pokemon["XP"]
        self.custo = pokemon["custo"]
        self.ataque_normal = pokemon["ataque normal"]
        self.ataque_especial = pokemon["ataque especial"]
        self.evolucao = pokemon["evolução"]
        self.xp_atu = pokemon["XP atu"]
        self.IV = pokemon["IV"]

    def evoluir(self):
        self.nome = self.evolucao["nome"]
        self.VidaMax = self.VidaMax * self.evolucao["vida"]
        self.Vida = self.Vida * self.evolucao["vida"]
        self.Def = self.Def * self.evolucao["def"]
        self.Def_sp = self.Def_sp * self.evolucao["def SP"]
        self.Atk = self.Atk * self.evolucao["atk"]
        self.Atk_sp = self.Atk_sp * self.evolucao["atk SP"]
        self.vel = self.evolucao["vel"]
        self.custo = self.evolucao["custo"]
        self.ataque_normal = self.evolucao["ataque normal"]
        self.ataque_especial = self.evolucao["ataque especial"]
        self.xp_atu = 0
        self.Estagio = self.evolucao["estagio"]

    def XP(self,quantidade):
        self.xp_atu = self.xp_atu + quantidade
        print (f"{self.nome} ganhou {quantidade} de XP, seu XP atual é {self.xp_atu}")
    
    def amplificar(self,tipo,amplificador,pokemon_amplificado):
        if tipo == "XP atu":
            pokemon_amplificado.XP(1)
        elif tipo == "atk":
            J = self.Atk
            self.Atk = self.Atk + (self.Atk * amplificador)
            print (f"{self.nome} amplificou seu ATK, foi de {J} para {self.Atk}")
        elif tipo == "atk SP":
            J = self.Atk_sp
            self.Atk_sp = self.Atk_sp + (self.Atk_sp * amplificador)
            print (f"{self.nome} amplificou seu sp ATK, foi de {J} para {self.Atk_sp}")
        elif tipo == "def":
            J = self.Def
            self.Def = self.Def + (self.Def * amplificador)
            print (f"{self.nome} amplificou sua DEF, foi de {J} para {self.Def}")
        elif tipo == "def SP":
            J = self.Def_sp
            self.Def_sp = self.Def_sp + (self.Def_sp * amplificador)
            print (f"{self.nome} amplificou sua sp DEF, foi de {J} para {self.Def_sp}")
    
    def atacado(self,dano):
        self.Vida = self.Vida - dano
        print (f"A vida atual do {self.nome} inimigo é {round(self.Vida,2)}")

    def curar(self,cura):
        dano_tomado = self.VidaMax - self.Vida
        self.Vida = self.Vida + cura
        if self.Vida > self.VidaMax:
            self.Vida = self.VidaMax
            cura = dano_tomado 
        print (f"{self.nome} curou {cura} de vida, sua vida atual é {self.Vida}")

    def atacar(self,alvo,player,inimigo,tipo):
        
        if tipo == 1:
            F = self.ataque_normal
            U = self.Atk
            V = alvo.Def
        else:
            F = self.ataque_especial
            U = self.Atk_sp
            V = alvo.Def_sp
        
  
        pagou = 0
        for i in range(len(F["custo"])):
            if F["custo"][i] == "normal":
                for j in range(len(player[4])):
                    if player[3][player[4][j]] >= 1:
                        player[3][player[4][j]] = player[3][player[4][j]] - 1
                        pagou += 1
                        break
            else:
                if player[3][F["custo"][i]] >= 1:
                    player[3][F["custo"][i]] = player[3][F["custo"][i]] - 1
                    pagou += 1
        
        if pagou != len(F["custo"]):
            print ("Sem energias, seu ataque falhou")
            return 0

        Dano_I = U * F["dano"]
        Tipo = F["tipo"]
        mitigação = 100 / (100 + V) 
        Dano_E = Dano_I * Funções.efetividade(Tipo,alvo.tipo)
        dano_F = Dano_E * mitigação


        print (f"O seu {self.nome} causou {round(dano_F,2)} de dano com o ataque {F['nome']} no {alvo.nome} inimigo")
        alvo.atacado(dano_F)
        
Pokedex = [0,Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo]
pokemons_possiveis = [Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo]

def Gerador(Pokemon):
    Pok = Pokemon

    Var_minuscula = (-5, 5)
    Var_baixa = (-10, 10)
    Var_media = (-20, 20)
    Var_alta = (-30, 30)

    if Pok["vida"] <= 50:
        Var_V = Var_minuscula
    elif Pok["vida"] <= 200:
        Var_V = Var_baixa
    elif Pok["vida"] <= 400:
        Var_V = Var_media
    else:
        Var_V = Var_alta
    Variacao = random.randint(*Var_V)
    vida = Pok["vida"] + Variacao

    if Pok["atk"] <= 20:
        Var_A = Var_minuscula
    elif Pok["atk"] <= 80:
        Var_A = Var_baixa
    else:
        Var_A = Var_media
    Variacao = random.randint(*Var_A)
    Atk = Pok["atk"] + Variacao

    if Pok["atk SP"] <= 20:
        Var_AS = Var_minuscula
    elif Pok["atk SP"] <= 80:
        Var_AS = Var_baixa
    else:
        Var_AS = Var_media
    Variacao = random.randint(*Var_AS)
    Atk_SP = Pok["atk SP"] + Variacao

    if Pok["def"] <= 20:
        Var_D = Var_minuscula
    elif Pok["def"] <= 80:
        Var_D = Var_baixa
    else:
        Var_D = Var_media
    Variacao = random.randint(*Var_D)
    Def = Pok["def"] + Variacao

    if Pok["def SP"] <= 20:
        Var_DS = Var_minuscula
    elif Pok["def SP"] <= 80:
        Var_DS = Var_baixa
    else:
        Var_DS = Var_media
    Variacao = random.randint(*Var_DS)
    Def_SP = Pok["def SP"] + Variacao
    
    def calc_iv(base, valor_final, intervalo):
        min_val, max_val = intervalo
        if max_val == min_val:
            return 0
        return ((valor_final - (base + min_val)) / (max_val - min_val)) * 100

    IVV = calc_iv(Pok["vida"], vida, Var_V)
    IVA = calc_iv(Pok["atk"], Atk, Var_A)
    IVAS = calc_iv(Pok["atk SP"], Atk_SP, Var_AS)
    IVD = calc_iv(Pok["def"], Def, Var_D)
    IVDS = calc_iv(Pok["def SP"], Def_SP, Var_DS)

    IV = round((IVV+IVA+IVAS+IVD+IVDS) / 5,2)

    return {
        "nome": Pok["nome"],
        "tipo": Pok["tipo"],
        "raridade": Pok["raridade"],
        "dificuldade": Pok["dificuldade"],
        "vida": vida,
        "estagio": "basico",
        "atk": Atk,
        "atk SP": Atk_SP,
        "def": Def,
        "def SP": Def_SP,
        "velocidade": Pok["velocidade"],
        "XP": Pok["XP"],
        "custo": Pok["custo"],
        "ataque normal": random.choice(Pok["ataques normais"]),
        "ataque especial": random.choice(Pok["ataques especiais"]),
        "evolução": Pok["evolução"],
        "XP atu": 0,
        "IV": f"{IV}%"
    }

def Gerador_final(code):
    return Pokemon(Gerador(Pokedex[code]))

def spawn_do_centro(centro):
    global pokemons_possiveis
    
    raridades = []
    for i in range(len(pokemons_possiveis)):
        for j in range(10 - pokemons_possiveis[i]["raridade"]):
            raridades.append(pokemons_possiveis[i])
    pokemon_apareceu = random.choice(raridades)
    centro.append(pokemon_apareceu)
    print (f"Um {pokemon_apareceu['nome']} selvagem apareceu no centro!")
    return centro

def ganhar_item(tipo):

    raridades = []

    if tipo == "item":
        U = itens_disponiveis
    elif tipo == "pokebola":
        U = pokebolas_disponiveis
    elif tipo == "amplificador":
        U = amplificadores_disponiveis

    for i in range(len(U)):
        for j in range(6 - U[i]["raridade"]):
            raridades.append(U[i])
    item = random.choice(raridades)
    return item
        