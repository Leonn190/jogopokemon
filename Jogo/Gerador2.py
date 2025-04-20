import random
import pygame
import Partida
import GeradoresVisuais as GV
from Dados.Basicos import Pokedex
from Dados.itens import pokebolas_disponiveis,itens_disponiveis,amplificadores_disponiveis,Estadios_disponiveis
from Dados.Estadios import Estadios
import Funções2 as FU
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30,Fonte35, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)


pygame.mixer.init()
clique = pygame.mixer.Sound("Jogo/Audio/Sons/Som1.wav")
Compra = pygame.mixer.Sound("Jogo/Audio/Sons/Compra.wav")
Usou = pygame.mixer.Sound("Jogo/Audio/Sons/Usou.wav")
Bom = pygame.mixer.Sound("Jogo/Audio/Sons/Bom.wav")
Bloq = pygame.mixer.Sound("Jogo/Audio/Sons/Bloq.wav")

efeitosPositivos = {
    "Confuso": 0,
    "Bloqueado": 0,
    "Envenenado": 0,
    "Tóxico": 0,
    "Fragilizado": 0,
    "Quebrado": 0,
    "Congelado": 0,
    "Queimado": 0,
    "Paralisado": 0,
    "Encharcado": 0,
    "Vampirico": 0,
    "Descarregado": 0,
    "Enfraquecido": 0
    }

EfeitosNegativos = {
    "Regeneração": 0,
    "Imune": 0,
    "Preparado": 0,
    "Provocando": 0,
    "Furtivo": 0,
    "Voando": 0,
    "Ofensivo": 0,
    "Reforçado": 0,
    "Imortal": 0,
    "Refletir": 0,
    "Focado": 0,
    "velocista": 0,
    "Energizado": 0,
    }

