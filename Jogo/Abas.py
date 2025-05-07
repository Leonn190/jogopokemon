import pygame
import random
import Visual.GeradoresVisuais as GV
from Visual.Sonoridade import tocar
from Visual.Efeitos import adicionar_efeito
from Funções2 import VAcerta,VCusto
from Geradores.GeradorAtaques import SelecionaAtaques
from Visual.GeradoresVisuais import VERMELHO,AMARELO,BRANCO,CINZA,PRETO,AZUL,Fonte20,Fonte15,Fonte25

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

def Status_Pokemon(pos, tela, pokemon, imagens_tipos, player, eventos=None, SoV=None):
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
        vida_str = f"HP: {int(vida)}/{int(vida_max)}"
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
            ("Attack", pokemon.Atk, pokemon.IV_atk, 120),
            ("Defense", pokemon.Def, pokemon.IV_def, 120),
            ("Sp. Atk", pokemon.Atk_sp, pokemon.IV_atkSP, 120),
            ("Sp. Def", pokemon.Def_sp, pokemon.IV_defSP, 120),
            ("Speed", pokemon.vel, pokemon.IV_vel, 120)
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
                        PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc = EstadoDaPergunta["info"]

                        GV.Botao(tela, opçao, botao_rect, CINZA, PRETO, AZUL,lambda: EstadoDaPergunta["funçao"](PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,opçao),Fonte20, Bpergunta, 3, None, True, eventos)
                    except ValueError:
                        GV.Botao(tela, opçao, botao_rect, CINZA, PRETO, AZUL,lambda: EstadoDaPergunta["funçao"](EstadoDaPergunta["info"][0],EstadoDaPergunta["info"][1],EstadoDaPergunta["info"][2],opçao),Fonte20, Bpergunta, 3, None, True, eventos)

        if x > 1600:
            desseleciona_ataque(SoV)
            Oculta_ataque(SoV)
            EstadoDaPergunta["estado"] = False

        if SoV == "S":
            if AtaqueV is not None:
                Mostrar_Ataque(tela, AtaqueV, (1540, y + 60), imagens_tipos)
        else:
            if AtaqueSV is not None:
                Mostrar_Ataque(tela, AtaqueSV, (1540, y + 60), imagens_tipos)

def Mostrar_Ataque(tela, ataque, posicao=(100, 100), imagens_tipos=None):
    FUNDO = (30, 30, 30)
    BORDA = (255, 255, 255)
    TEXTO = (255, 255, 255)
    LINHA = (200, 200, 200)
    BRANCO = (255, 255, 255)

    energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 255, 0), "verde": (0, 200, 0),
        "roxa": (128, 0, 128), 
        "laranja": (255, 140, 0), 
        "preta": (30, 30, 30), "cinza": (160, 160, 160)
    }

    # Fontes menores para caber melhor na ficha reduzida
    fonte_titulo = pygame.font.SysFont("arial", 22, bold=True)
    fonte_desc = pygame.font.SysFont("arial", 15)
    fonte_info = pygame.font.SysFont("arial", 15)
    fonte_infoStat = pygame.font.SysFont("arial", 15, bold=True)

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
        infos = [
            f"Dano: {ataque['dano']}",
            f"Alcance: {ataque['alcance']}m",
            f"Precisão: {ataque['precisão']}%"
        ]

        def obter_cor_status(status, tipo):
            if tipo == "dano":
                if status < 0.8: return (255, 0, 0)
                elif status < 1.2: return (255, 255, 0)
                elif status < 1.6: return (0, 200, 0)
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

FonteMenor = pygame.font.SysFont(None, 25)
Fonte = pygame.font.SysFont(None, 32)

