import pygame
import GeradoresVisuais as GV
import Gerador2 as G
import PygameAções as A
from GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

Mapa = []
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

def Desenhar_Casas_Disponiveis(tela, casas_disponiveis, player, inimigo, Fonte, eventos):
    cor_casa_disponivel = (150, 150, 150)
    tamanho_casa = 40
    tamanho_imagem = 38
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

                # Desenha o botão
                GV.Botao_Selecao(
                    tela=tela,
                    espaço=espaco,
                    texto="",
                    Fonte=Fonte,
                    cor_fundo=cor_fundo,
                    cor_borda_normal=PRETO,
                    cor_passagem=AMARELO,
                    cor_borda_esquerda=VERMELHO,
                    funcao_esquerdo=lambda p=pokemon_encontrado: seleciona_peça(p,dono,player),
                    desfazer_esquerdo=lambda: desseleciona_peça(),
                    estado_global=estadoTabuleiro,
                    eventos=eventos,
                    id_botao=id_ocupado,
                    grossura=2
                )

                # Centraliza e desenha a imagem do Pokémon por cima
                x_img = x + (tamanho_casa - tamanho_imagem) // 2
                y_img = y + (tamanho_casa - tamanho_imagem) // 2
                tela.blit(pokemon_encontrado.imagem, (x_img, y_img))

        else:
            pygame.draw.rect(tela, cor_casa_disponivel, espaco)
            pygame.draw.rect(tela, (0, 0, 0), espaco, 2)
   
    if PeçaS is not None:
        Mover_casas(tela,eventos,PeçaS,casas_disponiveis,player)

def Move(peça, L, C,player):
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
        antiga_linha, coluna = poke.local["id"]
        nova_linha = 14 - antiga_linha  # espelhamento vertical
        novo_local = novo_mapa[nova_linha][coluna]
        poke.local = novo_local
        novo_local["ocupado"] = poke.ID  # Corrigido para 'ID'

    # Substitui o mapa original
    Mapa = novo_mapa

def Mover_casas(tela, eventos, PeçaS, casas_disponiveis, player):
    tamanho_casa = 40
    x_inicial = (1920 - 25 * tamanho_casa) // 2
    y_inicial = (1080 - 15 * tamanho_casa) // 2

    vel = PeçaS.vel
    linha_atual, coluna_atual = PeçaS.local["id"]
    alcance = (vel + 10) // 20  # conforme padrão da imagem

    movimentos_possiveis = []

    for dx in range(-alcance, alcance + 1):
        for dy in range(-alcance, alcance + 1):
            if abs(dx) + abs(dy) <= alcance:
                nova_linha = linha_atual + dy
                nova_coluna = coluna_atual + dx

                if (0 <= nova_linha < 15 and 0 <= nova_coluna < 25 and
                    (nova_linha, nova_coluna) in casas_disponiveis):

                    casa = Mapa[nova_linha][nova_coluna]
                    if casa["ocupado"] is None:
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









    