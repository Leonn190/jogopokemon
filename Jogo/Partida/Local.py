# Importações principais de bibliotecas e módulos do projeto
import pygame
import random

# Módulos visuais e de lógica do jogo
from Visual.Imagens import Carregar_Imagens_Partida, Carrega_Gif_pokemon
from Visual.Mensagens import mensagens_passageiras
from Visual.Efeitos import gerar_gif, atualizar_efeitos
from Visual.Sonoridade import tocar
from Abas import Status_Pokemon, Inventario, Atacar, Loja
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
    PRETO, BRANCO, CINZA, CINZA_ESCURO, AZUL, AZUL_CLARO, AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO, VERMELHO_CLARO, VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA, LARANJA_CLARO, ROXO, ROXO_CLARO, ROSA, DOURADO, PRATA, cores_raridade
)

# Variáveis globais da partida e interface
import Partida.Compartilhados as C
import Partida.Telas as T

# Loop principal da partida - executa enquanto a partida estiver ativa
def PartidaLoop(tela, estados, relogio, config):

    # Inicializa os elementos do jogo local (jogador, inimigo, mapa, etc.)
    C.IniciaLocal(tela, config)

    while estados["Rodando_Partida"]:
        # Limpa a tela com cor branca e desenha o fundo do mapa atual
        tela.fill(BRANCO)
        tela.blit(C.FundosIMG[C.Partida.Mapa.Fundo], (0, 0))

        # Ajusta volume da música de fundo conforme configurações
        pygame.mixer.music.set_volume(config["Volume"])

        # Captura todos os eventos (teclado, mouse, etc.)
        eventos = pygame.event.get()
        pos_mouse = pygame.mouse.get_pos()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                # Encerra o jogo se o jogador fechar a janela
                estados["Rodando_Partida"] = False
                estados["Rodando_Jogo"] = False

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Clique esquerdo
                    # Verifica se clicou sobre alguma peça móvel
                    for peca in C.Partida.Mapa.Peças:
                        if peca.pokemon.PodeMover:
                            if peca.iniciar_arraste(pos_mouse):
                                C.peca_em_uso = peca
                                break

            elif evento.type == pygame.MOUSEBUTTONUP:
                # Solta a peça que estava sendo arrastada
                if evento.button == 1 and C.peca_em_uso is not None:
                    C.peca_em_uso.soltar(pos_mouse)
                    C.peca_em_uso = None

        # Toca a música do estádio se necessário
        C.tocar_musica_do_estadio()

        # Se o jogo não estiver pausado, atualiza as telas de jogo
        if not C.Pausa:
            # Atualiza os elementos principais da interface
            T.TelaTabuleiro(tela, eventos, estados, config)
            T.TelaOpções(tela, eventos, estados, config)
            T.TelaOutros(tela, eventos, estados, config)
            T.TelaPokemons(tela, eventos, estados, config)

            # Desenha as peças no tabuleiro
            for peca in C.Partida.Mapa.Peças:
                if peca.pokemon.local is not None:
                    peca.desenhar(pos_mouse)

            # Desenha mensagens temporárias (ex: dano, buffs, etc.)
            for mensagem in mensagens_passageiras[:]:
                mensagem.desenhar(tela)
                mensagem.atualizar()
                if not mensagem.ativa:
                    mensagens_passageiras.remove(mensagem)

        else:
            # Se o jogo estiver pausado, exibe tela de pausa ou configurações
            if C.Config == False:
                tela.blit(C.FundosIMG[0], (0, 0))
                T.Telapausa(tela, eventos, estados, config)
            else:
                # Se a aba de configurações estiver aberta, exibe ela
                C.Config = Configuraçoes(tela, eventos, config)

        # Se o jogador estiver movendo uma peça, atualiza sua posição e mostra o raio de alcance
        if C.peca_em_uso is not None:
            C.peca_em_uso.atualizar_local_durante_arrasto(pos_mouse)
            C.peca_em_uso.desenhar_raio_velocidade()

        # Mostra o contador de FPS, se estiver ativado nas configurações
        if config["Mostrar Fps"]:
            tela.blit(
                pygame.font.SysFont(None, 36).render(f"FPS: {relogio.get_fps():.2f}", True, (255, 255, 255)),
                (1780, 55)
            )

        # Aplica efeito visual de claridade na tela, conforme configuração
        aplicar_claridade(tela, config["Claridade"])

        # Atualiza a tela
        pygame.display.update()

        # Limita a taxa de quadros por segundo conforme configurado
        relogio.tick(config["FPS"])