import Visual.GeradoresVisuais as GV
import random
import Jogo.Funções2 as FU
from Dados.Gen1.Basicos import Pokemons_Todos
from Visual.Mensagens import adicionar_mensagem_passageira
from Visual.Imagens import Carrega_Icone_pokemon
from Visual.Sonoridade import tocar
from Visual.Efeitos import adicionar_efeito
from Jogo.Tabuleiro import GuardarPosicionar
from Jogo.Partida import VerificaGIF
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

class Pokemon:
    def __init__(self, pokemon, player):

        self.nome = pokemon["nome"]
        self.tipo = pokemon["tipo"]
        self.raridade = pokemon["raridade"]
        self.dificuldade = pokemon["dificuldade"]
        self.Estagio = pokemon["estagio"]

        self.Vida = pokemon["vida"]
        self.Atk = 0
        self.Atk_sp = 0
        self.Def = 0
        self.Def_sp = 0
        self.vel = 0 

        self.VidaMax = pokemon["vida"]
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

        self.movimento1 = pokemon["Move1"]
        self.movimento2 = pokemon["Move2"]
        self.movimento3 = pokemon["Move3"]
        self.movimento4 = pokemon["Move4"]

        self.code = pokemon["code"]
        self.ID = pokemon["ID"] #unico

        self.guardado = 0
        self.local = None
        self.icone = Carrega_Icone_pokemon(self.nome)
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
        self.PodeAtacar = True
        self.PodeSerAtacado = True

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
        nome_antigo = self.nome
        self.nome = self.FF[i]["nome"]
        self.VidaMax = round(self.VidaMax * self.FF[i]["vida"])
        self.Vida = round(self.Vida * self.FF[i]["vida"])
        self.DefB = round(self.DefB * self.FF[i]["def"])
        self.Def_spB = round(self.Def_spB * self.FF[i]["def SP"])
        self.AtkB = round(self.AtkB * self.FF[i]["atk"])
        self.Atk_spB = round(self.Atk_spB * self.FF[i]["atk SP"])
        self.velB = round(self.velB * self.FF[i]["velocidade"])
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
                    self.evolucao = random.randint(self.evolucao)
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
        nome_antigo = self.nome
        self.nome = self.evolucao["nome"]
        self.VidaMax = round(self.VidaMax * self.evolucao["vida"])
        self.Vida = round(self.Vida * self.evolucao["vida"])
        self.DefB = round(self.DefB * self.evolucao["def"])
        self.Def_spB = round(self.Def_spB * self.evolucao["def SP"])
        self.AtkB = round(self.AtkB * self.evolucao["atk"])
        self.Atk_spB = round(self.Atk_spB * self.evolucao["atk SP"])
        self.velB = round(self.velB * self.evolucao["velocidade"])
        self.custo = self.evolucao["custo"]
        self.Estagio = self.evolucao["estagio"]
        self.FF = self.evolucao["FF"]
        self.xp_total = self.evolucao["XP"]
        self.evolucao = self.evolucao["evolução"]
        self.icone = Carrega_Icone_pokemon(self.nome)
        VerificaGIF(player)
        GV.adicionar_mensagem(f"{nome_antigo} Evoluiu para um {self.nome}. Incrivel!")


    def Ganhar_XP(self,quantidade,player):
        self.xp_atu = self.xp_atu + quantidade
    
    def amplificar(self,tipo,amplificador,player):
        if tipo == "XP atu":
            self.Ganhar_XP(5,player)
        elif tipo == "atk":
            J = round(self.Atk)
            self.VarAtk_perm = round(self.VarAtk_perm + (self.AtkB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou seu ATK, foi de {J} para {self.Atk}")
        elif tipo == "atk SP":
            J = round(self.Atk_sp)
            self.VarAtk_sp_perm = round(self.VarAtk_sp_perm + (self.Atk_spB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou seu sp ATK, foi de {J} para {self.Atk_sp}")
        elif tipo == "def":
            J = round(self.Def)
            self.VarDef_perm = self.VarDef_perm + round((self.DefB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou sua DEF, foi de {J} para {self.Def}")
        elif tipo == "def SP":
            J = round(self.Def_sp)
            self.VarDef_sp_perm = self.VarDef_sp_perm + round((self.Def_spB * amplificador))
            GV.adicionar_mensagem(f"{self.nome} amplificou sua sp DEF, foi de {J} para {self.Def_sp}")
    
    def atacado(self,dano,player,inimigo,tela,Mapa):
        DanoOriginal = dano
        if self.Vida <= dano:
            if self.efeitosPosi["Imortal"]:
                dano = self.Vida - 0.1
                self.efeitosPosi["Imortal"] = 0
            else:
                dano = self.Vida
        
        self.Vida = round(self.Vida - dano,1)
        
        i = self.pos
        if self in inimigo.pokemons:
            adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",VERMELHO,Fonte35,((1410 - i * 190),180))
        else:
            adicionar_mensagem_passageira(tela,f"-{DanoOriginal}",VERMELHO,Fonte35,((425 + i * 190),975))

        if self.Vida == 0:
            GuardarPosicionar(self,player,0,Mapa.Zona)
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
                adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((510 + i * 190),1010))
            else:
                adicionar_mensagem_passageira(tela,f"+{round(cura,1)}",VERDE_CLARO,Fonte35,((1410 - i * 190),180))

IDpoke = 0

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
        "Move1": SelecionaAtaques("Sopro do Dragao","Gota Pesada"),
        "Move2": SelecionaAtaques("Chamar para Briga","Cristalizar"),
        "Move3": SelecionaAtaques("Energizar","Nas Sombras"),
        "Move4": SelecionaAtaques("Queimar","Choque do Trovao","Vasculhar"),
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
        "ID": IDpoke
    }

def Gerador_final(code,P,player):
    return Pokemon(Gerador(Pokemons_Todos[code],P),player)

def VerificaSituaçãoPokemon(player, inimigo):
    for pokemon in player.pokemons:
        if pokemon.atacou == True or pokemon.efeitosNega["Incapacitado"] > 0 or pokemon.efeitosNega["Congelado"] > 0 or pokemon.local is None:
            pokemon.PodeAtacar = False
        else:
            pokemon.PodeAtacar = True
        if pokemon.PodeEvoluir is True:
            if pokemon.local is None:
                pokemon.PodeEvoluir = False

    for pokemon in player.pokemons + inimigo.pokemons:
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
        if pokemon.efeitosNega["Paralisado"] > 0:
            pokemon.Varvel_temp += -pokemon.velB
        if pokemon.efeitosNega["Congelado"] > 0:
            pokemon.Varvel_temp += -pokemon.velB

        # --- Atualizar status finais (Base + Permanente + Temporário) ---
        pokemon.Atk = pokemon.AtkB + pokemon.VarAtk_perm + pokemon.VarAtk_temp
        pokemon.Atk_sp = pokemon.Atk_spB + pokemon.VarAtk_sp_perm + pokemon.VarAtk_sp_temp
        pokemon.Def = pokemon.DefB + pokemon.VarDef_perm + pokemon.VarDef_temp
        pokemon.Def_sp = pokemon.Def_spB + pokemon.VarDef_sp_perm + pokemon.VarDef_sp_temp
        pokemon.vel = pokemon.velB + pokemon.Varvel_perm + pokemon.Varvel_temp
