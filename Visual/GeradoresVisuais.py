import pygame
from Visual.Sonoridade import tocar
from Visual.Imagens import CarregarTexturas, Carregar_Imagens_Decks
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

AmareloClaroRar = (255, 255, 153)
AzulClaroRar = (173, 216, 230)
VerdeClaroRar = (144, 238, 144)
CinzaClaroRar = (211, 211, 211)
VermelhoClaroRar = (255, 182, 193)
RoxoClaroRar = (180, 110, 220)

cores_raridade = {
    "Comum": CinzaClaroRar,
    "Incomum": VerdeClaroRar,
    "Raro": AzulClaroRar,
    "Epico": RoxoClaroRar,
    "Mitico": VermelhoClaroRar,
    "Lendario": AmareloClaroRar,
}

energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 215, 0), 
        "verde": (0, 200, 0),
        "roxa": (128, 0, 128), "laranja": (255, 140, 0),
        "preta": (0, 0, 0)
    }

Fonte70 = pygame.font.SysFont(None, 70)
Fonte60 = pygame.font.SysFont(None, 60)
Fonte50 = pygame.font.SysFont(None, 50)
Fonte40 = pygame.font.SysFont(None, 40)
Fonte35 = pygame.font.SysFont(None, 35)
Fonte30 = pygame.font.SysFont(None, 30)
Fonte25 = pygame.font.SysFont(None, 25)
Fonte28 = pygame.font.SysFont(None, 28)
Fonte23 = pygame.font.SysFont(None, 23)
Fonte20 = pygame.font.SysFont(None, 20)
Fonte15 = pygame.font.SysFont(None, 15)

Fontes = [Fonte15,Fonte23,Fonte25,Fonte28,Fonte30,Fonte40,Fonte50]
Cores = [PRETO,BRANCO,CINZA,AZUL,AZUL_CLARO,AMARELO,VERMELHO,VERDE,VERDE_CLARO,LARANJA,ROXO,ROSA,DOURADO,PRATA]

def Botao(tela, texto, espaço, cor_normal, cor_borda, cor_passagem,
           acao, Fonte, estado_clique, grossura=2, tecla_atalho=None,
           mostrar_na_tela=True, eventos=None, som=None):

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
        if isinstance(cor_normal, pygame.Surface):
            imagem = pygame.transform.scale(cor_normal, (largura, altura))
            tela.blit(imagem, (x, y))
        else:
            pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))

        pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), grossura)

        if texto:
            texto_render = Fonte.render(texto, True, (0, 0, 0))
            texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
            tela.blit(texto_render, texto_rect)

    if mostrar_na_tela and mouse_sobre and clique[0] == 1 and not estado_clique.get("pressionado", False):
        estado_clique["pressionado"] = True
        if som:
            tocar(som)
        if acao:
            acao()

    if clique[0] == 0:
        estado_clique["pressionado"] = False

    if tecla_ativada and not estado_clique.get("pressionado_tecla", False):
        estado_clique["pressionado_tecla"] = True
        if som:
            tocar(som)
        if acao:
            acao()

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
    grossura=5, som=None,
    branco=False  # NOVO ARGUMENTO
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

    # Desenhar fundo como imagem ou cor
    if cor_fundo is not None:
        if isinstance(cor_fundo, pygame.Surface):
            imagem_redimensionada = pygame.transform.scale(cor_fundo, (largura, altura))
            tela.blit(imagem_redimensionada, (x, y))
        else:
            pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), grossura)

    cor_texto = (255, 255, 255) if branco else (0, 0, 0)  # NOVA LÓGICA
    texto_render = Fonte.render(texto, True, cor_texto)
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
                if som:
                    tocar(som)

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
                if som:
                    tocar(som)

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

