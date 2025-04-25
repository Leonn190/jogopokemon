import random
import pygame
import Efeitos as E
from Sonoridade import tocar
import Partida as P
import GeradoresVisuais as GV
from Dados.Gen1.Basicos import Pokedex
from Dados.itens import pokebolas_disponiveis,itens_disponiveis,amplificadores_disponiveis,Estadios_disponiveis
from Dados.Estadios import Estadios
import Funções2 as FU
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30,Fonte35, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

pygame.init()
pygame.mixer.init()
clique = pygame.mixer.Sound("Jogo/Audio/Sons/Som1.wav")
Compra = pygame.mixer.Sound("Jogo/Audio/Sons/Compra.wav")
Usou = pygame.mixer.Sound("Jogo/Audio/Sons/Usou.wav")
Bom = pygame.mixer.Sound("Jogo/Audio/Sons/Bom.wav")
Bloq = pygame.mixer.Sound("Jogo/Audio/Sons/Bloq.wav")

evoluirEFE = GV.carregar_frames('imagens/Efeitos/Evoluindo_frames')

EfeitosNegativos = {
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
    "Enfraquecido": 0,
    "Incapacitado": 0 
    }

EfeitosPositivos = {
    "Regeneração": 0,
    "Abençoado": 0,
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
    "Velocista": 0,
    "Energizado": 0,
    }

