import pygame
import sys

pygame.font.init()

mensagens_terminal = []
botao_cliques = {} 

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
AZUL = (100, 100, 255)
AZUL_CLARO = (173, 216, 230)
AZUL_SUPER_CLARO = (220, 235, 255)
AMARELO = (255, 255, 0)
AMARELO_CLARO = (255, 255, 153)
VERMELHO = (255, 0, 0)
VERMELHO_CLARO = (255, 102, 102)
VERDE = (0, 255, 0)
VERDE_CLARO = (144, 238, 144)
LARANJA = (255, 165, 0)
ROXO = (128, 0, 128)
ROSA = (255, 192, 203)
DOURADO = (255, 215, 0)
PRATA = (192, 192, 192)


Fonte70 = pygame.font.SysFont(None, 70)
Fonte50 = pygame.font.SysFont(None, 50)
Fonte40 = pygame.font.SysFont(None, 40)
Fonte30 = pygame.font.SysFont(None, 30)
Fonte25 = pygame.font.SysFont(None, 28)
Fonte20 = pygame.font.SysFont(None, 20)
Fonte15 = pygame.font.SysFont(None, 15)

Fontes = [Fonte15,Fonte20,Fonte25,Fonte30,Fonte40,Fonte50]
Cores = [PRETO,BRANCO,CINZA,AZUL,AZUL_CLARO,AMARELO,VERMELHO,VERDE,VERDE_CLARO,LARANJA,ROXO,ROSA,DOURADO,PRATA]

def Botao(tela, texto, espaço, cor_normal, cor_borda, cor_passagem,
           acao, Fonte, estado_clique, grossura=2, tecla_atalho=None,
           mostrar_na_tela=True, eventos=None):

    x, y, largura, altura = espaço
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    mouse_sobre = x <= mouse[0] <= x + largura and y <= mouse[1] <= y + altura

    # Detecta se a tecla foi pressionada agora (não está segurada)
    tecla_ativada = False
    if tecla_atalho and eventos:
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == tecla_atalho:
                tecla_ativada = True

    # Piscar a borda se ativado por tecla
    cor_borda_atual = cor_passagem if mouse_sobre or tecla_ativada else cor_borda

    # Desenha botão (se for visual)
    if mostrar_na_tela:
        pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))
        pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), grossura)

        if texto:
            texto_render = Fonte.render(texto, True, (0, 0, 0))
            texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
            tela.blit(texto_render, texto_rect)

    # Clique do mouse (somente uma vez)
    if mostrar_na_tela and mouse_sobre and clique[0] == 1 and not estado_clique.get("pressionado", False):
        estado_clique["pressionado"] = True
        if acao:
            acao()

    if clique[0] == 0:
        estado_clique["pressionado"] = False

    # Clique pela tecla (evento único)
    if tecla_ativada and not estado_clique.get("pressionado_tecla", False):
        estado_clique["pressionado_tecla"] = True
        if acao:
            acao()

    # Resetar após a tecla ser solta
    if tecla_atalho and eventos:
        for evento in eventos:
            if evento.type == pygame.KEYUP and evento.key == tecla_atalho:
                estado_clique["pressionado_tecla"] = False

