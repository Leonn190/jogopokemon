import pygame
import random
import math
import Visual.GeradoresVisuais as GV
from Visual.Sonoridade import tocar
from Visual.Efeitos import adicionar_efeito
from Funções2 import VAcerta,VCusto, distancia_entre_pokemons
from Geradores.GeradorAtaques import SelecionaAtaques
from Visual.GeradoresVisuais import VERMELHO,AMARELO,BRANCO,CINZA,PRETO,AZUL,Fonte20,Fonte15,Fonte25,Fonte50,VERDE_CLARO, energia_cores

AtaqueS = None
AtaqueSV = None
AtaqueV = None

estadoMostraAtaqueS = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
    }
estadoMostraAtaqueV = {
    "selecionado_esquerdo": None,
    "selecionado_direito": None
    }

EstadoDaPergunta = {
    "estado": False,
    "info": None,
    "opçoes": None,
    "funçao": None
}

Bpergunta = {"estado": False}

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
        estadoMostraAtaqueS["selecionado_esquerdo"] = None
    else:
        AtaqueSV = None
        estadoMostraAtaqueV["selecionado_direito"] = None
        estadoMostraAtaqueV["selecionado_esquerdo"] = None

def Vizualiza_ataque(ataque,SoV):
    global AtaqueS,AtaqueSV,AtaqueV
    if SoV == "S":
        AtaqueV = ataque
        AtaqueS = ataque
    else:
        AtaqueSV = ataque

def Oculta_ataque(SoV):
    global AtaqueS,AtaqueSV,AtaqueV
    if SoV == "S": 
        AtaqueS = None
        AtaqueV = None
        estadoMostraAtaqueS["selecionado_direito"] = None
    else:
        AtaqueSV = None
        estadoMostraAtaqueV["selecionado_direito"] = None
        estadoMostraAtaqueV["selecionado_esquerdo"] = None

fonte_titulo = pygame.font.SysFont("arial", 25, True)
fonte_HP = pygame.font.SysFont("arial", 23, True)
fonte_Stat = pygame.font.SysFont("arial", 20, True)
fonte_normal = pygame.font.SysFont("arial", 20)
fonte_pequena = pygame.font.SysFont("arial", 18)
fonte_iv = pygame.font.SysFont("arial", 18, True)
fonte_iv_destaque = pygame.font.SysFont("arial", 22, True)

