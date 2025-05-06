import random
import Visual.GeradoresVisuais as GV
from Visual.Sonoridade import tocar
from Visual.Mensagens import adicionar_mensagem_passageira
import math
import pygame

Energias = ["vermelha", "azul", "amarela", "verde", "roxo", "rosa", "laranja", "marrom", "preta", "cinza"]

def efetividade(Tipo_do_ataque,Tipo_do_atacado,tela,AlvoLoc):
    
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
    x,y = AlvoLoc
    adicionar_mensagem_passageira(tela,f"{texto}",(0,0,0),Fonte,(x,y + 50))

    return multiplicador

def distancia_entre_pokemons(poke1, poke2, tamanho_casa):
    linha1, coluna1 = poke1.local["id"]
    linha2, coluna2 = poke2.local["id"]

    dx = (coluna1 - coluna2) * tamanho_casa  # Coluna representa o eixo X
    dy = (linha1 - linha2) * tamanho_casa    # Linha representa o eixo Y

    return math.hypot(dx, dy)

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

def pokemons_nos_arredores(pokemon, player, inimigo, arredores, Mapa):
    if pokemon.local is None:
        return [], []

    linha, coluna = map(int, pokemon.local["id"])
    aliados_encontrados = []
    inimigos_encontrados = []

    for dx in range(-arredores, arredores + 1):
        for dy in range(-arredores, arredores + 1):
            nova_linha = linha + dx
            nova_coluna = coluna + dy

            # Ignora a própria posição
            if dx == 0 and dy == 0:
                continue

            # Verifica se está dentro dos limites do mapa
            if 0 <= nova_linha < len(Mapa) and 0 <= nova_coluna < len(Mapa[0]):
                ocupante = Mapa[nova_linha][nova_coluna]["ocupado"]
                if ocupante is not None:
                    # Procura nos aliados
                    for p in player.pokemons:
                        if p.ID == ocupante:
                            aliados_encontrados.append(p)
                            break
                    # Procura nos inimigos
                    for p in inimigo.pokemons:
                        if p.ID == ocupante:
                            inimigos_encontrados.append(p)
                            break

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

    distancia = distancia_entre_pokemons(pokemon,alvo,metros)
    Over = ataque["alcance"] - distancia
    if alvo.efeitosPosi["Voando"] > 0:
        Over = Over - 45
    if Over < 0:
        assertividade = ataque["precisão"] + Over
    else:
        assertividade = ataque["precisão"]
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