def passar_turno(tela, texto, espaço, cor_normal, cor_borda, cor_passagem,
                        Fonte, estado_clique, player, inimigo, grossura=2,
                        tecla_atalho=None, mostrar_na_tela=True, eventos=None):

    x, y, largura, altura = espaço
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()

    mouse_sobre = x <= mouse[0] <= x + largura and y <= mouse[1] <= y + altura

    tecla_ativada = False
    if tecla_atalho and eventos:
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == tecla_atalho:
                tecla_ativada = True

    cor_borda_atual = cor_passagem if mouse_sobre or tecla_ativada else cor_borda

    if mostrar_na_tela:
        pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))
        pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), grossura)

        if texto:
            texto_render = Fonte.render(texto, True, (0, 0, 0))
            texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
            tela.blit(texto_render, texto_rect)

    # Clique com mouse (executa apenas uma vez)
    if mouse_sobre and clique[0] == 1:
        if not estado_clique.get("pressionado", False):
            estado_clique["pressionado"] = True
            player, inimigo = inimigo, player
            for i in range(10):
                adicionar_mensagem("")
            adicionar_mensagem(f"Novo turno de {player.nome}!")
    else:
        estado_clique["pressionado"] = False

    # Clique com tecla (executa apenas uma vez)
    if tecla_ativada:
        if not estado_clique.get("pressionado_tecla", False):
            estado_clique["pressionado_tecla"] = True
            player, inimigo = inimigo, player
            for i in range(10):
                adicionar_mensagem("")
            adicionar_mensagem(f"Novo turno de {player.nome}!")
    elif tecla_atalho:
        # Libera o clique da tecla ao soltar
        for evento in eventos:
            if evento.type == pygame.KEYUP and evento.key == tecla_atalho:
                estado_clique["pressionado_tecla"] = False

    
    return player, inimigo, 

def Botao_Selecao(
    tela, espaço, texto, Fonte,
    cor_fundo, cor_borda_normal,
    cor_borda_esquerda=None, cor_borda_direita=None,
    cor_passagem=None, id_botao=None,
    estado_global=None, eventos=None,
    funcao_esquerdo=None, funcao_direito=None,
    desfazer_esquerdo=None, desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None
):

    x, y, largura, altura = espaço
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    mouse_sobre = x <= mouse[0] <= x + largura and y <= mouse[1] <= y + altura

    if "selecionado_esquerdo" not in estado_global:
        estado_global["selecionado_esquerdo"] = None
    if "selecionado_direito" not in estado_global:
        estado_global["selecionado_direito"] = None

    # Tecla de atalho
    ativado_por_tecla_esq = False
    ativado_por_tecla_dir = False
    if eventos:
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if tecla_esquerda and evento.key == tecla_esquerda:
                    ativado_por_tecla_esq = True
                if tecla_direita and evento.key == tecla_direita:
                    ativado_por_tecla_dir = True

    # Verificar seleção atual
    modo_selecionado = None
    if estado_global["selecionado_esquerdo"] == id_botao:
        modo_selecionado = "esquerdo"
    elif estado_global["selecionado_direito"] == id_botao:
        modo_selecionado = "direito"

    # Determinar cor da borda
    cor_borda_atual = cor_borda_normal
    if modo_selecionado == "esquerdo" and cor_borda_esquerda:
        cor_borda_atual = cor_borda_esquerda
    elif modo_selecionado == "direito" and cor_borda_direita:
        cor_borda_atual = cor_borda_direita
    elif mouse_sobre and cor_passagem:
        cor_borda_atual = cor_passagem

    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), 3)

    texto_render = Fonte.render(texto, True, (0, 0, 0))
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_render, texto_rect)

    # Função auxiliar para aplicar e desfazer
    def aplicar_selecao(modo):
        if modo == "esquerdo":
            if estado_global["selecionado_esquerdo"] == id_botao:
                if desfazer_esquerdo:
                    desfazer_esquerdo()
                estado_global["selecionado_esquerdo"] = None
            else:
                # Desfaz o direito se for o mesmo botão
                if estado_global["selecionado_direito"] == id_botao:
                    if desfazer_direito:
                        desfazer_direito()
                    estado_global["selecionado_direito"] = None

                if estado_global["selecionado_esquerdo"] and desfazer_esquerdo:
                    desfazer_esquerdo()
                estado_global["selecionado_esquerdo"] = id_botao
                if funcao_esquerdo:
                    funcao_esquerdo()

        elif modo == "direito":
            if estado_global["selecionado_direito"] == id_botao:
                if desfazer_direito:
                    desfazer_direito()
                estado_global["selecionado_direito"] = None
            else:
                # Desfaz o esquerdo se for o mesmo botão
                if estado_global["selecionado_esquerdo"] == id_botao:
                    if desfazer_esquerdo:
                        desfazer_esquerdo()
                    estado_global["selecionado_esquerdo"] = None

                if estado_global["selecionado_direito"] and desfazer_direito:
                    desfazer_direito()
                estado_global["selecionado_direito"] = id_botao
                if funcao_direito:
                    funcao_direito()

    # Clique do mouse
    if eventos:
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if mouse_sobre:
                    if evento.button == 1 and cor_borda_esquerda:
                        if modo_selecionado == "direito" and desfazer_direito:
                            desfazer_direito()
                            estado_global["selecionado_direito"] = None
                        aplicar_selecao("esquerdo")
                    elif evento.button == 3 and cor_borda_direita:
                        if modo_selecionado == "esquerdo" and desfazer_esquerdo:
                            desfazer_esquerdo()
                            estado_global["selecionado_esquerdo"] = None
                        aplicar_selecao("direito")

            # Teclas
            elif evento.type == pygame.KEYDOWN:
                if tecla_esquerda and evento.key == tecla_esquerda and cor_borda_esquerda:
                    if modo_selecionado == "direito" and desfazer_direito:
                        desfazer_direito()
                        estado_global["selecionado_direito"] = None
                    aplicar_selecao("esquerdo")
                if tecla_direita and evento.key == tecla_direita and cor_borda_direita:
                    if modo_selecionado == "esquerdo" and desfazer_esquerdo:
                        desfazer_esquerdo()
                        estado_global["selecionado_esquerdo"] = None
                    aplicar_selecao("direito")