def Inventario(local, tela, player, ImagensItens, estado, eventos, PokemonS, Mapa):
    x, y = local
    largura, altura = 380, 285  # ⬅️ Aumentado para 285

    cor_borda = (255, 255, 255)  # Borda branca
    global H  # Item selecionado com botão direito

    # Fundo escuro com borda branca
    pygame.draw.rect(tela, cor_borda, (x - 3, y - 3, largura + 4, altura + 4)) 
    pygame.draw.rect(tela, (30, 30, 30), (x, y, largura, altura))  

    # Cabeçalho com fundo escuro e texto branco
    pygame.draw.rect(tela, (30, 30, 30), (x, y, largura, 40))  
    texto_nome = Fonte.render(f"Inventário de {player.nome}", True, (255, 255, 255))  
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
            cor_normal=(0,0,0),  
            cor_borda=(0,0,0),   
            cor_passagem=(0,0,0), 
            acao=lambda i=i: player.usar_item(i, PokemonS, tela, Mapa, AtaqueS, EstadoDaPergunta),
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
            cor_borda_normal=(255, 255, 255), 
            cor_borda_esquerda=(255, 255, 255),  
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

        
    if H:
        nome = H.get("nome", "")
        FonteNome = pygame.font.SysFont(None, 28)
        render_nome = FonteNome.render(nome, True, (255, 255, 255))  # Texto branco
        tela.blit(render_nome, (x + largura // 2 - render_nome.get_width() // 2, y + 195))  # ⬅️ Acima da descrição

    # descrição se H foi definido
    if H:
        descricao = H.get("Descrição", "")

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
            render = FonteMenor.render(texto, True, (255, 255, 255)) 
            tela.blit(render, (x + 10, y + 218 + i * 20))  

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

fonte_ = pygame.font.SysFont(None, 24)
fonte_titulo_ = pygame.font.SysFont(None, 28)

def Tabela_Energias(tela, local, player, estadoEnergias, eventos):
    x, y = local
    largura, altura = 380, 285

    ret = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, (35, 35, 35), ret)
    pygame.draw.rect(tela, (255, 255, 255), ret, 3)

    energia_cores = {
        "vermelha": (255, 0, 0), "azul": (0, 0, 255),
        "amarela": (255, 215, 0), 
        "verde": (0, 200, 0),
        "roxa": (128, 0, 128), "laranja": (255, 140, 0),
        "preta": (0, 0, 0), "cinza": (160, 160, 160)
    }

    chaves = [k for k in player.energias.keys() if k in energia_cores]

    # Cabeçalho
    titulo = fonte_titulo_.render(f"Energias de {player.nome}", True, (255, 255, 255))
    tela.blit(titulo, (x + 190 - titulo.get_width() // 2, y + 10))
    pygame.draw.line(tela, (255, 255, 255), (x, y + 34), (x + largura, y + 34), 2)  

    # Parte inferior: barras verticais
    base_y = y + altura - 50
    topo_barra = y + 50 - 4  
    largura_barra = 28
    espaco_total = 360
    margem_x = 10
    espaco_entre = espaco_total // len(chaves)

    for i, chave in enumerate(chaves):
        cor = energia_cores[chave]
        valor = min(player.energias[chave], 25)  
        altura_barra = int((valor / 25) * (base_y - topo_barra))
        x_centro = x + margem_x + espaco_entre * i + espaco_entre // 2

        # Desenha a barra de energia
        pygame.draw.rect(tela, cor, (x_centro - largura_barra // 2, base_y - altura_barra, largura_barra, altura_barra))
        pygame.draw.rect(tela, (0, 0, 0), (x_centro - largura_barra // 2, topo_barra, largura_barra, base_y - topo_barra), 1)

        # Círculo na base com número de energias
        pygame.draw.circle(tela, cor, (x_centro, base_y + 3), 12)
        pygame.draw.circle(tela, (255, 255, 255), (x_centro, base_y + 3), 12, 1)
        num = fonte_.render(str(player.energias[chave]), True, (255, 255, 255)) 
        tela.blit(num, (x_centro - num.get_width() // 2, base_y - num.get_height() // 2 + 3))

        # Criação do botão de descarte
        estado_clique = estadoEnergias.setdefault(chave, {"clicado": False, "pressionado": False})
        GV.Botao(
            tela, "", (x_centro - 16, base_y + 24, 32, 18),  
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

        # Desenha o texto sobre o botão, na mesma posição
        if texto_ordem:
            texto = fonte_.render(texto_ordem, True, (255, 255, 255))  
            tela.blit(texto, (x_centro - texto.get_width() // 2, base_y + 24))  

def Atacar(PokemonS,PokemonV,PokemonA,player,inimigo,Mapa,tela):
    if PokemonS.PodeAtacar == True:
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
                alvos = AtaqueS["alvos"](PokemonS,player,inimigo,Mapa)
            elif AtaqueS["extra"] == "MAA":
                if PokemonA is None:
                    GV.adicionar_mensagem("Esse ataque requer um alvo")
                    tocar("Bloq")
                    return

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

            if AtaqueS["extra"] == "A" or AtaqueS["extra"] == "AV":
                if VAcerta(PokemonS,PokemonA,AtaqueS,Mapa.Metros) == False:
                    return
            
            if alvos is None:
                adicionar_efeito(AtaqueS["efeito"],AlvoLoc,lambda: AtaqueS["funçao"](PokemonS,PokemonV,PokemonA,player,inimigo,AtaqueS,Mapa,tela,AlvoLoc,EstadoDaPergunta,AtaqueS["irregularidade"]))
                if AlvoLoc2 is not None:
                    adicionar_efeito(AtaqueS["efeito2"],AlvoLoc2)
            else:
                jafoi = False
                for alvo in alvos:
                    idx = alvo.pos
                    if alvo in inimigo.pokemons:
                        AlvoLoc = ((1400 - idx * 190),95)
                    else:
                        AlvoLoc = ((510 + idx * 190),1010)
                    if jafoi == False:
                        adicionar_efeito(AtaqueS["efeito"],AlvoLoc,lambda: AtaqueS["funçao"](PokemonS,PokemonV,PokemonA,alvos,player,inimigo,AtaqueS,Mapa,tela,AlvoLoc,EstadoDaPergunta,AtaqueS["irregularidade"]))
                        jafoi = True
                    else:
                        adicionar_efeito(AtaqueS["efeito"],AlvoLoc)
        else: 
            GV.adicionar_mensagem("Selecione um ataque")
            tocar("Bloq")
            return
        
    else:
        GV.adicionar_mensagem("Esse pokemon não pode realizar ataques")
        tocar("Bloq")
        return


def Trocar_Ataque(Pokemon,EstadoDaPergunta,Ataque,escolha):
    if Pokemon.movimento1 == Ataque:
        Pokemon.movimento1 = SelecionaAtaques([escolha])
    elif Pokemon.movimento2 == Ataque:
        Pokemon.movimento2 = SelecionaAtaques([escolha])
    elif Pokemon.movimento3 == Ataque:
        Pokemon.movimento3 = SelecionaAtaques([escolha])
    elif Pokemon.movimento4 == Ataque:
        Pokemon.movimento4 = SelecionaAtaques([escolha])
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