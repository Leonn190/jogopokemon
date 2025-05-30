# Importações principais do Pygame e bibliotecas do projeto
import pygame
import random

# Importações dos módulos visuais e funcionais do jogo
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

# Importações específicas de fontes, cores e texturas para uso nos botões e elementos visuais
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte23, Fonte25, Fonte28, Fonte30, Fonte35, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA, CINZA_ESCURO, AZUL, AZUL_CLARO, AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO, VERMELHO_CLARO, VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA, LARANJA_CLARO, ROXO, ROXO_CLARO, ROSA, DOURADO, PRATA, cores_raridade, TexturasDic
)

# Importa constantes e variáveis globais compartilhadas
import Partida.Compartilhados as C

# Função principal responsável por desenhar a tela de escolha e ações dos pokémons
def TelaPokemons(tela, eventos, estados, config):

    # Verifica se algum pokémon inimigo está com o efeito "Provocando" ativo
    for pokemon in C.inimigo.pokemons:
        if pokemon.efeitosPosi["Provocando"] > 0:
            C.provocar = True

    # Atualiza e verifica exibição de GIFs ativos
    C.VerificaGIF(C.player, C.inimigo)

    # Calcula o valor vertical animado para botões (usado para animação de posição Y)
    YO = GV.animar(C.OP1, C.OP2, C.animaOP, tempo=250)

    # Caso seja a vez do jogador e a passagem de vez já tenha sido computada
    if C.SuaVez is True and C.ComputouPassagemVez is True:
        # Botão "Atacar" - habilitado se o Pokémon pode atacar
        try:
            if C.PokemonS.PodeAtacar == True:
                GV.Botao(tela, "Atacar", (1570, YO, 340, 50), TexturasDic["FundoAtacar"], PRETO, AZUL,
                         lambda: Atacar(C.PokemonS, C.PokemonV, C.PokemonA, C.player, C.inimigo, C.Partida.Mapa, tela, C.Partida.Baralho),
                         Fonte40, C.B22, 3, None, True, eventos)
            else:
                GV.Botao(tela, "Atacar", (1570, YO, 340, 50), (123, 138, 148), PRETO, AZUL,
                         lambda: tocar("Bloq"), Fonte40, C.B22, 3, None, True, eventos)
        except AttributeError:
            # Caso o Pokémon selecionado seja inválido
            GV.Botao(tela, "Atacar", (1570, YO, 340, 50), (123, 138, 148), PRETO, AZUL,
                     lambda: tocar("Bloq"), Fonte40, C.B22, 3, None, True, eventos)

        # Botão "Evoluir" - só aparece se o Pokémon puder evoluir
        try:
            if C.PokemonS.PodeEvoluir == True:
                GV.Botao(tela, "Evoluir", (1570, YO + 50, 340, 50), TexturasDic["FundoEvolui"], PRETO, AZUL,
                         lambda: C.PokemonS.evoluir(C.player), Fonte40, C.B22, 3, None, True, eventos)
            else:
                GV.Botao(tela, "Evoluir", (1570, YO + 50, 340, 50), (123, 138, 148), PRETO, AZUL,
                         lambda: tocar("Bloq"), Fonte40, C.B22, 3, None, True, eventos)
        except AttributeError:
            GV.Botao(tela, "Evoluir", (1570, YO + 50, 340, 50), (123, 138, 148), PRETO, AZUL,
                     lambda: tocar("Bloq"), Fonte40, C.B22, 3, None, True, eventos)

        # Botão "Guardar" ou "Posicionar"
        try:
            if C.PokemonS.local != []:
                GV.Botao(tela, "Guardar", (1570, YO + 100, 340, 50), TexturasDic["FundoGuardar"], PRETO, AZUL,
                         lambda: M.PosicionarGuardar(C.PokemonS, 2), Fonte40, C.B23, 3, None, True, eventos)
            else:
                if C.PokemonS.guardado > 0:
                    GV.Botao(tela, f"Posicione em {C.PokemonS.guardado} turnos", (1570, YO + 100, 340, 50),
                             (123, 138, 148), PRETO, AZUL, lambda: tocar("Bloq"), Fonte40, C.B23, 3, None, True, eventos)
                else:
                    GV.Botao(tela, "Posicionar", (1570, YO + 100, 340, 50), TexturasDic["FundoGuardar"], PRETO, AZUL,
                             lambda: M.PosicionarGuardar(C.PokemonS, 0), Fonte40, C.B23, 3, None, True, eventos)
        except AttributeError:
            pass

    # Renderiza botões dos 6 pokémons do jogador (embaixo)
    for i in range(6):
        x = 420 + i * 190
        if len(C.player.pokemons) > i:
            id_poke = C.player.pokemons[i]
        else:
            id_poke = f"A{i}"
        # Define fundo diferente se o pokémon já atacou
        if not isinstance(id_poke, str) and id_poke.atacou == True:
            cor_do_fundo_pokemon = (123, 138, 148)
        else:
            cor_do_fundo_pokemon = TexturasDic["FundoPokemonAliado"]

        # Botão de seleção com função de ataque ou visualização
        GV.Botao_Selecao2(
            tela, (x, 890, 190, 190), "", Fonte30,
            cor_fundo=cor_do_fundo_pokemon, cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE, cor_borda_direita=AZUL, cor_passagem=AMARELO,
            id_botao=id_poke,
            estado_global_esquerdo=C.estadoPokemon, estado_global_direito=C.estadoVisualiza, eventos=eventos,
            funcao_esquerdo=lambda i=i: C.seleciona(id_poke),
            funcao_direito=lambda i=i: C.visualiza(id_poke),
            desfazer_esquerdo=lambda: C.desseleciona(),
            desfazer_direito=lambda: C.oculta(), tecla_esquerda=pygame.K_1, tecla_direita=None, som="clique"
        )

    # Renderiza botões dos 6 pokémons do inimigo (em cima)
    for i in range(6):
        x = 1310 - i * 190
        if len(C.inimigo.pokemons) > i:
            id_poke = C.inimigo.pokemons[i]
        else:
            id_poke = f"I{i}"
        GV.Botao_Selecao2(
            tela, (x, 0, 190, 190), "", Fonte30,
            cor_fundo=TexturasDic["FundoPokemonInimigo"], cor_borda_normal=PRETO,
            cor_borda_esquerda=VERMELHO, cor_borda_direita=AZUL, cor_passagem=AMARELO,
            id_botao=id_poke,
            estado_global_esquerdo=C.estadoAlvo, estado_global_direito=C.estadoVisualiza, eventos=eventos,
            funcao_esquerdo=lambda i=i: C.selecionaAlvo(id_poke),
            funcao_direito=lambda i=i: C.visualiza(id_poke),
            desfazer_esquerdo=lambda: C.desselecionaAlvo(),
            desfazer_direito=lambda: C.oculta(), tecla_esquerda=pygame.K_1, tecla_direita=None, som="clique"
        )

        # Mostra ícones de efeitos positivos e negativos ao lado dos pokémons inimigos
        if not isinstance(id_poke, str):
            j = 0
            for efeito, valor in id_poke.efeitosPosi.items():
                if valor > 0:
                    GV.Efeito(tela, (x + 150, 30 + j * 30), C.EfeitosIMG[efeito], VERDE, valor)
                    j += 1
            for efeito, valor in id_poke.efeitosNega.items():
                if valor > 0:
                    GV.Efeito(tela, (x + 150, 30 + j * 30), C.EfeitosIMG[efeito], VERMELHO, valor)
                    j += 1

    # Desenha as barras de vida de cada pokémon (modo local ou online)
    if C.Partida.online is not True:
        for i in range(len(C.player.pokemons)):
            C.barra_vida(tela, 425 + i * 190, 875, 180, 15, C.player.pokemons[i].Vida, C.player.pokemons[i].VidaMax,
                         (100, 100, 100), C.player.pokemons[i].ID, C.player.pokemons[i].barreira)
        for i in range(len(C.inimigo.pokemons)):
            C.barra_vida(tela, 1315 - i * 190, 190, 180, 15, C.inimigo.pokemons[i].Vida, C.inimigo.pokemons[i].VidaMax,
                         (100, 100, 100), C.inimigo.pokemons[i].ID, C.inimigo.pokemons[i].barreira)
    else:
        for i in range(len(C.player.pokemons)):
            C.barra_vida_simples(tela, 425 + i * 190, 875, 180, 15, C.player.pokemons[i].Vida, C.player.pokemons[i].VidaMax,
                                 (100, 100, 100), C.player.pokemons[i].barreira)
        for i in range(len(C.inimigo.pokemons)):
            C.barra_vida_simples(tela, 1315 - i * 190, 190, 180, 15, C.inimigo.pokemons[i].Vida, C.inimigo.pokemons[i].VidaMax,
                                 (100, 100, 100), C.inimigo.pokemons[i].barreira)

    # Armazena as seleções de pokémon (selecionado e visualizado)
    if C.PokemonS is not None:
        C.PokemonSV = C.PokemonS
    if C.PokemonV is not None:
        C.PokemonVV = C.PokemonV

    # Animações e exibição da ficha de status do Pokémon selecionado
    XstatusS = GV.animar(C.S1, C.S2, C.animaS)
    if XstatusS != 1920:
        Status_Pokemon((XstatusS, 502), tela, C.PokemonSV, C.TiposEnergiaIMG, C.player, eventos, "S", C.Partida.Mapa, C.PokemonA)

    # Animações e exibição da ficha de status do alvo visualizado
    XstatusV = GV.animar(C.V1, C.V2, C.animaV)
    if XstatusV != 1920:
        Status_Pokemon((XstatusV, 115), tela, C.PokemonVV, C.TiposEnergiaIMG, C.player, eventos, "V", C.Partida.Mapa, C.PokemonA)

        # Tenta atualizar o objeto "alvo" caso ele esteja ativo e possua o método de atualização
    try:
        if C.alvo.ativo:
            C.alvo.atualizar(tela)
    except AttributeError:
        pass  # Caso C.alvo não exista ou não tenha o atributo 'ativo'

    # Tempo atual (em milissegundos) desde o início do jogo
    agora = pygame.time.get_ticks()

    # Atualiza e desenha os GIFs dos Pokémons do jogador
    for i in range(len(C.player.pokemons)):
        nome = C.player.pokemons[i].nome
        # Encontra o GIF correspondente ao Pokémon pelo nome
        gif = next(g for g in C.Gifs_ativos if g["nome"] == nome)

        # Troca de frame se passou o intervalo
        if agora - gif["tempo_anterior"] > gif["intervalo"]:
            gif["frame_atual"] = (gif["frame_atual"] + 1) % len(gif["frames"])
            gif["tempo_anterior"] = agora

        frame = gif["frames"][gif["frame_atual"]]

        # Calcula a posição do quadrado do Pokémon
        x = 420 + i * 190
        y = 890

        # Centraliza o frame no quadrado de 190x190
        pos_x = x + (190 - frame.get_width()) // 2
        pos_y = y + (190 - frame.get_height()) // 2

        # Desenha o frame do GIF
        tela.blit(frame, (pos_x, pos_y))

        # Se o Pokémon estiver fora do campo (não posicionado), exibe ícone especial
        if C.player.pokemons[i].local == []:
            tela.blit(C.OutrosIMG[11], ((x + 10), (y + 10)))

    # Atualiza e desenha os GIFs dos Pokémons inimigos (posição invertida no eixo X)
    for i in range(len(C.inimigo.pokemons)):
        nome = C.inimigo.pokemons[i].nome
        gif = next(g for g in C.Gifs_ativos if g["nome"] == nome)

        if agora - gif["tempo_anterior"] > gif["intervalo"]:
            gif["frame_atual"] = (gif["frame_atual"] + 1) % len(gif["frames"])
            gif["tempo_anterior"] = agora

        frame = gif["frames"][gif["frame_atual"]]

        x = 1305 - i * 190
        y = 5

        pos_x = x + (190 - frame.get_width()) // 2
        pos_y = y + (190 - frame.get_height()) // 2

        tela.blit(frame, (pos_x, pos_y))

        if C.inimigo.pokemons[i].local == []:
            tela.blit(C.OutrosIMG[11], ((x + 15), (y + 10)))

    # Mostra ícones e descrições de efeitos nos Pokémons do jogador
    for Pokemon in C.player.pokemons:
        j = 0
        x = 420 + Pokemon.pos * 190
        for efeito, valor in Pokemon.efeitosPosi.items():
            if valor > 0:
                GV.Efeito(tela, (x + 160, 920 + j * 30), C.EfeitosIMG[efeito], VERDE, valor)
                GV.tooltip((x + 146, 906 + j * 30, 28, 28), (x + 10, 810, 170, 60),
                        C.player.pokemons[0].descrição[efeito], efeito, Fonte20, Fonte28, tela)
                j += 1
        for efeito, valor in Pokemon.efeitosNega.items():
            if valor > 0:
                GV.Efeito(tela, (x + 160, 920 + j * 30), C.EfeitosIMG[efeito], VERMELHO, valor)
                GV.tooltip((x + 146, 906 + j * 30, 28, 28), (x + 10, 810, 170, 60),
                        C.player.pokemons[0].descrição[efeito], efeito, Fonte20, Fonte28, tela)
                j += 1

    # Mostra ícones e descrições de efeitos nos Pokémons inimigos
    for Pokemon in C.inimigo.pokemons:
        j = 0
        x = 1310 - Pokemon.pos * 190
        for efeito, valor in Pokemon.efeitosPosi.items():
            if valor > 0:
                GV.Efeito(tela, (x + 150, 30 + j * 30), C.EfeitosIMG[efeito], VERDE, valor)
                GV.tooltip((x + 136, 16 + j * 30, 28, 28), (x + 10, 210, 170, 60),
                        C.player.pokemons[0].descrição[efeito], efeito, Fonte20, Fonte28, tela)
                j += 1
        for efeito, valor in Pokemon.efeitosNega.items():
            if valor > 0:
                GV.Efeito(tela, (x + 150, 30 + j * 30), C.EfeitosIMG[efeito], VERMELHO, valor)
                GV.tooltip((x + 136, 16 + j * 30, 28, 28), (x + 10, 210, 170, 60),
                        C.player.pokemons[0].descrição[efeito], efeito, Fonte20, Fonte28, tela)
                j += 1

    # Atualiza todos os efeitos visuais do campo
    atualizar_efeitos(tela)

    # Verifica se algum Pokémon foi derrotado ou está em situação especial
    GPO.VerificaSituaçãoPokemon(C.player, C.inimigo, C.Partida.Mapa)

    # ---------------------------------------------
    # FUNÇÃO: TelaOpções
    # ---------------------------------------------
    # Mostra o painel lateral com nome, ouro e botões de acesso às abas do jogo
