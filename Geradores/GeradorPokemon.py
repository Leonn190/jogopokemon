import Visual.GeradoresVisuais as GV
import random
import pygame
import time
import json
from Jogo.Funções2 import verificar_serializabilidade
from Dados.Gen1.Basicos import Pokemons_Todos
from Visual.Mensagens import adicionar_mensagem_passageira
from Visual.Sonoridade import tocar
from Visual.Efeitos import adicionar_efeito
from Jogo.Mapa import PosicionarGuardar
from Geradores.GeradorAtaques import SelecionaAtaques
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30,Fonte35, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

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

EfeitosDescrição = {
    "Regeneração": "Cura 15 de vida por turno",
    "Abençoado": "Aumenta 30% da cura",
    "Imune": "Não pode receber efeitos negativos", 
    "Preparado": "bloqueia e contra ataca com valores baseados na velocidade",
    "Provocando": "Sempre é o alvo",
    "Furtivo": "Não pode ser um alvo",
    "Voando": "Ataques contra voce tem -50 assertividade",
    "Ofensivo": "Mais 30% de ataques",
    "Reforçado": "Mais 30% de defesas",
    "Imortal": "Não pode ser nocauteado",
    "Refletir": "Recebe apenas 20% do dano, o resto reflete",
    "Focado": "Sempre mais 50 assertividade",
    "Velocista": "Mais 50% de velocidade",
    "Energizado": "Precisa de só uma energia para atacar",
    "Confuso": "Menos 50 de assertividade sempre",
    "Bloqueado": "Não recebe efeitos positivos",
    "Envenenado": "10 de dano por turno",
    "Tóxico": "20 de dano por turno",
    "Fragilizado": "Menos 50% de Sp defesa ",
    "Quebrado": "Menos 50% de defesa",
    "Congelado": "Não pode ser selecionado",
    "Queimado": "Corta cura de 30% e toma 15 de dano por turno",
    "Paralisado": "Velocidade zerada",
    "Encharcado": "Mais 2 energias para se mover",
    "Vampirico": "Inimigos se curam em 30% do dano causado",
    "Descarregado": "Ataca com o dobro de energias",
    "Enfraquecido": "Menos 30% de ataques",
    "Incapacitado": "Não pode atacar"
}

def calcular_coef(iv):
            return 0.8 + (iv / 100) * 0.4

def remover_funcoes_do_dicionario(d):
    if d is not None:
        return {k: v for k, v in d.items() if not callable(v)}
    else:
        return None

