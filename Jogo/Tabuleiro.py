import pygame
import random 
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

Mapa = []
Area = []
PeçaS = None

pygame.mixer.init()
Bloq = pygame.mixer.Sound("Jogo/Audio/Sons/Bloq.wav")

estadoTabuleiro = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None}

def Gerar_Mapa():
    global Mapa

    Mapa = []
    for i in range(15):  # 15 linhas
        linha = []
        for j in range(25):  # 20 colunas
            casa = {
                "id": (i, j),
                "ocupado": None  # Aqui futuramente pode ser um Pokémon ou outro objeto
            }
            linha.append(casa)
        Mapa.append(linha)

def seleciona_peça(p,dono,player):
    global PeçaS
    if dono == "player":
        pagou = 0
        gastas = []
        for i in range(p.custo):
            for cor in player.energiasDesc:
                if player.energias[cor] >= 1:
                    player.energias[cor] -= 1
                    gastas.append(cor)
                    pagou += 1
                    break
        
        if pagou != p.custo:
            GV.tocar(Bloq)
            GV.adicionar_mensagem("Sem energias, não pode se mover")
            for i in range(len(gastas)):
                player.energias[gastas[i]] += 1
            desseleciona_peça()
            return 

        PeçaS = p
    else:
        GV.adicionar_mensagem("Não pode selecionar pokemon inimigo")

def desseleciona_peça():
    global PeçaS
    global estadoTabuleiro
    PeçaS = None
    estadoTabuleiro["selecionado_esquerdo"] =  False

def Desenhar_Casas_Disponiveis(tela, casas_disponiveis, player, inimigo, Fonte, eventos, cores_zebragem, metros):
    global Area
    tamanho_casa = 40
    tamanho_imagem = 38
    Area = casas_disponiveis
    x_inicial = (1920 - 25 * tamanho_casa) // 2
    y_inicial = (1080 - 15 * tamanho_casa) // 2

    # Se nenhuma casa foi passada, desenhar o mapa todo
    if not casas_disponiveis:
        casas_disponiveis = [(linha, coluna) for linha in range(15) for coluna in range(25)]

    for (linha, coluna) in casas_disponiveis:
        casa = Mapa[linha][coluna]
        x = x_inicial + coluna * tamanho_casa
        y = y_inicial + linha * tamanho_casa
        espaco = pygame.Rect(x, y, tamanho_casa, tamanho_casa)

        if casa["ocupado"] is not None:
            id_ocupado = casa["ocupado"]
            pokemon_encontrado = None
            dono = None  # "player" ou "inimigo"

            for poke in player.pokemons:
                if poke.ID == id_ocupado:
                    pokemon_encontrado = poke
                    dono = "player"
                    break

            if not pokemon_encontrado:
                for poke in inimigo.pokemons:
                    if poke.ID == id_ocupado:
                        pokemon_encontrado = poke
                        dono = "inimigo"
                        break

            if pokemon_encontrado:
                cor_fundo = (0, 0, 255) if dono == "player" else (255, 0, 0)

                GV.Botao_Selecao(
                    tela=tela,
                    espaço=espaco,
                    texto="",
                    Fonte=Fonte,
                    cor_fundo=cor_fundo,
                    cor_borda_normal=PRETO,
                    cor_passagem=AMARELO,
                    cor_borda_esquerda=VERMELHO,
                    funcao_esquerdo=lambda p=pokemon_encontrado: seleciona_peça(p, dono, player),
                    desfazer_esquerdo=lambda: desseleciona_peça(),
                    estado_global=estadoTabuleiro,
                    eventos=eventos,
                    id_botao=id_ocupado,
                    grossura=2
                )

                x_img = x + (tamanho_casa - tamanho_imagem) // 2
                y_img = y + (tamanho_casa - tamanho_imagem) // 2
                tela.blit(pokemon_encontrado.imagem, (x_img, y_img))

        else:
            cor_casa_disponivel = cores_zebragem[(linha + coluna) % 2]
            pygame.draw.rect(tela, cor_casa_disponivel, espaco)
            pygame.draw.rect(tela, (0, 0, 0), espaco, 2)

    if PeçaS is not None:
        Mover_casas(tela, eventos, PeçaS, casas_disponiveis, player, metros)

def Move(peça, L, C,player):
    peça.Ganhar_XP(1,player)
    if peça.local is not None:

        linha_antiga, coluna_antiga = peça.local["id"]
        Mapa[linha_antiga][coluna_antiga]["ocupado"] = None

        # Atualizar a nova posição
    peça.local = Mapa[L][C]
    Mapa[L][C]["ocupado"] = peça.ID

    desseleciona_peça()

