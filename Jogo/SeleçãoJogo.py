# Importações principais de bibliotecas do jogo
import pygame
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Config import aplicar_claridade
from Visual.Sonoridade import tocar

# Importação de constantes visuais e fontes utilizadas na interface
from Visual.GeradoresVisuais import (
    Fonte15, Fonte23, Fonte30, Fonte40, Fonte50, Fonte60 ,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO, AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO, VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA, TexturasDic
)

# ======================= #
# DEFINIÇÃO DOS MODOS DE JOGO
# Cada modo é representado por um título e uma lista de descrições.
# ======================= #

TituloModoPadrao = "Modo Padrão"
DescricaoModoPadrao = [
    "- Modo clássico do jogo, Cada jogador escolhe seu deck válido e joga localmente",
    "- O pokémon inicial é escolhido no Pré-jogo, os demais são capturados em jogo",
    "- Tempo de jogo médio de 45 minutos, pausas param o relógio nesse modo",
    "- Vence quem alcançar a própria condição de vitória ou a de derrota do inimigo",
    "- Também é possível vencer nocauteando todos os pokémons inimigos",
    "- Todas as mecânicas de itens e energias permanecem inalteradas"
]
ModoPadrão = [TituloModoPadrao, DescricaoModoPadrao]

# Modo Online (semelhante ao padrão, mas com pausa contínua e testes em rede)
TituloModoOnline = "Modo Online"
DescricaoModoOnline = [
    "- Modo de jogo ainda em fase de testes, tecnicamente igual ao modo padrão",
    "- O pokémon inicial é escolhido no Pré-jogo, os demais são capturados em jogo",
    "- Tempo de jogo médio de 45 minutos, pausas não param o relógio nesse modo",
    "- Vence quem alcançar a própria condição de vitória ou a de derrota do inimigo",
    "- Também é possível vencer nocauteando todos os pokémons inimigos",
    "- Todas as mecânicas de itens e energias permanecem inalteradas"
]
ModoOnline = [TituloModoOnline, DescricaoModoOnline]

# Modo Aberto (sem decks, com modificadores e regras livres)
TituloModoAberto = "Modo Aberto"
DescricaoModoAberto = [
    "- O modo original do jogo, com modificadores que deixam o jogo mais longo",
    "- Sem decks: todos os pokémons e itens são liberados desde o início",
    "- Pokémons ganham menos XP, e sofrem menos dano",
    "- Ainda não disponível para jogar"
]
ModoAberto = [TituloModoAberto, DescricaoModoAberto]

# Modo Rápido (versão acelerada do modo padrão)
TituloModoRapido = "Modo Rápido"
DescricaoModoRapido = [
    "- Versão do modo padrão com tempo de jogo menor",
    "- Menos pokémons por jogador, menos tempo por turno",
    "- Pokémons ganham mais XP por turno",
    "- Ainda não disponível para jogar"
]
ModoRapido = [TituloModoRapido, DescricaoModoRapido]

# Modo Combate (mais rápido e direto, com itens e pokémons pré-definidos)
TituloModoCombate = "Modo Combate"
DescricaoModoCombate = [
    "- Todos os pokémons e itens são escolhidos no Pré-jogo",
    "- Sem energias ou treinadores. Ataques tem recarga",
    "- Dano aumentado, tempo de turno fixo (1 minuto)",
    "- Ainda não disponível para jogar"
]
ModoCombate = [TituloModoCombate, DescricaoModoCombate]

# Modo Personalizado (jogador configura as próprias regras)
TituloModoPersonalizado = "Modo Personalizado"
DescricaoModoPersonalizado = [
    "- Os jogadores definem todas as regras no Pré-jogo",
    "- Ainda não disponível para jogar"
]
ModoPersonalizado = [TituloModoPersonalizado, DescricaoModoPersonalizado]

# Armazena o modo atualmente selecionado (inicialmente nenhum)
ModoSelecionado = [None, None]

