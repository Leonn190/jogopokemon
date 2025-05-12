import pygame
import os
import importlib
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

pygame.init()
pygame.mixer.init()

DeckSelecionado = None
Abrir = None
Decks = []

def salvar_dicionario_em_py(dicionario, nome_arquivo, pasta_destino):
    """Salva um dicionário em um arquivo .py no formato Python."""
    # Garante que a pasta existe
    os.makedirs(pasta_destino, exist_ok=True)

    # Monta o caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_destino, f"{nome_arquivo}.py")

    # Abre e escreve o dicionário em formato Python legível
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"# Arquivo gerado automaticamente\n\n")
        arquivo.write(f"{nome_arquivo} = {repr(dicionario)}\n")

def selecionaDeck(deck):
    global DeckSelecionado
    DeckSelecionado = deck

def desselecionaDeck():

def carregar_decks(pasta):
    global Decks
    Decks.clear()

    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(".py"):
            caminho = os.path.join(pasta, nome_arquivo)
            nome_modulo = nome_arquivo[:-3]

            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            # Procura diretamente no módulo por dicionários
            for atributo in dir(modulo):
                valor = getattr(modulo, atributo)  # Aqui ainda usamos getattr para acessar atributos, já que não há outra forma simples
                if isinstance(valor, dict):
                    Decks.append(valor)
                    break

estadoDecks = {"selecionado_esquerdo": None}

def TelaDecks(tela,eventos,estados):
    global Decks
    global DeckSelecionado
    global Abrir

    for i, deck in enumerate(Decks):
        GV.Botao_Selecao(
                tela, (i * 70, (YT - 60), 120, 120),
                "", Fonte30,
                cor_fundo=AZUL_CLARO, cor_borda_normal=PRETO,
                cor_borda_esquerda=VERDE, cor_borda_direita=None,
                cor_passagem=AMARELO, id_botao=deck["nome"],   
                estado_global=estadoDecks, eventos=eventos,
                funcao_esquerdo=lambda deck=deck: selecionaDeck(deck), 
                funcao_direito=None,
                desfazer_esquerdo=lambda: desselecionaDeck(), desfazer_direito=None,
                tecla_esquerda=pygame.K_1, tecla_direita=None)

def TelaCriador(tela,eventos,estados):


def Decks(tela,estados,relogio):
    global Parte2

    Parte2 = False
    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Decks.jpg", (1920,1080))

    pygame.mixer.music.load('Audio/Musicas/Decks.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    carregar_decks("Decks")

    while estados["Rodando_Decks"]:
        tela.blit(Fundo_Menu, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False

        if abrir is None:
            TelaDecks(tela,eventos,estados)
        else:
            TelaCriador(tela,eventos,estados)

        pygame.display.update()
        relogio.tick(60)

