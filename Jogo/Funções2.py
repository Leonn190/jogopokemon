import random
import Visual.GeradoresVisuais as GV
from Visual.Sonoridade import tocar
from Visual.Mensagens import adicionar_mensagem_passageira
import math
import json
import pygame

Energias = ["vermelha", "azul", "amarela", "verde", "roxo", "rosa", "laranja", "marrom", "preta", "cinza"]


def efetividade(Tipo_do_ataque,Tipo_do_atacado,tela,AlvoLoc):
    
    tipos = [
    "normal", "fogo", "agua", "eletrico", "planta", "gelo",
    "lutador", "venenoso", "terrestre", "voador", "psiquico", "inseto",
    "pedra", "fantasma", "dragao", "sombrio", "metal", "fada"]

    matriz_fraquezas = [
    # ATK \ DEF: NOR FOG AGU ELE GRA GEL LUT VEN TER VOA PSI INS PED FAN DRA NOT MET FAA
    [ 1,  1,  1,  1,  1,  1,  1, 1,  1,  1,  1, 1, 0.5,  0,  1,  1, 0.5, 1 ],  # normal
    [ 1, 0.5, 0.5, 1,  2,  2,  1, 1,  1,  1,  1, 2, 0.5, 1, 0.5, 1,  2,  1 ],  # fogo
    [ 1, 2,  0.5, 1,  0.5, 1,  1, 1,  2,  1,  1, 1, 2,   1, 0.5, 1,  1,  1 ],  # agua
    [ 1, 1,  2,  0.5, 0.5, 1,  1, 1,  0,  2,  1, 1, 1,   1, 0.5, 1,  1,  1 ],  # eletrico
    [ 1, 0.5, 2,  1,  0.5, 1,  1, 0.5,2,  0.5, 1, 0.5,2,  1, 0.5, 1,  0.5,1 ],  # grama
    [ 1, 0.5, 0.5,1,  2,  0.5,1, 1,  2,  2,  1, 1, 1,   1, 2,   1,  0.5,1 ],  # gelo
    [ 2, 1,  1,  1,  1,  2,  1, 0.5,1,  0.5,0.5,0.5,2,   0, 1,   2,  2,  0.5],  # lutador
    [ 1, 1,  1,  1,  2,  1,  1, 0.5,0.5,1,  1, 1, 0.5, 0.5,1,   1,  0,  2 ],  # venenoso
    [ 1, 2,  1,  2,  0.5,1,  1, 2,  1,  0,  1, 0.5,2,   1, 1,   1,  2,  1 ],  # terra
    [ 1, 1,  1,  0.5,2,  1,  2, 1,  1,  1,  1, 2, 0.5, 1, 1,   1,  0.5,1 ],  # voador
    [ 1, 1,  1,  1,  1,  1,  2, 2,  1,  1,  0.5,1, 1,   1, 1,   0,  0.5,1 ],  # psiquico
    [ 1, 0.5,1,  1,  2,  1,  0.5,0.5,1,  0.5,2, 1, 1,   0.5,1,   2,  0.5,0.5],  # inseto
    [ 1, 2,  1,  1,  1,  2,  0.5,1,  0.5,2,  1, 2, 1,   1, 1,   1,  0.5,1 ],  # pedra
    [ 0, 1,  1,  1,  1,  1,  1, 1,  1,  1,  2, 1, 1,   2, 1,   0.5,1,  1 ],  # fantasma
    [ 1, 1,  1,  1,  1,  1,  1, 1,  1,  1,  1, 1, 1,   1, 2,   1,  0.5,0 ],  # dragao
    [ 1, 1,  1,  1,  1,  1,  0.5,1,  1,  1,  2, 1, 1,   2, 1,   0.5,1,  0.5],  # noturno
    [ 1, 0.5,0.5,0.5,1,  2,  1, 1,  1,  1,  1, 1, 2,   1, 1,   1,  0.5,2 ],  # metal
    [ 1, 0.5,1,  1,  1,  1,  2, 0.5,1,  1,  1, 1, 1,   1, 2,   2,  0.5,1 ]   # fada
    ]
    
    multiplicador = 1
    for tipo_atk in Tipo_do_ataque:
        idx_atk = tipos.index(tipo_atk)
        for tipo_def in Tipo_do_atacado:
            idx_def = tipos.index(tipo_def)
            multiplicador *= matriz_fraquezas[idx_atk][idx_def]

    if multiplicador == 4:
        multiplicador -= 2
    elif multiplicador == 2:
        multiplicador -= 0.5
    elif multiplicador in [0.5,0.25]:
        multiplicador += 0.25
    
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
    x,y = AlvoLoc
    adicionar_mensagem_passageira(tela,f"{texto}",(0,0,0),Fonte,(x,y + 50))

    return multiplicador