def TelaOpções(tela, eventos, estados, config):

    # Anima a altura Y do painel de opções
    YT = GV.animar(C.T1, C.T2, C.animaT, 300)

    # Botão para abrir o terminal de comandos
    GV.Botao(tela, "", (0, YT, 420, 50), PRETO, PRETO, PRETO,
             lambda: C.Troca_Terminal(), Fonte40, C.B24, 3, None, True, eventos)

    # Mostra o valor de ouro do jogador
    GV.Texto_caixa(tela, f"{C.player.ouro}", (280, (YT - 60), 140, 60), Fonte40, LARANJA, PRETO)

    # Mostra o nome do jogador
    GV.Texto_caixa(tela, C.player.nome, (0, YT, 420, 50), Fonte50, AZUL, PRETO)

    # Caixa de terminal para mensagens
    GV.Terminal(tela, (0, (YT + 50), 420, 230), Fonte23, TexturasDic["FundoTerminal"], PRETO)

    # Nomes dos botões das abas do jogo
    nomes_botoes_outros = ["Inventario", "Centro", "Treinador", "Estadio"]

    # Cria os botões de acesso às abas secundárias
    for i, nome in enumerate(nomes_botoes_outros):
        GV.Botao_Selecao(
            tela, (i * 70, (YT - 60), 70, 60), "", Fonte30,
            cor_fundo=TexturasDic["FundoOpçoes"], cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE, cor_borda_direita=None,
            cor_passagem=AMARELO, id_botao=nome,
            estado_global=C.estadoOutros, eventos=eventos,
            funcao_esquerdo=lambda nome=nome: C.Abre(nome, C.player, C.inimigo),
            funcao_direito=None,
            desfazer_esquerdo=lambda: C.Fecha(), desfazer_direito=None,
            tecla_esquerda=pygame.K_1, tecla_direita=None)

    # Desenha os ícones de cada botão de forma precisa para evitar desalinhamentos
    tela.blit(C.OutrosIMG[0], (5, (YT - 60)))     # Inventario
    tela.blit(C.OutrosIMG[2], (69, (YT - 65)))    # Centro Pokémon
    tela.blit(C.OutrosIMG[13], (150, (YT - 55)))  # Treinador
    tela.blit(C.OutrosIMG[3], (217, (YT - 58)))   # Estádio

        # Verifica se houve mudança na aba lateral (Inventário, Centro, Treinador, Estádio)
    if C.EstadoOutrosAtual != C.estadoOutros["selecionado_esquerdo"]:
        C.EstadoOutrosAtual = C.estadoOutros["selecionado_esquerdo"]
        if C.estadoOutros["selecionado_esquerdo"] == None:
            # Fecha animação lateral (Aba Lateral - AL)
            if C.A8 == 1:
                C.A7 = 1
                C.A8 = -480
                C.animaAL = pygame.time.get_ticks()

    # Anima e exibe a aba de Inventário, se estiver aberta
    XInvetario = GV.animar(C.A1, C.A2, C.animaAI)
    if XInvetario != -385:
        Inventario((XInvetario, 310), tela, C.player, C.ImagensItens, C.estadoItens, eventos, C.PokemonS,
                C.Partida.Mapa, C.Partida.Baralho, C.estadoEnergias)

    # Anima e exibe a aba do Centro Pokémon
    XCentro = GV.animar(C.A5, C.A6, C.animaAC)
    if XCentro != -385:
        C.Centroo(tela, XCentro, 310, C.Partida.Centro, C.player, Fonte50, Fonte28, C.B6, C.estadoPokebola,
                C.estadoFruta, eventos)

    # Anima e exibe a aba do Treinador
    XTreinador = GV.animar(C.A3, C.A4, C.animaAT)
    if XTreinador != -385:
        TreinadorInfo((XTreinador, 310), tela, C.player.treinador, C.ImagensFichas, "P", C.player)

    # Exibe dicas (tooltips) se estiverem ativadas nas configurações
    if config["Dicas"]:
        GV.tooltip((280, (YT - 60), 140, 60), (30, (YT - 130), 360, 70),
                "Quanto mais fizer sua jogada, mais ouro vai ganhar",
                f"Ganho Atual {2 + (C.Partida.tempo_restante // 25)}", Fonte25, Fonte35, tela)
        GV.tooltip((210, (YT - 60), 70, 60), (30, (YT - 130), 360, 70),
                "Veja quais são as mudanças e as características do estádio atual", "Estádio", Fonte25, Fonte35, tela)
        GV.tooltip((140, (YT - 60), 70, 60), (30, (YT - 130), 360, 70),
                "Veja quais são as características do seu apoiador", "Apoiador", Fonte25, Fonte35, tela)
        GV.tooltip((70, (YT - 60), 70, 60), (30, (YT - 130), 360, 70),
                "Veja os pokémons que podem ser capturados", "Centro", Fonte25, Fonte35, tela)
        GV.tooltip((0, (YT - 60), 70, 60), (30, (YT - 130), 360, 70),
                "Veja suas energias e seus itens, podendo usá-los", "Inventário", Fonte25, Fonte35, tela)