def Status_Pokemon(pos, tela, pokemon, imagens_tipos, player, eventos, SoV, Mapa, Alvo):
    x, y = pos
    largura, altura = 380, 385  # Aumentado de 368 para 385
    global AtaqueSV

    if SoV == "S":
        estado_global = estadoMostraAtaqueS
    else:
        estado_global = estadoMostraAtaqueV

    if pokemon in player.pokemons:
        cor = (35, 35, 35)
    else:
        cor = (70, 35, 35)

    ret = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, cor, ret)
    pygame.draw.rect(tela, (255, 255, 255), ret, 2)

    if pokemon is not None:

        def cor_percentual(pct):
            if pct < 15:
                return (255, 0, 0)
            elif pct < 25:
                return (255, 165, 0)
            elif pct < 40:
                return (240, 255, 0)
            elif pct < 65:
                return (0, 255, 0)
            elif pct < 90:
                return (0, 200, 255)
            elif pct <= 100:
                return (255, 0, 255)
                
        def cor_percentual_vida(pct):
            if pct > 60:
                return (0, 200, 0)
            elif pct > 30:
                return (255, 200, 0)
            else:
                return (200, 0, 0)

        nome_txt = fonte_titulo.render(pokemon.nome, True, (255, 255, 255))
        tela.blit(nome_txt, (x + 10, y + 5))

        # Cálculo de vida e barreira
        vida = max(pokemon.Vida, 0)
        vida_max = max(pokemon.VidaMax, 1)
        barreira = max(getattr(pokemon, "barreira", 0), 0)

        vida_pct = vida / vida_max * 100
        vida_str = f"HP: {int(vida) + barreira}/{int(vida_max)}"
        vida_txt = fonte_HP.render(vida_str, True, (255, 255, 255))
        tela.blit(vida_txt, (x + largura - vida_txt.get_width() - 10, y + 8))

        largura_total = 360
        proporcao_vida = vida / vida_max
        proporcao_barreira = barreira / vida_max

        largura_vida = int(largura_total * proporcao_vida)
        largura_barreira = int(largura_total * proporcao_barreira)

        # Garante que a soma não ultrapasse o total da barra
        if largura_vida + largura_barreira > largura_total:
            excesso = (largura_vida + largura_barreira) - largura_total
            largura_vida = max(largura_vida - excesso, 0)

        # Desenha borda
        pygame.draw.rect(tela, (0, 0, 0), (x + 9, y + 34, largura_total + 2, 18), 1)

        # Desenha vida
        pygame.draw.rect(tela, cor_percentual_vida(vida_pct), (x + 10, y + 35, largura_vida, 16))

        # Desenha barreira à direita da vida (se houver)
        if largura_barreira > 0:
            pygame.draw.rect(tela, (0, 150, 255), (x + 10 + largura_vida, y + 35, largura_barreira, 16))

        pygame.draw.line(tela, (255, 255, 255), (x, y + 60), (x + largura, y + 60), 2)

        # Ajuste: aumentamos o espaçamento entre os atributos
        # SETOR 2 – Atributos com IVs e barras
        atributos = [
            ("HP", pokemon.VidaMax, pokemon.IV_vida, 350),
            ("Attack", pokemon.Atk, pokemon.IV_atk, 110),
            ("Defense", pokemon.Def, pokemon.IV_def, 110),
            ("Sp. Atk", pokemon.Atk_sp, pokemon.IV_atkSP, 110),
            ("Sp. Def", pokemon.Def_sp, pokemon.IV_defSP, 110),
            ("Speed", pokemon.vel, pokemon.IV_vel, 110)
        ]

        altura_total = 238 - 48  # altura disponível: 178px
        num_barras = 6
        altura_barra = 19
        num_espacos = num_barras + 1  # 7 espaços
        espacamento = (altura_total - num_barras * altura_barra) / num_espacos  # espaçamento vertical entre as barras

        for i, (nome, valor, iv_val, valor_max) in enumerate(atributos):
            top = y + 60 + espacamento * (i + 1) + altura_barra * i

            # Texto do nome do atributo
            label = fonte_normal.render(f"{nome}:", True, (230, 230, 230))
            tela.blit(label, (x + 10, int(top + 1)))

            # Valor numérico do atributo
            val_txt = fonte_Stat.render(f"{valor}", True, (255, 255, 255))
            tela.blit(val_txt, (x + 80, int(top + 2)))

            # Barra de progresso do atributo
            percentual = min(valor / valor_max, 1.0)
            largura_barra = int(percentual * 179)

            pygame.draw.rect(tela, cor_percentual(percentual * 100), (x + 116, int(top + 4), largura_barra, altura_barra))
            pygame.draw.rect(tela, (0, 0, 0), (x + 116, int(top + 4), 179, altura_barra), 1)

            # Texto do IV
            iv_txt = fonte_iv.render(f"IV: {iv_val}%", True, cor_percentual(iv_val))
            tela.blit(iv_txt, (x + 301, int(top + 2)))

        # Ajuste: linha divisória após os atributos
        pygame.draw.line(tela, (255, 255, 255), (x, y + 255), (x + largura, y + 255), 2)  # Era 238, agora +17

        # Tipos e info geral agora deslocados +17
        for i, tipo in enumerate(pokemon.tipo):
            tipo_render = fonte_pequena.render(tipo, True, (255, 255, 255))
            tela.blit(tipo_render, (x + 10, y + 261 + i * 18))  # Era 244

        for i, tipo in enumerate(pokemon.tipo):
            pos_x = x + 80 + i * 36
            pos_y = y + 262  # Era 245
            centro = (pos_x + 15, pos_y + 15)
            pygame.draw.circle(tela, (255, 255, 255), centro, 15)
            pygame.draw.circle(tela, (0, 0, 0), centro, 15, 1)
            if tipo in imagens_tipos:
                img = imagens_tipos[tipo]
                img_rect = img.get_rect(center=centro)
                tela.blit(img, img_rect)

        # Textos diversos
        tela.blit(fonte_pequena.render(f"XP: {pokemon.xp_atu}", True, (230, 230, 230)), (x + 160, y + 261))
        tela.blit(fonte_pequena.render(f"CT: {pokemon.custo}", True, (230, 230, 230)), (x + 160, y + 279))
        tela.blit(fonte_pequena.render(f"{pokemon.Altura}M", True, (230, 230, 230)), (x + 215, y + 261))
        tela.blit(fonte_pequena.render(f"{pokemon.Peso}Kg", True, (230, 230, 230)), (x + 215, y + 279))

        iv_txt = fonte_iv_destaque.render(f"IV: {pokemon.IV}%", True, cor_percentual(pokemon.IV))
        tela.blit(iv_txt, (x + 275, y + 267))  # Era 250

        # Linha final (ajustada)
        pygame.draw.line(tela, (255, 255, 255), (x, y + 302), (x + largura, y + 302), 2)

        # Botões de movimento (também deslocados)
        movimentos = [pokemon.movimento1, pokemon.movimento2, pokemon.movimento3, pokemon.movimento4]
        cores_estilos = {
            "N": (255, 165, 0),
            "E": (210, 160, 255),
            "S": (144, 238, 144)
        }

        largura_interface = 380  # Ajuste conforme a largura da área de botões
        margem_lateral = 16
        espaco_entre_botoes = 16
        largura_botao = (largura_interface - 2 * margem_lateral - espaco_entre_botoes) // 2

        if EstadoDaPergunta["estado"] == False or SoV == "V":
            for i, movimento in enumerate(movimentos):
                if movimento is not None:
                    linha = i // 2
                    coluna = i % 2
                    pos_y = y + 309 + linha * 38  # Ajuste vertical (309 é a base + 38 por linha)
                    pos_x = x + margem_lateral + coluna * (largura_botao + espaco_entre_botoes)

                    cor_fundo = cores_estilos.get(movimento["estilo"], (200, 200, 200))

                    botao_rect = pygame.Rect(pos_x, pos_y, largura_botao, 30)

                    

                    GV.Botao_Selecao(
                        tela, botao_rect, movimento["nome"], Fonte20,
                        cor_fundo, (255, 255, 255),
                        funcao_esquerdo=lambda mov=movimento: seleciona_ataque(mov, SoV),
                        desfazer_esquerdo=lambda SoV=SoV: desseleciona_ataque(SoV),
                        funcao_direito=lambda mov=movimento: Vizualiza_ataque(mov, SoV),
                        desfazer_direito=lambda SoV=SoV: Oculta_ataque(SoV),
                        id_botao=f"{pokemon.ID}{movimento['nome']}",
                        cor_borda_esquerda=VERMELHO,
                        cor_borda_direita=AZUL,
                        estado_global=estado_global, eventos=eventos,
                        grossura=2, cor_passagem=AMARELO
                    )
        else:
            for i, opçao in enumerate(EstadoDaPergunta["opçoes"]):
                if opçao is not None:
                    linha = i // 2
                    coluna = i % 2
                    pos_y = y + 309 + linha * 38  # Ajuste vertical (309 é a base + 38 por linha)
                    pos_x = x + margem_lateral + coluna * (largura_botao + espaco_entre_botoes)

                    botao_rect = pygame.Rect(pos_x, pos_y, largura_botao, 30)
                    
                    
                    try:
                        PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc = EstadoDaPergunta["info"]

                        GV.Botao(tela, opçao, botao_rect, CINZA, PRETO, AZUL,lambda: EstadoDaPergunta["funçao"](PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,opçao),Fonte20, Bpergunta, 3, None, True, eventos)
                    except ValueError:
                        GV.Botao(tela, opçao, botao_rect, CINZA, PRETO, AZUL,lambda: EstadoDaPergunta["funçao"](EstadoDaPergunta["info"][0],EstadoDaPergunta["info"][1],EstadoDaPergunta["info"][2],opçao),Fonte20, Bpergunta, 3, None, True, eventos)

        if x > 1600:
            desseleciona_ataque(SoV)
            Oculta_ataque(SoV)
            EstadoDaPergunta["estado"] = False

        if SoV == "V":
            pokemon = None

        if SoV == "S":
            if AtaqueV is not None:
                Mostrar_Ataque(tela, AtaqueV, Mapa, (1540, y + 60), imagens_tipos, Alvo, pokemon)
            if AtaqueS is not None:
                Desenhar_Alcance(tela,pokemon,AtaqueS["alcance"],Mapa.Metros, Alvo, AtaqueS["precisão"], Mapa)

        else:
            if AtaqueSV is not None:
                Mostrar_Ataque(tela, AtaqueSV, Mapa, (1540, y + 60), imagens_tipos)


    # Fontes menores para caber melhor na ficha reduzida