class Jogador:
    def __init__(self, informaçoes):
        self.nome = informaçoes[0]
        self.pokemons = [Gerador_final(informaçoes[1],1,self)]
        self.inventario = []
        self.Captura = []
        self.energias = { "vermelha": 0, "azul": 0, "amarela": 0, "verde": 0, "roxa": 0, "rosa": 0, "laranja": 0,"marrom": 0, "preta": 0, "cinza": 0}
        self.energiasDesc = []
        self.ouro = 10
    
    def ganhar_item(self,item):
        self.inventario.append(item)
    
    def usar_item(self,indice,Pokemon,tela):
            item = self.inventario[indice] 
            if item["classe"] in ["pokebola", "fruta"]:
                tocar("Bloq")
                GV.adicionar_mensagem("Pokebolas e frutas são usadas no centro")
            else:
                if item["classe"] in ["poçao"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            cura = item["cura"]
                            tocar("Usou")
                            self.inventario.remove(item)
                            Pokemon.curar(cura,self,tela)
                            return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser curados")
                elif item["classe"] in ["amplificador"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            tipo = item["aumento"]
                            if tipo == "Evolucional":
                                Pokemon.FormaFinal(item,self)
                            else:
                                tocar("Usou")
                                self.inventario.remove(item)
                                Pokemon.amplificar(tipo,0.1,self)
                                return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser amplificados")
                elif item["classe"] in ["caixa","coletor"]:
                    compras = item["compra"]
                    if item["classe"] in ["caixa"]:
                        tocar("Usou")
                        self.inventario.remove(item)
                        for _ in range(compras):
                            item = caixa()
                            if item in pokebolas_disponiveis:
                                self.Captura.append(item)
                            else:
                                self.inventario.append(item)
                        return
                    elif item["classe"] in ["coletor"]:
                        tocar("Usou")
                        self.inventario.remove(item)
                        for _ in range(compras):
                            self.energias[coletor()] += 1
                        return
                elif item["classe"] == "estadio":
                    tocar("Usou")
                    P.Mudar_estadio(item["ST Code"])
                    self.inventario.remove(item)
                    return
                else:
                    tocar("Bloq")
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
    def __init__(self, pokemon, player):
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
        self.FF = pokemon["FF"]
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
        self.efeitosPosi = EfeitosPositivos.copy()
        self.efeitosNega = EfeitosNegativos.copy()
        try:
            player.pokemons.append(self)
            self.pos = player.pokemons.index(self)
        except AttributeError:
            self.pos = None
        
        self.atacou = False
        self.vampirismo = 0
        self.PodeEvoluir = True

    def FormaFinal(self,item,player):
        if self.xp_atu >= self.xp_total:
            pos = self.pos
            if self.FF is not None:
                for i in range(len(self.FF)):
                    if item["nome"] == "Energia Mega":
                        if self.FF[i]["FF"] == "Mega":
                            player.inventario.remove(item)
                            E.adicionar_efeito("Evoluir",(360 + pos * 190,870),ao_terminar=lambda:self.Evoluir_Final(i))

                    elif item["nome"] == "Energia Vstar":
                        if self.FF[i]["FF"] == "Vstar":
                            player.inventario.remove(item)
                            E.adicionar_efeito("Evoluir",(360 + pos * 190,870),ao_terminar=lambda:self.Evoluir_Final(1))

                    elif item["nome"] == "Energia GigantaMax":
                        if self.FF[i]["FF"] == "Vmax":
                            player.inventario.remove(item)
                            E.adicionar_efeito("Evoluir",(360 + pos * 190,870),ao_terminar=lambda:self.Evoluir_Final(0))

            else:
                GV.adicionar_mensagem("Esse pokemon não tem forma final")
                return
            
            GV.adicionar_mensagem("Energia não condiz com a forma final")
            return

        else:
            GV.adicionar_mensagem("Xp insuficiente")
            return
        
    def Evoluir_Final(self,i):
        nome_antigo = self.nome
        self.nome = self.FF[i]["nome"]
        self.VidaMax = round(self.VidaMax * self.FF[i]["vida"])
        self.Vida = round(self.Vida * self.FF[i]["vida"])
        self.Def = round(self.Def * self.FF[i]["def"])
        self.Def_sp = round(self.Def_sp * self.FF[i]["def SP"])
        self.Atk = round(self.Atk * self.FF[i]["atk"])
        self.Atk_sp = round(self.Atk_sp * self.FF[i]["atk SP"])
        self.vel = round(self.velB * self.FF[i]["velocidade"])
        self.custo = self.FF[i]["custo"]
        self.ataque_normal = random.choice(self.FF[i]["ataques normais"])
        self.ataque_especial = random.choice(self.FF[i]["ataques especiais"])
        self.Estagio = self.FF[i]["estagio"]
        self.xp_total = self.FF[i]["XP"]
        self.evolucao = self.FF[i]["evolução"]
        P.VerificaGIF()
        self.PodeEvoluir = True
        GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Insano!")

    def evoluir(self,player):
        if self.xp_atu >= self.xp_total:
            if self.PodeEvoluir is True:
                if isinstance(self.evolucao,list):
                    self.evolucao = random.randint(self.evolucao)
                if self.evolucao is not None:
                    i = self.pos
                    self.PodeEvoluir = False
                    E.adicionar_efeito("Evoluir",(360 + i * 190,870),ao_terminar=lambda:self.Evoluir_de_fato())
                    return
            else:
                tocar("Bloq")
                GV.adicionar_mensagem("Evoluindo...")
        tocar("Bloq")
        GV.adicionar_mensagem("Seu pokemon não pode evoluir")

    def Evoluir_de_fato(self):
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
        if self.evolucao["estagio"] < 4:
            self.ataque_normal = random.choice(self.evolucao["ataques normais"])
            self.ataque_especial = random.choice(self.evolucao["ataques especiais"])
        self.Estagio = self.evolucao["estagio"]
        self.FF = self.evolucao["FF"]
        self.xp_total = self.evolucao["XP"]
        self.evolucao = self.evolucao["evolução"]
        self.PodeEvoluir = True
        P.VerificaGIF()
        P.AddIMGpokemon(self)
        GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Incrivel!")


    def Ganhar_XP(self,quantidade,player):
        self.xp_atu = self.xp_atu + quantidade
    
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
    
    def atacado(self,dano,player,inimigo,tipo,tela):
        DanoOriginal = dano
        if self.Vida <= dano:
            if self.efeitosPosi["Imortal"]:
                dano = self.Vida - 0.1
                self.efeitosPosi["Imortal"] = 0
            else:
                dano = self.Vida
        
        self.Vida = round(self.Vida - dano,1)

        if tipo == "N":
            cor = LARANJA
        elif tipo == "E":
            cor = ROXO
        else:
            cor = PRETO
        
        i = self.pos
        if self in inimigo.pokemons:
            P.adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",cor,Fonte35,((1400 - i * 190),190))
        else:
            P.adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",cor,Fonte35,((425 + i * 190),975))

        if self.Vida == 0:
            GV.adicionar_mensagem(f"{self.nome} foi nocauteado")

    def curar(self,cura,player,tela):
            if self.efeitosPosi["Abençoado"] != 0:
                cura = cura * 1.3
            if self.efeitosNega["Queimado"] != 0:
                cura = cura * 0.7

            dano_tomado = self.VidaMax - self.Vida
            self.Vida = round(self.Vida + cura,1)
            if self.Vida > self.VidaMax:
                self.Vida = self.VidaMax
                cura = dano_tomado 
            
            i = self.pos
            if self in player.pokemons:
                P.adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((425 + i * 190),975))
            else:
                P.adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((1400 - i * 190),190))

    def atacar(self,alvo,player,inimigo,tipo,tela,Mapa):
        

        if tipo == "N":
            F = self.ataque_normal
            U = self.Atk
            V = alvo.Def
            if alvo.efeitosNega["Quebrado"] > 0:
                V = V * 0.5
        else:
            F = self.ataque_especial
            U = self.Atk_sp
            V = alvo.Def_sp
            if alvo.efeitosNega["Fragilizado"] > 0:
                V = V * 0.5

        if alvo.efeitosPosi["Reforçado"] > 0:
            V = V * 1.5
        if self.efeitosNega["Enfraquecido"] > 0:
            U = U * 0.5
        if self.efeitosPosi["Ofensivo"] > 0:
            U = U * 1.5
        
        Custo = F["custo"].copy()
        if self.efeitosNega["Descarregado"] > 0:
            for i in range(len(F["custo"])):
                Custo.append(F["custo"][i]) 
        if self.efeitosPosi["Energizado"] > 0:
            Custo = ["normal"]

        pagou = 0
        gastas = []
        for i in range(len(Custo)):
            if Custo[i] == "normal":
                for cor in player.energiasDesc:
                    if player.energias[cor] >= 1:
                        player.energias[cor] -= 1
                        gastas.append(cor)
                        pagou += 1
                        break
            else:
                if player.energias[Custo[i]] >= 1:
                    player.energias[Custo[i]] -= 1
                    gastas.append(Custo[i])
                    pagou += 1

        if pagou != len(Custo):
            tocar("Bloq")
            GV.adicionar_mensagem("Sem energias, seu ataque falhou")
            for i in range(len(gastas)):
                player.energias[gastas[i]] += 1
            return None

        distancia = FU.distancia_entre_pokemons(self,alvo,Mapa.Metros)
        Over = F["alcance"] - distancia
        if alvo.efeitosPosi["Voando"] > 0:
            Over = Over - 45
        if Over < 0:
            assertividade = F["precisão"] + Over
        else:
            assertividade = F["precisão"]
        if self.efeitosNega["Confuso"] > 0:
            assertividade = assertividade * 0.5
        if self.efeitosPosi["Focado"] > 0:
            assertividade = assertividade * 1.5


        desfoco = random.randint(0,100)
        if desfoco > assertividade:
            GV.adicionar_mensagem("Você errou o ataque")
            return

        self.atacou = True
        Dano_I = U * F["dano"]
        
        if F["função"] != []:
            V, Dano_I = FU.seleciona_função_ataque(F,self,alvo,player,inimigo,Mapa,tela,Dano_I,V)

        Tipo = F["tipo"]
        mitigação = 100 / (100 + V) 
        Dano_E = Dano_I * FU.efetividade(Tipo,alvo.tipo,tela,alvo)
        dano_F = round(Dano_E * mitigação,1)

        if alvo.efeitosNega["Vampirico"] > 0:
            vampirismo = dano_F * 0.3
            self.curar(vampirismo,player,tela)
        if alvo.efeitosPosi["Preparado"] > 0:
            preparo = round((alvo.vel / 3),1)
            dano_F = dano_F - preparo
            self.atacado(preparo,player,inimigo,tipo,tela)
        if alvo.efeitosPosi["Refletir"] > 0:
            reflexão = dano_F * 0.8
            self.atacado(reflexão,player,inimigo,tipo,tela)
            dano_F = dano_F * 0.2
        if self.vampirismo > 0:
            self.curar(dano_F * self.vampirismo,player,tela)
            self.vampirismo = 0

        GV.adicionar_mensagem (f"O seu {self.nome} causou {dano_F} de dano com o ataque")
        GV.adicionar_mensagem(f"{F['nome']} no {alvo.nome} inimigo")
        XP_ATK = random.randint(3,5)
        self.Ganhar_XP(XP_ATK,player)
        alvo.atacado(dano_F,player,inimigo,tipo,tela)

        
Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "rosa", "laranja", "marrom", "cinza", "preta"]