# ---------------------------------------------
# FUNÇÃO: TelaOutros - Tela de ações extras durante a partida
# ---------------------------------------------
def TelaOutros(tela, eventos, estados, config):
    # Botão de Pausar/Despausar (modo local ou online)
    if C.Partida.online is False:
        GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: C.pausarEdespausar(), Fonte50, C.B1, 3, pygame.K_ESCAPE, False, eventos)
    else:
        GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,
                 lambda: C.PausarOnline(), Fonte50, C.B1, 3, pygame.K_ESCAPE, False, eventos)

    # Botão para mutar/desmutar sons
    GV.Botao(tela, "", (300, 400, 320, 80), CINZA, PRETO, AZUL,
             lambda: C.Muter(), Fonte50, C.B1, 3, pygame.K_m, False, eventos)

    # Botão para passar o turno (regras diferentes em online/local)
    if C.Partida.online is True:
        if C.SuaVez is True and C.ComputouPassagemVez:
            GV.Botao(tela, "Passar Turno", (10, 90, 340, 50), AMARELO_CLARO, PRETO, AZUL,
                     lambda: C.PassarTurnoOnline(estados), Fonte40, C.B7, 3, None, True, eventos)
        else:
            GV.Botao(tela, "Passar Turno", (10, 90, 340, 50), AMARELO_CLARO, PRETO, AZUL,
                     lambda: C.Invalido, Fonte40, C.B7, 3, None, True, eventos)
    else:
        GV.Botao(tela, "Passar Turno", (10, 90, 340, 50), AMARELO_CLARO, PRETO, AZUL,
                 lambda: C.passar_turno(estados), Fonte40, C.B7, 3, None, True, eventos)

    # Mostra o número do turno atual
    GV.Texto_caixa(tela, f"Turno: {C.Partida.Turno}", (0, 0, 360, 60), Fonte70, AMARELO, PRETO)

    # Painel lateral com informações do treinador inimigo (animado)
    YTI = GV.animar(C.TI1, C.TI2, C.animaTI, 450)
    if YTI != 0:
        pygame.draw.rect(tela, PRETO, (1500, YTI - 430, 420, 430))
        TreinadorInfo((1520, YTI - 420), tela, C.inimigo.treinador, C.ImagensFichas, "P", C.inimigo)

    # Botão para alternar terminal do inimigo
    GV.Botao(tela, "", (1500, YTI, 420, 50), PRETO, PRETO, PRETO,
             lambda: C.Troca_Terminal_Inimigo(), Fonte40, C.B24, 3, None, True, eventos)

    # Nome do treinador inimigo
    GV.Texto_caixa(tela, C.inimigo.nome, (1500, YTI, 420, 50), Fonte50, VERMELHO_CLARO, PRETO)

    # Cronômetro da vez do jogador ou do oponente (dependendo do modo)
    if C.Partida.online is True:
        if C.SuaVez is True and C.ComputouPassagemVez:
            C.cronometro(tela, (0, 60, 360, 30), C.player.tempo, Fonte40, CINZA, PRETO, AMARELO,
                         lambda: C.PassarTurnoOnline(estados), C.Partida.Turno)
        else:
            C.cronometro_falso(tela, (0, 60, 360, 30), C.Partida.tempo_restante, C.inimigo.tempo,
                               Fonte40, CINZA, PRETO, AMARELO)
    else:
        C.cronometro(tela, (0, 60, 360, 30), C.player.tempo, Fonte40, CINZA, PRETO, AMARELO,
                     lambda: C.passar_turno(estados), C.Partida.Turno)

    # Exibe a loja (animação lateral)
    XL = GV.animar(C.A7, C.A8, C.animaAL)
    Loja((XL, 195), tela, C.Partida.Baralho, C.ImagensItens, C.Partida.Turno, eventos, C.player, 2, C.Partida.Loja)