def Inverter_Tabuleiro(player, inimigo):
    global Mapa

    # Cria novo mapa espelhado verticalmente
    novo_mapa = []
    for i in range(15):
        linha = []
        for j in range(25):
            casa = {
                "id": (i, j),
                "ocupado": None
            }
            linha.append(casa)
        novo_mapa.append(linha)

    # Reposiciona todos os pokémons no novo mapa invertido
    for poke in player.pokemons + inimigo.pokemons:
        if poke.local is not None:
            antiga_linha, coluna = poke.local["id"]
            nova_linha = 14 - antiga_linha  # espelhamento vertical
            novo_local = novo_mapa[nova_linha][coluna]
            poke.local = novo_local
            novo_local["ocupado"] = poke.ID  # Corrigido para 'ID'

    # Substitui o mapa original
    Mapa = novo_mapa

def Mover_casas(tela, eventos, PeçaS, casas_disponiveis, player, metros=10):
    tamanho_casa = 40
    x_inicial = (1920 - 25 * tamanho_casa) // 2
    y_inicial = (1080 - 15 * tamanho_casa) // 2

    # Calcular alcance com base na velocidade
    vel = PeçaS.vel
    if vel <= 0:
        return  # Pokémon imóvel

    alcance = int(vel / metros)
    if vel > 0 and alcance < 1:
        alcance = 1  # Pelo menos 1 movimento lateral garantido

    # Definir limites de movimento lateral e diagonal conforme escala personalizada
    if alcance == 1:
        alcance_lateral = 1
        alcance_diagonal = 1
    elif alcance == 2:
        alcance_lateral = 2
        alcance_diagonal = 1
    elif alcance == 3:
        alcance_lateral = 2
        alcance_diagonal = 2
    elif alcance == 4:
        alcance_lateral = 3
        alcance_diagonal = 2
    elif alcance == 5:
        alcance_lateral = 3
        alcance_diagonal = 3
    elif alcance == 6:
        alcance_lateral = 4
        alcance_diagonal = 3
    else:
        alcance_lateral = min(4 + (alcance - 6), 10)  # opcional: limitar para evitar exageros
        alcance_diagonal = min(3 + (alcance - 5), 10)

    linha_atual, coluna_atual = PeçaS.local["id"]
    movimentos_possiveis = []

    for dx in range(-alcance_lateral, alcance_lateral + 1):
        for dy in range(-alcance_lateral, alcance_lateral + 1):
            nova_linha = linha_atual + dy
            nova_coluna = coluna_atual + dx

            if (0 <= nova_linha < 15 and 0 <= nova_coluna < 25 and
                (nova_linha, nova_coluna) in casas_disponiveis and
                Mapa[nova_linha][nova_coluna]["ocupado"] is None):

                # Verifica se é diagonal
                if dx != 0 and dy != 0:
                    if abs(dx) <= alcance_diagonal and abs(dy) <= alcance_diagonal:
                        movimentos_possiveis.append((nova_linha, nova_coluna))
                else:
                    movimentos_possiveis.append((nova_linha, nova_coluna))

    for linha, coluna in movimentos_possiveis:
        x = x_inicial + coluna * tamanho_casa
        y = y_inicial + linha * tamanho_casa
        espaco = pygame.Rect(x, y, tamanho_casa, tamanho_casa)

        GV.Botao(
            tela=tela,
            texto="",
            espaço=espaco,
            cor_normal=(100, 255, 100),
            cor_borda=BRANCO,
            cor_passagem=(150, 255, 150),
            acao=lambda linha=linha, coluna=coluna: Move(PeçaS, linha, coluna, player),
            Fonte=pygame.font.SysFont("arial", 16),
            estado_clique={"estado": False},
            grossura=2,
            eventos=eventos
        )

def GuardarPosicionar(pokemon,player):
    if pokemon.local is not None:
        if len(player.pokemons) > 1:
            linha_antiga, coluna_antiga = pokemon.local["id"]
            Mapa[linha_antiga][coluna_antiga]["ocupado"] = None
            pokemon.local = None
            pokemon.guardado = 1
        else:
            GV.tocar(Bloq)
            GV.adicionar_mensagem("Você não deve guardar seu unico pokemon")
    else:
        for i in range(len(Mapa)):
            for tentativa in range(30):
                j = random.randint(0, 24)
                if Mapa[14 - i][j]["ocupado"] is None:
                    if Mapa[14 - i][j]["id"] in Area:
                        pokemon.local = Mapa[14 - i][j]
                        Mapa[14 - i][j]["ocupado"] = pokemon.ID
                        return







    