def Gerador(Pokemon,P):
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
        "estagio": 1,
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
        "FF": Pok["FF"],
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

def Gerador_final(code,P,player):
    return Pokemon(Gerador(Pokedex[code],P),player)

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
    if player.ouro >= custo:
        if tipo == "energia":
            player.ouro -= custo
            energia_sorteada = random.choice(Energias)
            player.energias[energia_sorteada] += 1
            energia_sorteada = random.choice(Energias)
            player.energias[energia_sorteada] += 1
        
        else:
            raridades = []
            if tipo == "pokebola":
                if len(player.Captura) < 9:
                    U = pokebolas_disponiveis
                else:
                    tocar("Bloq")
                    GV.adicionar_mensagem("Seu inventário está cheio")
            else:
                if len(player.inventario) < 10:
                    if tipo == "item":
                        U = itens_disponiveis
                    elif tipo == "amplificador":
                        if Turno > 3:
                            U = amplificadores_disponiveis
                    elif tipo == "estadio":
                        if Turno > 5:
                            U = Estadios_disponiveis
                else:
                    tocar("Bloq")
                    GV.adicionar_mensagem("Seu inventário está cheio")
    
            if U is not None:
                for i in range(len(U)):
                    for j in range(6 - U[i]["raridade"]):
                        raridades.append(U[i])
                player.ouro -= custo
                item = random.choice(raridades)
                tocar("Compra")
                GV.adicionar_mensagem(f"Você comprou um item: {item["nome"]}")
                if tipo == "pokebola":
                    player.Captura.append(item)
                else:
                    player.inventario.append(item)
            else:
                tocar("Bloq")
    else:
        tocar("Bloq")
        GV.adicionar_mensagem("Você não tem ouro o suficiente")

def caixa():
        while True:
            raridades = []
            U = itens_disponiveis + pokebolas_disponiveis + amplificadores_disponiveis
            for i in range(len(U)):
                        for j in range(6 - U[i]["raridade"]):
                            raridades.append(U[i])
            item = random.choice(raridades)
            if item["classe"] != "caixa":
                break
        
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