fonte_titulo = pygame.font.SysFont("arial", 22, bold=True)
fonte_desc = pygame.font.SysFont("arial", 17)
fonte_info = pygame.font.SysFont("arial", 15)
fonte_infoStat = pygame.font.SysFont("arial", 15, bold=True)

def Mostrar_Ataque(tela, ataque, Mapa, posicao=(100, 100), imagens_tipos=None, Alvo=None, Pokemon=None):
    FUNDO = (35, 35, 35)
    BORDA = (255, 255, 255)
    TEXTO = (255, 255, 255)
    LINHA = (200, 200, 200)
    BRANCO = (255, 255, 255)

    energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 255, 0), "verde": (0, 200, 0),
        "roxa": (128, 0, 128), 
        "laranja": (255, 140, 0), 
        "preta": (0, 0, 0),
    }

    # Novo tamanho da ficha
    largura_total = 380
    altura_total = 244
    x, y = posicao

    # Fundo da ficha
    fundo = pygame.Rect(x, y, largura_total, altura_total)
    pygame.draw.rect(tela, FUNDO, fundo)
    pygame.draw.rect(tela, BORDA, fundo, 2)

    if ataque is not None:
        nome_render = fonte_titulo.render(ataque["nome"], True, TEXTO)
        nome_rect = nome_render.get_rect(center=(x + largura_total // 2, y + 20))
        tela.blit(nome_render, nome_rect)

    # Tipos
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
        for i, linha in enumerate(linhas[:5]):  # Menos linhas por espaço
            texto_linha = fonte_desc.render(linha.strip(), True, TEXTO)
            tela.blit(texto_linha, (x + 10, y_desc_inicio + i * 18))

        y_divisoria = y + altura_total - 65
        pygame.draw.line(tela, LINHA, (x + 10, y_divisoria), (x + largura_total - 10, y_divisoria), 2)

        # Status
        alcance = ataque["alcance"]
        precisao = ataque["precisão"]

        if alcance != 0:
            if Alvo is not None:
                distancia = distancia_entre_pokemons(Alvo,Pokemon,Mapa.Metros)
                if distancia > alcance:
                    over = distancia - alcance
                    precisao -= over * 5
        
        infos = [
            f"Dano: {round(ataque['dano'] * 100)}%",
            f"Alcance: {round(alcance)}m" if not ataque.get("global") else "Alcance: Global",
            f"Precisão: {round(precisao)}%"
        ]

        def obter_cor_status(status, tipo):
            if tipo == "dano":
                if status < 80: return (255, 0, 0)
                elif status < 120: return (255, 255, 0)
                elif status < 160: return (0, 200, 0)
                else: return (180, 90, 255)
            elif tipo == "alcance":
                if isinstance(status, str) and status.lower() == "global":
                    return (180, 90, 255)
                elif status == 0: return (180, 90, 255)
                elif status < 5: return (255, 0, 0)
                elif status < 8: return (255, 255, 0)
                elif status < 90: return (0, 200, 0)
                else: return (180, 90, 255)
            elif tipo == "precisão":
                if status < 35: return (255, 0, 0)
                elif status < 70: return (255, 255, 0)
                elif status < 101: return (0, 200, 0)
                else: return (180, 90, 255)

        espacamento = largura_total // len(infos)
        for i, info in enumerate(infos):
            tipo = info.split(":")[0].lower().strip()
            valor_str = info.split(":")[1].replace("m", "").replace("%", "").strip()

            try:
                valor_bruto = float(valor_str)
            except ValueError:
                valor_bruto = "global"  # ou qualquer string para indicar valor especial

            cor = obter_cor_status(valor_bruto, tipo)
            texto_info = fonte_info.render(info.split(":")[0], True, TEXTO)
            texto_valor = fonte_infoStat.render(info.split(":")[1], True, cor)

            centro_x = x + espacamento * i + espacamento // 2
            tela.blit(texto_info, texto_info.get_rect(center=(centro_x, y + altura_total - 55)))
            tela.blit(texto_valor, texto_valor.get_rect(center=(centro_x, y + altura_total - 38)))

        pygame.draw.line(tela, LINHA, (x + 10, y + altura_total - 28), (x + largura_total - 10, y + altura_total - 28), 2)

        # Custo
        custo_label = fonte_info.render("Custo:", True, TEXTO)
        tela.blit(custo_label, (x + 10, y + altura_total - 22))
        if "custo" in ataque:
            for i, energia in enumerate(ataque["custo"]):
                cor = energia_cores.get(energia, BRANCO)
                cx = x + 65 + i * 24
                cy = y + altura_total - 14
                pygame.draw.circle(tela, cor, (cx, cy), 8)

H = None
B1 = {"estado": False}
BotaoCompraEnergia = {"estado": False}

FonteMenor = pygame.font.SysFont("arial", 16)
Fonte = pygame.font.SysFont("arial", 22, True)

fonte_ = pygame.font.SysFont(None, 24)
fonte_titulo_ = pygame.font.SysFont(None, 28)

def Inventario(local, tela, player, ImagensItens, estado, eventos, PokemonS, Mapa, Baralho, estadoEnergias):
    x, y = local
    largura, altura = 380, 420
    cor_borda = (255, 255, 255)

    # 1. Cabeçalho
    pygame.draw.rect(tela, (35, 35, 35), (x, y, largura, 30))

    # 2. Fundo do inventário
    pygame.draw.rect(tela, (35, 35, 35), (x, y, largura, altura))

    # 3. Borda branca
    pygame.draw.rect(tela, cor_borda, (x, y, largura, altura), 2)

    # 4. Texto do cabeçalho
    texto_nome = Fonte.render(f"Inventário de {player.nome}", True, (255, 255, 255))
    tela.blit(texto_nome, (x + largura // 2 - texto_nome.get_width() // 2, y + 5))

    # 5. Linha divisória abaixo do cabeçalho
    pygame.draw.line(tela, (255, 255, 255), (x, y + 30), (x + largura - 2, y + 30), 2)

    def TiraDescriçao():
        global H
        estado["selecionado_esquerdo"] = None
        H = None

    for i, item in enumerate(player.inventario[:12]):
        col = i % 6
        row = i // 6
        bx = x + col * 63
        by = y + 30 + row * 63  # ✅ novo cabeçalho é 30 px
        espaço_botao = pygame.Rect(bx, by, 63, 63)
        nome_item = item["nome"]
        classe_item = item.get("classe", "").lower()

        def Descriçao(item):
            global H
            H = item

        if classe_item == "pokebola":
            cor_fundo = (255, 100, 100)
        elif classe_item == "poçao":
            cor_fundo = (100, 150, 255)
        elif classe_item in ["caixa", "coletor"]:
            cor_fundo = (100, 200, 100)
        elif classe_item == "amplificador":
            cor_fundo = (255, 150, 50)
        elif classe_item == "fruta":
            cor_fundo = (255, 255, 100)
        else:
            cor_fundo = (150, 100, 255)

        GV.Botao_Selecao(
            tela=tela,
            espaço=espaço_botao,
            texto="",
            Fonte=Fonte,
            cor_fundo=cor_fundo,
            cor_borda_normal=(255, 255, 255),
            cor_borda_esquerda= VERMELHO,
            cor_borda_direita=(255, 255, 255),
            cor_passagem=(255, 255, 0),
            id_botao=f"item_sel_{i}",
            estado_global=estado,
            eventos=eventos,
            funcao_esquerdo=lambda item=item: Descriçao(item),
            funcao_direito=None,
            desfazer_esquerdo=lambda: TiraDescriçao(),
            desfazer_direito=None,
            tecla_esquerda=None,
            tecla_direita=None,
            grossura=3,
            som=None
        )

        imagem = ImagensItens.get(nome_item) or ImagensItens[classe_item]
        imagem = pygame.transform.smoothscale(imagem, (55, 55))  # ✅ tamanho padronizado

        img_x = bx + (63 - 55) // 2
        img_y = by + (63 - 55) // 2
        tela.blit(imagem, (img_x, img_y))

    pygame.draw.line(tela, (255, 255, 255), (x, y + 156), (x + largura - 2, y + 156), 2)

    if H in player.inventario:
        # Proporção ajustada: 75% descrição e nome, 25% botões
        largura_desc = int(largura * 0.75)
        largura_botoes = largura - largura_desc
        x_desc = x
        x_botoes = x + largura_desc

        # --- Linha divisória vertical entre descrição e botões ---
        pygame.draw.line(tela, (255, 255, 255), (x_botoes, y + 156), (x_botoes, y + altura - 180), 2)

        # --- Botões laterais usando GV ---
        GV.Botao(
            tela, "Usar",
            (x_botoes + 6, y + 160, largura_botoes - 10, 36),
            AZUL, PRETO, AZUL,
            lambda: player.usar_item(H, PokemonS, tela, Mapa, AtaqueS, EstadoDaPergunta, Baralho),
            fonte_pequena, B1
        )
        GV.Botao(
            tela, "Vender",
            (x_botoes + 6, y + 200, largura_botoes - 10, 36),
            VERMELHO, PRETO, VERMELHO,
            lambda: player.vender_item(H, Baralho),
            fonte_pequena, B1
        )

        # --- Nome do item ---
        nome = H.get("nome", "")
        render_nome = Fonte.render(nome, True, (255, 255, 255))
        tela.blit(render_nome, (
            x_desc + (largura_desc // 2 - render_nome.get_width() // 2),
            y + 160
        ))

        # --- Descrição do item ---
        descricao = H.get("Descrição", "")
        palavras = descricao.split()
        linhas = []
        linha = ""
        for palavra in palavras:
            teste = linha + " " + palavra if linha else palavra
            if FonteMenor.size(teste)[0] > (largura_desc - 20):
                linhas.append(linha)
                linha = palavra
            else:
                linha = teste
        linhas.append(linha)

        for i, texto in enumerate(linhas[:3]):
            render = FonteMenor.render(texto, True, (255, 255, 255))
            tela.blit(render, (x_desc + 10, y + 188 + i * 15))

    if x < 0:
        TiraDescriçao()

    # Energias
    
    y = y + 240

    pygame.draw.line(tela, (255, 255, 255), (x, y), (x + largura - 2, y), 2)

    altura = 175

    chaves = [k for k in player.energias.keys() if k in energia_cores]

    # Parte inferior: barras verticais
    base_y = y + altura - 45
    topo_barra = y + 10
    largura_barra = 30
    margem_x = 10
    espaco_total = largura - 2 * margem_x
    espaco_entre = espaco_total // len(chaves) if chaves else 1

    for i, chave in enumerate(chaves):
        cor = energia_cores[chave]
        valor = min(player.energias[chave], 15)  
        altura_barra = int((valor / 15) * (base_y - topo_barra))
        x_centro = x + margem_x + espaco_entre * i + espaco_entre // 2

        # Desenha a barra de energia
        pygame.draw.rect(tela, cor, (x_centro - largura_barra // 2, base_y - altura_barra, largura_barra, altura_barra))
        pygame.draw.rect(tela, (0, 0, 0), (x_centro - largura_barra // 2, topo_barra, largura_barra, base_y - topo_barra), 1)

        # Círculo na base com número de energias
        pygame.draw.circle(tela, cor, (x_centro, base_y + 3), 13)
        pygame.draw.circle(tela, (255, 255, 255), (x_centro, base_y + 3), 13, 1)
        num = fonte_.render(str(player.energias[chave]), True, (255, 255, 255)) 
        tela.blit(num, (x_centro - num.get_width() // 2, base_y - num.get_height() // 2 + 3))

        # Criação do botão de descarte
        estado_clique = estadoEnergias.setdefault(chave, {"clicado": False, "pressionado": False})
        GV.Botao(
            tela, "", (x_centro - 16, base_y + 22, 32, 18),  
            (50, 50, 50), (255, 255, 255), (80, 80, 80),
            lambda ch=chave: player.muda_descarte(ch),
            fonte_, estado_clique,
            grossura=1, tecla_atalho=None, mostrar_na_tela=True, eventos=eventos, som=None
        )

        # Texto "D1", "D2", "D3" sobre o botão
        if chave in player.energiasDesc:
            ordem = player.energiasDesc.index(chave) + 1
            texto_ordem = f"D{ordem}"
        else:
            texto_ordem = ""

        if texto_ordem:
            texto = fonte_.render(texto_ordem, True, (255, 255, 255))  
            tela.blit(texto, (x_centro - texto.get_width() // 2, base_y + 22))

def Atacar(PokemonS,PokemonV,PokemonA,player,inimigo,Mapa,tela,Baralho):
    if AtaqueS is not None:
            alvos = None
            AlvoLoc2 = None
            if AtaqueS["extra"] == "V":
                if PokemonV is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo visualizado")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonV.pos
                    if PokemonV in inimigo.pokemons:
                        AlvoLoc = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc = ((510 + idx * 190),1010)

            elif AtaqueS["extra"] == "A":
                if PokemonA is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonA.pos
                    AlvoLoc = ((1400 - idx * 190),95)

            elif AtaqueS["extra"] == "AV":
                if PokemonA is None or PokemonV is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo e um alvo visualizado")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonA.pos
                    AlvoLoc = ((1400 - idx * 190),95)
                    
                    idx = PokemonV.pos
                    if PokemonV in inimigo.pokemons:
                        AlvoLoc2 = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc2 = ((510 + idx * 190),1010)
            elif AtaqueS["extra"] == "MA":
                alvos = AtaqueS["alvos"](PokemonS,PokemonA,player,inimigo,Mapa)
            elif AtaqueS["extra"] == "MAA":
                alvos = AtaqueS["alvos"](PokemonS,PokemonA,player,inimigo,Mapa)
                if PokemonA is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo")
                    tocar("Bloq")
                    return
                else:
                    idx = PokemonA.pos
                    AlvoLoc = ((1400 - idx * 190),95)

            else:
                if PokemonV is not None and AtaqueS["extra"] == "TV":
                    idx = PokemonV.pos
                    if PokemonV in inimigo.pokemons:
                        AlvoLoc2 = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc2 = ((510 + idx * 190),1010)
                idx = PokemonS.pos
                AlvoLoc = ((510 + idx * 190),1010)
            
            if VCusto(player,PokemonS,AtaqueS) == False:
                return
            
            PokemonS.atacou = True
            PokemonS.Ganhar_XP(4,player)

            if AtaqueS["extra"] == "A" or AtaqueS["extra"] == "AV":
                if VAcerta(PokemonS,PokemonA,AtaqueS,Mapa.Metros) == False:
                    return
            
            adicionar_efeito(AtaqueS["efeito"],AlvoLoc,lambda: AtaqueS["funçao"](PokemonS,PokemonV,PokemonA,alvos,player,inimigo,AtaqueS,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,AtaqueS["irregularidade"]))
            if alvos is not None:
                for alvo in alvos:
                    idx = alvo.pos
                    if alvo in inimigo.pokemons:
                        AlvoLoc = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc = ((520 + idx * 190),1000)
                    adicionar_efeito(AtaqueS["efeito"],AlvoLoc)

            if AlvoLoc2 is not None:
                adicionar_efeito(AtaqueS["efeito2"],AlvoLoc2)

    else: 
        GV.adicionar_mensagem("Selecione um ataque")
        tocar("Bloq")
        return

def Trocar_Ataque(Pokemon,EstadoDaPergunta,Ataque,escolha):
    if Pokemon.movimento1 == Ataque:
        Pokemon.movimento1 = SelecionaAtaques(escolha)
    elif Pokemon.movimento2 == Ataque:
        Pokemon.movimento2 = SelecionaAtaques(escolha)
    elif Pokemon.movimento3 == Ataque:
        Pokemon.movimento3 = SelecionaAtaques(escolha)
    elif Pokemon.movimento4 == Ataque:
        Pokemon.movimento4 = SelecionaAtaques(escolha)
    EstadoDaPergunta["estado"] = False

def Trocar_Ataque_Pergunta(Pokemon,Ataque,EstadoDaPergunta):
    EstadoDaPergunta["funçao"] = Trocar_Ataque
    EstadoDaPergunta["info"] = [Pokemon,EstadoDaPergunta,Ataque]
    EstadoDaPergunta["opçoes"] = []
    EstadoDaPergunta["estado"] = True
    
    contador = 0
    for i in range(20):
        if contador == 4:
            break
        move = random.choice(Pokemon.movePossiveis)
        if move not in Pokemon.moveList and move not in EstadoDaPergunta["opçoes"]:
            EstadoDaPergunta["opçoes"].append(move)
            contador += 1

superficie_transparente = None

def Desenhar_Alcance(tela, PeçaS, alcance_metros, pixels_por_metro, Alvo, precisao, Mapa):
    global superficie_transparente
    if PeçaS is None or PeçaS.local is []:
        return

    if superficie_transparente == None:
        superficie_transparente = pygame.Surface(tela.get_size(), pygame.SRCALPHA).convert_alpha()

    superficie_transparente.fill((0, 0, 0, 0))  # limpar a surface com transparência

    centro_x, centro_y = PeçaS.local
    raio = int((alcance_metros + PeçaS.tamanho) * pixels_por_metro )

    # Círculo de alcance
    pygame.draw.circle(superficie_transparente, (255, 0, 0, 120), (centro_x, centro_y), raio + 5)
    pygame.draw.circle(superficie_transparente, (255, 0, 0, 50), (centro_x, centro_y), raio)

    # Reta até o alvo, se houver
    if Alvo is not None and hasattr(Alvo, 'local') and Alvo.local is not []:
        alvo_x, alvo_y = Alvo.local

        # Distância real entre os Pokémon
        distancia = distancia_entre_pokemons(PeçaS, Alvo, Mapa.Metros)

        # Ajustar a precisão com base na distância fora do alcance
        if distancia > alcance_metros:
            over = distancia - alcance_metros
            reducao = over * 5  # 5% por metro extra
            precisao = max(0, precisao - reducao)

                # Coordenadas de início e fim
        x1, y1 = centro_x, centro_y
        x2, y2 = alvo_x, alvo_y

        dx, dy = x2 - x1, y2 - y1
        dist_total = math.hypot(dx, dy)

        if dist_total == 0:
            return  # evita divisão por zero se o Pokémon tentar mirar a si mesmo

        num_pontos = int(dist_total // 4)  # Número de segmentos (quanto menor, mais suave)

        # Normalizar direção
        dir_x = dx / dist_total
        dir_y = dy / dist_total

        # Tempo atual (para animar o pulso)
        t = pygame.time.get_ticks() / 1000  # segundos
        frequencia = 4  # quantidade de pulsos na linha
        velocidade = 3  # velocidade da onda

        for i in range(num_pontos):
            # Posição ao longo da linha
            fator = i / num_pontos
            px = int(x1 + dir_x * fator * dist_total)
            py = int(y1 + dir_y * fator * dist_total)

            # Cálculo da intensidade da onda (vai de 0 a 1)
            onda = 0.5 + 0.5 * math.sin(2 * math.pi * frequencia * fator - velocidade * t)
            onda2 = 0.85 + 0.15 * math.sin(2 * math.pi * frequencia * fator - velocidade * t)

            # Determinar cor com base na precisão
            if precisao == 0:
                base_cor = (255, 0, 0)  # vermelho
            elif distancia > alcance_metros:
                base_cor = (255, 255, 0)  # amarelo
            else:
                base_cor = (0, 255, 0)  # verde

            # Aplicar onda como alpha
            alpha2 = (onda2 * 255)
            alpha = int(onda * 255)
            cor_pulso = (*base_cor, alpha)
            cor_seta = (*base_cor,alpha2)

            # Desenhar ponto/trecho
            pygame.draw.circle(superficie_transparente, cor_pulso, (px, py), 3)

        texto = Fonte20.render(f"{int(distancia)}m", True, (255, 255, 255))

        # Animação da seta: sobe e desce suavemente com o tempo
        offset = int(8 * math.sin(t * 7))  # frequência da oscilação

        # Posição do texto (acima do inimigo)
        texto_x = alvo_x - texto.get_width() // 2
        texto_y = alvo_y - 45 + offset # ajustável

        # Desenhar o texto
        superficie_transparente.blit(texto, (texto_x, texto_y))

        # Pontos da seta (triângulo) apontando para o inimigo
        seta_x = alvo_x
        seta_y = alvo_y - 18 + offset # base da seta animada

        pontos_seta = [
            (seta_x, seta_y),         # ponta da seta
            (seta_x - 5, seta_y - 10),
            (seta_x + 5, seta_y - 10)
        ]

        # Desenhar a seta branca
        pygame.draw.polygon(superficie_transparente, cor_seta, pontos_seta)

    tela.blit(superficie_transparente, (0, 0))

botao_RR = {"estado": False}
botaoitem = {"estado": False}

def Loja(pos, tela, baralho, imagens, turnos, eventos, player, preco, itens_loja):
    x, y = pos
    largura = 480
    altura = 110
    cor_fundo = (35, 35, 35)

    pygame.draw.rect(tela, cor_fundo, (x, y, largura, altura))

    if turnos < 4:
        raridades = { "Comum": 55, "Incomum": 40, "Raro": 5, "Lendario": 0}
    elif turnos < 8:
        raridades = { "Comum": 40, "Incomum": 45, "Raro": 15, "Lendario": 0}
    elif turnos < 15:
        raridades = { "Comum": 35, "Incomum": 30, "Raro": 30, "Lendario": 5}
    elif turnos > 14:
        raridades = { "Comum": 32, "Incomum": 32, "Raro": 26, "Lendario": 10}

    baralhos_por_raridade = {
        "Comum": baralho.Comuns,
        "Incomum": baralho.Incomuns,
        "Raro": baralho.Raros,
        "Lendario": baralho.Lendarios
    }

    def Comprar(item,indice):
        if player.ouro < item["preço"]:
            tocar("Bloq")
            return
        player.ouro -= item["preço"]
        tocar ("Compra")
        Comprou = player.ganhar_item(item,baralho)
        if Comprou == True:
            itens_loja[indice] = None


    def Roletar(lista_itens, baralho, raridades):
        if player.ouro < preco:
            tocar("Bloq")
            return  # ouro insuficiente
        player.ouro -= preco
        tocar ("Roletar")

        for item in lista_itens:
            if item is not None:
                baralho.devolve_item(item)

        for i in range(len(lista_itens)):
            lista_itens[i] = None

        for i in range(len(lista_itens)):
            raridade_escolhida = random.choices(
                population=["Comum", "Incomum", "Raro", "Lendario"],
                weights=[raridades["Comum"], raridades["Incomum"], raridades["Raro"], raridades["Lendario"]],
                k=1
            )[0]
            baralho_da_raridade = baralhos_por_raridade[raridade_escolhida]
            if baralho_da_raridade:
                novo_item = random.choice(baralho_da_raridade)
                lista_itens[i] = novo_item
                baralho_da_raridade.remove(novo_item)

    espacamento = 85
    base_x = x + 10
    base_y = y + 10

    cor_raridade = {
    "Comum": (200, 200, 200),       # Cinza claro
    "Incomum": (0, 200, 0),         # Verde
    "Raro": (0, 100, 255),          # Azul
    "Lendario": (255, 215, 0)       # Amarelo
    }

    porcentagens = [raridades["Comum"], raridades["Incomum"], raridades["Raro"], raridades["Lendario"]]
    pos_base_x = x + largura - 42
    pos_base_y = y + 5
    espacamento_y = 20

    for idx, porcentagem in enumerate(porcentagens):
        cor = list(cor_raridade.values())[idx]
        texto = f"{porcentagem}%"
        GV.Texto_caixa(
            tela, texto,
            (pos_base_x, pos_base_y + idx * espacamento_y, 40, 20),
            Fonte15, cor, PRETO, 2
        )

    for i in range(5):
        bx = base_x + i * espacamento
        by = base_y

        if i < 4:
            item = itens_loja[i]
            if item is not None:
                
                CorBotao = cor_raridade[item["raridade"]]

                GV.Botao(
                    tela, "", (bx, by, 80, 80),
                    CorBotao, PRETO, VERDE_CLARO,
                    lambda: Comprar(item,i),
                    Fonte50, botaoitem, 3, None, True, eventos
                )

                preco_item = item["preço"]  # ← como você pediu, diretamente do dicionário
                GV.Texto_caixa(
                    tela, str(preco_item), (bx + 15, by + 80, 50, 20),
                    Fonte20, CINZA, PRETO, 2
                )

                nome_item = item["nome"]
                if nome_item in imagens:
                    imagem = pygame.transform.scale(imagens[nome_item], (65, 65))
                    iw, ih = imagem.get_size()
                    img_x = bx + (80 - iw) // 2
                    img_y = by + (80 - ih) // 2
                    tela.blit(imagem, (img_x, img_y))
            else:
                pygame.draw.rect(tela, (60, 60, 60), (bx, by, 80, 80), border_radius=5)
        else:
            # Botão Roletar
            GV.Botao(
                tela, "R", (bx, by, 80, 80),
                (70,70,70), PRETO, VERDE_CLARO,
                lambda: Roletar(itens_loja, baralho, raridades),
                Fonte50, botao_RR, 3, None, True, eventos
            )
            # Exibir preço do roletar
            GV.Texto_caixa(
                tela, str(preco), (bx + 15, by + 80, 50, 20),
                Fonte20, AMARELO, PRETO, 2
            )



    # botao_compra_x = x + largura - 40  # 10px de margem da borda direita
    # GV.Botao(
    #     tela, "", (botao_compra_x, y + 5, 28, 28),
    #     (50, 50, 50), (255, 255, 255), (80, 80, 80),
    #     lambda: Comprar_Energias(player, 1),
    #     fonte_, BotaoCompraEnergia,
    #     grossura=1, tecla_atalho=None, mostrar_na_tela=True, eventos=eventos, som=None
    # )
    # tela.blit(Imagem,(botao_compra_x, y + 5))