def Botao_Selecao2(
    tela, espaço, texto, Fonte,
    cor_fundo, cor_borda_normal,
    cor_borda_esquerda=None, cor_borda_direita=None,
    cor_passagem=None, id_botao=None,
    estado_global_esquerdo=None, estado_global_direito=None,
    eventos=None,
    funcao_esquerdo=None, funcao_direito=None,
    desfazer_esquerdo=None, desfazer_direito=None,
    tecla_esquerda=None, tecla_direita=None,
    grossura=5, som=None  
):

    x, y, largura, altura = espaço
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    mouse_sobre = x <= mouse[0] <= x + largura and y <= mouse[1] <= y + altura

    if "selecionado" not in estado_global_esquerdo:
        estado_global_esquerdo["selecionado"] = None
    if "selecionado" not in estado_global_direito:
        estado_global_direito["selecionado"] = None

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
    if estado_global_esquerdo["selecionado"] == id_botao:
        modo_selecionado = "esquerdo"
    elif estado_global_direito["selecionado"] == id_botao:
        modo_selecionado = "direito"

    cor_borda_atual = cor_borda_normal
    if modo_selecionado == "esquerdo" and cor_borda_esquerda:
        cor_borda_atual = cor_borda_esquerda
    elif modo_selecionado == "direito" and cor_borda_direita:
        cor_borda_atual = cor_borda_direita
    elif mouse_sobre and cor_passagem:
        cor_borda_atual = cor_passagem

    if isinstance(cor_fundo, pygame.Surface):
        imagem_redimensionada = pygame.transform.scale(cor_fundo, (largura, altura))
        tela.blit(imagem_redimensionada, (x, y))
    else:
        pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))
        
    pygame.draw.rect(tela, cor_borda_atual, (x, y, largura, altura), grossura)

    texto_render = Fonte.render(texto, True, (0, 0, 0))
    texto_rect = texto_render.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_render, texto_rect)

    def aplicar_selecao(modo):
        if modo == "esquerdo":
            if estado_global_esquerdo["selecionado"] == id_botao:
                if desfazer_esquerdo:
                    desfazer_esquerdo()
                estado_global_esquerdo["selecionado"] = None
            else:
                if estado_global_direito["selecionado"] == id_botao:
                    if desfazer_direito:
                        desfazer_direito()
                    estado_global_direito["selecionado"] = None

                if estado_global_esquerdo["selecionado"] and desfazer_esquerdo:
                    desfazer_esquerdo()
                estado_global_esquerdo["selecionado"] = id_botao
                if funcao_esquerdo:
                    funcao_esquerdo()
                if som:
                    tocar(som)

        elif modo == "direito":
            if estado_global_direito["selecionado"] == id_botao:
                if desfazer_direito:
                    desfazer_direito()
                estado_global_direito["selecionado"] = None
            else:
                if estado_global_esquerdo["selecionado"] == id_botao:
                    if desfazer_esquerdo:
                        desfazer_esquerdo()
                    estado_global_esquerdo["selecionado"] = None

                if estado_global_direito["selecionado"] and desfazer_direito:
                    desfazer_direito()
                estado_global_direito["selecionado"] = id_botao
                if funcao_direito:
                    funcao_direito()
                if som:
                    tocar(som)

    if eventos:
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and mouse_sobre:
                if evento.button == 1 and cor_borda_esquerda:
                    if modo_selecionado == "direito" and desfazer_direito:
                        desfazer_direito()
                        estado_global_direito["selecionado"] = None
                    aplicar_selecao("esquerdo")
                elif evento.button == 3 and cor_borda_direita:
                    if modo_selecionado == "esquerdo" and desfazer_esquerdo:
                        desfazer_esquerdo()
                        estado_global_esquerdo["selecionado"] = None
                    aplicar_selecao("direito")
            elif evento.type == pygame.KEYDOWN:
                if evento.key == tecla_esquerda and cor_borda_esquerda:
                    if modo_selecionado == "direito" and desfazer_direito:
                        desfazer_direito()
                        estado_global_direito["selecionado"] = None
                    aplicar_selecao("esquerdo")
                elif evento.key == tecla_direita and cor_borda_direita:
                    if modo_selecionado == "esquerdo" and desfazer_esquerdo:
                        desfazer_esquerdo()
                        estado_global_esquerdo["selecionado"] = None
                    aplicar_selecao("direito")

