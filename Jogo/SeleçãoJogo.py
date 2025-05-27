import pygame
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Config import aplicar_claridade
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import (
    Fonte15, Fonte23, Fonte30, Fonte40, Fonte50, Fonte60 ,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA, TexturasDic)

TituloModoPadrao = "Modo Padrão"
DescriçaoModoPadrao = [
    "- Modo clássico do jogo, Cada jogador escolhe seu deck válido e joga localmente",
    "- O pokemon inicial é escolhido no Pré-jogo, os demais são capturados em jogo",
    "- Tempo de jogo médio de 45 minutos, pausas param o relógio nesse modo",
    "- Vence quem alcançar a própria condiçao de vitória ou a de derrota do inimigo",
    "- Também é possível vencer nocauteando todos os pokemons inimigos",
    "- Todas as mecânicas de itens e energias permanecem inalteradas"
]
ModoPadrão = [TituloModoPadrao, DescriçaoModoPadrao]

TituloModoOnline = "Modo Online"
DescriçaoModoOnline = [
    "- Modo de jogo ainda em fase de testes, técnicamente igual ao modo padrão",
    "- O pokemon inicial é escolhido no Pré-jogo, os demais são capturados em jogo",
    "- Tempo de jogo médio de 45 minutos, pausas não param o relógio nesse modo",
    "- Vence quem alcançar a própria condiçao de vitória ou a de derrota do inimigo",
    "- Também é possível vencer nocauteando todos os pokemons inimigos",
    "- Todas as mecânicas de itens e energias permanecem inalteradas"
]
ModoOnline = [TituloModoOnline, DescriçaoModoOnline]

TituloModoAberto = "Modo Aberto"
DescriçaoModoAberto = [
    "- O modo original do jogo, tendo modificadores que deixam o jogo mais longo",
    "- O pokemon inicial é escolhido no Pré-jogo, os demais são capturados em jogo",
    "- Tempo de jogo médio de 1 hora, pausas param o relógio nesse modo",
    "- Vence quem alcançar a própria condiçao de vitória ou a de derrota do inimigo",
    "- Também é possível vencer nocauteando todos os pokemons inimigos",
    "- Todas as mecânicas de itens e energias permanecem inalteradas",
    "- Pokemons ganham menos 1 de XP por turno apenas por estarem em campo",
    "- Todos os treinadores tem mais 10% de tempo para jogar o turno",
    "- Não temos decks nesse modo, todos os pokemons e itens são liberados",
    "- Pokemons Recebem menos 10% de dano ao serem atacados",
    "- Ainda não disponivel para jogar"
]
ModoAberto = [TituloModoAberto, DescriçaoModoAberto]

TituloModoRapido = "Modo Rapido"
DescriçaoModoRapido = [
    "- Funciona como o modo padrão com modificadores que deixam o jogo rapido",
    "- O pokemon inicial é escolhido no Pré-jogo, os demais são capturados em jogo",
    "- Tempo de jogo médio de 30 minutos, pausas param o relógio nesse modo",
    "- Vence quem alcançar a própria condiçao de vitória ou a de derrota do inimigo",
    "- Também é possível vencer nocauteando todos os pokemons inimigos",
    "- Todas as mecânicas de itens e energias permanecem inalteradas",
    "- Pokemons ganham mais 1 de XP por turno apenas por estarem em campo",
    "- Todos os treinadores tem menos 10% de tempo para jogar o turno",
    "- Em vez de 6 pokemons por jogador, teremos apenas 5 pokemons",
    "- Ainda não disponivel para jogar",
]
ModoRapido = [TituloModoRapido, DescriçaoModoRapido]

TituloModoCombate = "Modo Combate"
DescriçaoModoCombate = [
    "- O modo mais diferente até agora, sendo muito rapido",
    "- Todos os pokemons sao escolhidos no Pré-jogo, um de cada raridade",
    "- Os unicos itens que serão usados são os 10 adquiridos no Pré-jogo",
    "- Tempo de jogo médio 15 minutos, pausas param o relógio nesse modo",
    "- O jogo sempre termina no Turno 18, quem tiver mais pokemons vivos ganha",
    "- Pokemons ganham mais 2 de XP por turno apenas por estarem em campo",
    "- Alguns pokemons tem seu XP para evoluir alterados por conta de balanceamento",
    "- Vence quem derrotar todos os pokemons do oponente",
    "- Pokemons causam 20% de dano a mais em seus ataques",
    "- Sem treinadores, loja e energias; ataques tem turnos de recarga",
    "- Todo turno tem o tempo fixo de apenas 1 minuto",
    "- Qualquer item que permita o pokemon reviver está banido",
    "- Ainda não disponivel para jogar"
]
ModoCombate = [TituloModoCombate, DescriçaoModoCombate]

TituloModoPersonalizado = "Modo Personalizado"
DescriçaoModoPersonalizado = [
    "- Modo aberto para ser personalizado pelos jogadores",
    "- Todas as regras e modificadores são selecionados no Pré-jogo",
    "- Ainda não disponivel para jogar"
]
ModoPersonalizado = [TituloModoPersonalizado, DescriçaoModoPersonalizado]