# ======================= #
# Funções de Controle da Seleção de Modo
# ======================= #

def SelecionaModo(Modo):
    """Ativa a seleção de um modo de jogo e toca um som de feedback."""
    global ModoSelecionado
    tocar("Seleciona")
    ModoSelecionado = Modo

def DesselecionaModo():
    """Cancela a seleção atual, limpando o modo ativo."""
    global ModoSelecionado
    ModoSelecionado = [None, None]

# ======================= #
# Painel Visual para Exibir Descrição do Modo
# ======================= #

def PainelModo(tela, pos, titulo, descricao, fonte_titulo, fonte_texto):
    """
    Renderiza um painel com o nome e a descrição do modo de jogo selecionado.
    
    Parâmetros:
    - tela: superfície do pygame onde será desenhado
    - pos: posição (x, y) do canto superior esquerdo do painel
    - titulo: string com o nome do modo
    - descricao: lista de strings com as regras e características
    - fonte_titulo: fonte usada para o título
    - fonte_texto: fonte usada para a descrição
    """
    x, y = pos
    largura = 820
    altura = 900

    # Cores do painel
    cor_fundo = (50, 50, 50)
    cor_divisoria = (0, 0, 0)
    cor_borda = (0, 0, 0)
    cor_texto = (255, 255, 255)

    # Fundo do painel
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 3)

    # Cabeçalho (6% da altura total)
    altura_cabecalho = int(altura * 0.06)
    pygame.draw.line(tela, cor_divisoria, (x, y + altura_cabecalho), (x + largura, y + altura_cabecalho), 2)

    # Título centralizado
    if titulo is not None:
        texto_titulo = fonte_titulo.render(titulo, True, cor_texto)
        rect_titulo = texto_titulo.get_rect(center=(x + largura // 2, y + altura_cabecalho // 2))
        tela.blit(texto_titulo, rect_titulo)

    # Descrição linha por linha
    espaco_entre_linhas = 30
    y_texto = y + altura_cabecalho + 22
    if descricao is not None:
        for linha in descricao:
            texto_linha = fonte_texto.render(linha, True, cor_texto)
            rect_linha = texto_linha.get_rect(center=(x + largura // 2, y_texto + texto_linha.get_height() // 2))
            tela.blit(texto_linha, rect_linha)
            y_texto += texto_linha.get_height() + espaco_entre_linhas

# ======================= #
# Botões de Controle e Estado do Menu de Modos
# ======================= #

B1 = {"estado": False}  # Estado de clique do botão "Jogar"
estadoModos = {"selecionado_esquerdo": None}  # Armazena qual modo está selecionado no menu

def TelaSeleção(tela, eventos, estados, Config):
    """
    Renderiza a tela de seleção de modo de jogo.
    Mostra os modos disponíveis e exibe detalhes sobre o modo atualmente selecionado.
    Permite ao jogador clicar em um modo e iniciar o jogo, caso ele esteja disponível.
    
    Parâmetros:
    - tela: superfície pygame onde tudo será desenhado
    - eventos: lista de eventos capturados do pygame (cliques, teclas, etc.)
    - estados: dicionário com os estados lógicos do jogo
    - Config: dicionário com as configurações atuais (volume, FPS, claridade, etc.)
    """
    global ModoSelecionado

    # Exibe o painel à direita com título e descrição do modo selecionado
    PainelModo(tela, (900, 120), ModoSelecionado[0], ModoSelecionado[1], Fonte60, Fonte30)

    # Lista dos modos disponíveis para seleção
    ListaModos = [ModoPadrão, ModoOnline, ModoAberto, ModoRapido, ModoCombate, ModoPersonalizado]

    # Cria um botão para cada modo
    for i in range(len(ListaModos)):
        y_base = 120 + i * 146  # Define a posição vertical com espaçamento entre botões

        # Cria o botão interativo de seleção de modo
        GV.Botao_Selecao(
            tela,
            (180, y_base, 540, 120),  # Posição e tamanho do botão
            ListaModos[i][0],  # Nome do modo como texto e identificador
            Fonte50,  # Fonte usada no botão
            cor_fundo=TexturasDic["FundoAzul"],
            cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE,
            cor_borda_direita=None,
            cor_passagem=AMARELO,
            id_botao=ListaModos[i][0],
            estado_global=estadoModos,  # Estado de seleção controlado externamente
            eventos=eventos,
            funcao_esquerdo=lambda modo=ListaModos[i]: SelecionaModo(modo),  # Seleciona o modo ao clicar
            funcao_direito=None,
            desfazer_esquerdo=DesselecionaModo,
            desfazer_direito=None,
            tecla_esquerda=pygame.K_1 + i,  # Atalho de teclado (teclas 1 a 6)
            tecla_direita=None
        )

    # Se algum modo foi selecionado
    if ModoSelecionado != [None, None]:
        if ModoSelecionado in [ModoPadrão, ModoOnline]:
            # Cria botão "Jogar" se for um modo disponível
            GV.Botao(
                tela, "Jogar", (1020, 860, 600, 130), TexturasDic["FundoAmarelo"],
                PRETO, DOURADO,
                lambda: A.iniciar_prépartida(estados, Config, ModoSelecionado[0]),
                Fonte70, B1, 4, None, True, eventos, "clique"
            )
        else:
            # Se for um modo ainda indisponível
            GV.Botao(
                tela, "Em breve...", (1020, 860, 600, 130), TexturasDic["FundoVermelho"],
                PRETO, DOURADO,
                lambda: tocar("Bloq"), Fonte70, B1, 4, None, True, eventos
            )
    else:
        # Se nenhum modo estiver selecionado
        GV.Botao(
            tela, "Escolha um Modo", (1020, 860, 600, 130), CINZA,
            PRETO, DOURADO,
            lambda: tocar("Bloq"), Fonte70, B1, 4, None, True, eventos
        )

    # Botão "Voltar" no canto inferior esquerdo
    GV.Botao(
        tela, "Voltar", (0, 1020, 200, 60), TexturasDic["FundoCinza"],
        PRETO, AZUL,
        lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos
    )


def Seleção(tela, estados, relogio, Config):
    """
    Controla o loop da tela de seleção de modo.
    Carrega a música de fundo, exibe o fundo da tela e atualiza os elementos gráficos.
    
    Parâmetros:
    - tela: superfície onde o conteúdo será desenhado
    - estados: dicionário com os estados principais do jogo
    - relogio: clock do pygame para controlar o FPS
    - Config: dicionário com as configurações do usuário
    """
    global ModoSelecionado

    # Toca música da tela de seleção
    pygame.mixer.music.load('Audio/Musicas/Sele.ogg')
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play(-1)  # -1 faz repetir infinitamente

    # Carrega o fundo da tela de seleção
    Fundo_Seleção = GV.Carregar_Imagem("imagens/fundos/FundoSeleção.jpg", (1920, 1080))

    # Limpa a seleção anterior, se houver
    DesselecionaModo()

    # Loop principal da tela de seleção
    while estados["Rodando_Seleção"]:
        tela.blit(Fundo_Seleção, (0, 0))  # Desenha o fundo

        eventos = pygame.event.get()  # Captura os eventos do pygame
        for evento in eventos:
            if evento.type == pygame.QUIT:
                # Se o jogador fechar a janela, encerra tudo
                estados["Rodando_Seleção"] = False
                estados["Rodando_Jogo"] = False

        # Atualiza os botões e painel da tela
        TelaSeleção(tela, eventos, estados, Config)

        # Aplica efeito de claridade se configurado
        aplicar_claridade(tela, Config["Claridade"])

        # Atualiza a tela e mantém FPS constante
        pygame.display.update()
        relogio.tick(Config["FPS"])