class Jogador:
    def __init__(self, informaçoes):
        self.nome = informaçoes[0]
        self.pokemons = [Gerador_final(informaçoes[1],1)]
        self.inventario = []
        self.energias = { "vermelha": 0, "azul": 0, "amarela": 0, "verde": 0, "roxa": 0, "rosa": 0, "laranja": 0,"marrom": 0, "preta": 0, "cinza": 0}
        self.energiasDesc = []
        self.ouro = 10
    
    def ganhar_item(self,item):
        self.inventario.append(item)
    
    def usar_item(self,indice,Pokemon):
            item = self.inventario[indice] 
            if item["classe"] in ["pokebola", "fruta"]:
                GV.tocar(Bloq)
                GV.adicionar_mensagem("Pokebolas e frutas são usadas no centro")
            else:
                if item["classe"] in ["poçao"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            cura = item["cura"]
                            GV.tocar(Usou)
                            self.inventario.remove(item)
                            Pokemon.curar(cura)
                            return
                        else:
                            GV.tocar(Bloq)
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser curados")
                elif item["classe"] in ["amplificador"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            tipo = item["aumento"]
                            GV.tocar(Usou)
                            self.inventario.remove(item)
                            Pokemon.amplificar(tipo,0.1,self)
                            return
                        else:
                            GV.tocar(Bloq)
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser amplificados")
                elif item["classe"] in ["caixa","coletor"]:
                    compras = item["compra"]
                    if item["classe"] in ["caixa"]:
                        GV.tocar(Usou)
                        self.inventario.remove(item)
                        for _ in range(compras):
                            self.inventario.append(caixa())
                        return
                    elif item["classe"] in ["coletor"]:
                        GV.tocar(Usou)
                        self.inventario.remove(item)
                        for _ in range(compras):
                            self.energias[coletor()] += 1
                        return
                elif item["classe"] == "estadio":
                    GV.tocar(Usou)
                    Partida.Mudar_estadio(item["ST Code"])
                    self.inventario.remove(item)
                    return
                else:
                    GV.tocar(Bloq)
                    GV.adicionar_mensagem("selecione um pokemon para usar um item")
    
    def ganhar_pokemon(self,pokemon):
        self.pokemons.append(pokemon)

    def muda_descarte(self,energia):
        if energia in self.energiasDesc:
            self.energiasDesc.remove(energia)
        else:
            self.energiasDesc.append(energia)

def Gerador_player(informaçoes):
    return Jogador(informaçoes)

IDpoke = 0

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
        self.AtkB = pokemon["atk"]
        self.Atk_spB = pokemon["atk SP"]
        self.DefB = pokemon["def"]
        self.Def_spB = pokemon["def SP"] 
        self.velB = pokemon["velocidade"]
        self.xp_total = pokemon["XP"]
        self.custo = pokemon["custo"]
        self.ataque_normal = pokemon["ataque normal"]
        self.ataque_especial = pokemon["ataque especial"]
        self.evolucao = pokemon["evolução"]
        self.xp_atu = pokemon["XP atu"]
        self.IV = pokemon["IV"]
        self.IV_vida = pokemon["IV vida"]
        self.IV_atk = pokemon["IV atk"]
        self.IV_atkSP = pokemon["IV atk SP"]
        self.IV_def = pokemon["IV def"]
        self.IV_defSP = pokemon["IV def SP"]
        self.IV_vel = pokemon["IV vel"]
        self.code = pokemon["code"]
        self.ID = pokemon["ID"] #unico
        self.guardado = 0
        self.local = None
        self.imagem = None
        self.efeitosPosi = efeitosPositivos
        self.efeitosNega = EfeitosNegativos


    def evoluir(self,player):
        if self.xp_atu >= self.xp_total:
            if isinstance(self.evolucao,list):
                self.evolucao = random.randint(self.evolucao)
            if self.evolucao is not None:
                nome_antigo = self.nome
                self.nome = self.evolucao["nome"]
                self.VidaMax = round(self.VidaMax * self.evolucao["vida"])
                self.Vida = round(self.Vida * self.evolucao["vida"])
                self.Def = round(self.Def * self.evolucao["def"])
                self.Def_sp = round(self.Def_sp * self.evolucao["def SP"])
                self.Atk = round(self.Atk * self.evolucao["atk"])
                self.Atk_sp = round(self.Atk_sp * self.evolucao["atk SP"])
                self.vel = round(self.vel * self.evolucao["velocidade"])
                self.custo = self.evolucao["custo"]
                self.ataque_normal = random.choice(self.evolucao["ataques normais"])
                self.ataque_especial = random.choice(self.evolucao["ataques especiais"])
                self.Estagio = self.evolucao["estagio"]
                self.xp_total = self.evolucao["XP"]
                self.evolucao = self.evolucao["evolução"]
                Partida.VerificaGIF()
                Partida.AddIMGpokemon(self)
                GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Incrivel!")
                return
        GV.tocar(Bloq)
        GV.adicionar_mensagem("Seu pokemon não pode evoluir")

    def Ganhar_XP(self,quantidade,player):
        self.xp_atu = self.xp_atu + quantidade
        GV.adicionar_mensagem(f"{self.nome} ganhou {quantidade} de XP, seu XP atual é {self.xp_atu}")
    
    def amplificar(self,tipo,amplificador,player):
        if tipo == "XP atu":
            self.Ganhar_XP(5,player)
        elif tipo == "atk":
            J = round(self.Atk)
            self.Atk = round(self.Atk + (self.AtkB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou seu ATK, foi de {J} para {self.Atk}")
        elif tipo == "atk SP":
            J = round(self.Atk_sp)
            self.Atk_sp = round(self.Atk_sp + (self.Atk_spB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou seu sp ATK, foi de {J} para {self.Atk_sp}")
        elif tipo == "def":
            J = round(self.Def)
            self.Def = self.Def + round((self.DefB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou sua DEF, foi de {J} para {self.Def}")
        elif tipo == "def SP":
            J = round(self.Def_sp)
            self.Def_sp = self.Def_sp + round((self.Def_spB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou sua sp DEF, foi de {J} para {self.Def_sp}")
    
    def atacado(self,dano,player,tipo,tela):
        DanoOriginal = dano
        if self.Vida <= dano:
            dano = self.Vida
        
        self.Vida = round(self.Vida - dano,1)

        if tipo == "N":
            cor = LARANJA
        else:
            cor = ROXO
        i = player.pokemons.index(self)
        Partida.adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",cor,Fonte35,((1375 - i * 190),260))
        GV.adicionar_mensagem(f"{self.nome} recebeu {DanoOriginal} de dano, sua vida atual é {self.Vida}")
        if self.Vida == 0:
            GV.adicionar_mensagem(f"{self.nome} foi nocauteado")

    def curar(self,cura):
            dano_tomado = self.VidaMax - self.Vida
            self.Vida = round(self.Vida + cura,1)
            if self.Vida > self.VidaMax:
                self.Vida = self.VidaMax
                cura = dano_tomado 
            GV.adicionar_mensagem(f"{self.nome} curou {round(cura,1)} de vida, sua vida atual é {self.Vida}")

    def atacar(self,alvo,player,inimigo,tipo,tela,Mapa):
        
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
                for cor in player.energiasDesc:
                    if player.energias[cor] >= 1:
                        player.energias[cor] -= 1
                        gastas.append(cor)
                        pagou += 1
                        break
            else:
                if player.energias[F["custo"][i]] >= 1:
                    player.energias[F["custo"][i]] -= 1
                    gastas.append(F["custo"][i])
                    pagou += 1

        
        
        if pagou != len(F["custo"]):
            GV.tocar(Bloq)
            GV.adicionar_mensagem("Sem energias, seu ataque falhou")
            for i in range(len(gastas)):
                player.energias[gastas[i]] += 1
            return None

        distancia = FU.distancia_entre_pokemons(self,alvo,Mapa.Metros)
        Over = F["alcance"] - distancia
        if Over < 0:
            assertividade = F["precisão"] + Over
        else:
            assertividade = F["precisão"]
        desfoco = random.randint(0,100)
        if desfoco > assertividade:
            GV.adicionar_mensagem("Você errou o ataque")
            return



        Dano_I = U * F["dano"]
        Tipo = F["tipo"]
        mitigação = 100 / (100 + V) 
        Dano_E = Dano_I * FU.efetividade(Tipo,alvo.tipo)
        dano_F = round(Dano_E * mitigação,1)

        GV.adicionar_mensagem (f"O seu {self.nome} causou {dano_F} de dano com o ataque")
        GV.adicionar_mensagem(f"{F['nome']} no {alvo.nome} inimigo")
        XP_ATK = random.randint(3,5)
        self.Ganhar_XP(XP_ATK,player)
        alvo.atacado(dano_F,inimigo,tipo,tela)
        
Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "rosa", "laranja", "marrom", "cinza", "preta"]

def Gerador(Pokemon,P):
    print (P)
    global IDpoke
    IDpoke += 1
    Pok = Pokemon

    vida_min = int(Pok["vida"] * 0.8)
    vida_max = int(Pok["vida"] * 1.2)
    vida_max_real = int(vida_max * P)
    vida = random.randint(vida_min, vida_max_real)
    vida = min(vida, int(Pok["vida"] * 1.2))

    atk_min = int(Pok["atk"] * 0.8)
    atk_max = int(Pok["atk"] * 1.2)
    atk_max_real = int(atk_max * P)
    Atk = random.randint(atk_min, atk_max_real)
    Atk = min(Atk, int(Pok["atk"] * 1.2))

    atkSP_min = int(Pok["atk SP"] * 0.8)
    atkSP_max = int(Pok["atk SP"] * 1.2)
    atkSP_max_real = int(atkSP_max * P)
    Atk_SP = random.randint(atkSP_min, atkSP_max_real)
    Atk_SP = min(Atk_SP, int(Pok["atk SP"] * 1.2))

    def_min = int(Pok["def"] * 0.8)
    def_max = int(Pok["def"] * 1.2)
    def_max_real = int(def_max * P)
    Def = random.randint(def_min, def_max_real)
    Def = min(Def, int(Pok["def"] * 1.2))

    defSP_min = int(Pok["def SP"] * 0.8)
    defSP_max = int(Pok["def SP"] * 1.2)
    defSP_max_real = int(defSP_max * P)
    Def_SP = random.randint(defSP_min, defSP_max_real)
    Def_SP = min(Def_SP, int(Pok["def SP"] * 1.2))

    vel_min = int(Pok["velocidade"] * 0.8)
    vel_max = int(Pok["velocidade"] * 1.2)
    vel_max_real = int(vel_max * P)
    vel = random.randint(vel_min, vel_max_real)
    vel = min(vel, int(Pok["velocidade"] * 1.2))

    IVV = ((vida - vida_min) / (vida_max - vida_min)) * 100
    IVA = ((Atk - atk_min) / (atk_max - atk_min)) * 100
    IVAS = ((Atk_SP - atkSP_min) / (atkSP_max - atkSP_min)) * 100
    IVD = ((Def - def_min) / (def_max - def_min)) * 100
    IVDS = ((Def_SP - defSP_min) / (defSP_max - defSP_min)) * 100
    IVVE = ((vel - vel_min) / (vel_max - vel_min)) * 100

    IV = round((IVV + IVA + IVAS + IVD + IVDS + IVVE) / 6, 2)

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
        "velocidade": vel,
        "XP": Pok["XP"],
        "custo": Pok["custo"],
        "ataque normal": random.choice(Pok["ataques normais"]),
        "ataque especial": random.choice(Pok["ataques especiais"]),
        "evolução": Pok["evolução"],
        "XP atu": 0,
        "IV": IV,
        "IV vida": round(IVV, 1),
        "IV atk": round(IVA, 1),
        "IV atk SP": round(IVAS, 1),
        "IV def": round(IVD, 1),
        "IV def SP": round(IVDS, 1),
        "IV vel": round(IVVE, 1),
        "code": Pok["code"],
        "ID": IDpoke 
    }

def Gerador_final(code,P):
    return Pokemon(Gerador(Pokedex[code],P))

def spawn_do_centro(centro):
    pokemons_possiveis = Pokedex.copy()
    if 0 in pokemons_possiveis:
        pokemons_possiveis.remove(0)


    if len(centro) < 9:
        if random.choice(["s", "n"]) == "s":
            # Cria uma lista ponderada com base na raridade (quanto menor a raridade, mais comum)
            raridades = []
            for pokemon in pokemons_possiveis:
                raridades.extend([pokemon] * (11 - pokemon["raridade"]))

            # Seleciona um Pokémon aleatório com base na raridade
            pokemon_apareceu = random.choice(raridades)
            centro.append(pokemon_apareceu)

            GV.adicionar_mensagem(f"Um {pokemon_apareceu['nome']} selvagem apareceu no centro!")

    return centro

def gera_item(tipo,player,custo=0,Turno=10):
    U = None
    if len(player.inventario) < 10:
        raridades = []
        if player.ouro >= custo:
            if tipo == "energia":
                player.ouro -= custo
                energia_sorteada = random.choice(Energias)
                player.energias[energia_sorteada] += 1
                energia_sorteada = random.choice(Energias)
                player.energias[energia_sorteada] += 1

            else:
                if tipo == "item":
                    U = itens_disponiveis
                elif tipo == "pokebola":
                    U = pokebolas_disponiveis
                elif tipo == "amplificador":
                    if Turno > 3:
                        U = amplificadores_disponiveis
                elif tipo == "estadio":
                    if Turno > 5:
                        U = Estadios_disponiveis
    
                if U is not None:
                    for i in range(len(U)):
                        for j in range(6 - U[i]["raridade"]):
                            raridades.append(U[i])
                    player.ouro -= custo
                    item = random.choice(raridades)
                    GV.tocar(Compra)
                    GV.adicionar_mensagem(f"Você comprou um item: {item["nome"]}")
                    player.inventario.append(item)
                else:
                        GV.tocar(Bloq)
        else:
            GV.tocar(Bloq)
            GV.adicionar_mensagem("Você não tem ouro o suficiente")
    else:
        GV.tocar(Bloq)
        GV.adicionar_mensagem("Seu inventário está cheio")

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

def Gera_Mapa(i):
    return Mapa(Estadios[i])


class Mapa:
    def __init__(self, Info):
        self.tempo = Info["Tempo"]
        self.area = Info["zona"]
        self.cores = Info["cores"]
        self.PlojaI = Info["LojaItens"]
        self.PlojaP = Info["LojaPokebolas"]
        self.PlojaE = Info["LojaEnergias"]
        self.PlojaA = Info["LojaAmplificadores"]
        self.pLojaT = Info["LojaTreEst"]
        self.Musica = Info["Code Musica"]
        self.Fundo = Info["Code Tela"]
        self.Metros = Info["Metros"]