def adicionar_mensagem(texto, max_linhas=9):
    mensagens_terminal.append(texto)
    if len(mensagens_terminal) > max_linhas:
        mensagens_terminal.pop(0)  

def Terminal(tela, espaço, fonte, cor_fundo, cor_texto):
    x, y, largura, altura = espaço
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    pygame.draw.rect(tela, cor_texto, (x, y, largura, altura), 2)

    espaco_linha = fonte.get_height() + 6
    for i, mensagem in enumerate(mensagens_terminal):
        texto = fonte.render(mensagem, True, cor_texto)
        tela.blit(texto, (x + 10, y + 5 + i * espaco_linha))            

def Tabela(nome, colunas, linhas, tela, x, y, largura_total, fonte, cor_fundo, cor_texto, cor_borda):
    num_colunas = len(colunas)
    altura_linha = fonte.get_height() + 10

    # Calcular largura proporcional das colunas com base no conteúdo
    larguras_reais = []
    for i in range(num_colunas):
        textos_coluna = [colunas[i]] + [linha[i] for linha in linhas]
        largura_max = max(fonte.size(texto)[0] for texto in textos_coluna)
        larguras_reais.append(largura_max)

    soma_larguras = sum(larguras_reais)
    larguras_ajustadas = [int((larg * largura_total) / soma_larguras) for larg in larguras_reais]

    # Recalcular a largura total real após arredondamento
    largura_total_real = sum(larguras_ajustadas)

    # CALCULA a altura total de forma correta:
    num_linhas_total = 1 + 1 + len(linhas)
    altura_total = num_linhas_total * altura_linha

    # Desenhar fundo da tabela
    pygame.draw.rect(tela, cor_fundo, (x, y, largura_total_real, altura_total))

    # Desenhar borda completa
    pygame.draw.rect(tela, cor_borda, (x, y, largura_total_real, altura_total), 2)

    # Desenhar título (linha 0)
    titulo_render = fonte.render(nome, True, cor_texto)
    titulo_rect = titulo_render.get_rect(center=(x + largura_total_real // 2, y + altura_linha // 2))
    tela.blit(titulo_render, titulo_rect)

    # Cabeçalho (linha 1)
    for i, coluna in enumerate(colunas):
        coluna_x = x + sum(larguras_ajustadas[:i])
        texto = fonte.render(coluna, True, cor_texto)
        texto_rect = texto.get_rect(center=(coluna_x + larguras_ajustadas[i] // 2, y + altura_linha + altura_linha // 2))
        tela.blit(texto, texto_rect)

    # Linhas de dados (a partir da linha 2)
    for j, linha in enumerate(linhas):
        linha_y = y + (j + 2) * altura_linha
        for i, valor in enumerate(linha):
            coluna_x = x + sum(larguras_ajustadas[:i])
            texto = fonte.render(valor, True, cor_texto)
            texto_rect = texto.get_rect(center=(coluna_x + larguras_ajustadas[i] // 2, linha_y + altura_linha // 2))
            tela.blit(texto, texto_rect)
        for i in range(1, num_colunas):
            linha_x = x + sum(larguras_ajustadas[:i])
            pygame.draw.line(
                tela,
                cor_borda,
                (linha_x, y + altura_linha),
                (linha_x, y + altura_total),
                1
            )

    for j in range(1, len(linhas) + 2):
        pygame.draw.line(
            tela,
            cor_borda,
            (x, y + j * altura_linha),
            (x + largura_total_real, y + j * altura_linha),
            1
        )

def Carregar_Imagem(nome_arquivo,tamanho,tipo="n"):
    if tipo == "PNG":
        Imagem_original = pygame.image.load(nome_arquivo).convert_alpha()
        return pygame.transform.scale(Imagem_original, tamanho)
    else:
        Imagem_original = pygame.image.load(nome_arquivo).convert()
        return pygame.transform.scale(Imagem_original, tamanho)

def Barra_De_Texto(tela, espaço, fonte, cor_fundo, cor_borda, cor_texto,
                   eventos, texto_atual, ao_enviar, cor_selecionado, selecionada):

    x, y, largura, altura = espaço
    retangulo = pygame.Rect(x, y, largura, altura)

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if retangulo.collidepoint(evento.pos):
                selecionada = not selecionada  # Clica nela → alterna
            else:
                selecionada = False  # Clica fora → desativa

        if selecionada and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                if texto_atual.strip() != "":
                    ao_enviar(texto_atual)
                texto_atual = ""
            elif evento.key == pygame.K_BACKSPACE:
                texto_atual = texto_atual[:-1]
            else:
                texto_atual += evento.unicode

    # Cor da borda dependendo se está ativa
    cor_borda_atual = cor_selecionado if selecionada else cor_borda

    pygame.draw.rect(tela, cor_fundo, retangulo)
    pygame.draw.rect(tela, cor_borda_atual, retangulo, 2)

    texto_surface = fonte.render(str(texto_atual), True, cor_texto)
    tela.blit(texto_surface, (retangulo.x + 10, retangulo.y + (altura - texto_surface.get_height()) // 2))

    return texto_atual, selecionada

def Texto(tela, texto, posicao, fonte, cor):
    render = fonte.render(texto, True, cor)
    tela.blit(render, posicao)

def Texto_caixa(tela, texto, espaço, fonte, cor_fundo, borda=PRETO, grossura=3):
    """
    Desenha um retângulo com texto centralizado e uma borda.

    :param tela: A superfície onde será desenhado.
    :param texto: Texto a ser exibido.
    :param espaço: Tupla (x, y, largura, altura) com a posição e tamanho do retângulo.
    :param fonte: Fonte usada para renderizar o texto.
    :param cor_fundo: Cor de fundo do retângulo.
    :param borda: Cor da borda.
    :param grossura: Espessura da borda (default=2).
    """
    x, y, largura, altura = espaço

    # Desenha o retângulo de fundo
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Desenha a borda
    pygame.draw.rect(tela, borda, (x, y, largura, altura), grossura)

    # Renderiza o texto
    texto_render = fonte.render(texto, True, (0, 0, 0))  # Texto preto
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))

    # Desenha o texto na tela
    tela.blit(texto_render, texto_rect)

def Reta_Central(tela, largura_tela, altura_tela, cor=PRETO, espessura=2):
    x_centro = largura_tela // 2
    pygame.draw.line(tela, cor, (x_centro, 0), (x_centro, altura_tela), espessura)
