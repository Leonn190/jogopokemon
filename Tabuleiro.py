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

def Desenhar_Casas_Disponiveis(tela, casas_disponiveis, player, inimigo, Fonte, estado_global, eventos):
    cor_casa_disponivel = (100, 255, 100)
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
                    estado_global=estado_global,
                    eventos=eventos,
                    id_botao=id_ocupado,
                    grossura=1
                )

                # Centraliza e desenha a imagem do Pokémon por cima
                x_img = x + (tamanho_casa - tamanho_imagem) // 2
                y_img = y + (tamanho_casa - tamanho_imagem) // 2
                tela.blit(pokemon_encontrado.imagem, (x_img, y_img))

        else:
            pygame.draw.rect(tela, cor_casa_disponivel, espaco)
            pygame.draw.rect(tela, (0, 0, 0), espaco, 2)

def Move(peça,L,C):
    if Mapa[L][C]["ocupado"] == None:
        peça.local = Mapa[L][C] 
        Mapa[L][C]["ocupado"] = peça.ID
    
    else:
        GV.adicionar_mensagem("Essa posição já está ocupada")

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
