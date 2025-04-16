import pygame
import os

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

def Texto_caixa(tela, texto, espaço, fonte, cor_fundo, borda=PRETO,cor_texto=PRETO, grossura=3):
  
    x, y, largura, altura = espaço

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

def Status_Pokemon(pos, tela, pokemon, cor, imagens_tipos, eventos=None, estado_global=None):
    x, y = pos
    largura, altura = 360, 330
    ret = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, cor, ret)
    pygame.draw.rect(tela, (255, 255, 255), ret, 2)

    # Fontes atualizadas
    fonte_titulo = pygame.font.SysFont("arial", 25, True)
    fonte_HP = pygame.font.SysFont("arial", 23, True)
    fonte_Stat = pygame.font.SysFont("arial", 20, True)
    fonte_normal = pygame.font.SysFont("arial", 20)
    fonte_pequena = pygame.font.SysFont("arial", 18)
    fonte_iv_destaque = pygame.font.SysFont("arial", 20, True)

    def cor_percentual(pct):
        if pct < 14:
            return (255, 0, 0)
        elif pct < 28:
            return (255, 128, 0)
        elif pct < 40:
            return (255, 255, 0)
        elif pct < 50:
            return (192, 255, 0)
        elif pct < 60:
            return (0, 200, 0)
        elif pct < 70:
            return (0, 200, 128)
        elif pct < 82:
            return (0, 128, 255)
        elif pct < 95:
            return (0, 0, 180)
        elif pct <= 100:
            return (128, 0, 200)
        else:
            return (255, 0, 150)

    # Seção 1 - Nome e HP
    nome_txt = fonte_titulo.render(pokemon.nome, True, (255, 255, 255))
    tela.blit(nome_txt, (x + 10, y + 5))

    vida_pct = pokemon.Vida / pokemon.VidaMax * 100
    vida_str = f"HP: {pokemon.Vida}/{pokemon.VidaMax}"
    vida_txt = fonte_HP.render(vida_str, True, (255, 255, 255))
    tela.blit(vida_txt, (x + largura - vida_txt.get_width() - 10, y + 8))

    pygame.draw.rect(tela, (0, 0, 0), (x + 9, y + 34, 342, 18), 1)
    pygame.draw.rect(tela, cor_percentual(vida_pct), (x + 10, y + 35, (340 * (pokemon.Vida / pokemon.VidaMax)), 16))

    pygame.draw.line(tela, (255, 255, 255), (x, y + 60), (x + largura, y + 60), 2)

    # Seção 2 - Status, Barras e IVs
    atributos = [
        ("HP", pokemon.VidaMax, pokemon.IV_vida, 300),
        ("Attack", pokemon.Atk, pokemon.IV_atk, 120),
        ("Defense", pokemon.Def, pokemon.IV_def, 120),
        ("Sp. Atk", pokemon.Atk_sp, pokemon.IV_atkSP, 120),
        ("Sp. Def", pokemon.Def_sp, pokemon.IV_defSP, 120),
        ("Speed", pokemon.vel, pokemon.IV_vel, 120)
    ]

    for i, (nome, valor, iv_val, valor_max) in enumerate(atributos):
        top = y + 68 + i * 28
        label = fonte_normal.render(f"{nome}:", True, (230, 230, 230))
        tela.blit(label, (x + 10, top))

        val_txt = fonte_Stat.render(f"{valor}", True, (255, 255, 255))
        tela.blit(val_txt, (x + 85, top))

        # Trava para impedir que a barra ultrapasse
        percentual = min(valor / valor_max, 1.0)
        largura_barra = int(percentual * 140)

        pygame.draw.rect(tela, cor_percentual(percentual * 100), (x + 130, top + 4, largura_barra, 16))
        pygame.draw.rect(tela, (0, 0, 0), (x + 130, top + 4, 140, 16), 1)

        iv_txt = fonte_pequena.render(f"IV: {iv_val}%", True, cor_percentual(iv_val))
        tela.blit(iv_txt, (x + 280, top))

    pygame.draw.line(tela, (255, 255, 255), (x, y + 238), (x + largura, y + 238), 2)

    # Seção 3 - Tipos (texto) e imagens
    for i, tipo in enumerate(pokemon.tipo):
        tipo_render = fonte_pequena.render(tipo, True, (255, 255, 255))
        tela.blit(tipo_render, (x + 10, y + 244 + i * 18))

    # Círculos e imagens dos tipos
    for i, tipo in enumerate(pokemon.tipo):
        pos_x = x + 80 + i * 36
        pos_y = y + 245
        centro = (pos_x + 15, pos_y + 15)  # centro do círculo
        pygame.draw.circle(tela, (255, 255, 255), centro, 15)
        pygame.draw.circle(tela, (0, 0, 0), centro, 15, 1)  # borda preta
        if tipo in imagens_tipos:
            img = imagens_tipos[tipo]
            img_rect = img.get_rect(center=centro)
            tela.blit(img, img_rect)


    # XP / Peso deslocados mais para a direita
    xp_txt = fonte_pequena.render(f"XP: {pokemon.xp_atu}", True, (230, 230, 230))
    peso_txt = fonte_pequena.render(f"Peso: {pokemon.custo}", True, (230, 230, 230))
    tela.blit(xp_txt, (x + 165, y + 244))
    tela.blit(peso_txt, (x + 165, y + 262))

    iv_txt = fonte_iv_destaque.render(f"IV: {pokemon.IV}%", True, cor_percentual(pokemon.IV))
    tela.blit(iv_txt, (x + 235, y + 250))

    pygame.draw.line(tela, (255, 255, 255), (x, y + 285), (x + largura, y + 285), 2)

    # Seção 4 - Botões de ataque
    botao_rect1 = pygame.Rect(x + 17, y + 292, 156, 30)
    botao_rect2 = pygame.Rect(x + 187, y + 292, 156, 30)

    Botao_Selecao(
        tela, botao_rect1, pokemon.ataque_normal["nome"], Fonte20,
        (255, 200, 120), (255, 255, 255),
        estado_global=estado_global, eventos=eventos, grossura=2, cor_passagem=AMARELO
    )

    Botao_Selecao(
        tela, botao_rect2, pokemon.ataque_especial["nome"], Fonte20,
        (210, 160, 255), (255, 255, 255),
        estado_global=estado_global, eventos=eventos, grossura=2, cor_passagem=AMARELO
    )

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

