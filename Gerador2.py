import random
import pygame
import Partida
import GeradoresVisuais as GV
from Basicos import Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo
from itens import pokebolas_disponiveis,itens_disponiveis,amplificadores_disponiveis
import Funções2
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30,Fonte35, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)


pygame.mixer.init()
clique = pygame.mixer.Sound("Musicas/Som1.wav")
Compra = pygame.mixer.Sound("Musicas/Compra.wav")
Usou = pygame.mixer.Sound("Musicas/Usou.wav")
Bom = pygame.mixer.Sound("Musicas/Bom.wav")
Bloq = pygame.mixer.Sound("Musicas/Bloq.wav")

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
                GV.tocar(Bloq)
                GV.adicionar_mensagem("Pokebolas devem ser usadas apenas para capturar pokemons")
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
                            Pokemon.amplificar(tipo,0.15,Pokemon)
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
                else:
                    GV.tocar(Bloq)
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
        self.IV_vida = pokemon["IV vida"]
        self.IV_atk = pokemon["IV atk"]
        self.IV_atkSP = pokemon["IV atk SP"]
        self.IV_def = pokemon["IV def"]
        self.IV_defSP = pokemon["IV def SP"]
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
        if self.xp_atu >= self.xp_total:
            nome_antigo = self.nome
            self.evoluir()
            GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Incrivel!")
        else:
            GV.adicionar_mensagem(f"{self.nome} ganhou {quantidade} de XP, seu XP atual é {self.xp_atu}")
    
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

    def atacar(self,alvo,player,inimigo,tipo,tela):
        
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
            GV.tocar(Bloq)
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
        alvo.atacado(dano_F,inimigo,tipo,tela)
        
Pokedex = [0,Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo]
pokemons_possiveis = [Bulbasaur,Charmander,Squirtle,Machop,Gastly,Geodude,Caterpie,Abra,Dratini,Pikachu,Zorua,Magikarp,Jigglypuff,Magnemite,Snorlax,Aerodactyl,Jynx,Mewtwo]
Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "rosa", "laranja", "marrom", "cinza", "preta"]

def Gerador(Pokemon):
    Pok = Pokemon

    vida_min = int(Pok["vida"] * 0.8)
    vida_max = int(Pok["vida"] * 1.2)
    vida = random.randint(vida_min, vida_max)

    atk_min = int(Pok["atk"] * 0.8)
    atk_max = int(Pok["atk"] * 1.2)
    Atk = random.randint(atk_min, atk_max)

    atkSP_min = int(Pok["atk SP"] * 0.8)
    atkSP_max = int(Pok["atk SP"] * 1.2)
    Atk_SP = random.randint(atkSP_min, atkSP_max)

    def_min = int(Pok["def"] * 0.8)
    def_max = int(Pok["def"] * 1.2)
    Def = random.randint(def_min, def_max)

    defSP_min = int(Pok["def SP"] * 0.8)
    defSP_max = int(Pok["def SP"] * 1.2)
    Def_SP = random.randint(defSP_min, defSP_max)

    IVV = ((vida - vida_min) / (vida_max - vida_min)) * 100
    IVA = ((Atk - atk_min) / (atk_max - atk_min)) * 100
    IVAS = ((Atk_SP - atkSP_min) / (atkSP_max - atkSP_min)) * 100
    IVD = ((Def - def_min) / (def_max - def_min)) * 100
    IVDS = ((Def_SP - defSP_min) / (defSP_max - defSP_min)) * 100

    IV = round((IVV + IVA + IVAS + IVD + IVDS) / 5, 2)

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
        "IV vida": f"{round(IVV, 1)}%",
        "IV atk": f"{round(IVA, 1)}%",
        "IV atk SP": f"{round(IVAS, 1)}%",
        "IV def": f"{round(IVD, 1)}%",
        "IV def SP": f"{round(IVDS, 1)}%",
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
            GV.tocar(Compra)
            GV.adicionar_mensagem(f"Você comprou um item: {item["nome"]}")
            player.inventario.append(item)
    else:
        GV.tocar(Bloq)
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