def distancia_entre_pokemons(poke1, poke2, Metros):
    if not isinstance(poke1.local, list) or len(poke1.local) != 2:
        return None
    if not isinstance(poke2.local, list) or len(poke2.local) != 2:
        return None

    x1 = poke1.local[0]
    y1 = poke1.local[1]
    x2 = poke2.local[0]
    y2 = poke2.local[1]

    dx = x1 - x2
    dy = y1 - y2
    distancia_px = math.hypot(dx, dy)

    distancia_real = max(0, distancia_px - poke1.raio - poke2.raio)

    return distancia_real / Metros

def Aliado_menos_vida(pokemon,player,numero=1):
    selecionados = []
    for _ in range(numero):
        menos_vida = None
        for aliado in player.pokemons:
            if aliado.Vida > 0:
                if aliado != pokemon:
                    if aliado not in selecionados:
                        if menos_vida is None or aliado.Vida < menos_vida.Vida:
                            menos_vida = aliado
        if menos_vida is None:
            return selecionados

        selecionados.append(menos_vida)
    return selecionados    

def Inimigo_menos_vida(playerinimigo, numero=1):
    selecionados = []
    for _ in range(numero):
        menos_vida = None
        for inimigo in playerinimigo.pokemons:
            if inimigo.Vida > 0 and inimigo not in selecionados:
                if menos_vida is None or inimigo.Vida < menos_vida.Vida:
                    menos_vida = inimigo
        if menos_vida is None:
            return selecionados
        selecionados.append(menos_vida)
    return selecionados

def aliado_aleatorio(pokemon, player, numero=1):
    selecionados = []
    for _ in range(numero):
        opcoes = []
        for aliado in player.pokemons:
            if aliado.Vida > 0 and aliado != pokemon and aliado not in selecionados:
                opcoes.append(aliado)
        if not opcoes:
            return selecionados
        escolhido = random.choice(opcoes)
        selecionados.append(escolhido)
    return selecionados

def inimigo_aleatorio(playerinimigo, numero=1):
    selecionados = []
    for _ in range(numero):
        opcoes = []
        for inimigo in playerinimigo.pokemons:
            if inimigo.Vida > 0 and inimigo not in selecionados:
                opcoes.append(inimigo)
        if not opcoes:
            return selecionados
        escolhido = random.choice(opcoes)
        selecionados.append(escolhido)
    return selecionados

def aliado_mais_proximo(pokemon, player, mapa, numero=1):
    selecionados = []
    for _ in range(numero):
        mais_proximo = None
        distancia_mp = None
        for aliado in player.pokemons:
            if aliado.local is not None and aliado.Vida > 0 and aliado != pokemon and aliado not in selecionados:
                d = distancia_entre_pokemons(pokemon, aliado, mapa.Metros)
                if mais_proximo is None or d < distancia_mp:
                    mais_proximo = aliado
                    distancia_mp = d
        if mais_proximo is None:
            return selecionados
        selecionados.append(mais_proximo)
    return selecionados

def aliado_mais_longe(pokemon, player, mapa, numero=1):
    selecionados = []
    for _ in range(numero):
        mais_longe = None
        distancia_ml = None
        for aliado in player.pokemons:
            if aliado.local is not None and aliado.Vida > 0 and aliado != pokemon and aliado not in selecionados:
                d = distancia_entre_pokemons(pokemon, aliado, mapa.Metros)
                if mais_longe is None or d > distancia_ml:
                    mais_longe = aliado
                    distancia_ml = d
        if mais_longe is None:
            return selecionados
        selecionados.append(mais_longe)
    return selecionados

def inimigo_mais_proximo(pokemon, playerinimigo, mapa, numero=1):
    selecionados = []
    for _ in range(numero):
        mais_proximo = None
        distancia_mp = None
        for inimigo in playerinimigo.pokemons:
            if inimigo.local is not None and inimigo.Vida > 0 and inimigo not in selecionados:
                d = distancia_entre_pokemons(pokemon, inimigo, mapa.Metros)
                if mais_proximo is None or d < distancia_mp:
                    mais_proximo = inimigo
                    distancia_mp = d
        if mais_proximo is None:
            return selecionados
        selecionados.append(mais_proximo)
    return selecionados