class Pokemon:
    def __init__(self, pokemon, player,dados=False):

        if dados is False:
            self.origem = pokemon["origem"]
            self.nome = pokemon["nome"]
            self.tipo = pokemon["tipo"]
            self.raridade = pokemon["raridade"]
            self.Estagio = pokemon["estagio"]
            self.Altura = pokemon["altura"]
            self.Peso = pokemon["peso"]
            self.dono = player

            self.CoefPeso = pokemon["coefP"]
            self.CoefAltura = pokemon["coefA"]

            self.raio = 0
            self.tamanho = 1.4

            self.barreira = 0
            self.amplificações = 0

            self.Vida = pokemon["vida"]
            self.Atk = 0
            self.Atk_sp = 0
            self.Def = 0
            self.Def_sp = 0
            self.vel = 0 

            self.VidaMaxB = pokemon["vida"]
            self.VidaMax = 1
            self.VarVida = 0

            self.AtkB = pokemon["atk"]
            self.Atk_spB = pokemon["atk SP"]
            self.DefB = pokemon["def"]
            self.Def_spB = pokemon["def SP"] 
            self.velB = pokemon["velocidade"]

            self.VarAtk_temp = 0
            self.VarAtk_sp_temp = 0
            self.VarDef_temp = 0
            self.VarDef_sp_temp = 0
            self.Varvel_temp = 0

            self.VarAtk_perm = 0
            self.VarAtk_sp_perm = 0
            self.VarDef_perm = 0
            self.VarDef_sp_perm = 0
            self.Varvel_perm = 0

            self.custo = pokemon["custo"]
            self.evolucao = pokemon["evolução"]
            self.FF = pokemon["FF"]
            self.xp_atu = pokemon["XP atu"]
            self.xp_total = pokemon["XP"]

            self.IV = pokemon["IV"]
            self.IV_vida = pokemon["IV vida"]
            self.IV_atk = pokemon["IV atk"]
            self.IV_atkSP = pokemon["IV atk SP"]
            self.IV_def = pokemon["IV def"]
            self.IV_defSP = pokemon["IV def SP"]
            self.IV_vel = pokemon["IV vel"]

            self.CoefVida = calcular_coef(self.IV_vida)
            self.CoefAtk = calcular_coef(self.IV_atk)
            self.CoefAtkSP = calcular_coef(self.IV_atkSP)
            self.CoefDef = calcular_coef(self.IV_def)
            self.CoefDefSP = calcular_coef(self.IV_defSP)
            self.CoefVel = calcular_coef(self.IV_vel)

            self.movimento1 = pokemon["Move1"]
            self.movimento2 = pokemon["Move2"]
            self.movimento3 = pokemon["Move3"]
            self.movimento4 = pokemon["Move4"]
            self.moveList = pokemon["MoveList"]
            self.movePossiveis = pokemon["possiveis"]

            self.code = pokemon["code"]
            self.ID = pokemon["ID"] #unico

            self.guardado = 0
            self.local = []
            self.efeitosPosi = EfeitosPositivos.copy()
            self.efeitosNega = EfeitosNegativos.copy()
            self.descrição = EfeitosDescrição
            
            try:
                player.pokemons.append(self)
                self.pos = player.pokemons.index(self)
            except AttributeError:
                self.pos = None
            
            self.atacou = False
            self.moveu = False
            self.PodeMover = True
            self.PodeEvoluir = True
            self.PodeAtacar = True
            self.PodeSerAtacado = True

        else:

            self.origem = dados["origem"]
            self.nome = dados["nome"]
            self.tipo = dados["tipo"]
            self.raridade = dados["raridade"]
            self.Estagio = dados["estagio"]
            self.Altura = dados["altura"]
            self.Peso = dados["peso"]
            self.tamanho = dados["tamanho"]
            self.dono = player
            self.barreira = dados["barreira"]
            self.amplificações = dados["amplificações"]
            self.Vida = dados["vida"]
            self.VidaMaxB = dados["vida_max_base"]
            self.VidaMax = dados["vida_max"]
            self.VarVida = dados["var_vida"]
            self.Atk = dados["atk"]
            self.Atk_sp = dados["atk_sp"]
            self.Def = dados["def"]
            self.Def_sp = dados["def_sp"]
            self.vel = dados["vel"]
            self.AtkB = dados["atkB"]
            self.Atk_spB = dados["atk_spB"]
            self.DefB = dados["defB"]
            self.Def_spB = dados["def_spB"]
            self.velB = dados["velB"]
            self.VarAtk_temp = dados["var_atk_temp"]
            self.VarAtk_sp_temp = dados["var_atk_sp_temp"]
            self.VarDef_temp = dados["var_def_temp"]
            self.VarDef_sp_temp = dados["var_def_sp_temp"]
            self.Varvel_temp = dados["var_vel_temp"]
            self.VarAtk_perm = dados["var_atk_perm"]
            self.VarAtk_sp_perm = dados["var_atk_sp_perm"]
            self.VarDef_perm = dados["var_def_perm"]
            self.VarDef_sp_perm = dados["var_def_sp_perm"]
            self.Varvel_perm = dados["var_vel_perm"]
            self.custo = dados["custo"]
            self.xp_atu = dados["XP atu"]
            self.xp_total = dados["XP"]
            self.IV = dados["IV"]
            self.IV_vida = dados["IV vida"]
            self.IV_atk = dados["IV atk"]
            self.IV_atkSP = dados["IV atk SP"]
            self.IV_def = dados["IV def"]
            self.IV_defSP = dados["IV def SP"]
            self.IV_vel = dados["IV vel"]
            self.CoefVida = dados["CoefVida"]
            self.CoefAtk = dados["CoefAtk"]
            self.CoefAtkSP = dados["CoefAtkSP"]
            self.CoefDef = dados["CoefDef"]
            self.CoefDefSP = dados["CoefDefSP"]
            self.CoefVel = dados["CoefVel"]
            self.CoefPeso = dados["CoefPeso"]
            self.CoefAltura = dados["CoefAltura"]
            self.raio = dados["raio"]
            self.FF = dados["FF"]
            self.evolucao = dados["evolucao"]
            self.atacou = dados["atacou"]
            self.moveu = dados["moveu"]
            self.PodeMover = dados["PodeMover"]
            self.PodeEvoluir = dados["PodeEvoluir"]
            self.PodeAtacar = dados["PodeAtacar"]
            self.movimento1 = SelecionaAtaques(dados["Move1"])
            self.movimento2 = SelecionaAtaques(dados["Move2"])
            if dados["Move3"] is not None:
                self.movimento3 = SelecionaAtaques(dados["Move3"])
            else:
                self.movimento3 = None
            if dados["Move4"] is not None:
                self.movimento4 = SelecionaAtaques(dados["Move4"])
            else:
                self.movimento4 = None
            self.moveList = dados["MoveList"]
            self.movePossiveis = dados["possiveis"]
            self.code = dados["code"]
            self.ID = dados["ID"]
            self.guardado = dados["guardado"]
            self.local = dados["local"]
            if self.local is not None:
                local = [1080 - 1 - local[0], local[1]]
                self.local = local
            self.efeitosPosi = dados["efeitosPositivos"]
            self.efeitosNega = dados["efeitosNegativos"]
            self.PodeSerAtacado = dados["PodeSerAtacado"]
            self.pos = dados["pos"]
            self.descrição = EfeitosDescrição

    def FormaFinal(self,item,player):
        if self.xp_atu >= self.xp_total:
            pos = self.pos
            if self.FF is not None:
                for i in range(len(self.FF)):
                    if item["nome"] == "Energia Mega":
                        if self.FF[i]["FF"] == "Mega":
                            player.inventario.remove(item)
                            adicionar_efeito("Evoluindo",(520 + pos * 190, 980),ao_terminar=lambda:self.Evoluir_Final(i,player))

                    elif item["nome"] == "Energia Vstar":
                        if self.FF[i]["FF"] == "Vstar":
                            player.inventario.remove(item)
                            adicionar_efeito("Evoluindo",(520 + pos * 190, 980),ao_terminar=lambda:self.Evoluir_Final(1,player))

                    elif item["nome"] == "Energia GigantaMax":
                        if self.FF[i]["FF"] == "Vmax":
                            player.inventario.remove(item)
                            adicionar_efeito("Evoluindo",(520 + pos * 190, 980),ao_terminar=lambda:self.Evoluir_Final(0,player))
            else:
                GV.adicionar_mensagem("Esse pokemon não tem forma final")
                return
            
            GV.adicionar_mensagem("Energia não condiz com a forma final")
            return

        else:
            GV.adicionar_mensagem("Xp insuficiente")
            return
        
    def Evoluir_Final(self,i,player):
        from Jogo.Partida.Partida import VerificaGIF
        nome_antigo = self.nome
        self.nome = self.FF[i]["nome"]
        self.VidaMaxB = round(self.CoefVida * self.FF[i]["vida"])
        self.Vida = round(self.CoefVida * self.FF[i]["vida"] - (self.Vida - self.VidaMax))
        self.DefB = round(self.CoefDef * self.FF[i]["def"])
        self.Def_spB = round(self.CoefDefSP * self.FF[i]["def SP"])
        self.AtkB = round(self.CoefAtk * self.FF[i]["atk"])
        self.Atk_spB = round(self.CoefAtkSP * self.FF[i]["atk SP"])
        self.velB = round(self.CoefVel * self.FF[i]["velocidade"])
        self.custo = self.FF[i]["custo"]
        self.Estagio = self.FF[i]["estagio"]
        self.xp_total = self.FF[i]["XP"]
        self.evolucao = self.FF[i]["evolução"]
        VerificaGIF(player)
        GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Insano!")

    def evoluir(self,player):
        if self.xp_atu >= self.xp_total:
            if self.PodeEvoluir is True:
                if isinstance(self.evolucao,list):
                    self.evolucao = random.choice(self.evolucao)
                if self.evolucao is not None:
                    i = self.pos
                    self.PodeEvoluir = False
                    adicionar_efeito("Evoluindo", (520 + i * 190, 980), ao_terminar=lambda: self.Evoluir_de_fato(player))
                    return
            else:
                tocar("Bloq")
                GV.adicionar_mensagem("Evoluindo...")
                return
        tocar("Bloq")
        GV.adicionar_mensagem("Seu pokemon não pode evoluir")

    def Evoluir_de_fato(self,player):
        from Jogo.Partida.Partida import VerificaGIF
        nome_antigo = self.nome

        if self.evolucao["moves"] >= 3 and self.movimento3 is None:
            while True:
                sorteado = random.choice(self.evolucao["movelist"])
                ataque = SelecionaAtaques(sorteado)
                if sorteado not in self.moveList:
                    self.moveList.append(sorteado)
                    self.movimento3 = ataque
                    break
        if self.evolucao["moves"] == 4 and self.movimento4 is None:
            while True:
                sorteado = random.choice(self.evolucao["movelist"])
                ataque = SelecionaAtaques(sorteado)
                if sorteado not in self.moveList:
                    self.moveList.append(sorteado)
                    self.movimento4 = ataque
                    break
        
        self.movePossiveis = self.evolucao["movelist"]
        self.nome = self.evolucao["nome"]
        self.VidaMaxB = round(self.CoefVida * self.evolucao["vida"])
        self.Vida = round(self.CoefVida * self.evolucao["vida"] - (self.Vida - self.VidaMax))
        self.DefB = round(self.CoefDef * self.evolucao["def"])
        self.Def_spB = round(self.CoefDefSP * self.evolucao["def SP"])
        self.AtkB = round(self.CoefAtk * self.evolucao["atk"])
        self.Atk_spB = round(self.CoefAtkSP * self.evolucao["atk SP"])
        self.velB = round(self.CoefVel * self.evolucao["velocidade"])
        self.custo = self.evolucao["custo"]
        self.Estagio = self.evolucao["estagio"]
        self.FF = self.evolucao["FF"]
        self.xp_total = self.evolucao["XP"]
        self.evolucao = self.evolucao["evolução"]
        VerificaGIF(player)
        GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Incrivel!")


    def Ganhar_XP(self,quantidade,player):
        self.xp_atu = self.xp_atu + quantidade
    
    def amplificar(self,tipo,tela,player):
        if tipo == "atk":
            J = round(self.Atk)
            self.VarAtk_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou seu ataque, foi de {J} para {J + 2}")
        elif tipo == "atk SP":
            J = round(self.Atk_sp)
            self.VarAtk_sp_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou seu ataque especial, foi de {J} para {J + 2}")
        elif tipo == "def":
            J = round(self.Def)
            self.VarDef_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou sua defesa, foi de {J} para {J + 2}")
        elif tipo == "def SP":
            J = round(self.Def_sp)
            self.VarDef_sp_perm += 2
            GV.adicionar_mensagem(f"{self.nome} amplificou sua defesa especial, foi de {J} para {J + 2}")
        elif tipo == "vel":
            J = round(self.vel)
            self.Varvel_perm += 3
            GV.adicionar_mensagem(f"{self.nome} amplificou sua velocidade, foi de {J} para {J + 3}")
        elif tipo == "Vida":
            J = round(self.VidaMax)
            self.VarVida += 6
            self.Vida += 6
            GV.adicionar_mensagem(f"{self.nome} amplificou sua vida máxima, foi de {J} para {J + 6}")
        
        self.amplificações += 1
        
    
    def atacado(self,dano,player,inimigo,tela,Mapa):
        DanoOriginal = dano

        if self.barreira > 0:
            if self.barreira <= dano:
                dano = self.barreira
            self.barreira = self.barreira - dano
            self.barreira = round(self.barreira,1)

        else:
            if self.Vida <= dano:
                if self.efeitosPosi["Imortal"]:
                    dano = self.Vida - 0.1
                    self.efeitosPosi["Imortal"] = 0
                else:
                    dano = self.Vida
            
            self.Vida = self.Vida - dano
            self.Vida = round(self.Vida,1)
        
        i = self.pos
        if self in inimigo.pokemons:
            adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",VERMELHO,Fonte35,((1410 - i * 190),180))
        else:
            adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",VERMELHO,Fonte35,((425 + i * 190),975))

        if self.Vida == 0:
            PosicionarGuardar(self,0)
            
            GV.adicionar_mensagem(f"{self.nome} foi nocauteado")
            player.NocautesSofridos += 1
            player.PokemonsNocauteados += 1
            inimigo.NocautesRealizados += 1

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
                adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((510 + i * 190),1010))
            else:
                adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((1410 - i * 190),180))
    
    def atualizar_rect(self):
        if len(self.local) == 2:
            x = self.local[0]
            y = self.local[1]
            self.rect = pygame.Rect(x - self.raio, y - self.raio, self.raio * 2, self.raio * 2)
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)  # rect nulo ou invisível

    def ToDic(self):
        data = {
            "origem": self.origem,
            "nome": self.nome,
            "tipo": self.tipo,
            "raridade": self.raridade,
            "estagio": self.Estagio,
            "altura": self.Altura,
            "peso": self.Peso,
            "tamanho": self.tamanho,
            "barreira": self.barreira,
            "amplificações": self.amplificações,
            "vida": self.Vida,
            "vida_max_base": self.VidaMaxB,
            "vida_max": self.VidaMax,
            "var_vida": self.VarVida,
            "atk": self.Atk,
            "atk_sp": self.Atk_sp,
            "def": self.Def,
            "def_sp": self.Def_sp,
            "vel": self.vel,
            "atkB": self.AtkB,
            "atk_spB": self.Atk_spB,
            "defB": self.DefB,
            "def_spB": self.Def_spB,
            "velB": self.velB,
            "var_atk_temp": self.VarAtk_temp,
            "var_atk_sp_temp": self.VarAtk_sp_temp,
            "var_def_temp": self.VarDef_temp,
            "var_def_sp_temp": self.VarDef_sp_temp,
            "var_vel_temp": self.Varvel_temp,
            "var_atk_perm": self.VarAtk_perm,
            "var_atk_sp_perm": self.VarAtk_sp_perm,
            "var_def_perm": self.VarDef_perm,
            "var_def_sp_perm": self.VarDef_sp_perm,
            "var_vel_perm": self.Varvel_perm,
            "custo": self.custo,
            "XP atu": self.xp_atu,
            "XP": self.xp_total,
            "IV": self.IV,
            "IV vida": self.IV_vida,
            "IV atk": self.IV_atk,
            "IV atk SP": self.IV_atkSP,
            "IV def": self.IV_def,
            "IV def SP": self.IV_defSP,
            "IV vel": self.IV_vel,
            "CoefVida": self.CoefVida,
            "CoefAtk": self.CoefAtk,
            "CoefAtkSP": self.CoefAtkSP,
            "CoefDef": self.CoefDef,
            "CoefDefSP": self.CoefDefSP,
            "CoefVel": self.CoefVel,
            "CoefPeso": self.CoefPeso,
            "CoefAltura": self.CoefAltura,
            "Move1": self.movimento1["nome"],
            "Move2": self.movimento2["nome"],
            "Move3": self.movimento3["nome"] if self.movimento3 else None,
            "Move4": self.movimento4["nome"] if self.movimento4 else None,
            "MoveList": self.moveList,
            "possiveis": self.movePossiveis,
            "guardado": self.guardado,
            "local": self.local,
            "code": self.code,
            "ID": self.ID,
            "efeitosPositivos": self.efeitosPosi,
            "efeitosNegativos": self.efeitosNega,
            "PodeSerAtacado": self.PodeSerAtacado,
            "raio": self.raio,
            "FF": self.FF,
            "evolucao": self.evolucao,
            "atacou": self.atacou,
            "moveu": self.moveu,
            "PodeMover": self.PodeMover,
            "PodeEvoluir": self.PodeEvoluir,
            "PodeAtacar": self.PodeAtacar,
            "pos": self.pos
        }

        verificar_serializabilidade(data)
        return data

