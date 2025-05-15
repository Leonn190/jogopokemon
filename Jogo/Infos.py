import pygame
import Visual.GeradoresVisuais as GV
from Geradores.GeradorAtaques import SelecionaAtaques
from Visual.Imagens import Carrega_Gif_pokemon
from Visual.Efeitos import gerar_gif
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte23, Fonte25, Fonte28, Fonte30, Fonte35, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA,CINZA_ESCURO, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO,VERMELHO_SUPER_CLARO, VERDE, VERDE_CLARO,
    LARANJA,LARANJA_CLARO, ROXO,ROXO_CLARO, ROSA, DOURADO, PRATA,)

def EstadioInfo(pos, tela, Mapa):
    pass


def TreinadorInfo(pos, tela, treinador):
    pass

AtaqueObservado = None

def OlhaAtaque(ataque):
    global AtaqueObservado
    AtaqueObservado = ataque

def FecharAtaque():
    global AtaqueObservado
    AtaqueObservado = None

def Mostrar_Ataque(tela, ataque, posicao=(45, 660), imagens_tipos=None):
    FUNDO = (35, 35, 35)
    BORDA = (255, 255, 255)
    TEXTO = (255, 255, 255)
    LINHA = (200, 200, 200)
    BRANCO = (255, 255, 255)

    energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 255, 0), "verde": (0, 200, 0),
        "roxa": (128, 0, 128), "laranja": (255, 140, 0),
        "preta": (0, 0, 0), 
    }

    fonte_titulo = pygame.font.SysFont("arial", 22, bold=True)
    fonte_desc = pygame.font.SysFont("arial", 16)
    fonte_info = pygame.font.SysFont("arial", 15)
    fonte_infoStat = pygame.font.SysFont("arial", 15, bold=True)

    largura_total = 380
    altura_total = 224
    x, y = posicao

    fundo = pygame.Rect(x, y, largura_total, altura_total)
    pygame.draw.rect(tela, FUNDO, fundo)
    pygame.draw.rect(tela, BORDA, fundo, 2)

    if ataque is not None:
        nome_render = fonte_titulo.render(ataque["nome"], True, TEXTO)
        nome_rect = nome_render.get_rect(center=(x + largura_total // 2, y + 18))
        tela.blit(nome_render, nome_rect)

    if imagens_tipos and "tipo" in ataque:
        tipos = ataque["tipo"]
        raio = 12
        tamanho_icon = 30

        def desenhar_tipo(tipo, centro):
            pygame.draw.circle(tela, (255, 255, 255), centro, raio)
            pygame.draw.circle(tela, (0, 0, 0), centro, raio, 1)
            if tipo in imagens_tipos:
                img = pygame.transform.scale(imagens_tipos[tipo], (tamanho_icon, tamanho_icon))
                img_rect = img.get_rect(center=centro)
                tela.blit(img, img_rect)

        centro_esq = (x + 10 + raio, y + 10 + raio)
        centro_dir = (x + largura_total - 10 - raio, y + 10 + raio)
        if len(tipos) == 1:
            desenhar_tipo(tipos[0], centro_esq)
            desenhar_tipo(tipos[0], centro_dir)
        elif len(tipos) >= 2:
            desenhar_tipo(tipos[0], centro_esq)
            desenhar_tipo(tipos[1], centro_dir)

        pygame.draw.line(tela, LINHA, (x + 10, y + 40), (x + largura_total - 10, y + 40), 2)

        # Descrição
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

        y_desc_inicio = y + 45
        for i, linha in enumerate(linhas[:4]):
            texto_linha = fonte_desc.render(linha.strip(), True, TEXTO)
            tela.blit(texto_linha, (x + 10, y_desc_inicio + i * 18))

        y_divisoria = y + altura_total - 70
        pygame.draw.line(tela, LINHA, (x + 10, y_divisoria), (x + largura_total - 10, y_divisoria), 2)

        # Status
        infos = [
            f"Dano: {round(ataque['dano'] * 100)}%",
            f"Alcance: {ataque['alcance']}m",
            f"Precisão: {ataque['precisão']}%"
        ]

        def obter_cor_status(status, tipo):
            if tipo == "dano":
                if status < 80: return (255, 0, 0)
                elif status < 120: return (255, 255, 0)
                elif status < 160: return (0, 200, 0)
                else: return (180, 90, 255)
            elif tipo == "alcance":
                if status < 20: return (255, 0, 0)
                elif status < 50: return (255, 255, 0)
                elif status < 90: return (0, 200, 0)
                else: return (180, 90, 255)
            elif tipo == "precisão":
                if status < 35: return (255, 0, 0)
                elif status < 70: return (255, 255, 0)
                elif status < 101: return (0, 200, 0)
                else: return (180, 90, 255)

        espacamento = largura_total // len(infos)
        for i, info in enumerate(infos):
            tipo = info.split(":")[0].lower()
            valor_bruto = float(info.split(":")[1].replace("m", "").replace("%", ""))
            texto_info = fonte_info.render(info.split(":")[0], True, TEXTO)
            texto_valor = fonte_infoStat.render(info.split(":")[1], True, obter_cor_status(valor_bruto, tipo))

            centro_x = x + espacamento * i + espacamento // 2
            tela.blit(texto_info, texto_info.get_rect(center=(centro_x, y + altura_total - 60)))
            tela.blit(texto_valor, texto_valor.get_rect(center=(centro_x, y + altura_total - 43)))

        pygame.draw.line(tela, LINHA, (x + 10, y + altura_total - 30), (x + largura_total - 10, y + altura_total - 30), 2)

        # Custo
        custo_label = fonte_info.render("Custo:", True, TEXTO)
        tela.blit(custo_label, (x + 10, y + altura_total - 22))
        if "custo" in ataque:
            for i, energia in enumerate(ataque["custo"]):
                cor = energia_cores.get(energia, BRANCO)
                cx = x + 65 + i * 24
                cy = y + altura_total - 14
                pygame.draw.circle(tela, cor, (cx, cy), 8)

estadoOlharAtaques = {"selecionado_esquerdo": None}
Gif_Ativo = None
Gif_Ativo_Atual = None

def Desenha_Barras_Status(tela, centro, largura_total, altura_maxima, pokemon):
    # Lista dos atributos com nomes abreviados, máximos conhecidos e cores
    atributos = [
        ('Vid', pokemon.get('vida', 0), 350, (100, 255, 100)),
        ('Atk', pokemon.get('atk', 0), 110, (255, 100, 100)),
        ('Def', pokemon.get('def', 0), 110, (255, 220, 100)),
        ('Spa', pokemon.get('atk SP', 0), 110, (200, 100, 255)),
        ('Spd', pokemon.get('def SP', 0), 110, (100, 150, 255)),
        ('Vel', pokemon.get('velocidade', 0), 110, (255, 100, 200))
    ]

    num_atributos = len(atributos)
    espacamento = largura_total / num_atributos
    barra_largura = espacamento * 0.5  # barras mais finas para espaçar mais

    font_nome = Fonte25
    font_valor = Fonte23

    for i, (nome, valor, max_valor, cor_barra) in enumerate(atributos):
        proporcao = min(valor / max_valor, 1.0)
        altura_barra = altura_maxima * proporcao

        x_barra = centro[0] - largura_total / 2 + i * espacamento + (espacamento - barra_largura) / 2
        y_barra = centro[1] + altura_maxima / 2 - altura_barra

        # Fundo da barra (cinza claro)
        pygame.draw.rect(tela, (200, 200, 200), (x_barra, centro[1] - altura_maxima / 2, barra_largura, altura_maxima), 1)
        # Barra preenchida com cor específica
        pygame.draw.rect(tela, cor_barra, (x_barra, y_barra, barra_largura, altura_barra))
        # Contorno da barra preenchida
        pygame.draw.rect(tela, (255, 255, 255), (x_barra, y_barra, barra_largura, altura_barra), 2)

        # Nome abreviado do atributo abaixo da barra
        texto_nome = font_nome.render(nome, True, (255, 255, 255))
        tela.blit(texto_nome, (x_barra + barra_largura / 2 - texto_nome.get_width() / 2, centro[1] + altura_maxima / 2 + 4))

        # Valor no topo da barra
        texto_valor = font_valor.render(f'{int(valor)}', True, (255, 255, 255))
        tela.blit(texto_valor, (x_barra + barra_largura / 2 - texto_valor.get_width() / 2, y_barra - texto_valor.get_height() - 2))

def PokemonInfo(espaço, tela, pokemon, PokemonEvo, PokemonEvoLim, ListaFormas, eventos, TiposEnergiasIMG):
    global Gif_Ativo, Gif_Ativo_Atual, AtaqueObservado, estadoOlharAtaques

    pokemon = ListaFormas[PokemonEvo]

    x, y, w, h = espaço

    setor1_h = h * 0.40
    setor2_h = h * 0.37

    pos_centro_x = x + w // 2
    pos_centro_y = y + int(setor1_h / 2)

    texto_nome = Fonte40.render(pokemon['nome'], True, (255, 255, 255))
    texto_w, texto_h = texto_nome.get_size()
    texto_x = x + (w - texto_w) // 2
    texto_y = y + 10  # Margem superior opcional de 10 pixels
    tela.blit(texto_nome, (texto_x, texto_y))

    if Gif_Ativo is None or Gif_Ativo_Atual != pokemon['nome']:
        frames = Carrega_Gif_pokemon(pokemon['nome'])
        Gif_Ativo = gerar_gif(frames, (pos_centro_x, pos_centro_y + 22), intervalo=24)
        Gif_Ativo_Atual = pokemon['nome']
        estadoOlharAtaques = {"selecionado_esquerdo": None}
        AtaqueObservado = None

    if Gif_Ativo:
        Gif_Ativo.atualizar(tela)

    # ▪️ Desenhar retângulos com setas no setor 1 (puramente estético)
    ret_w = 40  # largura dos retângulos pequenos
    ret_h = 30  # altura dos retângulos pequenos

    margem_borda = 30  # distância mínima das bordas esquerda/direita da ficha

    # ▪️ Esquerda (só se tiver evolução anterior)
    if PokemonEvo > 0:
        ret_esq_x = x + margem_borda
        ret_esq_y = pos_centro_y - ret_h // 2
        pygame.draw.rect(tela, (100, 100, 100), (ret_esq_x, ret_esq_y, ret_w, ret_h), border_radius=6)
        pygame.draw.polygon(tela, (255, 255, 0), [
            (ret_esq_x + ret_w * 0.65, ret_esq_y + ret_h * 0.25),
            (ret_esq_x + ret_w * 0.35, ret_esq_y + ret_h // 2),
            (ret_esq_x + ret_w * 0.65, ret_esq_y + ret_h * 0.75)
        ])

    # ▪️ Direita (só se tiver evolução seguinte)
    if PokemonEvo < PokemonEvoLim:
        ret_dir_x = x + w - margem_borda - ret_w
        ret_dir_y = pos_centro_y - ret_h // 2
        pygame.draw.rect(tela, (100, 100, 100), (ret_dir_x, ret_dir_y, ret_w, ret_h), border_radius=6)
        pygame.draw.polygon(tela, (255, 255, 0), [
            (ret_dir_x + ret_w * 0.35, ret_dir_y + ret_h * 0.25),
            (ret_dir_x + ret_w * 0.65, ret_dir_y + ret_h // 2),
            (ret_dir_x + ret_w * 0.35, ret_dir_y + ret_h * 0.75)
        ])

    linha1_y = y + setor1_h
    linha2_y = linha1_y + setor2_h

    # ▪️ Exibir tipos no canto superior direito do setor 1 com fundo circular branco em linha
    tipos = pokemon["tipo"]
    margem_direita = 10
    espacamento_entre_tipos = 8  # espaço entre as imagens se houver dois tipos
    tipo_img_tamanho = 40  # tamanho das imagens de tipo
    raio_circulo = 18

    # Calcula o total de largura ocupada pelos tipos (imagens + espaçamento)
    total_largura_tipos = len(tipos) * tipo_img_tamanho + (len(tipos) - 1) * espacamento_entre_tipos

    # Começa a partir do canto superior direito menos o total de largura
    inicio_x_tipos = x + w - margem_direita - total_largura_tipos
    pos_y = y + 50  # Fixa em 10px abaixo do topo do setor 1 (ou pode centralizar em setor1_h)

    for i, tipo in enumerate(tipos):
        pos_x = inicio_x_tipos + i * (tipo_img_tamanho + espacamento_entre_tipos)

        centro_x = pos_x + tipo_img_tamanho // 2
        centro_y = pos_y + tipo_img_tamanho // 2

        # Desenhar círculo branco atrás
        pygame.draw.circle(tela, (255, 255, 255), (centro_x, centro_y), raio_circulo)

        # Desenhar imagem do tipo por cima
        img_tipo = TiposEnergiasIMG[tipo]
        img_tipo = pygame.transform.smoothscale(img_tipo, (tipo_img_tamanho, tipo_img_tamanho))
        tela.blit(img_tipo, (pos_x, pos_y))

    pygame.draw.line(tela, (0, 0, 0), (x + 2, linha1_y), (x + w - 2, linha1_y), 3)
    pygame.draw.line(tela, (0, 0, 0), (x + 2, linha2_y), (x + w - 2, linha2_y), 3)

    setor2_top = linha1_y
    setor2_bottom = linha2_y

    linha_v1_x = x + int(w * 0.15)
    linha_v2_x = x + int(w * 0.85)

    pygame.draw.line(tela, (0, 0, 0), (linha_v1_x, setor2_top + 2), (linha_v1_x, setor2_bottom - 1), 3)
    pygame.draw.line(tela, (0, 0, 0), (linha_v2_x, setor2_top + 2), (linha_v2_x, setor2_bottom - 1), 3)

    # 🟦 Centro do setor 2 corrigido
    centro_grafico_x = x + w // 2
    centro_grafico_y = setor2_top + (setor2_h / 2)

    # ▪️ Texto "Evolui" e XP na lateral esquerda do setor 2
    texto_evolui = Fonte20.render("Evolui:", True, (255, 255, 255))
    texto_xp = Fonte25.render(f"{pokemon['XP']} Xp", True, (255, 255, 255))

    # Posição horizontal: centro da área entre x e linha_v1_x
    centro_lateral_esq_x = x + (linha_v1_x - x) // 2

    # Desenhar "Evolui" no topo da lateral esquerda
    tela.blit(texto_evolui, (
        centro_lateral_esq_x - texto_evolui.get_width() // 2,
        setor2_top + 10
    ))

    # Desenhar o XP logo abaixo
    tela.blit(texto_xp, (
        centro_lateral_esq_x - texto_xp.get_width() // 2,
        setor2_top + 25
    ))

    # ▪️ Texto "Altura" e XP na lateral esquerda do setor 2
    texto_evolui = Fonte20.render("Altura:", True, (255, 255, 255))
    texto_xp = Fonte23.render(f"{pokemon['H']} M", True, (255, 255, 255))

    # Posição horizontal: centro da área entre x e linha_v1_x
    centro_lateral_esq_x = x + (linha_v1_x - x) // 2

    # Desenhar "Altura" no topo da lateral esquerda
    tela.blit(texto_evolui, (
        centro_lateral_esq_x - texto_evolui.get_width() // 2,
        setor2_top + 90
    ))

    # Desenhar o Metros logo abaixo
    tela.blit(texto_xp, (
        centro_lateral_esq_x - texto_xp.get_width() // 2,
        setor2_top + 105
    ))

    # ▪️ Texto "Peso" e XP na lateral esquerda do setor 2
    texto_evolui = Fonte20.render("Peso:", True, (255, 255, 255))
    texto_xp = Fonte23.render(f"{pokemon['W']} Kg", True, (255, 255, 255))

    # Posição horizontal: centro da área entre x e linha_v1_x
    centro_lateral_esq_x = x + (linha_v1_x - x) // 2

    # Desenhar "Peso" no topo da lateral esquerda
    tela.blit(texto_evolui, (
        centro_lateral_esq_x - texto_evolui.get_width() // 2,
        setor2_top + 160
    ))

    # Desenhar o KG logo abaixo
    tela.blit(texto_xp, (
        centro_lateral_esq_x - texto_xp.get_width() // 2,
        setor2_top + 175
    ))

        # ▪️ Texto "Moves" e quantidade no topo da lateral direita
    texto_moves = Fonte20.render("Moves:", True, (255, 255, 255))
    valor_moves = Fonte25.render(str(pokemon.get("moves", "-")), True, (255, 255, 255))

    centro_lateral_dir_x = linha_v2_x + (x + w - linha_v2_x) // 2

    tela.blit(texto_moves, (
        centro_lateral_dir_x - texto_moves.get_width() // 2,
        setor2_top + 10
    ))

    tela.blit(valor_moves, (
        centro_lateral_dir_x - valor_moves.get_width() // 2,
        setor2_top + 25
    ))

    # ▪️ Texto "Custo" e valor na parte inferior da lateral direita
    texto_custo = Fonte20.render("Custo:", True, (255, 255, 255))
    valor_custo = Fonte25.render(str(pokemon['custo']), True, (255, 255, 255))

    tela.blit(texto_custo, (
        centro_lateral_dir_x - texto_custo.get_width() // 2,
        setor2_top + 90
    ))

    tela.blit(valor_custo, (
        centro_lateral_dir_x - valor_custo.get_width() // 2,
        setor2_top + 105
    ))

    # ▪️ Texto "Custo" e valor na parte inferior da lateral direita
    texto_custo = Fonte20.render("Classe:", True, (255, 255, 255))
    valor_custo = Fonte25.render("", True, (255, 255, 255))

    tela.blit(texto_custo, (
        centro_lateral_dir_x - texto_custo.get_width() // 2,
        setor2_top + 160
    ))

    tela.blit(valor_custo, (
        centro_lateral_dir_x - valor_custo.get_width() // 2,
        setor2_top + 175
    ))

    # Ajuste automático da largura e altura do gráfico dentro do setor 2
    largura_grafico = w * 0.6
    altura_grafico = setor2_h * 0.8

    Desenha_Barras_Status(
        tela,
        centro=(int(centro_grafico_x), int(centro_grafico_y - 6)),
        largura_total=int(largura_grafico + 15),
        altura_maxima=int(altura_grafico + 5),
        pokemon=pokemon
    )

    moves = []
    for ataque in pokemon["movelist"]:
        moves.append(SelecionaAtaques(ataque))

    setor3_top = linha2_y

    margem_lateral = 20
    largura_botao = (w - 2 * margem_lateral - 10) // 2  # 10px entre colunas
    espaco_entre_botoes = 10
    altura_botao = 32
    espaco_entre_linhas = 8

    movimentos = moves[:6]  # Apenas os 6 primeiros ataques se existirem

    for i, movimento in enumerate(movimentos):
        if movimento is not None:
            linha = i // 2
            coluna = i % 2

            pos_y = setor3_top + 12 + linha * (altura_botao + espaco_entre_linhas)
            pos_x = x + margem_lateral + coluna * (largura_botao + espaco_entre_botoes)

            botao_rect = pygame.Rect(pos_x, pos_y - 2, largura_botao, altura_botao)

            GV.Botao_Selecao(
                tela, botao_rect, movimento["nome"], Fonte23,
                (180,180,180), (255, 255, 255),
                funcao_esquerdo=lambda mov=movimento: OlhaAtaque(mov),
                desfazer_esquerdo=lambda: FecharAtaque(),
                funcao_direito=None,
                desfazer_direito=None,
                id_botao=f"{pokemon["vida"]}{movimento['nome']}",
                cor_borda_esquerda=VERMELHO,
                cor_borda_direita=AZUL,
                estado_global=estadoOlharAtaques, eventos=eventos,
                grossura=2, cor_passagem=AMARELO
            )
    
    if AtaqueObservado is not None:
        Mostrar_Ataque(tela,AtaqueObservado,imagens_tipos=TiposEnergiasIMG)


def ItemInfo(pos, tela, item):
    pass