def adicionar_mensagem(texto, max_linhas=9):
    mensagens_terminal.append(texto)
    if len(mensagens_terminal) > max_linhas:
        mensagens_terminal.pop(0)  

def Terminal(tela, espaço, fonte, cor_fundo, cor_texto):
    x, y, largura, altura = espaço

    # Se cor_fundo for uma imagem (Surface), aplica a imagem como fundo
    if isinstance(cor_fundo, pygame.Surface):
        fundo_redimensionado = pygame.transform.scale(cor_fundo, (largura, altura))
        tela.blit(fundo_redimensionado, (x, y))
    else:
        pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    # Borda do terminal
    pygame.draw.rect(tela, cor_texto, (x, y, largura, altura), 2)

    # Renderizar mensagens
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

def TextoBorda(tela, texto, pos, fonte, cor):
    cor_borda = (0, 0, 0)  # cor da borda preta

    # Renderiza as superfícies
    texto_superficie = fonte.render(texto, True, cor)
    borda_superficie = fonte.render(texto, True, cor_borda)

    # Centraliza
    rect = texto_superficie.get_rect(center=pos)

    # Desenha borda ao redor
    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-2, -2), (-2, 2), (2, -2), (2, 2)]:
        tela.blit(borda_superficie, rect.move(dx, dy))

    # Desenha o texto principal por cima
    tela.blit(texto_superficie, rect)

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

def carregar_frames(pasta):
    def extrair_numero(nome):
        numeros = re.findall(r'\d+', nome)
        return int(numeros[0]) if numeros else -1

    arquivos = [nome for nome in os.listdir(pasta) if nome.lower().endswith((".png", ".jpg", ".jpeg"))]
    arquivos.sort(key=extrair_numero)  # ordena com base nos números encontrados no nome

    frames = []
    for nome in arquivos:
        caminho = os.path.join(pasta, nome)
        imagem = pygame.image.load(caminho).convert_alpha()
        frames.append(imagem)

    return frames

import re
import os

def ordenacao_natural(texto):
    return [int(c) if c.isdigit() else c.lower() for c in re.split('(\d+)', texto)]

def carregar_frames2(pasta):
    frames = []
    arquivos = sorted([f for f in os.listdir(pasta) if f.endswith(".png")], key=ordenacao_natural)
    
    # Pula de 0, 2, 4... (índices pares, que correspondem aos arquivos ímpares se numerados corretamente)
    for i, nome in enumerate(arquivos[::2], start=1):
        caminho = os.path.join(pasta, nome)
        imagem = pygame.image.load(caminho).convert_alpha()
        frames.append(imagem)
        print(i)
    
    return frames

def animar(D_inicial,D_final,anima,tempo=200):
    
    if anima is None:
        anima = pygame.time.get_ticks()
    tempo_passado = pygame.time.get_ticks() - anima
    progresso = min(tempo_passado / tempo, 1.0)
    D = int(D_inicial + (D_final - D_inicial) * progresso)

    return D

def Efeito(tela, posicao, imagem, cor, numero):
    x, y = posicao
    raio = 14
    borda = 3  # Espessura da borda

    fonte = pygame.font.SysFont(None, 15)

    # Círculo com borda colorida e fundo branco
    pygame.draw.circle(tela, cor, (x, y), raio)  # Desenha a borda
    pygame.draw.circle(tela, (255, 255, 255), (x, y), raio - borda)  # Desenha o centro branco

    # Desenha imagem centralizada no círculo, se houver
    if imagem:
        imagem_rect = imagem.get_rect(center=(x, y))
        tela.blit(imagem, imagem_rect)

    # Desenha o número ao lado direito do círculo
    texto = fonte.render(str(numero), True, (0, 0, 0))  # Preto
    texto_rect = texto.get_rect(midleft=(x + raio + 4, y))
    tela.blit(texto, texto_rect)