IDpoke = 0

def Gerador(Pokemon,P):
    global IDpoke
    IDpoke += 1
    Pok = Pokemon

    vida_min = int(Pok["vida"] * 0.85)
    vida_max = int(Pok["vida"] * 1.15)
    vida_max_real = int(vida_max * P)
    vida = random.randint(vida_min, vida_max_real)
    vida = min(vida, int(Pok["vida"] * 1.15))

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

    Coef_Genetico = random.uniform(0.75,1.1)

    Altura = Pok["H"] * (Coef_Genetico + (IVV/800) + (IVA/900) + (IVAS/900))
    Peso = Pok["W"] * (Coef_Genetico + (IVV/700) + (IVD/700) + (IVDS/700) - (IVVE/400))

    CoefPeso = (Coef_Genetico + (IVV/800) + (IVA/900) + (IVAS/900))
    CoefAltura = (Coef_Genetico + (IVV/700) + (IVD/700) + (IVDS/700) - (IVVE/400))

    if Altura > 9.9:
        Altura = round(Altura,1)
    else:
        Altura = round(Altura,2)

    if Peso > 99.5:
        Peso = round(Peso,0)
    else:
        Peso = round(Peso,1)

    Stats = {
        "nome": Pok["nome"],
        "tipo": Pok["tipo"],
        "raridade": Pok["raridade"],
        "origem": Pok,
        "vida": vida,
        "estagio": 1,
        "altura": Altura,
        "peso": Peso,
        "coefP": CoefPeso,
        "coefA": CoefAltura,
        "atk": Atk,
        "atk SP": Atk_SP,
        "def": Def,
        "def SP": Def_SP,
        "velocidade": vel,
        "XP": Pok["XP"],
        "custo": Pok["custo"],
        "evolução": Pok["evolução"],
        "FF": Pok["FF"],
        "XP atu": 0,
        "IV": round(IV,1),
        "IV vida": round(IVV),
        "IV atk": round(IVA),
        "IV atk SP": round(IVAS),
        "IV def": round(IVD),
        "IV def SP": round(IVDS),
        "IV vel": round(IVVE),
        "code": Pok["code"],
        "ID": IDpoke,
        "MoveList": [],
        "possiveis": Pok["movelist"],
        "Move1": None,
        "Move2": None,
        "Move3": None,
        "Move4": None
    }

    for i in range(Pok["moves"]):
        while True:
            sorteado = random.choice(Pok["movelist"])
            ataque = SelecionaAtaques(sorteado)
            if sorteado not in Stats["MoveList"]:
                Stats["MoveList"].append(sorteado)
                Stats[f"Move{i+1}"] = ataque
                break

    return Stats

