import pygame
import Visual.GeradoresVisuais as GV
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import VERMELHO,AMARELO,BRANCO,Fonte20,Fonte15,Fonte25

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

def Status_Pokemon(pos, tela, pokemon, imagens_tipos, player, eventos=None, estado_global=None, SoV=None):
    x, y = pos
    largura, altura = 360, 368
    global AtaqueSV

    if pokemon in player.pokemons:
        cor = (35,35,35)
    else:
        cor = (80,35,35)

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

        # -- Botões de movimentos
        movimentos = [pokemon.movimento1, pokemon.movimento2, pokemon.movimento3, pokemon.movimento4]
        cores_estilos = {
            "N": (255, 165, 0),   # Laranja
            "E": (210, 160, 255), # Roxo
            "S": (144, 238, 144)  # Verde
            }

        for i, movimento in enumerate(movimentos):
            if movimento is not None:
                pos_x = x + 17 + (i % 2) * 170
                pos_y = y + 292 + (i // 2) * 38
                cor_fundo = cores_estilos.get(movimento["estilo"], (200, 200, 200))  # Cor cinza se estilo desconhecido

                botao_rect = pygame.Rect(pos_x, pos_y, 156, 30)
                GV.Botao_Selecao(
                    tela, botao_rect, movimento["nome"], Fonte20,
                    cor_fundo, (255, 255, 255),
                    funcao_esquerdo=lambda mov=movimento:seleciona_ataque(mov, SoV),
                    desfazer_esquerdo=lambda SoV=SoV:desseleciona_ataque(SoV),
                    id_botao=f"{pokemon.ID}{movimento['nome']}",
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

H = None
B1 = {"estado": False}

def Inventario(local, tela, player, ImagensItens, estado, eventos, PokemonS):
    x, y = local
    largura, altura = 380, 285  # ⬅️ Aumentado para 285

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
        GV.Botao(
            tela=tela,
            texto="",
            espaço=espaço_botao,
            cor_normal=(0,0,0),  # Fundo escuro para o botão
            cor_borda=(0,0,0),   # Borda discreta
            cor_passagem=(0,0,0), # Cor ao passar o mouse
            acao=lambda i=i: player.usar_item(i, PokemonS,tela),
            Fonte=Fonte,
            estado_clique=B1,
            grossura=2,
            tecla_atalho=None,
            mostrar_na_tela=True,
            eventos=eventos,
            som=None)

        # Botão de seleção
        GV.Botao_Selecao(
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

def Tabela_Energias(tela, local, player, estadoEnergias, eventos):

    x, y = local
    largura, altura = 380, 320

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

    
    chaves = list(player.energias.keys())
    for i in range(5):
        nome1 = chaves[i].capitalize()
        valor1 = str(player.energias[chaves[i]])
        nome2 = chaves[i+5].capitalize()
        valor2 = str(player.energias[chaves[i+5]])

        y_pos = y + 37 + i * 22

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

        pygame.draw.rect(tela, cor, (x_centro - largura_barra // 2, base_y - altura, largura_barra, altura))
        pygame.draw.rect(tela, (0, 0, 0), (x_centro - largura_barra // 2, barra_topo, largura_barra, base_y - barra_topo), 1)

        largura_botao = largura_barra + 8
        altura_botao = 18
        x_botao = x_centro - largura_botao // 2
        y_botao = base_y + 7
        
        GV.Botao(tela, "",(x_botao, y_botao, largura_botao, altura_botao), (35,35,35), BRANCO, (35,35,35),
           lambda:player.muda_descarte(chave), Fonte15, BB[i], grossura=2, tecla_atalho=None,
           mostrar_na_tela=True, eventos=None, som=None)

        pygame.draw.circle(tela, cor, (x_centro, base_y + 3), 12)
        pygame.draw.circle(tela, (255, 255, 255), (x_centro, base_y + 3), 12, 1)
        cor_texto = (255, 255, 255) if sum(cor) < 300 else (0, 0, 0)
        num = fonte.render(str(player.energias[chave]), True, cor_texto)
        tela.blit(num, (x_centro - num.get_width() // 2, base_y - num.get_height() // 2 + 3))

        if chave in player.energiasDesc:
            GV.Texto_caixa(tela,f"D{player.energiasDesc.index(chave)}",(x_botao,( base_y - 150), largura_botao, 20),Fonte25,(30,30,30),(30,30,30),BRANCO)

def Atacar(PokemonS,PokemonV,PokemonA,player,inimigo):
    if PokemonS.PodeAtacar == True:
        if PokemonS is None or PokemonA is None or AtaqueS is None:
            print (PokemonS,PokemonA,AtaqueS)
            GV.adicionar_mensagem("Selecione um alvo, um ataque, e um atacante")
            tocar("Bloq")
            return
        
    else:
        GV.adicionar_mensagem("Esse pokemon não pode realizar ataques")
        tocar("Bloq")
        return
    