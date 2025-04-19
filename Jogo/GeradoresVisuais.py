import pygame
import os

pygame.font.init()

mensagens_terminal = []
botao_cliques = {} 

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
CINZA_ESCURO = (100, 100, 100)
AZUL = (100, 100, 255)
AZUL_CLARO = (173, 216, 230)
AZUL_SUPER_CLARO = (220, 235, 255)
AMARELO = (255, 255, 0)
AMARELO_CLARO = (255, 255, 153)
VERMELHO = (255, 0, 0)
VERMELHO_CLARO = (255, 102, 102)
VERMELHO_SUPER_CLARO = (255, 153, 153)
VERDE = (0, 255, 0)
VERDE_CLARO = (144, 238, 144)
LARANJA = (255, 165, 0)
LARANJA_CLARO = (255, 200, 100) 
ROXO = (128, 0, 128)
ROXO_CLARO = (216, 191, 216)     
ROSA = (255, 192, 203)
DOURADO = (255, 215, 0)
PRATA = (192, 192, 192)

Fonte70 = pygame.font.SysFont(None, 70)
Fonte50 = pygame.font.SysFont(None, 50)
Fonte40 = pygame.font.SysFont(None, 40)
Fonte35 = pygame.font.SysFont(None, 35)
Fonte30 = pygame.font.SysFont(None, 30)
Fonte25 = pygame.font.SysFont(None, 25)
Fonte28 = pygame.font.SysFont(None, 28)
Fonte20 = pygame.font.SysFont(None, 23)
Fonte15 = pygame.font.SysFont(None, 15)

Fontes = [Fonte15,Fonte20,Fonte25,Fonte28,Fonte30,Fonte40,Fonte50]
Cores = [PRETO,BRANCO,CINZA,AZUL,AZUL_CLARO,AMARELO,VERMELHO,VERDE,VERDE_CLARO,LARANJA,ROXO,ROSA,DOURADO,PRATA]

def Botao(tela, texto, espaço, cor_normal, cor_borda, cor_passagem,
           acao, Fonte, estado_clique, grossura=2, tecla_atalho=None,
           mostrar_na_tela=True, eventos=None, som=None):
    
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
        if som:
            som.play()
        if acao:
            acao()

    if clique[0] == 0:
        estado_clique["pressionado"] = False

    # Clique pela tecla (evento único)
    if tecla_ativada and not estado_clique.get("pressionado_tecla", False):
        estado_clique["pressionado_tecla"] = True
        if som:
            som.play()
        if acao:
            acao()

    # Resetar após a tecla ser solta
    if tecla_atalho and eventos:
        for evento in eventos:
            if evento.type == pygame.KEYUP and evento.key == tecla_atalho:
                estado_clique["pressionado_tecla"] = False

def Botao_Selecao(
    tela, espaço, texto, Fonte,
    cor_fundo, cor_borda_normal,
    cor_borda_esquerda=None, cor_borda_direita=None,
    cor_passagem=None, id_botao=None,
    estado_global=None, eventos=None,
    funcao_esquerdo=None, funcao_direito=None,
    desfazer_esquerdo=None, desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None,
    grossura=5, som=None  
):

    x, y, largura, altura = espaço
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    mouse_sobre = x <= mouse[0] <= x + largura and y <= mouse[1] <= y + altura

    if "selecionado_esquerdo" not in estado_global:
        estado_global["selecionado_esquerdo"] = None
    if "selecionado_direito" not in estado_global:
        estado_global["selecionado_direito"] = None

    ativado_por_tecla_esq = False
    ativado_por_tecla_dir = False
    if eventos:
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if tecla_esquerda and evento.key == tecla_esquerda:
                    ativado_por_tecla_esq = True
                if tecla_direita and evento.key == tecla_direita:
                    ativado_por_tecla_dir = True

    modo_selecionado = None
    if estado_global["selecionado_esquerdo"] == id_botao:
        modo_selecionado = "esquerdo"
    elif estado_global["selecionado_direito"] == id_botao:
        modo_selecionado = "direito"

    cor_borda_atual = cor_borda_normal
    if modo_selecionado == "esquerdo" and cor_borda_esquerda:
        cor_borda_atual = cor_borda_esquerda
    elif modo_selecionado == "direito" and cor_borda_direita:
        cor_borda_atual = cor_borda_direita
    elif mouse_sobre and cor_passagem:
        cor_borda_atual = cor_passagem

    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
    pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), grossura)

    texto_render = Fonte.render(texto, True, (0, 0, 0))
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_render, texto_rect)

    def aplicar_selecao(modo):
        if modo == "esquerdo":
            if estado_global["selecionado_esquerdo"] == id_botao:
                if desfazer_esquerdo:
                    desfazer_esquerdo()
                estado_global["selecionado_esquerdo"] = None
            else:
                if estado_global["selecionado_direito"] == id_botao:
                    if desfazer_direito:
                        desfazer_direito()
                    estado_global["selecionado_direito"] = None

                if estado_global["selecionado_esquerdo"] and desfazer_esquerdo:
                    desfazer_esquerdo()
                estado_global["selecionado_esquerdo"] = id_botao
                if funcao_esquerdo:
                    funcao_esquerdo()
                if som:  # ← Som ao selecionar
                    som.play()

        elif modo == "direito":
            if estado_global["selecionado_direito"] == id_botao:
                if desfazer_direito:
                    desfazer_direito()
                estado_global["selecionado_direito"] = None
            else:
                if estado_global["selecionado_esquerdo"] == id_botao:
                    if desfazer_esquerdo:
                        desfazer_esquerdo()
                    estado_global["selecionado_esquerdo"] = None

                if estado_global["selecionado_direito"] and desfazer_direito:
                    desfazer_direito()
                estado_global["selecionado_direito"] = id_botao
                if funcao_direito:
                    funcao_direito()
                if som:  # ← Som ao selecionar
                    som.play()

    if eventos:
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and mouse_sobre:
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
            elif evento.type == pygame.KEYDOWN:
                if evento.key == tecla_esquerda and cor_borda_esquerda:
                    if modo_selecionado == "direito" and desfazer_direito:
                        desfazer_direito()
                        estado_global["selecionado_direito"] = None
                    aplicar_selecao("esquerdo")
                elif evento.key == tecla_direita and cor_borda_direita:
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

