# Importações de bibliotecas internas do jogo
import pygame
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Config import aplicar_claridade

# Importação de constantes visuais e fontes usadas na interface
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO, AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO, VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,
)

# Estado do botão, usado para controle de cliques e animações
B1 = {"estado": False}

# Função Final - Exibe a tela de vitória ao final da partida
def Final(tela, estados, relogio, Config):

    # Carrega imagens de fundo
    Fundo_pré = GV.Carregar_Imagem("imagens/fundos/Fundo1.jpg", (1920, 1080))
    Carregar = GV.Carregar_Imagem("imagens/fundos/carregando.jpg", (1920, 1080))

    # Exibe tela de carregamento temporária
    tela.blit(Carregar, (0, 0))
    fonte = pygame.font.SysFont(None, 70)
    texto = fonte.render("Carregando ...", True, PRETO)
    tela.blit(texto, (tela.get_width() // 2 - 200, tela.get_height() // 2))
    pygame.display.update()

    # Toca música de transição ("pos.ogg") por ~8,8 segundos
    pygame.mixer.music.load('Audio/Musicas/pos.ogg')  
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play(-1)
    pygame.time.wait(8800)

    # Carrega e inicia a música de resultados após a transição
    pygame.mixer.music.load('Audio/Musicas/resultados.ogg')  
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play()

    # Define que a música, ao terminar, enviará um evento USEREVENT
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

    # Importa variáveis globais compartilhadas da partida
    import Partida.Compartilhados as C

    # Loop principal da tela final (executa enquanto Rodando_Final for True)
    while estados["Rodando_Final"]:
        tela.blit(Fundo_pré, (0, 0))  # Fundo da tela final
        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                # Sai do jogo se clicar no botão fechar
                estados["Rodando_Final"] = False
                estados["Rodando_Jogo"] = False

            elif evento.type == pygame.USEREVENT:
                # Quando a música terminar, volta a tocar a música do menu
                pygame.mixer.music.load('Audio/Musicas/Menu.ogg')
                pygame.mixer.music.play()

        # Exibe mensagem de vitória com nome do vencedor
        GV.Texto_caixa(
            tela,
            f"{C.Partida.Vencedor.nome} Venceu, Parabens!",
            (450, 200, 1020, 260),
            Fonte70,
            DOURADO,
            PRETO,
            4  # Espessura da borda
        )

        # Botão para sair completamente do jogo
        GV.Botao(
            tela, "Sair do jogo", (300, 400, 320, 80),
            CINZA, PRETO, AZUL,
            lambda: A.fechar_jogo(estados),
            Fonte50, B1, 3, pygame.K_ESCAPE, False, eventos
        )

        # Botão para voltar ao menu inicial do jogo
        GV.Botao(
            tela, "Voltar para o inicio", (700, 600, 520, 150),
            CINZA, PRETO, DOURADO,
            lambda: A.Voltar(estados),
            Fonte70, B1, 4, None, True, eventos,
            "clique"
        )

        # Aplica o efeito de claridade baseado nas configurações do jogador
        aplicar_claridade(tela, Config["Claridade"])

        # Atualiza a tela com todos os elementos renderizados
        pygame.display.update()

        # Controla a taxa de atualização da tela (FPS)
        relogio.tick(Config["FPS"])
