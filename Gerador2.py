import random
import GeradoresVisuais as GV
from Basicos import Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo
from itens import pokebolas_disponiveis,itens_disponiveis,amplificadores_disponiveis
import Funções2

class Jogador:
    def __init__(self, informaçoes):
        self.nome = informaçoes[0]
        self.pokemons = [Gerador_final(informaçoes[1])]
        self.inventario = []
        self.energias = { "vermelha": 0, "azul": 0, "amarela": 0, "verde": 0, "roxa": 0, "rosa": 0, "laranja": 0,"marrom": 0, "preta": 0, "cinza": 0}
        self.ouro = 10
    
    def ganhar_item(self,item):
        self.inventario.append(item)
    
    def usar_item(self,indice,Pokemon):
            item = self.inventario[indice] 
            if item["classe"] == "pokebola":
                GV.adicionar_mensagem("Pokebolas devem ser utilizadas apenas para capturar pokemons")
            else:
                if item["classe"] in ["poçao"] and Pokemon is not None:
                        cura = item["cura"]
                        self.inventario.remove(item)
                        Pokemon.curar(cura)
                        return
                elif item["classe"] in ["amplificador"] and Pokemon is not None:
                        tipo = item["aumento"]
                        self.inventario.remove(item)
                        Pokemon.amplificar(tipo,0.15,Pokemon)
                        return
                elif item["classe"] in ["caixa","coletor"]:
                    compras = item["compra"]
                    if item["classe"] in ["caixa"]:
                        self.inventario.remove(item)
                        for _ in range(compras):
                            self.inventario.append(caixa())
                        return
                    elif item["classe"] in ["coletor"]:
                        self.inventario.remove(item)
                        for _ in range(compras):
                            self.energias[coletor()] += 1
                        return
                else:
                    GV.adicionar_mensagem("selecione um pokemon para usar um item")
    def ganhar_pokemon(self,pokemon):
        self.pokemons.append(pokemon)


def Gerador_player(informaçoes):
    return Jogador(informaçoes)

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
        self.code = pokemon["code"]

    def evoluir(self):
        self.nome = self.evolucao["nome"]
        self.VidaMax = self.VidaMax * self.evolucao["vida"]
        self.Vida = round(self.Vida * self.evolucao["vida"],1)
        self.Def = round(self.Def * self.evolucao["def"],1)
        self.Def_sp = round(self.Def_sp * self.evolucao["def SP"],1)
        self.Atk = round(self.Atk * self.evolucao["atk"],1)
        self.Atk_sp = round(self.Atk_sp * self.evolucao["atk SP"],1)
        self.vel = self.evolucao["velocidade"]
        self.custo = self.evolucao["custo"]
        self.ataque_normal = random.choice(self.evolucao["ataques normais"])
        self.ataque_especial = random.choice(self.evolucao["ataques especiais"])
        self.xp_atu = 0
        self.Estagio = self.evolucao["estagio"]
        self.evolucao = self.evolucao["evolução"]

    def XP(self,quantidade):
        self.xp_atu = self.xp_atu + quantidade
        GV.adicionar_mensagem(f"{self.nome} ganhou {quantidade} de XP, seu XP atual é {self.xp_atu}")
        if self.xp_atu >= self.xp_total:
            self.evoluir()
    
    def amplificar(self,tipo,amplificador,pokemon_amplificado):
        if tipo == "XP atu":
            pokemon_amplificado.XP(1)
        elif tipo == "atk":
            J = self.Atk
            self.Atk = round(self.Atk + (self.Atk * amplificador),1)
            GV.adicionar_mensagem(f"{self.nome} amplificou seu ATK, foi de {J} para {self.Atk}")
        elif tipo == "atk SP":
            J = self.Atk_sp
            self.Atk_sp = round(self.Atk_sp + (self.Atk_sp * amplificador),1)
            GV.adicionar_mensagem(f"{self.nome} amplificou seu sp ATK, foi de {J} para {self.Atk_sp}")
        elif tipo == "def":
            J = self.Def
            self.Def = self.Def + round((self.Def * amplificador),1)
            GV.adicionar_mensagem(f"{self.nome} amplificou sua DEF, foi de {J} para {self.Def}")
        elif tipo == "def SP":
            J = self.Def_sp
            self.Def_sp = self.Def_sp + round((self.Def_sp * amplificador),1)
            GV.adicionar_mensagem(f"{self.nome} amplificou sua sp DEF, foi de {J} para {self.Def_sp}")
    
    def atacado(self,dano,player):
        danoOriginal = dano
        if self.Vida <= dano:
            dano = self.Vida
        
        self.Vida = round(self.Vida - dano,1)
        GV.adicionar_mensagem(f"{self.nome} recebeu {danoOriginal} de dano, sua vida atual é {self.Vida}")
        if self.Vida == 0:
            GV.adicionar_mensagem(f"{self.nome} foi nocauteado")
            player.pokemons.remove(self)

    def curar(self,cura):
        dano_tomado = self.VidaMax - self.Vida
        self.Vida = round(self.Vida + cura,1)
        if self.Vida > self.VidaMax:
            self.Vida = self.VidaMax
            cura = dano_tomado 
        GV.adicionar_mensagem(f"{self.nome} curou {round(cura,1)} de vida, sua vida atual é {self.Vida}")

    def atacar(self,alvo,player,inimigo,tipo):
        
        if tipo == "N":
            F = self.ataque_normal
            U = self.Atk
            V = alvo.Def
        else:
            F = self.ataque_especial
            U = self.Atk_sp
            V = alvo.Def_sp
        
        pagou = 0
        gastas = []
        for i in range(len(F["custo"])):
            if F["custo"][i] == "normal":
                for j in range(30):
                    j = random.randint(0,9)
                    if player.energias[Energias[j]] >= 1:
                        player.energias[Energias[j]] -= 1
                        gastas.append(Energias[j])
                        pagou += 1
                        break
            else:
                if player.energias[F["custo"][i]] >= 1:
                    player.energias[F["custo"][i]] -= 1
                    gastas.append(F["custo"][i])
                    pagou += 1
        
        if pagou != len(F["custo"]):
            GV.adicionar_mensagem("Sem energias, seu ataque falhou")
            for i in range(len(gastas)):
                player.energias[gastas[i]] += 1
            return None


        Dano_I = U * F["dano"]
        Tipo = F["tipo"]
        mitigação = 100 / (100 + V) 
        Dano_E = Dano_I * Funções2.efetividade(Tipo,alvo.tipo)
        dano_F = round(Dano_E * mitigação,1)


        GV.adicionar_mensagem (f"O seu {self.nome} causou {dano_F} de dano com o ataque")
        GV.adicionar_mensagem(f"{F['nome']} no {alvo.nome} inimigo")
        self.XP(1)
        alvo.atacado(dano_F,inimigo)
        