# ---------------------------------------------
# FUNÇÃO: Telapausa - Tela exibida ao pausar o jogo
# ---------------------------------------------
def Telapausa(tela, eventos, estados, config):
    GV.Botao(tela, "Despausar partida", (600, 160, 720, 130), TexturasDic["FundoPausa"],
             PRETO, AZUL, lambda: C.pausarEdespausar(), Fonte70, C.B6, 5, pygame.K_ESCAPE, True, eventos)

    GV.Botao(tela, "Configurações", (600, 385, 720, 130), TexturasDic["FundoPausa"],
             PRETO, AZUL, lambda: C.TrocaConfig(), Fonte70, C.B6, 5, None, True, eventos)

    GV.Botao(tela, "Sair da partida", (600, 610, 720, 130), TexturasDic["FundoPausa"],
             PRETO, AZUL, lambda: A.Voltar(estados), Fonte70, C.B6, 5, None, True, eventos)

    GV.Botao(tela, "Sair do jogo", (600, 835, 720, 130), TexturasDic["FundoPausa"],
             PRETO, AZUL, lambda: A.fechar_jogo(estados), Fonte70, C.B6, 5, None, True, eventos)

# ---------------------------------------------
# FUNÇÃO: TelaTabuleiro - Mostra o tabuleiro com casas disponíveis
# ---------------------------------------------
def TelaTabuleiro(tela, eventos, estados, config):
    # Desenha as casas disponíveis para posicionamento, ataque e movimentação
    M.Desenhar_Casas_Disponiveis(
        tela, C.Partida.Mapa, C.player, C.inimigo, eventos,
        C.estadoAlvo, C.estadoVisualiza, C.selecionaAlvo,
        C.desselecionaAlvo, C.oculta, C.visualiza)

    # Verifica alterações no mapa (ex: clima, terreno, efeitos)
    if C.Partida.Mapa.mudança == True:
        C.Partida.Mapa.Verifica(C.player, C.inimigo)