ModoSelecionado = [None,None]

def SelecionaModo(Modo):
    global ModoSelecionado
    tocar("Seleciona")
    ModoSelecionado = Modo

def DesselecionaModo():
    global ModoSelecionado
    ModoSelecionado = [None,None]

def PainelModo(tela, pos, titulo, descricao, fonte_titulo, fonte_texto):
    x, y = pos
    largura = 820
    altura = 900
    cor_fundo = (50, 50, 50)
    cor_divisoria = (0, 0, 0)
    cor_borda = (0, 0, 0)
    cor_texto = (255, 255, 255)

    # Desenha o painel principal
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Desenha a borda
    pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 3)

    # Calcula a altura do cabeçalho (6% da altura total)
    altura_cabecalho = int(altura * 0.06)

    # Linha divisória abaixo do cabeçalho
    pygame.draw.line(tela, cor_divisoria, (x, y + altura_cabecalho), (x + largura, y + altura_cabecalho), 2)

    # Desenha o título centralizado no cabeçalho
    if titulo is not None:
        texto_titulo = fonte_titulo.render(titulo, True, cor_texto)
        rect_titulo = texto_titulo.get_rect(center=(x + largura // 2, y + altura_cabecalho // 2))
        tela.blit(texto_titulo, rect_titulo)

    # Desenha a descrição centralizada no corpo do painel
    espaco_entre_linhas = 30
    y_texto = y + altura_cabecalho + 22

    if descricao is not None:
        for linha in descricao:
            texto_linha = fonte_texto.render(linha, True, cor_texto)
            rect_linha = texto_linha.get_rect(center=(x + largura // 2, y_texto + texto_linha.get_height() // 2))
            tela.blit(texto_linha, rect_linha)
            y_texto += texto_linha.get_height() + espaco_entre_linhas

B1 = {"estado": False}

estadoModos = {"selecionado_esquerdo": None}

def TelaSeleção(tela,eventos,estados,Config):
    global ModoSelecionado

    PainelModo(tela,(900, 120),ModoSelecionado[0],ModoSelecionado[1],Fonte60,Fonte30)

    ListaModos = [ModoPadrão, ModoOnline, ModoAberto, ModoRapido, ModoCombate, ModoPersonalizado]

    for i in range(len(ListaModos)):
        y_base = 120 + i * 146 
        
        GV.Botao_Selecao(
            tela,
            (180, y_base, 540, 120),  # Posição com y dinâmico
            ListaModos[i][0],
            Fonte50,
            cor_fundo=TexturasDic["FundoAzul"],
            cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE,
            cor_borda_direita=None,
            cor_passagem=AMARELO,
            id_botao=ListaModos[i][0],  # Corrigido para pegar o nome certo
            estado_global=estadoModos,
            eventos=eventos,
            funcao_esquerdo=lambda modo=ListaModos[i]: SelecionaModo(modo),  # Corrigido scoping da lambda
            funcao_direito=None,
            desfazer_esquerdo=DesselecionaModo,
            desfazer_direito=None,
            tecla_esquerda=pygame.K_1 + i,  # Teclas 1, 2, 3 etc.
            tecla_direita=None
        )
    if ModoSelecionado != [None,None]:
        if ModoSelecionado in [ModoPadrão, ModoOnline]:
            GV.Botao(tela, "Jogar", (1020, 860, 600, 130), TexturasDic["FundoAmarelo"], PRETO, DOURADO,
                        lambda: A.iniciar_prépartida(estados, Config, ModoSelecionado[0]), Fonte70, B1, 4, None, True, eventos,"clique")
        else:
            GV.Botao(tela, "Em breve...", (1020, 860, 600, 130), TexturasDic["FundoVermelho"], PRETO, DOURADO,
                        lambda: tocar("Bloq"), Fonte70, B1, 4, None, True, eventos,)
    else:
        GV.Botao(tela, "Escolha um Modo", (1020, 860, 600, 130), CINZA, PRETO, DOURADO,
                    lambda: tocar("Bloq"), Fonte70, B1, 4, None, True, eventos,)
        

    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), TexturasDic["FundoCinza"], PRETO, AZUL,
                 lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)

def Seleção(tela,estados,relogio,Config):
    global ModoSelecionado

    pygame.mixer.music.load('Audio/Musicas/Sele.ogg')
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play(-1)

    Fundo_Seleção = GV.Carregar_Imagem("imagens/fundos/FundoSeleção.jpg", (1920,1080))


    DesselecionaModo()
    while estados["Rodando_Seleção"]:
        tela.blit(Fundo_Seleção, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Seleção"] = False
                estados["Rodando_Jogo"] = False

        TelaSeleção(tela,eventos,estados,Config)

        aplicar_claridade(tela,Config["Claridade"])
        pygame.display.update()
        relogio.tick(Config["FPS"])