Pokedex = [0,Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo]
pokemons_possiveis = [Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo]
Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "rosa", "laranja", "marrom", "cinza", "preta"]

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
        "IV": f"{IV}%",
        "code": Pok["code"]
    }

def Gerador_final(code):
    return Pokemon(Gerador(Pokedex[code]))

def spawn_do_centro(centro):
    global pokemons_possiveis

    if len(centro) < 9: 
        chance = random.choice(["s","n"])
        if chance == "s":
            raridades = []
            for i in range(len(pokemons_possiveis)):
                for j in range(10 - pokemons_possiveis[i]["raridade"]):
                    raridades.append(pokemons_possiveis[i])
            pokemon_apareceu = random.choice(raridades)
            centro.append(pokemon_apareceu)
            GV.adicionar_mensagem(f"Um {pokemon_apareceu['nome']} selvagem apareceu no centro!")
    
    return centro

def gera_item(tipo,player,custo=0):

    raridades = []
    if player.ouro >= custo:
        if tipo == "energia":
            player.ouro -= custo
            energia_sorteada = random.choice(Energias)
            player.energias[energia_sorteada] += 1

        else:
            if tipo == "item":
                U = itens_disponiveis
            elif tipo == "pokebola":
                U = pokebolas_disponiveis
            elif tipo == "amplificador":
                U = amplificadores_disponiveis

            for i in range(len(U)):
                for j in range(6 - U[i]["raridade"]):
                    raridades.append(U[i])
            player.ouro -= custo
            item = random.choice(raridades)
            GV.adicionar_mensagem(f"Você comprou um item: {item["nome"]}")
            player.inventario.append(item)
    else:
        GV.adicionar_mensagem("Você não tem ouro o suficiente")

def caixa():
        raridades = []
        U = itens_disponiveis + pokebolas_disponiveis + amplificadores_disponiveis
        for i in range(len(U)):
                    for j in range(6 - U[i]["raridade"]):
                        raridades.append(U[i])
        item = random.choice(raridades)
        return item
def coletor():
    energia_sorteada = random.choice(Energias)
    return energia_sorteada