def quebrar_texto(texto, fonte, largura_max):
    palavras = texto.split()
    linhas = []
    linha_atual = ""
    for palavra in palavras:
        teste = linha_atual + " " + palavra if linha_atual else palavra
        if fonte.size(teste)[0] <= largura_max:
            linha_atual = teste
        else:
            linhas.append(linha_atual)
            linha_atual = palavra
    if linha_atual:
        linhas.append(linha_atual)
    return linhas

def tooltip(area, local, texto, titulo, fonte_texto, fonte_titulo, tela):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    area_rect = pygame.Rect(area)
    local_rect = pygame.Rect(local)

    if not area_rect.collidepoint((mouse_x, mouse_y)):
        return

    # Prepara texto quebrado sem limite artificial de largura
    linhas_texto = quebrar_texto(texto, fonte_texto, local_rect.width - 20)
    altura_texto = fonte_texto.get_height() * len(linhas_texto)

    # Prepara título (sem quebra)
    titulo_render = fonte_titulo.render(titulo, True, (255, 255, 255))
    altura_titulo = titulo_render.get_height()

    # Cria fundo com transparência no tamanho definido por 'local'
    fundo = pygame.Surface((local_rect.width, local_rect.height), pygame.SRCALPHA)
    fundo.fill((0, 0, 0, 200))

    # Desenha o título centralizado horizontalmente no topo
    titulo_rect = titulo_render.get_rect(center=(local_rect.width // 2, altura_titulo // 2 + 5))
    fundo.blit(titulo_render, titulo_rect)

    # Desenha o texto abaixo, centralizado horizontalmente
    y_texto_inicio = altura_titulo + 10
    for i, linha in enumerate(linhas_texto):
        render_linha = fonte_texto.render(linha, True, (255, 255, 255))
        linha_rect = render_linha.get_rect(center=(local_rect.width // 2, y_texto_inicio + fonte_texto.get_height() // 2 + i * fonte_texto.get_height()))
        fundo.blit(render_linha, linha_rect)

    # Blita no local especificado
    tela.blit(fundo, local_rect.topleft)

def Slider(tela, nome, x, y, largura, valor, min_val, max_val, cor_base, cor_botao, eventos, Mostragem=None):
    # Desenha a linha base
    pygame.draw.line(tela, cor_base, (x, y), (x + largura, y), 13)
    
    # Converte valor para posição
    proporcao = (valor - min_val) / (max_val - min_val)
    pos_botao = x + proporcao * largura
    
    # Desenha o botão do slider
    pygame.draw.circle(tela, cor_botao, (int(pos_botao), y), 20)
    
    # Nome e valor
    fonte = pygame.font.SysFont(None, 24)
    if Mostragem == "%":
        texto = fonte.render(f"{nome}: {int(proporcao * 100)}%", True, BRANCO)
    else:
        texto = fonte.render(f"{nome}: {int(valor)}", True, BRANCO)
    
    tela.blit(texto, (x + largura + 25, y - 10))

    # Verifica se está arrastando
    mouse = pygame.mouse.get_pos()
    clicando = pygame.mouse.get_pressed()[0]

    for evento in eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and abs(mouse[0] - pos_botao) < 20 and abs(mouse[1] - y) < 20:
            Slider.arrastando = nome  # Define qual slider está sendo arrastado
        if evento.type == pygame.MOUSEBUTTONUP:
            Slider.arrastando = None

    if Slider.arrastando == nome and clicando:
        # Atualiza valor com base no mouse
        novo_pos = max(x, min(mouse[0], x + largura))
        nova_proporcao = (novo_pos - x) / largura
        return min_val + nova_proporcao * (max_val - min_val)

    return valor

# Atributo estático para controlar arraste
Slider.arrastando = None

TexturasDic = {}
TexturasDic = CarregarTexturas(TexturasDic)

ImagensItens = {}
ImagensPokemon = {}
TiposEnergiaIMG = {}
IconesDeckIMG = {}
ImagensTreinadores = {}
ImagensFichas = {}

ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG,ImagensTreinadores, ImagensFichas = Carregar_Imagens_Decks(
    ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG, ImagensTreinadores, ImagensFichas)