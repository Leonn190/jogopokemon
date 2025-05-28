# Importações principais
import pygame
import requests
import json
import threading
import time

# Importações de módulos do jogo
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
    Fonte15, Fonte23, Fonte30, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO, AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO, VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,
)

# Carrega os frames da animação de carregamento
Carregando_Frames = GV.carregar_frames("imagens/Efeitos/!Loading_frames")

# URL base da API online
Url = "https://apipokemon-i9bb.onrender.com"

# Estado de botão
B1 = {"estado": False}

# Armazena os dados da partida criada ou recebida
DadosGerais = [None, None]

# -------------------------------
# Gera uma nova partida online com dois jogadores
def CriaPartidaOnline(player1, Dadosplayer2, ID):
    player2 = Gerador_player_clone(Dadosplayer2)

    # Executa coleta de pokémons para ambos os jogadores
    for i in range(15):
        coletor(player1)
        coletor(player2)

    mapa = Gera_Mapa(0)
    baralho = Gera_Baralho(player1.deck, player2.deck)
    partida = GeraPartidaOnline(player1, player2, baralho, mapa)
    partida.ID = ID
    return partida

# -------------------------------
# Função que gerencia a tela de fila online
def Fila(tela, estados, relogio, Config):
    global DadosGerais

    # Inicia música de carregamento
    pygame.mixer.music.load('Audio/Musicas/Carregamento.ogg')
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play(-1)

    # Gera o jogador com base nas informações pré-selecionadas
    from PygameAções import informaçoesp1
    Jogador = Gerador_player(informaçoesp1)

    # Envia os dados do jogador para a API entrar na fila
    JogadorDados = Jogador.ToDic()
    resposta = requests.post(f"{Url}/entrar_partida", json=JogadorDados)
    data = resposta.json()

    # Gera animação de carregamento
    Gif = gerar_gif(Carregando_Frames, (1765, 930), 62)

    # Texto centralizado na tela
    texto = Fonte50.render("Carregando...", True, (255, 255, 255))
    pos_texto = (
        (1920 - texto.get_width()) // 2,
        (1080 - texto.get_height()) // 2
    )

    # -------------------------------
    # Thread para verificar pareamento com oponente
    def contata_servidor():
        global DadosGerais
        while True:
            try:
                if data["estado"] == "criou":
                    # Jogador criou a partida e aguarda oponente
                    resposta = requests.get(f"{Url}/buscar_jogador", json=data)
                    pronto = resposta.json()
                    if pronto["pronto"]:
                        partida_on = CriaPartidaOnline(Jogador, pronto["jogador2"], data["partida"])

                        # Posicionamento inicial dos pokémons no campo
                        partida_on.Jogador2.pokemons[0].local = [960, 570 - 600 // 2]
                        partida_on.Jogador1.pokemons[0].local = [960, 510 + 600 // 2]

                        # Envia estado inicial para o servidor
                        envio = {"partida": data["partida"], "dados": partida_on.anterior}
                        requests.post(f"{Url}/inicializar_partida", json=envio)

                        # Salva os dados localmente e inicia a partida
                        DadosGerais = [partida_on, 1]
                        A.Iniciar_partida_online(estados)
                        break  # Encerra a thread

                elif data["estado"] == "entrou":
                    # Jogador entrou em partida já existente
                    resposta = requests.post(f"{Url}/verificar_partida_criada", json={"partida": data["partida"]})
                    pronto = resposta.json()
                    if pronto["criada"]:
                        partida_on = GeraPartidaOnlineClone(pronto["estado"], data["partida"])
                        partida_on.Jogador2 = Jogador

                        # Posicionamento inicial dos pokémons no campo
                        partida_on.Jogador1.pokemons[0].local = [960, 570 - 600 // 2]
                        partida_on.Jogador2.pokemons[0].local = [960, 510 + 600 // 2]

                        DadosGerais = [partida_on, 2]
                        A.Iniciar_partida_online(estados)
                        break  # Encerra a thread
                time.sleep(3)  # Aguarda entre as verificações
            except Exception as e:
                print("Erro na thread contata_servidor:", e)
                time.sleep(5)  # Tempo de espera maior em caso de erro

    # Inicia a thread de pareamento
    threading.Thread(target=contata_servidor, daemon=True).start()

    # Loop da tela de espera (fila)
    while estados["Rodando_Fila"]:
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Fila"] = False
                estados["Rodando_Jogo"] = False

        # Fundo preto e elementos visuais
        tela.fill((0, 0, 0))
        tela.blit(texto, pos_texto)

        # Atualiza e desenha a animação de carregamento
        Gif.atualizar(tela)

        # Botão para sair da fila e voltar ao menu
        GV.Botao(
            tela, "Voltar", (0, 1020, 200, 60),
            CINZA, PRETO, AZUL,
            lambda: A.Voltar(estados),
            Fonte40, B1, 3, None, True, eventos
        )

        # Aplica claridade na tela e atualiza frame
        aplicar_claridade(tela, Config["Claridade"])
        pygame.display.update()
        relogio.tick(Config["FPS"])
