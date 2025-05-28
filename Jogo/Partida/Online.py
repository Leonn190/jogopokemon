import pygame
import random
import time 
import requests
import threading
from Visual.Imagens import Carregar_Imagens_Partida, Carrega_Gif_pokemon
from Visual.Mensagens import mensagens_passageiras
from Visual.Efeitos import gerar_gif, atualizar_efeitos
from Visual.Sonoridade import tocar
from Abas import Status_Pokemon,Inventario,Atacar, Loja
from Infos import TreinadorInfo
from Config import Configuraçoes, aplicar_claridade, aplicar_acinzentamento
from Jogo.Funções2 import verificar_serializabilidade
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

def obter_dados_partida(numero):
    url = "https://apipokemon-i9bb.onrender.com/estado_partida"
    nome = f"partida{numero}"
    resposta = requests.get(url, json={"partida": nome})

    if resposta.status_code != 200:
        print(f"Erro {resposta.status_code}: {resposta.text}")
        return None

    dados = resposta.json()

    try:
        resultado1 = dados["estado"]["partida"]
        resultado2 = dados["estado"]["jogador"]
        if isinstance(resultado1, dict):
            return resultado1, resultado2
        else:
            print("Os dados da partida não são um dicionário válido.")
            return None
    except (KeyError, TypeError):
        print("Formato inesperado da resposta:", dados)
        return None

def enviar_dados(partida_id):

    while True:
        dados_para_enviar = C.Partida.ToDic_Inic()

        envio = {"dados": dados_para_enviar, "partida": partida_id, "PassouVez": C.PassouVez}
        verificar_serializabilidade(envio)
        # Envia o estado atualizado da partida uma vez
        resposta = requests.post(
            "https://apipokemon-i9bb.onrender.com/atualizar_partida",
            json=envio
        )

        if C.PassouVez is True:
            C.PassouVez = False
            C.SuaVez = False
            C.comunicaçao = False
            C.ComputouPassagemVez = True
            break
        time.sleep(8)

def coletar_dados_loop(partida_id, ID):
    while True:
        try:
            Dados, JogadorDaVez = obter_dados_partida(1)
            print(Dados["tempo_restante"])
            nova_partida = GP.GeraPartidaOnlineClone(Dados, partida_id)
            C.atualizacoes_online.put(nova_partida)
        except Exception as e:
            print("Erro na coleta de dados online:", e)
        if JogadorDaVez == ID:
            C.DeveIniciarTurno = True
            break
        time.sleep(8)

def PartidaOnlineLoop(tela,estados,relogio,config):

    C.IniciaOnline(tela,config)

    while estados["Rodando_PartidaOnline"]:
        tela.fill(BRANCO)
        tela.blit(C.FundosIMG[C.Partida.Mapa.Fundo],(0,0))

        if C.SuaVez is not True:
            aplicar_acinzentamento(tela)

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
        
        if C.DeveIniciarTurno == True:
            C.DeveIniciarTurno = False
            C.IniciarTurno()

        if not C.comunicaçao:
            if C.SuaVez:
                threading.Thread(target=enviar_dados, args=(C.Partida.ID,)).start()
            else:
                threading.Thread(target=coletar_dados_loop, args=(C.Partida.ID, C.player.ID_online), daemon=True).start()
            C.comunicaçao = True

        if not C.atualizacoes_online.empty():
            try:
                nova = C.atualizacoes_online.get_nowait()
                
                ID_online_antigo = getattr(C.player, "ID_online", None)  # Salva antes de perder

                C.Partida = nova

                if ID_online_antigo == 1:
                    C.player = C.Partida.Jogador1
                    C.inimigo = C.Partida.Jogador2
                else:
                    C.inimigo = C.Partida.Jogador1
                    C.player = C.Partida.Jogador2

                # Reaplica o atributo que está faltando
                C.player.ID_online = ID_online_antigo

                print("Estado da partida atualizado com sucesso.")
            
            except Exception as e:
                print("Erro ao aplicar nova partida:", e)

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
