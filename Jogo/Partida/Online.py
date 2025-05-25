import pygame
import random
import requests
import threading
from Visual.Imagens import Carregar_Imagens_Partida, Carrega_Gif_pokemon
from Visual.Mensagens import mensagens_passageiras
from Visual.Efeitos import gerar_gif, atualizar_efeitos
from Visual.Sonoridade import tocar
from Abas import Status_Pokemon,Inventario,Atacar, Loja
from Infos import TreinadorInfo
from Config import Configuraçoes, aplicar_claridade
import Mapa as M
import Geradores.GeradorPlayer as GPA
import Geradores.GeradorPokemon as GPO
import Geradores.GeradorOutros as GO
import Geradores.GeradorPartida as GP
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte23, Fonte25, Fonte28, Fonte30, Fonte35, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA,CINZA_ESCURO, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA, cores_raridade)

import Partida.Compartilhados as C
import Partida.Telas as T


def enviar_diff(diff, partida_id, ID):
    requests.post(
        "https://apipokemon-i9bb.onrender.com/atualizar_partida",
        json={"diff": diff, "partida": partida_id, "ID Jogador": ID}
    )

def coletar_diffs(partida_id, ID, callback):
    resposta = requests.post(
        "https://apipokemon-i9bb.onrender.com/coletar_diffs",
        json={"partida": partida_id, "ID Jogador": ID}
    )
    diffs = resposta.json()
    callback(diffs)

def PartidaOnlineLoop(tela,estados,relogio,config):

    print (75)
    C.IniciaOnline(tela,config)
    print (5)

    while estados["Rodando_PartidaOnline"]:
        tela.fill(BRANCO)
        tela.blit(C.FundosIMG[C.Partida.Mapa.Fundo],(0,0))
        pygame.mixer.music.set_volume(config["Volume"])
        eventos = pygame.event.get()

        pos_mouse = pygame.mouse.get_pos()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_PartidaOnline"] = False
                estados["Rodando_Jogo"] = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Clique esquerdo
                    for peca in C.Partida.Mapa.Peças:
                        if peca.pokemon.PodeMover:
                            if peca.iniciar_arraste(pos_mouse):
                                C.peca_em_uso = peca
                                break

            elif evento.type == pygame.MOUSEBUTTONUP:
                if evento.button == 1 and C.peca_em_uso is not None:
                    C.peca_em_uso.soltar(pos_mouse)
                    C.peca_em_uso = None

        if C.SuaVez is True:
            diff = C.Partida.VerificaDiferença()
            threading.Thread(target=enviar_diff, args=(diff, C.Partida.ID, C.player.ID_online), daemon=True).start()
        else:
            # Possivel Bug de Multiplas Threads alterando a partida
            def processar_diffs(diffs):
                for diff in diffs:
                    C.Partida.atualizar(diff)

            threading.Thread(target=coletar_diffs, args=(C.Partida.ID, C.player.ID_online, processar_diffs), daemon=True).start()
        
        C.tocar_musica_do_estadio()

        if not C.Pausa:
            # Atualiza as telas do jogo
            T.TelaTabuleiro(tela, eventos, estados, config)
            T.TelaOpções(tela, eventos, estados, config)
            T.TelaOutros(tela, eventos, estados, config)
            T.TelaPokemons(tela, eventos, estados, config)

            # Desenha as peças
            for peca in C.Partida.Mapa.Peças:
                if peca.pokemon.local is not None:
                    peca.desenhar(pos_mouse)

            # Desenha mensagens passageiras
            for mensagem in mensagens_passageiras[:]:
                mensagem.desenhar(tela)
                mensagem.atualizar()
                if not mensagem.ativa:
                    mensagens_passageiras.remove(mensagem)
        else:
            if C.Config == False:
                tela.blit(C.FundosIMG[0], (0, 0))
                T.Telapausa(tela, eventos, estados, config)
            else:
                C.Config = Configuraçoes(tela,eventos,config)

        # Se tiver uma peça sendo usada, desenha o raio de alcance dela
        if C.peca_em_uso is not None:
            C.peca_em_uso.atualizar_local_durante_arrasto(pos_mouse)
            C.peca_em_uso.desenhar_raio_velocidade()

        if config["Mostrar Fps"]:
            tela.blit(pygame.font.SysFont(None, 36).render(f"FPS: {relogio.get_fps():.2f}", True, (255, 255, 255)), (1780, 55))

        aplicar_claridade(tela,config["Claridade"])
        pygame.display.update()
        relogio.tick(config["FPS"])
