import pygame
import requests
import json
import threading
import time
import Visual.GeradoresVisuais as GV
import PygameAções as A
import Mapa as M
from Config import aplicar_claridade
from Geradores.GeradorPlayer import Gerador_player, Gerador_player_clone
from Geradores.GeradorPartida import GeraPartidaOnline, GeraPartidaOnlineClone
from Geradores.GeradorOutros import Gera_Baralho, Gera_Mapa, coletor
from Visual.Sonoridade import tocar
from Visual.Efeitos import gerar_gif
from Visual.GeradoresVisuais import (
    Fonte15, Fonte23, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

Carregando_Frames = GV.carregar_frames("imagens/Efeitos/!Loading_frames")

Url = "https://apipokemon-i9bb.onrender.com"

B1 = {"estado": False}

DadosGerais = [None,None]

def CriaPartidaOnline(player1,player2,ID):

    player2 = Gerador_player_clone(player2)

    for i in range(15):
        coletor(player1)
        coletor(player2)

    Mapa = Gera_Mapa(0)
    Baralho = Gera_Baralho(player1.deck,player2.deck)
    Partida = GeraPartidaOnline(player1,player2,Baralho,Mapa)

    largura, altura = M.Tabuleiros[Mapa.terreno].get_size()

    player2.pokemons[0].local = 960, 570 - altura // 2
    player1.pokemons[0].local = 960, 510 + altura // 2

    Partida.ID = ID

    return Partida

def Fila(tela, estados, relogio, Config):
    global DadosGerais

    pygame.mixer.music.load('Audio/Musicas/Carregamento.ogg')
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play(-1)
    
    from PygameAções import informaçoesp1
    Jogador = Gerador_player(informaçoesp1)

    JogadorDados = Jogador.ToDic_Inicial()
    resposta = requests.post("https://apipokemon-i9bb.onrender.com/entrar_partida", json=JogadorDados)
    data = resposta.json()

    Gif = gerar_gif(Carregando_Frames,(1765,930), 62)

    texto = Fonte50.render("Carregando...", True, (255, 255, 255))  # branco
    pos_texto = (
        (1920 - texto.get_width()) // 2,
        (1080 - texto.get_height()) // 2
    )

    def contata_servidor():
        global DadosGerais
        while True:
            try:
                if data["estado"] == "criou":
                    resposta = requests.get("https://apipokemon-i9bb.onrender.com/buscar_jogador", json=data)
                    pronto = resposta.json()
                    if pronto["pronto"]:
                        PartidaOn = CriaPartidaOnline(Jogador, pronto["jogador2"], data["partida"])
                        envio = {"partida": data["partida"], "dados": PartidaOn.anterior}
                        resposta = requests.post("https://apipokemon-i9bb.onrender.com/inicializar_partida", json=envio)
                        print (resposta.json())
                        DadosGerais = [PartidaOn, 1]
                        A.Iniciar_partida_online(estados)
                        break  # Finaliza a thread após iniciar

                elif data["estado"] == "entrou":
                    resposta = requests.get("https://apipokemon-i9bb.onrender.com/verificar_partida_criada", json={"partida": data["partida"]})
                    pronto = resposta.json()
                    print (pronto)
                    if pronto["criada"]:
                        PartidaOn = GeraPartidaOnlineClone(pronto["dados"])
                        PartidaOn.Jogador2 = Jogador
                        DadosGerais = [PartidaOn, 2]
                        A.Iniciar_partida_online(estados)
                        break  # Finaliza a thread após iniciar

                time.sleep(2)  # Espera 2 segundos antes de checar novamente

            except Exception as e:
                print("Erro na thread contata_servidor:", e)
                time.sleep(5)

    threading.Thread(target=contata_servidor, daemon=True).start()
    while estados["Rodando_Fila"]:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Fila"] = False
                estados["Rodando_Jogo"] = False
            
        tela.fill((0, 0, 0))  # Fundo preto
        tela.blit(texto, pos_texto)

        Gif.atualizar(tela)

        GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
             lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)

        aplicar_claridade(tela, Config["Claridade"])
        pygame.display.update()
        relogio.tick(Config["FPS"])