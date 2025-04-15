import pygame
import os

pygame.font.init()
pygame.mixer.init()

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

def Texto_caixa(tela, texto, espaço, fonte, cor_fundo, borda=PRETO, grossura=3):
  
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

def limpa_terminal():
    mensagens_terminal.clear()

def tocar(som):
    if som:
        som.play()

def Status_Pokemon(pos, tela, pokemon, cor, eventos=None, estado_global=None):
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
    vida_txt = fonte_HP.render(vida_str, True, (255, 255, 255))  # cor fixa branca
    tela.blit(vida_txt, (x + largura - vida_txt.get_width() - 10, y + 8))

    # Barra de vida corrigida
    pygame.draw.rect(tela, (0, 0, 0), (x + 9, y + 34, 342, 18), 1)  # Barra de fundo
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

        # Barra de status corrigida (sem lacunas)
        largura_barra = int((valor / valor_max) * 140)
        pygame.draw.rect(tela, cor_percentual(valor / valor_max * 100), (x + 130, top + 4, largura_barra, 16))
        pygame.draw.rect(tela, (0, 0, 0), (x + 130, top + 4, 140, 16), 1)  # Barra de fundo agora tem a largura ajustada corretamente
    
        # Reposicionar os IVs mais à direita
        iv_txt = fonte_pequena.render(f"IV: {iv_val}%", True, cor_percentual(iv_val))
        tela.blit(iv_txt, (x + 280, top))  # Ajustando a posição para mais à direita

    pygame.draw.line(tela, (255, 255, 255), (x, y + 238), (x + largura, y + 238), 2)

    # Seção 3 - Tipos / XP / Peso / IV médio
    for i, tipo in enumerate(pokemon.tipo):
        tipo_render = fonte_pequena.render(tipo, True, (255, 255, 255))
        tela.blit(tipo_render, (x + 10, y + 244 + i * 18))

    xp_txt = fonte_pequena.render(f"XP: {pokemon.xp_atu}", True, (230, 230, 230))
    peso_txt = fonte_pequena.render(f"Peso: {pokemon.custo}", True, (230, 230, 230))
    tela.blit(xp_txt, (x + 120, y + 244))
    tela.blit(peso_txt, (x + 120, y + 262))

    iv_txt = fonte_iv_destaque.render(f"IV: {pokemon.IV}%", True, cor_percentual(pokemon.IV))
    tela.blit(iv_txt, (x + 230, y + 250))  # IV médio movido mais para a esquerda

    # Linha separadora ajustada
    pygame.draw.line(tela, (255, 255, 255), (x, y + 285), (x + largura, y + 285), 2)  # Linha 5px mais para baixo

    # Seção 4 - Botões de ataque (reposicionados e reduzidos)
    botao_rect1 = pygame.Rect(x + 17, y + 292, 156, 30)  # Botões movidos 5px para baixo
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







    