def inimigo_mais_longe(pokemon, playerinimigo, mapa, numero=1):
    selecionados = []
    for _ in range(numero):
        mais_longe = None
        distancia_ml = None
        for inimigo in playerinimigo.pokemons:
            if inimigo.local is not None and inimigo.Vida > 0 and inimigo not in selecionados:
                d = distancia_entre_pokemons(pokemon, inimigo, mapa.Metros)
                if mais_longe is None or d > distancia_ml:
                    mais_longe = inimigo
                    distancia_ml = d
        if mais_longe is None:
            return selecionados
        selecionados.append(mais_longe)
    return selecionados

def pokemons_nos_arredores(pokemon, player, inimigo, arredores_metros, Mapa):
    if not isinstance(pokemon.local, list) or len(pokemon.local) != 2:
        return [], []

    x0 = pokemon.local[0]
    y0 = pokemon.local[1]
    raio_busca = arredores_metros * Mapa.Metros + pokemon.raio

    aliados_encontrados = []
    inimigos_encontrados = []

    def dentro_do_raio(p):
        if not isinstance(p.local, list) or len(p.local) != 2 or p is pokemon:
            return False
        x = p.local[0]
        y = p.local[1]
        distancia = math.hypot(x - x0, y - y0)
        return distancia <= (raio_busca + p.raio)

    for p in player.pokemons:
        if dentro_do_raio(p):
            aliados_encontrados.append(p)

    for p in inimigo.pokemons:
        if dentro_do_raio(p):
            inimigos_encontrados.append(p)

    return aliados_encontrados, inimigos_encontrados

def VCusto(player,pokemon,ataque):
    
    Custo = ataque["custo"].copy()
    if pokemon.efeitosNega["Descarregado"] > 0:
        for i in range(len(ataque["custo"])):
            Custo.append(ataque["custo"][i]) 
    if pokemon.efeitosPosi["Energizado"] > 0:
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
        return False
    else:
        return True

def VAcerta(pokemon,alvo,ataque,metros):

    alcance = ataque["alcance"]
    assertividade = ataque["precisão"]

    try:
        alcance,assertividade = ataque["var"](alcance,assertividade,pokemon,alvo,ataque)
    except KeyError:
        pass

    distancia = distancia_entre_pokemons(pokemon,alvo,metros)
    Over = alcance - distancia
    if alvo.efeitosPosi["Voando"] > 0:
        Over = Over - 45
    if Over < 0:
        assertividade = assertividade + Over * 5
    else:
        pass
    if pokemon.efeitosNega["Confuso"] > 0:
        assertividade = assertividade * 0.5
    if pokemon.efeitosPosi["Focado"] > 0:
        assertividade = assertividade * 1.5

    desfoco = random.randint(0,100)
    if desfoco > assertividade:
        GV.adicionar_mensagem("Você errou o ataque")
        tocar("Falhou")
        return False
    else:
        return True
    
def VEstilo(pokemon,alvo,ataque):
    if ataque["estilo"] == "N":
        Dano = pokemon.Atk
        Defesa = alvo.Def
    elif ataque["estilo"] == "E":
        Dano = pokemon.Atk_sp
        Defesa = alvo.Def_sp
    elif ataque["estilo"] == "S":
        Dano = None
        Defesa = None
    Dano = Dano * ataque["dano"]
    return Dano, Defesa

def VEfeitos(pokemon,alvo,player,inimigo,dano_F,tipo,tela):
    
    if alvo.efeitosNega["Vampirico"] > 0:
        vampirismo = dano_F * 0.3
        pokemon.curar(vampirismo,player,tela)
    if alvo.efeitosPosi["Preparado"] > 0:
        preparo = round((alvo.vel / 3),1)
        dano_F = dano_F - preparo
        pokemon.atacado(preparo,player,inimigo,tipo,tela)
    if alvo.efeitosPosi["Refletir"] > 0:
        reflexão = dano_F * 0.8
        pokemon.atacado(reflexão,player,inimigo,tipo,tela)
        dano_F = dano_F * 0.2
    
    return round(dano_F,1)

def Vsteb(pokemon,dano,ataque):
    if ataque["tipo"] in pokemon.tipo:
        dano = dano * 1.2
    return dano

def verificar_serializabilidade(dicionario):
    for chave, valor in dicionario.items():
        try:
            json.dumps(valor)
        except (TypeError, OverflowError) as e:
            print(f"Erro na chave '{chave}': {repr(valor)} do tipo {type(valor)} não é serializável. Erro: {e}")
            dd = input("erro")