def Tabela(nome, colunas, linhas, tela, x, y, largura_total, fonte, fonte_cabecalho, cor_fundo, cor_borda, cor_cabecalho):
    PRETO = (0, 0, 0)  # Cor padrão para texto
    num_colunas = len(colunas)
    if y == 250:
        altura_linha = fonte.get_height() + 15
    else:
        altura_linha = fonte.get_height() + 10

    # Garantir que todos os valores em 'colunas' e 'linhas' sejam strings
    colunas = [str(coluna) for coluna in colunas]
    linhas = [[str(valor) for valor in linha] for linha in linhas]

    # Calcular largura proporcional das colunas com base no conteúdo
    larguras_reais = []
    for i in range(num_colunas):
        textos_coluna = [colunas[i]] + [linha[i] for linha in linhas]
        largura_max = max(fonte.size(texto)[0] for texto in textos_coluna)
        larguras_reais.append(largura_max)

    soma_larguras = sum(larguras_reais)
    larguras_ajustadas = [int((larg * largura_total) / soma_larguras) for larg in larguras_reais]
    largura_total_real = sum(larguras_ajustadas)

    # Altura total
    num_linhas_total = 1 + 1 + len(linhas)
    altura_total = num_linhas_total * altura_linha

    # Fundo da tabela
    pygame.draw.rect(tela, cor_fundo, (x, y, largura_total_real, altura_total))

    # Borda externa da tabela
    pygame.draw.rect(tela, cor_borda, (x, y, largura_total_real, altura_total), 2)

    # Título (linha 0)
    pygame.draw.rect(tela, cor_cabecalho, (x, y, largura_total_real, altura_linha))
    titulo_render = fonte_cabecalho.render(nome, True, PRETO)
    titulo_rect = titulo_render.get_rect(center=(x + largura_total_real // 2, y + altura_linha // 2))
    tela.blit(titulo_render, titulo_rect)

    # Cabeçalho (linha 1)
    pygame.draw.rect(tela, cor_cabecalho, (x, y + altura_linha, largura_total_real, altura_linha))
    for i, coluna in enumerate(colunas):
        coluna_x = x + sum(larguras_ajustadas[:i])
        texto = fonte_cabecalho.render(coluna, True, PRETO)
        texto_rect = texto.get_rect(center=(coluna_x + larguras_ajustadas[i] // 2, y + altura_linha + altura_linha // 2))
        tela.blit(texto, texto_rect)

    # Reforçar bordas do cabeçalho (mais grossas)
    pygame.draw.line(tela, cor_borda, (x, y), (x + largura_total_real, y), 3)  # topo
    pygame.draw.line(tela, cor_borda, (x, y + 2 * altura_linha), (x + largura_total_real, y + 2 * altura_linha), 3)  # base do cabeçalho
    pygame.draw.line(tela, cor_borda, (x, y), (x, y + 2 * altura_linha), 3)  # esquerda
    pygame.draw.line(tela, cor_borda, (x + largura_total_real, y), (x + largura_total_real, y + 2 * altura_linha), 3)  # direita

    # Linhas de dados
    for j, linha in enumerate(linhas):
        linha_y = y + (j + 2) * altura_linha
        for i, valor in enumerate(linha):
            coluna_x = x + sum(larguras_ajustadas[:i])
            texto = fonte.render(valor, True, PRETO)
            texto_rect = texto.get_rect(center=(coluna_x + larguras_ajustadas[i] // 2, linha_y + altura_linha // 2))
            tela.blit(texto, texto_rect)

        for i in range(1, num_colunas):
            linha_x = x + sum(larguras_ajustadas[:i])
            pygame.draw.line(tela, cor_borda, (linha_x, y + altura_linha), (linha_x, y + altura_total), 1)

    for j in range(1, len(linhas) + 2):
        pygame.draw.line(tela, cor_borda, (x, y + j * altura_linha), (x + largura_total_real, y + j * altura_linha), 1)

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

def Texto_caixa(tela, texto, espaço, fonte, cor_fundo, borda=PRETO,cor_texto=PRETO, grossura=3, y_final=None, anima=None, tempo=200):
    x, y_inicial, largura, altura = espaço
   
    if y_final is not None:
        if anima is None:
            anima = pygame.time.get_ticks()
        tempo_passado = pygame.time.get_ticks() - anima
        progresso = min(tempo_passado / tempo, 1.0)
        y = int(y_inicial + (y_final - y_inicial) * progresso)
    else:
        y = y_inicial

    # Desenha o retângulo de fundo
    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Desenha a borda
    pygame.draw.rect(tela, borda, (x, y, largura, altura), grossura)

    # Renderiza o texto
    texto_render = fonte.render(texto, True, cor_texto)  # Texto preto
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))

    # Desenha o texto na tela
    tela.blit(texto_render, texto_rect)

def Reta_Central(tela, largura_tela, altura_tela, cor=PRETO, espessura=2):
    x_centro = largura_tela // 2
    pygame.draw.line(tela, cor, (x_centro, 0), (x_centro, altura_tela), espessura)

def limpa_terminal():
    mensagens_terminal.clear()

def tocar(som):
    if som:
        som.play()


AtaqueS = None
AtaqueSV = None

def seleciona_ataque(ataque,SoV):
    global AtaqueS,AtaqueSV
    if SoV == "S":
        AtaqueS = ataque
    else:
        AtaqueSV = ataque

def desseleciona_ataque(SoV):
    global AtaqueS,AtaqueSV
    if SoV == "S":
        AtaqueS = None
    else:
        AtaqueSV = None

def Status_Pokemon(pos, tela, pokemon, imagens_tipos, player, eventos=None, estado_global=None, x_final=None, anima=None, tempo=200, SoV=None):
    x_inicial, y = pos
    largura, altura = 360, 330
    global AtaqueSV

    if pokemon in player.pokemons:
        cor = (35,35,35)
    else:
        cor = (80,35,35)


    # Controle de animação
    if x_final is not None: 
        if anima is None:
            anima = pygame.time.get_ticks()
        tempo_passado = pygame.time.get_ticks() - anima
        progresso = min(tempo_passado / tempo, 1.0)
        x = int(x_inicial + (x_final - x_inicial) * progresso)
    else:
        x = x_inicial

    # Rect principal
    ret = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, cor, ret)
    pygame.draw.rect(tela, (255, 255, 255), ret, 2)

    if pokemon is not None:

        # Fontes
        fonte_titulo = pygame.font.SysFont("arial", 25, True)
        fonte_HP = pygame.font.SysFont("arial", 23, True)
        fonte_Stat = pygame.font.SysFont("arial", 20, True)
        fonte_normal = pygame.font.SysFont("arial", 20)
        fonte_pequena = pygame.font.SysFont("arial", 18)
        fonte_iv_destaque = pygame.font.SysFont("arial", 20, True)

        def cor_percentual(pct):
            if pct < 15:
                return (255, 0, 0)  # Vermelho
            elif pct < 30:
                return (255, 165, 0)  # Laranja
            elif pct < 50:
                return (255, 255, 0)  # Amarelo
            elif pct < 70:
                return (0, 255, 0)  # Verde
            elif pct < 90:
                return (0, 0, 255)  # Azul
            elif pct < 100:
                return (75, 0, 130)  # Roxo
            elif pct == 100:
                return (255, 0, 255)  # Rosa

        # Nome e HP
        nome_txt = fonte_titulo.render(pokemon.nome, True, (255, 255, 255))
        tela.blit(nome_txt, (x + 10, y + 5))

        vida_pct = pokemon.Vida / pokemon.VidaMax * 100
        vida_str = f"HP: {pokemon.Vida}/{pokemon.VidaMax}"
        vida_txt = fonte_HP.render(vida_str, True, (255, 255, 255))
        tela.blit(vida_txt, (x + largura - vida_txt.get_width() - 10, y + 8))

        pygame.draw.rect(tela, (0, 0, 0), (x + 9, y + 34, 342, 18), 1)
        pygame.draw.rect(tela, cor_percentual(vida_pct), (x + 10, y + 35, (340 * (pokemon.Vida / pokemon.VidaMax)), 16))

        pygame.draw.line(tela, (255, 255, 255), (x, y + 60), (x + largura, y + 60), 2)

        atributos = [
            ("HP", pokemon.VidaMax, pokemon.IV_vida, 300),
            ("Attack", pokemon.Atk, pokemon.IV_atk, 100),
            ("Defense", pokemon.Def, pokemon.IV_def, 100),
            ("Sp. Atk", pokemon.Atk_sp, pokemon.IV_atkSP, 100),
            ("Sp. Def", pokemon.Def_sp, pokemon.IV_defSP, 100),
            ("Speed", pokemon.vel, pokemon.IV_vel, 100)
        ]

        for i, (nome, valor, iv_val, valor_max) in enumerate(atributos):
            top = y + 68 + i * 28
            label = fonte_normal.render(f"{nome}:", True, (230, 230, 230))
            tela.blit(label, (x + 10, top))

            val_txt = fonte_Stat.render(f"{valor}", True, (255, 255, 255))
            tela.blit(val_txt, (x + 85, top))

            percentual = min(valor / valor_max, 1.0)
            largura_barra = int(percentual * 140)

            pygame.draw.rect(tela, cor_percentual(percentual * 100), (x + 130, top + 4, largura_barra, 16))
            pygame.draw.rect(tela, (0, 0, 0), (x + 130, top + 4, 140, 16), 1)

            iv_txt = fonte_pequena.render(f"IV: {iv_val}%", True, cor_percentual(iv_val))
            tela.blit(iv_txt, (x + 280, top))

        pygame.draw.line(tela, (255, 255, 255), (x, y + 238), (x + largura, y + 238), 2)

        for i, tipo in enumerate(pokemon.tipo):
            tipo_render = fonte_pequena.render(tipo, True, (255, 255, 255))
            tela.blit(tipo_render, (x + 10, y + 244 + i * 18))

        for i, tipo in enumerate(pokemon.tipo):
            pos_x = x + 80 + i * 36
            pos_y = y + 245
            centro = (pos_x + 15, pos_y + 15)
            pygame.draw.circle(tela, (255, 255, 255), centro, 15)
            pygame.draw.circle(tela, (0, 0, 0), centro, 15, 1)
            if tipo in imagens_tipos:
                img = imagens_tipos[tipo]
                img_rect = img.get_rect(center=centro)
                tela.blit(img, img_rect)

        xp_txt = fonte_pequena.render(f"XP: {pokemon.xp_atu}", True, (230, 230, 230))
        peso_txt = fonte_pequena.render(f"Peso: {pokemon.custo}", True, (230, 230, 230))
        tela.blit(xp_txt, (x + 165, y + 244))
        tela.blit(peso_txt, (x + 165, y + 262))

        iv_txt = fonte_iv_destaque.render(f"IV: {pokemon.IV}%", True, cor_percentual(pokemon.IV))
        tela.blit(iv_txt, (x + 235, y + 250))

        pygame.draw.line(tela, (255, 255, 255), (x, y + 285), (x + largura, y + 285), 2)

        # Botões
        botao_rect1 = pygame.Rect(x + 17, y + 292, 156, 30)
        botao_rect2 = pygame.Rect(x + 187, y + 292, 156, 30)

        Botao_Selecao(
            tela, botao_rect1, pokemon.ataque_normal["nome"], Fonte20,
            (255, 200, 120), (255, 255, 255),funcao_esquerdo=lambda:seleciona_ataque(pokemon.ataque_normal,SoV),
            desfazer_esquerdo=lambda:desseleciona_ataque(SoV),id_botao=f"{pokemon.ID}{pokemon.ataque_normal["nome"]}",
            cor_borda_esquerda=VERMELHO,
            estado_global=estado_global, eventos=eventos, grossura=2, cor_passagem=AMARELO
        )

        Botao_Selecao(
            tela, botao_rect2, pokemon.ataque_especial["nome"], Fonte20,
            (210, 160, 255), (255, 255, 255),funcao_esquerdo=lambda:seleciona_ataque(pokemon.ataque_especial,SoV),
            desfazer_esquerdo=lambda:desseleciona_ataque(SoV),id_botao=f"{pokemon.ID}{pokemon.ataque_especial["nome"]}",
            cor_borda_esquerda=VERMELHO,
            estado_global=estado_global, eventos=eventos, grossura=2, cor_passagem=AMARELO
        )

        if x > 1600:
            desseleciona_ataque(SoV)

        if SoV == "S":
            if AtaqueS is not None:
                Mostrar_Ataque(tela,AtaqueS,(1228,y),imagens_tipos)
        else:
            if AtaqueSV is not None:
                Mostrar_Ataque(tela,AtaqueSV,(1228,y),imagens_tipos)
       

def Mostrar_Ataque(tela, ataque, posicao=(100, 100), imagens_tipos=None):
    # Cores
    FUNDO = (30, 30, 30)
    BORDA = (255, 255, 255)
    TEXTO = (255, 255, 255)
    LINHA = (200, 200, 200)
    BRANCO = (255, 255, 255)

    energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 255, 0), "verde": (0, 200, 0),
        "roxa": (128, 0, 128), "rosa": (255, 105, 180),
        "laranja": (255, 140, 0), "marrom": (139, 69, 19),
        "preta": (30, 30, 30), "cinza": (160, 160, 160)
    }

    # Fontes
    fonte_titulo = pygame.font.SysFont("arial", 28, bold=True)
    fonte_desc = pygame.font.SysFont("arial", 18)
    fonte_info = pygame.font.SysFont("arial", 18)
    fonte_infoStat = pygame.font.SysFont("arial", 18, bold=True)

    # Tamanho da ficha
    largura_total = 330
    altura_total = 330
    x, y = posicao

    # Fundo principal da ficha
    fundo = pygame.Rect(x, y, largura_total, altura_total)
    pygame.draw.rect(tela, FUNDO, fundo)
    pygame.draw.rect(tela, BORDA, fundo, 2)

    if ataque is not None:
        # 1. Cabeçalho - Nome
        nome_render = fonte_titulo.render(ataque["nome"], True, TEXTO)
        nome_rect = nome_render.get_rect(center=(x + largura_total // 2, y + 25))
        tela.blit(nome_render, nome_rect)

    # Tipos com borda branca e preta centralizados
    if imagens_tipos and "tipo" in ataque:
        tipos = ataque["tipo"]
        raio = 15
        tamanho_icon = 30

        def desenhar_tipo(tipo, centro):
            pygame.draw.circle(tela, (255, 255, 255), centro, raio)  # Fundo branco
            pygame.draw.circle(tela, (0, 0, 0), centro, raio, 1)     # Borda preta

            if tipo in imagens_tipos:
                img = pygame.transform.scale(imagens_tipos[tipo], (tamanho_icon, tamanho_icon))
                img_rect = img.get_rect(center=centro)
                tela.blit(img, img_rect)

        if len(tipos) == 1:
            centro_esq = (x + 8 + raio, y + 8 + raio)
            centro_dir = (x + largura_total - 8 - raio, y + 8 + raio)
            desenhar_tipo(tipos[0], centro_esq)
            desenhar_tipo(tipos[0], centro_dir)
        elif len(tipos) >= 2:
            centro_esq = (x + 8 + raio, y + 8 + raio)
            centro_dir = (x + largura_total - 8 - raio, y + 8 + raio)
            desenhar_tipo(tipos[0], centro_esq)
            desenhar_tipo(tipos[1], centro_dir)

        pygame.draw.line(tela, LINHA, (x + 10, y + 50), (x + largura_total - 10, y + 50), 2)

        # 2. Descrição (até 8 linhas)
        palavras = ataque["descrição"].split(" ")
        linhas = []
        linha = ""
        max_largura = largura_total - 20
        for palavra in palavras:
            if fonte_desc.size(linha + palavra)[0] > max_largura:
                linhas.append(linha)
                linha = palavra + " "
            else:
                linha += palavra + " "
        if linha:
            linhas.append(linha)

        y_desc_inicio = y + 60
        for i, linha in enumerate(linhas[:9]):
            texto_linha = fonte_desc.render(linha.strip(), True, TEXTO)
            tela.blit(texto_linha, (x + 10, y_desc_inicio + i * 22))

        # Ajustar a linha de separação para não ultrapassar os limites da ficha
        y_divisoria = y + altura_total - 80
        pygame.draw.line(tela, LINHA, (x + 10, y_divisoria), (x + largura_total - 10, y_divisoria), 2)

        # 3. Status
        infos = [
            f"Dano: {ataque['dano']}",
            f"Alcance: {ataque['alcance']}m",
            f"Precisão: {ataque['precisão']}%"
        ]
        
        # Função para definir a cor do status
        def obter_cor_status(status, tipo):
            if tipo == "dano":
                if status < 0.8:
                    return (255, 0, 0)  # Vermelho
                elif status < 1.2:
                    return (255, 255, 0)  # Amarelo
                elif status < 1.6:
                    return (0, 200, 0)  # Verde
                else:
                    return (180, 90, 255)  # Roxo claro
            elif tipo == "alcance":
                if status < 20:
                    return (255, 0, 0)  # Vermelho
                elif status < 50:
                    return (255, 255, 0)  # Amarelo
                elif status < 90:
                    return (0, 200, 0)  # Verde
                else:
                    return (180, 90, 255)  # Roxo claro
            elif tipo == "precisão":
                if status < 35:
                    return (255, 0, 0)  # Vermelho
                elif status < 70:
                    return (255, 255, 0)  # Amarelo
                elif status < 101:
                    return (0, 200, 0)  # Verde
                else:
                    return (180, 90, 255)  # Roxo claro

        espacamento = largura_total // len(infos)
        for i, info in enumerate(infos):
            texto_info = fonte_info.render(info.split(":")[0], True, TEXTO)
            texto_valor = fonte_infoStat.render(info.split(":")[1], True, obter_cor_status(float(info.split(":")[1].replace("m", "").replace("%", "")), infos[i].split(":")[0].lower()))
            
            rect_info = texto_info.get_rect(center=(x + espacamento * i + espacamento // 2, y + altura_total - 68))
            rect_valor = texto_valor.get_rect(center=(x + espacamento * i + espacamento // 2, y + altura_total - 48))

            tela.blit(texto_info, rect_info)
            tela.blit(texto_valor, rect_valor)

        pygame.draw.line(tela, LINHA, (x + 10, y + altura_total - 35), (x + largura_total - 10, y + altura_total - 35), 2)

        # 4. Custo
        custo_label = fonte_info.render("Custo:", True, TEXTO)
        tela.blit(custo_label, (x + 10, y + altura_total - 28))

        if "custo" in ataque:
            for i, energia in enumerate(ataque["custo"]):
                cor = energia_cores.get(energia, BRANCO)
                cx = x + 70 + i * 28
                cy = y + altura_total - 18
                pygame.draw.circle(tela, cor, (cx, cy), 10)
                pygame.draw.circle(tela, BORDA, (cx, cy), 10, 1)



def carregar_frames(pasta):
    frames = []
    for nome in sorted(os.listdir(pasta)):
        if nome.endswith(".png"):
            caminho = os.path.join(pasta, nome)
            imagem = pygame.image.load(caminho).convert_alpha()
            frames.append(imagem)
    return frames

H = None
B1 = {"estado": False}

def Inventario(local, tela, player, ImagensItens, estado, eventos, PokemonS, x_final=None, anima=None, tempo=200):
    x_inicial, y = local
    largura, altura = 380, 285  # ⬅️ Aumentado para 285

    # Controle de animação (exatamente igual ao Status_Pokemon)
    if x_final is not None:
        if anima is None:
            anima = pygame.time.get_ticks()
        tempo_passado = pygame.time.get_ticks() - anima
        progresso = min(tempo_passado / tempo, 1.0)
        x = int(x_inicial + (x_final - x_inicial) * progresso)
    else:
        x = x_inicial

    cor_borda = (255, 255, 255)  # Borda branca
    global H  # Item selecionado com botão direito

    # Fundo escuro com borda branca
    pygame.draw.rect(tela, cor_borda, (x - 3, y - 3, largura + 4, altura + 4))  # Borda branca
    pygame.draw.rect(tela, (30, 30, 30), (x, y, largura, altura))  # Fundo escuro

    Fonte = pygame.font.SysFont(None, 32)

    # Cabeçalho com fundo escuro e texto branco
    pygame.draw.rect(tela, (30, 30, 30), (x, y, largura, 40))  # Escuro para o cabeçalho
    texto_nome = Fonte.render(f"Inventário de {player.nome}", True, (255, 255, 255))  # Texto branco
    tela.blit(texto_nome, (x + largura // 2 - texto_nome.get_width() // 2, y + 10))

    pygame.draw.line(tela, (255, 255, 255), (x, y + 40), (x + largura, y + 40), 2)  # Linha branca
    pygame.draw.line(tela, (255, 255, 255), (x, y + 192), (x + largura, y + 192), 2)  # Linha branca

    def TiraDescriçao():
        global H
        H = None

    for i, item in enumerate(player.inventario[:10]):
        col = i % 5
        row = i // 5
        bx = x + col * 76
        by = y + 40 + row * 76
        espaço_botao = pygame.Rect(bx, by, 76, 76)
        nome_item = item["nome"]
        classe_item = item.get("classe", "").lower()

        def Descriçao(item=item):
            global H
            H = item  # Guarda o item clicado com o botão direito

        # Cor de fundo conforme a classe
        if classe_item == "pokebola":
            cor_fundo = (255, 100, 100)  # Vermelho claro
        elif classe_item == "poçao":
            cor_fundo = (100, 150, 255)  # Azul claro
        elif classe_item in ["caixa", "coletor"]:
            cor_fundo = (100, 200, 100)  # Verde claro
        elif classe_item == "amplificador":
            cor_fundo = (255, 150, 50)   # Laranja claro
        elif classe_item == "fruta":
            cor_fundo = (255, 255, 100)  # Amarelo claro
        else:
            cor_fundo = (150, 100, 255)  # Roxo claro

        pygame.draw.line(tela, (255, 255, 255), (x, y + 40), (x + largura, y + 40), 2)
        pygame.draw.line(tela, (255, 255, 255), (x, y + 192), (x + largura, y + 192), 2)

        # Botão de item
        Botao(
            tela=tela,
            texto="",
            espaço=espaço_botao,
            cor_normal=(0,0,0),  # Fundo escuro para o botão
            cor_borda=(0,0,0),   # Borda discreta
            cor_passagem=(0,0,0), # Cor ao passar o mouse
            acao=lambda i=i: player.usar_item(i, PokemonS),
            Fonte=Fonte,
            estado_clique=B1,
            grossura=2,
            tecla_atalho=None,
            mostrar_na_tela=True,
            eventos=eventos,
            som=None)

        # Botão de seleção
        Botao_Selecao(
            tela=tela,
            espaço=espaço_botao,
            texto="",
            Fonte=Fonte,
            cor_fundo=cor_fundo,
            cor_borda_normal=(255, 255, 255),  # Borda branca
            cor_borda_esquerda=(255, 255, 255),  # Borda branca
            cor_borda_direita=(0, 0, 255),
            cor_passagem=(255, 255, 0),
            id_botao=f"item_sel_{i}",
            estado_global=estado,
            eventos=eventos,
            funcao_esquerdo=None,
            funcao_direito=Descriçao,
            desfazer_esquerdo=None,
            desfazer_direito=TiraDescriçao,
            tecla_esquerda=None,
            tecla_direita=None,
            grossura=3,
            som=None
        )

        if nome_item in ImagensItens:
            imagem = ImagensItens[nome_item]
            iw, ih = imagem.get_size()
            img_x = bx + (76 - iw) // 2
            img_y = by + (76 - ih) // 2
            tela.blit(imagem, (img_x, img_y))
        else:
            imagem = ImagensItens[classe_item]
            iw, ih = imagem.get_size()
            img_x = bx + (76 - iw) // 2
            img_y = by + (76 - ih) // 2
            tela.blit(imagem, (img_x, img_y))

        # Mostrar nome do item clicado com botão direito (nova seção)
    if H:
        nome = H.get("nome", "")
        FonteNome = pygame.font.SysFont(None, 28)
        render_nome = FonteNome.render(nome, True, (255, 255, 255))  # Texto branco
        tela.blit(render_nome, (x + largura // 2 - render_nome.get_width() // 2, y + 195))  # ⬅️ Acima da descrição

    # Mostrar descrição se H foi definido
    if H:
        descricao = H.get("Descrição", "")
        FonteMenor = pygame.font.SysFont(None, 25)

        # Quebrar descrição em até 2 linhas
        palavras = descricao.split()
        linhas = []
        linha = ""
        for palavra in palavras:
            teste = linha + " " + palavra if linha else palavra
            if FonteMenor.size(teste)[0] > (largura - 20):
                linhas.append(linha)
                linha = palavra
            else:
                linha = teste
        linhas.append(linha)

        for i, texto in enumerate(linhas[:2]):
            render = FonteMenor.render(texto, True, (255, 255, 255))  # Texto branco
            tela.blit(render, (x + 10, y + 218 + i * 20))  # ⬅️ Descrição rebaixada 20px

B2 = {"estado": False}
B3 = {"estado": False}
B4 = {"estado": False}
B5 = {"estado": False}
B6 = {"estado": False}
B7 = {"estado": False}
B8 = {"estado": False}
B9 = {"estado": False}
B10 = {"estado": False}
B11 = {"estado": False}
BB = [B2,B3,B4,B5,B6,B7,B8,B9,B10,B11]

def Tabela_Energias(tela, local, player, estadoEnergias, eventos, x_final=None, anima=None, tempo=200):

    x_inicial, y = local
    largura, altura = 380, 320

    # Controle de animação
    if x_final is not None: 
        if anima is None:
            anima = pygame.time.get_ticks()
        tempo_passado = pygame.time.get_ticks() - anima
        progresso = min(tempo_passado / tempo, 1.0)
        x = int(x_inicial + (x_final - x_inicial) * progresso)
    else:
        x = x_inicial

    # Rect principal
    ret = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, (30, 30, 30), ret)  # fundo escuro
    pygame.draw.rect(tela, (255, 255, 255), ret, 3)  # borda branca

    fonte = pygame.font.SysFont(None, 24)
    fonte_titulo = pygame.font.SysFont(None, 28)

    energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 255, 0), "verde": (0, 200, 0),
        "roxa": (128, 0, 128), "rosa": (255, 105, 180),
        "laranja": (255, 140, 0), "marrom": (139, 69, 19),
        "preta": (30, 30, 30), "cinza": (160, 160, 160)
    }

    # Cabeçalho
    titulo = fonte_titulo.render(f"Energias de {player.nome}", True, (255, 255, 255))
    tela.blit(titulo, (x + 190 - titulo.get_width() // 2, y + 10))
    pygame.draw.line(tela, (0, 0, 0), (x, y + 34), (x + largura, y + 34), 2)

    # Linhas de energias em 4 colunas: nome1 | valor1 | nome2 | valor2
    chaves = list(player.energias.keys())
    for i in range(5):
        nome1 = chaves[i].capitalize()
        valor1 = str(player.energias[chaves[i]])
        nome2 = chaves[i+5].capitalize()
        valor2 = str(player.energias[chaves[i+5]])

        y_pos = y + 37 + i * 22

        # Colunas ajustadas
        texto_nome1 = fonte.render(nome1 + ":", True, (255, 255, 255))
        texto_valor1 = fonte.render(valor1, True, (255, 255, 255))
        texto_nome2 = fonte.render(nome2 + ":", True, (255, 255, 255))
        texto_valor2 = fonte.render(valor2, True, (255, 255, 255))

        x1 = x + 10
        x2 = x + 130
        x3 = x + 200
        x4 = x + 320

        tela.blit(texto_nome1, (x1, y_pos))
        tela.blit(texto_valor1, (x2, y_pos))
        tela.blit(texto_nome2, (x3, y_pos))
        tela.blit(texto_valor2, (x4, y_pos))

    # Linhas divisoras
    for i in range(6):
        y_pos = y + 34 + i * 22
        # Alteração aqui: primeira e última linha serão brancas
        if i == 0 or i == 5:  # Primeira e última linha
            pygame.draw.line(tela, (255, 255, 255), (x + 2, y_pos), (x + largura - 2, y_pos), 2)
        else:
            pygame.draw.line(tela, (0, 0, 0), (x + 2, y_pos), (x + largura - 2, y_pos), 1)

    # Parte inferior: barras verticais
    base_y = y + 310
    barra_topo = y + 150
    largura_barra = 20
    espaco_total = 360
    margem_x = 10
    espaco_entre = espaco_total // 10

    for i, chave in enumerate(chaves):
        cor = energia_cores[chave]
        valor = min(player.energias[chave], 20)
        altura = int((valor / 20) * (base_y - barra_topo))

        x_centro = x + margem_x + espaco_entre * i + espaco_entre // 2

        # Barra vertical
        pygame.draw.rect(tela, cor, (x_centro - largura_barra // 2, base_y - altura, largura_barra, altura))
        pygame.draw.rect(tela, (0, 0, 0), (x_centro - largura_barra // 2, barra_topo, largura_barra, base_y - barra_topo), 1)

        # Botão de seleção na base
        largura_botao = largura_barra + 8
        altura_botao = 18
        x_botao = x_centro - largura_botao // 2
        y_botao = base_y + 7
        
        Botao(tela, "",(x_botao, y_botao, largura_botao, altura_botao), (35,35,35), BRANCO, (35,35,35),
           lambda:player.muda_descarte(chave), Fonte15, BB[i], grossura=2, tecla_atalho=None,
           mostrar_na_tela=True, eventos=None, som=None)

        # Círculo com número
        pygame.draw.circle(tela, cor, (x_centro, base_y + 3), 12)
        pygame.draw.circle(tela, (255, 255, 255), (x_centro, base_y + 3), 12, 1)
        cor_texto = (255, 255, 255) if sum(cor) < 300 else (0, 0, 0)
        num = fonte.render(str(player.energias[chave]), True, cor_texto)
        tela.blit(num, (x_centro - num.get_width() // 2, base_y - num.get_height() // 2 + 3))

        if chave in player.energiasDesc:
            Texto_caixa(tela,f"D{player.energiasDesc.index(chave)}",(x_botao,( base_y - 150), largura_botao, 20),Fonte25,(30,30,30),(30,30,30),BRANCO)

def animar(D_inicial,D_final,anima,tempo=200):
    
    if anima is None:
        anima = pygame.time.get_ticks()
    tempo_passado = pygame.time.get_ticks() - anima
    progresso = min(tempo_passado / tempo, 1.0)
    D = int(D_inicial + (D_final - D_inicial) * progresso)

    return D


        






    