def Inventario(local, tela, player, ImagensItens, estado, eventos, PokemonS):
    x, y = local
    largura, altura = 380, 265  # Altura aumentada pra descrição
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
            tela.blit(render, (x + 10, y + 198 + i * 20))  # Descrição em branco

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

def Tabela_Energias(tela, local, player, estadoEnergias,eventos):
    import pygame
    pygame.draw.rect(tela, (30, 30, 30), (*local, 380, 320))  # fundo escuro
    pygame.draw.rect(tela, (255, 255, 255), (*local, 380, 320), 3)  # borda branca

    fonte = pygame.font.SysFont(None, 24)
    fonte_titulo = pygame.font.SysFont(None, 28)  # título sem negrito

    energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 255, 0), "verde": (0, 200, 0),
        "roxa": (128, 0, 128), "rosa": (255, 105, 180),
        "laranja": (255, 140, 0), "marrom": (139, 69, 19),
        "preta": (30, 30, 30), "cinza": (160, 160, 160)
    }

    # Cabeçalho
    titulo = fonte_titulo.render(f"Energias de {player.nome}", True, (255, 255, 255))
    tela.blit(titulo, (local[0] + 190 - titulo.get_width() // 2, local[1] + 10))
    pygame.draw.line(tela, (0, 0, 0), (local[0], local[1] + 34), (local[0] + 380, local[1] + 34), 2)

    # Linhas de energias em 4 colunas: nome1 | valor1 | nome2 | valor2
    chaves = list(player.energias.keys())
    for i in range(5):
        nome1 = chaves[i].capitalize()
        valor1 = str(player.energias[chaves[i]])
        nome2 = chaves[i+5].capitalize()
        valor2 = str(player.energias[chaves[i+5]])

        y = local[1] + 37 + i * 22

        # Colunas ajustadas
        texto_nome1 = fonte.render(nome1 + ":", True, (255, 255, 255))
        texto_valor1 = fonte.render(valor1, True, (255, 255, 255))
        texto_nome2 = fonte.render(nome2 + ":", True, (255, 255, 255))
        texto_valor2 = fonte.render(valor2, True, (255, 255, 255))

        x1 = local[0] + 10
        x2 = local[0] + 130
        x3 = local[0] + 200
        x4 = local[0] + 320

        tela.blit(texto_nome1, (x1, y))
        tela.blit(texto_valor1, (x2, y))
        tela.blit(texto_nome2, (x3, y))
        tela.blit(texto_valor2, (x4, y))

    # Linhas divisoras
    for i in range(6):
        y = local[1] + 34 + i * 22
        # Alteração aqui: primeira e última linha serão brancas
        if i == 0 or i == 5:  # Primeira e última linha
            pygame.draw.line(tela, (255, 255, 255), (local[0] + 2, y), (local[0] + 380 - 2, y), 2)
        else:
            pygame.draw.line(tela, (0, 0, 0), (local[0] + 2, y), (local[0] + 380 - 2, y), 1)

    # Parte inferior: barras verticais (sem alteração)
    base_y = local[1] + 310
    barra_topo = local[1] + 150
    largura_barra = 20
    espaco_total = 360
    margem_x = 10
    espaco_entre = espaco_total // 10

    for i, chave in enumerate(chaves):
        cor = energia_cores[chave]
        valor = min(player.energias[chave], 20)
        altura = int((valor / 20) * (base_y - barra_topo))

        x_centro = local[0] + margem_x + espaco_entre * i + espaco_entre // 2

        # Barra vertical
        pygame.draw.rect(tela, cor, (x_centro - largura_barra//2, base_y - altura, largura_barra, altura))
        pygame.draw.rect(tela, (0, 0, 0), (x_centro - largura_barra//2, barra_topo, largura_barra, base_y - barra_topo), 1)

        # BOTÃO DE SELEÇÃO NA BASE
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


        # # BOTÃO DE SELEÇÃO NA BASE
        # largura_botao = largura_barra + 8
        # altura_botao = 25
        # x_botao = x_centro - largura_botao // 2
        # y_botao = base_y

        # # Chamada do botão de seleção
        # Botao_Selecao(
        #     tela=tela,
        #     espaço=(x_botao, y_botao, largura_botao, altura_botao),
        #     texto=str(player.energias[chave]),
        #     Fonte=fonte,
        #     cor_fundo=cor,
        #     cor_borda_normal=(255, 255, 255),
        #     cor_borda_esquerda=VERMELHO,
        #     cor_borda_direita=AZUL,
        #     cor_passagem=AMARELO,
        #     id_botao=f"energia_{chave}",
        #     estado_global=estadoEnergias,
        #     eventos=eventos,
        #     funcao_esquerdo=None,
        #     funcao_direito=None,
        #     desfazer_esquerdo=None,
        #     desfazer_direito=None,
        #     tecla_esquerda=None,
        #     tecla_direita=None,
        #     grossura=3,
        #     som=None
        # )



            
        






    


