import Partida as P
import random
import FunçõesDeAtaques as FA
import math
import pygame

Energias = ["vermelha", "azul", "amarela", "verde", "roxo", "rosa", "laranja", "marrom", "preta", "cinza"]

def efetividade(Tipo_do_ataque,Tipo_do_atacado,tela,atacado):
    
    tabela_tipos = {
    "normal":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "venenoso": 0, "terrestre": 0,
                  "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": -0.75, "dragao": 0, "sombrio": 0, "metal": 0, "fada": 0},

    "fogo":      {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": 0, "planta": 0.5, "gelo": 0.5, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "metal": 0.5, "fada": 0},

    "agua":      {"normal": 0, "fogo": 0.5, "agua": -0.25, "eletrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": 0.5, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0.5, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "metal": 0, "fada": 0},

    "eletrico":  {"normal": 0, "fogo": 0, "agua": 0.5, "eletrico": -0.25, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": -0.75, "voador": 0.5, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": -0.25, "sombrio": 0,
                  "metal": 0, "fada": 0},

    "planta":    {"normal": 0, "fogo": -0.25, "agua": 0.5, "eletrico": 0, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": -0.25,
                  "terrestre": 0.5, "voador": -0.25, "psiquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragao": -0.25,
                  "sombrio": 0, "metal": -0.25, "fada": 0},

    "gelo":      {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": 0, "planta": 0.5, "gelo": -0.25, "lutador": 0, "venenoso": 0,
                  "terrestre": 0.5, "voador": 0.5, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5, "sombrio": 0,
                  "metal": -0.25, "fada": 0},

    "lutador":   {"normal": 0.5, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0.5, "lutador": 0, "venenoso": -0.25,
                  "terrestre": 0, "voador": -0.25, "psiquico": -0.25, "inseto": -0.25, "pedra": 0.5, "fantasma": -0.75, "dragao": 0,
                  "sombrio": 0.5, "metal": 0.5, "fada": -0.25},

    "venenoso":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0.5, "gelo": 0, "lutador": 0, "venenoso": -0.25,
                  "terrestre": -0.25, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": -0.25, "fantasma": -0.25, "dragao": 0,
                  "sombrio": 0, "metal": -0.75, "fada": 0.5},

    "terrestre":     {"normal": 0, "fogo": 0.5, "agua": 0, "eletrico": 0.5, "planta": -0.25, "gelo": 0, "lutador": 0, "venenoso": 0.5,
                  "terrestre": 0, "voador": -0.75, "psiquico": 0, "inseto": -0.25, "pedra": 0.5, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": 0.5, "fada": 0},

    "voador":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": -0.25, "planta": 0.5, "gelo": 0, "lutador": 0.5, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0.5, "pedra": -0.25, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": -0.25, "fada": 0},

    "psiquico":  {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "venenoso": 0.5,
                  "terrestre": 0, "voador": 0, "psiquico": -0.25, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": -0.75, "metal": -0.25, "fada": 0},

    "inseto":    {"normal": 0, "fogo": -0.25, "agua": 0, "eletrico": 0, "planta": 0.5, "gelo": 0, "lutador": -0.25, "venenoso": -0.25,
                  "terrestre": 0, "voador": -0.25, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": -0.25, "dragao": 0,
                  "sombrio": 0.5, "metal": -0.25, "fada": -0.25},

    "pedra":     {"normal": 0, "fogo": 0.5, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0.5, "lutador": -0.25, "venenoso": 0,
                  "terrestre": -0.25, "voador": 0.5, "psiquico": 0, "inseto": 0.5, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": -0.25, "fada": 0},

    "fantasma":  {"normal": -0.75, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragao": 0,
                  "sombrio": -0.25, "metal": 0, "fada": 0},

    "dragao":    {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5,
                  "sombrio": 0, "metal": -0.25, "fada": -0.75},

    "sombrio":   {"normal": 0, "fogo": 0, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": -0.25, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0.5, "inseto": 0, "pedra": 0, "fantasma": 0.5, "dragao": 0,
                  "sombrio": -0.25, "metal": 0, "fada": -0.25},

    "metal":       {"normal": 0, "fogo": -0.25, "agua": -0.25, "eletrico": -0.25, "planta": 0, "gelo": 0.5, "lutador": 0, "venenoso": 0,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0,
                  "sombrio": 0, "metal": -0.25, "fada": 0.5},

    "fada":      {"normal": 0, "fogo": -0.25, "agua": 0, "eletrico": 0, "planta": 0, "gelo": 0, "lutador": 0.5, "venenoso": -0.25,
                  "terrestre": 0, "voador": 0, "psiquico": 0, "inseto": 0, "pedra": 0, "fantasma": 0, "dragao": 0.5,
                  "sombrio": 0.5, "metal": -0.25, "fada": 0},
    }
    
    multiplicador = 1
    for i in range(len(Tipo_do_ataque)):
        for j in range(len(Tipo_do_atacado)):
            multiplicador = multiplicador + tabela_tipos[Tipo_do_ataque[i]][Tipo_do_atacado[j]]
    if multiplicador < 0:
        multiplicador = 0
    
    
    if multiplicador > 1.5:
        texto = "Super Efetivo"
    elif multiplicador > 1:
        texto = "Efetivo"
    elif multiplicador == 1:
        return multiplicador
    elif multiplicador > 0.5:
        texto = "Pouco Efetivo"
    elif multiplicador > 0:
        texto = "Não Efetivo"
    else:
        texto = "Não Afeta"
    Fonte = pygame.font.SysFont(None, 30)
    P.adicionar_mensagem_passageira(tela,f"{texto}",(0,0,0),Fonte,((1365 - atacado.pos * 190),220))

    return multiplicador

def distancia_entre_pokemons(poke1, poke2, tamanho_casa):

    if poke1.local is None or poke2.local is None:
        return None

    linha1, coluna1 = map(int, poke1.local["id"])
    linha2, coluna2 = map(int, poke2.local["id"])

    dx = (linha1 - linha2) * tamanho_casa
    dy = (coluna1 - coluna2) * tamanho_casa

    return math.hypot(dx, dy)

def seleciona_função_ataque(ataque,pokemon,alvo,player,inimigo,mapa,tela,dano,defesa,tipo):

    funçao = ataque["função"]
    valores = ataque["valores"]

    for i,valor in enumerate(funçao):


        if valor == "AutoCura":
            if isinstance(valores[i],list):
                if valores[i][1] == "Atk":
                    pokemon.curar(pokemon,valores[i][0] * pokemon.Atk,player,tela)
                elif valores[i][1] == "Atk sp":
                    pokemon.curar(pokemon,valores[i][0] * pokemon.Atk_sp,player,tela)
                elif valores[i][1] == "Vida":
                    pokemon.curar(pokemon,valores[i][0] * pokemon.Vida,player,tela)
            else:
                pokemon.curar(pokemon,valores[i],player,tela)


        elif valor == "CuraAliadoAleatorio":
            opçoes = []
            for pokemon in player.pokemons:
                if pokemon.Vida > 0:
                    opçoes.append(pokemon)
            if isinstance(valores[i],list):
                if valores[i][1] == "Atk":
                    pokemon.curar(random.choice(opçoes),valores[i][0] * pokemon.Atk,player,tela)
                elif valores[i][1] == "Atk sp":
                    pokemon.curar(random.choice(opçoes),valores[i][0] * pokemon.Atk_sp,player,tela)
                elif valores[i][1] == "Vida":
                    pokemon.curar(random.choice(opçoes),valores[i][0] * pokemon.Vida,player,tela)
            else:
                pokemon.curar(random.choice(opçoes),valores[i],player,tela)


        elif valor == "CuraAliadoMenosVida":
            menos_vida = None
            for aliado in player.pokemons:
                if aliado.Vida > 0:
                    if aliado != pokemon:
                        if menos_vida is None or aliado.Vida < menos_vida.Vida:
                            menos_vida = aliado
            if menos_vida:
                if isinstance(valores[i],list):
                    if valores[i][1] == "Atk":
                        pokemon.curar(menos_vida,valores[i][0] * pokemon.Atk,player,tela)
                    elif valores[i][1] == "Atk sp":
                        pokemon.curar(menos_vida,valores[i][0] * pokemon.Atk_sp,player,tela)
                    elif valores[i][1] == "Vida":
                        pokemon.curar(menos_vida,valores[i][0] * pokemon.Vida,player,tela)
                else:
                    pokemon.curar(menos_vida,valores[i],player,tela)


        elif valor == "CuraAliadoMaisProximo":
            mais_proximo = None
            distancia_mais_proximo = None
            for aliado in player.pokemons:
                distancia = distancia_entre_pokemons(pokemon,aliado,mapa.Metros)
                if aliado.Vida > 0:
                    if aliado != pokemon:
                        if mais_proximo is None or distancia < distancia_mais_proximo:
                            mais_proximo = aliado
                            distancia_mais_proximo = distancia
            if isinstance(valores[i],list):
                if valores[i][1] == "Atk":
                    pokemon.curar(mais_proximo,valores[i][0] * pokemon.Atk,player,tela)
                elif valores[i][1] == "Atk sp":
                    pokemon.curar(mais_proximo,valores[i][0] * pokemon.Atk_sp,player,tela)
                elif valores[i][1] == "Vida":
                    pokemon.curar(mais_proximo,valores[i][0] * pokemon.Vida,player,tela)
            else:
                pokemon.curar(mais_proximo,valores[i],player,tela)


        elif valor == "CuraAliadoMaisLonge":
            mais_longe = None
            distancia_mais_longe = None
            for aliado in player.pokemons:
                distancia = distancia_entre_pokemons(pokemon,aliado,mapa.Metros)
                if aliado.Vida > 0:
                    if aliado != pokemon:
                        if mais_longe is None or distancia > distancia_mais_longe:
                            mais_longe = aliado
                            distancia_mais_longe = distancia
            if isinstance(valores[i],list):
                if valores[i][1] == "Atk":
                    pokemon.curar(mais_longe,valores[i][0] * pokemon.Atk,player,tela)
                elif valores[i][1] == "Atk sp":
                    pokemon.curar(mais_longe,valores[i][0] * pokemon.Atk_sp,player,tela)
                elif valores[i][1] == "Vida":
                    pokemon.curar(mais_longe,valores[i][0] * pokemon.Vida,player,tela)
                elif valores[i][1] == "Distancia":
                    pokemon.curar(mais_longe,valores[i][0] * distancia_mais_longe,player,tela)
            else:
                pokemon.curar(mais_longe,valores[i],player,tela)


        elif valor == "DanoPerfuraçao":
            if isinstance(valores[i],list):
                if valores[i][1] == "Atk":
                    perfuraçao = valores[i][0] * pokemon.Atk
                elif valores[i][1] == "Atk sp":
                    perfuraçao = valores[i][0] * pokemon.Atk_sp
                elif valores[i][1] == "Vel":
                    perfuraçao = valores[i][0] * pokemon.Vel
                perfuraçaoFinal = 1 - perfuraçao
                defesa = defesa * perfuraçaoFinal
            else:
                perfuraçao = 1 - valores[i]
                defesa = defesa * perfuraçao
        

        elif valor == "DanoCorrosão":
            defesa = 0
            dano = dano * alvo.Vida

        elif valor == "DanoBaseVelocidade":
            dano = ataque["dano"] * pokemon.Vel
        
        elif valor == "DanoBaseOuro":
            dano = ataque["dano"] * player.ouro

        elif valor == "DanoBaseOuroInimigo":
            dano = ataque["dano"] * inimigo.ouro
        
        elif valor == "DanoBaseDistancia":
            distancia = distancia_entre_pokemons(pokemon,alvo,mapa.Metros)
            dano = ataque["dano"] * distancia
        
        elif valor == "DanoBaseXP":
            dano = ataque["dano"] * pokemon.xp_atu

        elif valor == "Vampirismo":
            pokemon.vampirismo = valores[i]

        elif valor == "AdicionaEfeitoPosi":
            alvo.efeitosPosi[valores[i][0]] = valores[i][1]
        
        elif valor == "AdicionaEfeitoNega":
            alvo.efeitosNega[valores[i][0]] = valores[i][1]
        
        elif valor == "AutoAdicionarEfeitoPosi":
            pokemon.efeitosPosi[valores[i][0]] = valores[i][1]

        elif valor == "AutoAdicionaEfeitoNega":
            pokemon.efeitosNega[valores[i][0]] = valores[i][1]
        
        elif valor == "AutoDano":
            if valores[i] > 1:
                pokemon.Vida -= valores[i]
            else:
                pokemon.Vida = dano * valores[i]
        
        elif valor == "GanharOuro":
            player.ouro += valores[i]

        elif valor == "GanharOuroAleatorio":
            Min, Max = valores[i]
            player.ouro += random.randint(Min,Max)
        
        elif valor == "PerderOuro":
            player.ouro -= valores[i]

        elif valor == "TirarOuro":
            inimigo.ouro -= valores[i]

        elif valor == "RoubarOuro":
            inimigo.ouro -= valores[i]
            player.ouro += valores[i]

        elif valor == "GanharEnergia":
            pass
        
        elif valor == "Executar":
            Tipo = ataque["tipo"]
            mitigação = 100 / (100 + defesa) 
            dano_E = dano * efetividade(Tipo,alvo.tipo,tela,alvo)
            dano_F = round(dano_E * mitigação,1)
            if alvo.Vida - dano_F < alvo.VidaMax / valores[i]:
                dano = alvo.Vida
        
        elif valor == "AumentoDanoBaseVelocidade":
            aumento = pokemon.Vel * valores[i]
            dano = dano + aumento

        elif valor == "AumentoDanoBaseVelocidadeInimiga":
            aumento = alvo.Vel * valores[i]
            dano = dano + aumento

        elif valor == "AumentoDanoBaseVida":
            aumento = pokemon.VidaMax * valores[i]
            dano = dano + aumento

        elif valor == "AumentoDanoBaseVidaInimiga":
            aumento = alvo.VidaMax * valores[i]
            dano = dano + aumento

        elif valor == "AumentoDanoBaseDefesa":
            aumento = pokemon.Def * valores[i]
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseDefesaSP":
            aumento = pokemon.Def_sp * valores[i]
            dano = dano + aumento

        elif valor == "AumentoDanoBaseOuro":
            aumento = player.ouro * valores[i]
            dano = dano + aumento

        elif valor == "AumentoDanoBaseOuroInimigo":
            aumento = inimigo.ouro * valores[i]
            dano = dano + aumento

        elif valor == "AumentoDanoBaseItens":
            aumento = len(player.inventario) * valores[i]
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseItensInimigo":
            aumento = len(inimigo.inventario) * valores[i]
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseEnergias":
            aumento = len(player.energias.values()) * valores[i]
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseEnergiasInimigo":
            aumento = len(inimigo.energias.values()) * valores[i]
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseSorte50%":
            aumento = random.choice(0,valores[i])
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseSorte":
            Min, Max = valores[i]
            aumento = random.randint(Min,Max)
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseDistancia":
            distancia = distancia_entre_pokemons(pokemon,alvo,mapa.Metros)
            aumento = distancia * valores[i]
            dano = dano + aumento
        
        elif valor == "AumentoDanoBaseEfeitoPosiEspecifico":
            if alvo.efeitosPosi[valores[i][0]]:
                if valores[i][1] < 1:
                    dano = dano * valores[i][1]
                else:
                    dano = dano + valores[i][1]
        
        elif valor == "AumentoDanoBaseEfeitoNegaEspecifico":
            if alvo.efeitosNega[valores[i][0]]:
                if valores[i][1] < 1:
                    dano = dano * valores[i][1]
                else:
                    dano = dano + valores[i][1]
        
        elif valor == "AutoAumentoDanoBaseEfeitoPosiEspecifico":
            if pokemon.efeitosPosi[valores[i][0]]:
                if valores[i][1] < 1:
                    dano = dano * valores[i][1]
                else:
                    dano = dano + valores[i][1]
        
        elif valor == "AutoAumentoDanoBaseEfeitoNegaEspecifico":
            if pokemon.efeitosNega[valores[i][0]]:
                if valores[i][1] < 1:
                    dano = dano * valores[i][1]
                else:
                    dano = dano + valores[i][1]