def Gerador_final(code,P,player):
    return Pokemon(Gerador(Pokemons_Todos[code],P),player)

def Gerador_Clone(Dados,player):
    return Pokemon(None,player,Dados)

Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "laranja", "preta"]

def VerificaSituaçãoPokemon(player, inimigo, Mapa):
    for pokemon in player.pokemons:
        if pokemon.atacou == True or pokemon.efeitosNega["Incapacitado"] > 0 or pokemon.efeitosNega["Congelado"] > 0 or pokemon.local is None:
            pokemon.PodeAtacar = False
        else:
            pokemon.PodeAtacar = True

        if pokemon.moveu == True or pokemon.efeitosNega["Congelado"] > 0 or pokemon.efeitosNega["Paralisado"] > 0:
            pokemon.PodeMover = False
        else:
            pokemon.PodeMover = True
        
        if pokemon.PodeEvoluir is True:
            if pokemon.local is None:
                pokemon.PodeEvoluir = False


    for pokemon in player.pokemons + inimigo.pokemons:

        pokemon.raio = pokemon.tamanho * Mapa.Metros // 2

        # --- Resetar apenas os modificadores TEMPORÁRIOS ---
        pokemon.VarAtk_temp = 0
        pokemon.VarAtk_sp_temp = 0
        pokemon.VarDef_temp = 0
        pokemon.VarDef_sp_temp = 0
        pokemon.Varvel_temp = 0

        # --- Aplicar efeitos negativos/positivos TEMPORÁRIOS ---
        if pokemon.efeitosNega["Quebrado"] > 0:
            pokemon.VarDef_temp += -pokemon.DefB * 0.5
        if pokemon.efeitosNega["Fragilizado"] > 0:
            pokemon.VarDef_sp_temp += -pokemon.Def_spB * 0.5
        if pokemon.efeitosPosi["Reforçado"] > 0:
            pokemon.VarDef_temp += pokemon.DefB * 0.3
            pokemon.VarDef_sp_temp += pokemon.Def_spB * 0.3
        if pokemon.efeitosNega["Enfraquecido"] > 0:
            pokemon.VarAtk_temp += -pokemon.AtkB * 0.3
            pokemon.VarAtk_sp_temp += -pokemon.Atk_spB * 0.3
        if pokemon.efeitosPosi["Ofensivo"] > 0:
            pokemon.VarAtk_temp += pokemon.AtkB * 0.3
            pokemon.VarAtk_sp_temp += pokemon.Atk_spB * 0.3
        if pokemon.efeitosPosi["Velocista"] > 0:
            pokemon.Varvel_temp += pokemon.velB * 1.5
        if pokemon.efeitosNega["Paralisado"] > 0:
            pokemon.Varvel_temp += -pokemon.velB
        if pokemon.efeitosNega["Congelado"] > 0:
            pokemon.Varvel_temp += -pokemon.velB

        # --- Atualizar status finais (Base + Permanente + Temporário) ---
        pokemon.VidaMax = pokemon.VidaMaxB + pokemon.VarVida
        pokemon.Atk = round(pokemon.AtkB + pokemon.VarAtk_perm + pokemon.VarAtk_temp)
        pokemon.Atk_sp = round(pokemon.Atk_spB + pokemon.VarAtk_sp_perm + pokemon.VarAtk_sp_temp)
        pokemon.Def = round(pokemon.DefB + pokemon.VarDef_perm + pokemon.VarDef_temp)
        pokemon.Def_sp = round(pokemon.Def_spB + pokemon.VarDef_sp_perm + pokemon.VarDef_sp_temp)
        pokemon.vel = round(pokemon.velB + pokemon.Varvel_perm + pokemon.Varvel_temp)


        if sum(player.energias[energia] for energia in Energias) > 0:
            if player.energiasDesc == []:
                while True:
                    energiaSort = random.choice(Energias)
                    if energiaSort not in player.energiasDesc and player.energias[energiaSort] != 0:
                        player.energiasDesc.append(energiaSort)
                        break

            while True:
                SomaDesc = sum(player.energias[energia] for energia in player.energiasDesc)

                if SomaDesc >= 1:
                    break

                energiaSort = random.choice(Energias)
                if energiaSort not in player.energiasDesc and player.energias[energiaSort] != 0:
                    player.energiasDesc.append(energiaSort)

