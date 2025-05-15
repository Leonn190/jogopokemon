import pygame
import os
import importlib
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Infos import PokemonInfo, ItemInfo
from Visual.Arrastaveis import Arrastavel
from Visual.Imagens import Carregar_Imagens2
from Geradores.GeradorOutros import Amplificadores_Todos,Frutas_Todas,Pokebolas_Todas,Poçoes_Todas,Estadios_Todos,Outros_Todos,Pokemons_Todos,Treinadores_Todos
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte25, Fonte28, Fonte30, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA, cores_raridade, energia_cores)

pygame.init()
pygame.mixer.init()

selecionadoTXT = False
TextoBara = ""

Baralho_atual_pokemons = None
Baralho_atual_itens = None
Baralho_atual_energias = None

Lista_atual_pokemons = None
Lista_atual_itens = None
Lista_atual_energias = None

Arrastaveis = []
ArrastaveisEditor = []

listaPokemon = Pokemons_Todos[1:]
listaItens = Amplificadores_Todos + Frutas_Todas + Pokebolas_Todas + Poçoes_Todas + Estadios_Todos + Outros_Todos
listaEnergias = ["vermelha", "azul", "amarela", "verde", "roxa", "laranja", "preta"]
listaTreinadores = Treinadores_Todos
listaicones = ["icone1","icone2","icone3","icone4","icone5","icone6","icone7","icone8"]

DeckSelecionado = None
Abrir = None
ListaDecks = []
EditorSelecionado = None
EditorSelecionado_atual = None
PokemonSelecionado = None
ItemSelecionado = None

Aviso_Apagar = False

ImagensPokemon = {}
ImagensItens = {}
TiposEnergiaIMG = {}
IconesDeckIMG = {}

Areas_pokemon = []
Areas_itens = []
Areas_Energias = []
Criou_Areas_pokemon = 0
Criou_Areas_itens = 0
Criou_Areas_energia = 0
AreaEditor = pygame.Rect(470,450,980,560)

EvoPokemon = 0
EvoPokemonLim = 0
ListaFormas = []

#Botao generico
BG = {"estado": False}

def TrocaTexto(t):
    global selecionadoTXT, DeckSelecionado
    selecionadoTXT = False
    DeckSelecionado["nome"] = t

def Trocar(Idx1,Idx2,categoria):
    DeckSelecionado[categoria][Idx1],DeckSelecionado[categoria][Idx2] = DeckSelecionado[categoria][Idx2],DeckSelecionado[categoria][Idx1]

def Executar(pos,dados,categoria,interno):    

    if categoria == "pokemons":
        if interno == True:
            for i,area in enumerate(Areas_pokemon):
                if area.collidepoint(pos):
                    Trocar(DeckSelecionado[categoria].index(dados),i,categoria)
                    break
            if AreaEditor.collidepoint(pos):
                DeckSelecionado[categoria][DeckSelecionado[categoria].index(dados)] = None
        
        if interno == False:
            for i,area in enumerate(Areas_pokemon):
                 if area.collidepoint(pos):
                     DeckSelecionado[categoria][i] = dados
                     break
                 
    if categoria == "itens":
        if interno == True:
            for i,area in enumerate(Areas_itens):
                if area.collidepoint(pos):
                    Trocar(DeckSelecionado[categoria].index(dados),i,categoria)
                    break
            if AreaEditor.collidepoint(pos):
                DeckSelecionado[categoria][DeckSelecionado[categoria].index(dados)] = None
        
        if interno == False:
            for i,area in enumerate(Areas_itens):
                 if area.collidepoint(pos):
                     DeckSelecionado[categoria][i] = dados
                     break
                 
    if categoria == "energiasD":
        if interno == True:
            for i,area in enumerate(Areas_Energias):
                if area.collidepoint(pos):
                    Trocar(DeckSelecionado[categoria].index(dados),i,categoria)
                    break
            if AreaEditor.collidepoint(pos):
                DeckSelecionado[categoria][DeckSelecionado[categoria].index(dados)] = None
        
        if interno == False:
            for i,area in enumerate(Areas_Energias):
                 if area.collidepoint(pos):
                     DeckSelecionado[categoria][i] = dados
                     break
                 
    return False

def salvar_dicionario_em_py(dicionario, nome_arquivo, pasta_destino):
    """Salva um dicionário em um arquivo .py no formato Python, apagando o antigo se existir."""
    # Garante que a pasta existe
    os.makedirs(pasta_destino, exist_ok=True)

    # Monta o caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_destino, f"{nome_arquivo}.py")

    # Remove o arquivo existente, se existir
    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)

    # Cria e escreve o novo arquivo
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"# Arquivo gerado automaticamente\n\n")
        arquivo.write(f"{nome_arquivo} = {repr(dicionario)}\n")

    IniciaDecks()

def Apagar_Deck(nome_arquivo, pasta):
    caminho_arquivo = os.path.join(pasta, f"{nome_arquivo}.py")
    os.remove(caminho_arquivo)
    IniciaDecks()

def selecionaDeck(deck):
    global DeckSelecionado
    DeckSelecionado = deck

def desselecionaDeck():
    global DeckSelecionado
    DeckSelecionado = None

def carregar_decks(pasta,ListaDecks):
    ListaDecks.clear()

    for nome_arquivo in os.listdir(pasta):
        if nome_arquivo.endswith(".py"):
            caminho = os.path.join(pasta, nome_arquivo)
            nome_modulo = nome_arquivo[:-3]

            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(modulo)

            # Procura diretamente no módulo por dicionários
            for atributo in dir(modulo):
                valor = getattr(modulo, atributo)  # Aqui ainda usamos getattr para acessar atributos, já que não há outra forma simples
                if isinstance(valor, dict):
                    ListaDecks.append(valor)
                    break
    
    for i,deck in enumerate(ListaDecks):
        deck["ID"] = f"Deck{i + 1}"
    
    return ListaDecks

def MudaForma(sentido):
    global EvoPokemon
    if sentido is True:
        EvoPokemon += 1
    else:
        EvoPokemon -= 1

def desenhaBaralho(tela, Baralho, eventos):
    global Arrastaveis, Baralho_atual_pokemons, Baralho_atual_itens, Baralho_atual_energias
    global Areas_pokemon, Areas_itens, Areas_Energias, Criou_Areas_pokemon, Criou_Areas_itens, Criou_Areas_energia
    global selecionadoTXT, TextoBara

    x_inicial = 120
    y_inicial = 90
    largura = 1680
    altura = 320
    largura_extra = 280  # Largura da extensão
    altura_extra = 55    # Altura da extensão

    cor_fundo = (50, 50, 50)
    cor_fundo2 = (25, 25, 25)
    cor_borda = (0, 0, 0)
    cor_linha = (0, 0, 0)

    # Desenha o fundo principal
    pygame.draw.rect(tela, cor_fundo, (x_inicial, y_inicial, largura, altura))

    # Desenha a extensão superior direita
    pygame.draw.rect(tela, cor_fundo2, (x_inicial + largura - largura_extra - 52, y_inicial - altura_extra, largura_extra + 52, altura_extra))

    # Desenha a borda ao redor
    pontos = [
        (x_inicial, y_inicial),
        (x_inicial + largura - largura_extra - 52, y_inicial),
        (x_inicial + largura - largura_extra - 52, y_inicial - altura_extra),
        (x_inicial + largura, y_inicial - altura_extra),
        (x_inicial + largura, y_inicial + altura),
        (x_inicial, y_inicial + altura)
    ]
    pygame.draw.polygon(tela, cor_borda, pontos, width=5)

    # === Extensão canto superior esquerdo para o ícone do baralho ===
    largura_icon = 80
    altura_icon = 80
    x_icon = x_inicial - largura_icon + 80  # Fica à esquerda da área do deck
    y_icon = y_inicial - altura_icon        # Fica acima da área do deck

    # Fundo da área do ícone
    pygame.draw.rect(tela, cor_fundo2, (x_icon, y_icon, largura_icon, altura_icon))

    # Borda ao redor da área do ícone
    pygame.draw.rect(tela, cor_borda, (x_icon, y_icon, largura_icon, altura_icon), width=4)

    # --- Desenha o ícone dentro da área ---
    icone_img = IconesDeckIMG[Baralho["icone"]]
    icone_redimensionado = pygame.transform.smoothscale(icone_img, (75, 75))

    # Calcula a posição centralizada dentro do quadrado 80x80
    icone_x = x_icon + (largura_icon - 75) // 2
    icone_y = y_icon + (altura_icon - 75) // 2

    tela.blit(icone_redimensionado, (icone_x, icone_y))

    # === Linhas internas ===
    # Linha vertical separando canto direito (280px)
    x_divisao = x_inicial + largura - largura_extra
    pygame.draw.line(tela, cor_linha, (x_divisao, y_inicial), (x_divisao, y_inicial + altura), width=4)

    # Linha horizontal dentro do setor direito separando a extensão superior
    pygame.draw.line(tela, cor_linha, (x_divisao - 52, y_inicial), (x_inicial + largura, y_inicial), width=4)

    # Linha horizontal 280px abaixo da linha horizontal superior, dentro do setor direito
    y_linha_inferior = y_inicial - altura_extra + 70
    pygame.draw.line(tela, cor_linha, (x_divisao, y_linha_inferior + 25), (x_inicial + largura, y_linha_inferior + 25), width=4)

    y_linha_inferior = y_inicial - altura_extra + 290
    pygame.draw.line(tela, cor_linha, (x_divisao, y_linha_inferior + 25), (x_inicial + largura, y_linha_inferior + 25), width=4)

    y_linha_inferior = y_inicial - altura_extra + 305
    pygame.draw.line(tela, cor_linha, (x_divisao, y_linha_inferior + 25), (x_inicial + largura, y_linha_inferior + 25), width=4)

    # Linha horizontal dentro do setor esquerdo dividindo 120px em cima e 200px em baixo
    linha_esquerda_y = y_inicial + 40
    pygame.draw.line(tela, cor_linha, (x_inicial, linha_esquerda_y), (x_divisao, linha_esquerda_y), width=4)

    # Área da faixa inferior do setor direito
    faixa_y_inicial = y_inicial
    faixa_y_final = y_linha_inferior + 287
    faixa_altura = faixa_y_final - faixa_y_inicial

    # Texto da faixa
    texto_faixa = "Prédefinições de descarte"
    superficie_texto_faixa = Fonte20.render(texto_faixa, True, (255, 255, 255))
    rect_texto_faixa = superficie_texto_faixa.get_rect(center=(
        x_divisao + largura_extra // 2,
        faixa_y_inicial + faixa_altura // 2
    ))

    tela.blit(superficie_texto_faixa, rect_texto_faixa)

    # Área da faixa superior do setor direito
    faixa_y_inicial = y_inicial
    faixa_y_final = y_linha_inferior - 207
    faixa_altura = faixa_y_final - faixa_y_inicial

    # Texto da faixa
    texto_faixa = "Treinador"
    superficie_texto_faixa = Fonte40.render(texto_faixa, True, (255, 255, 255))
    rect_texto_faixa = superficie_texto_faixa.get_rect(center=(
        x_divisao + largura_extra // 2,
        faixa_y_inicial + faixa_altura // 2
    ))

    tela.blit(superficie_texto_faixa, rect_texto_faixa)

    # Nova linha vertical dentro do setor esquerdo dividindo em 60% / 40%
    largura_esquerda = x_divisao - x_inicial
    x_linha_interna_esquerda = x_inicial + int(largura_esquerda * 0.6)
    pygame.draw.line(tela, cor_linha, (x_linha_interna_esquerda, y_inicial), (x_linha_interna_esquerda, y_inicial + altura), width=4)

        # Calcula a área da extensão superior direita
    barra_x = x_inicial + largura - largura_extra - 52
    barra_y = y_inicial - altura_extra
    barra_largura = largura_extra + 52
    barra_altura = altura_extra

    # Usa a área exata da extensão como área da barra de texto
    if Abrir is not None:
        TextoBara, selecionadoTXT = GV.Barra_De_Texto(
            tela, (barra_x, barra_y, barra_largura, barra_altura),
            Fonte50, 
            (50,50,50), PRETO, BRANCO, eventos, TextoBara,
            TrocaTexto, AZUL, selecionadoTXT
        )

    if selecionadoTXT == False:
        texto = Baralho["nome"]
        cor_texto = (255, 255, 255)

        superficie_texto = Fonte50.render(texto, True, cor_texto)

        rect_texto = superficie_texto.get_rect()
        rect_texto.center = (
            x_inicial + largura - ((largura_extra + 52) / 2),
            y_inicial - (altura_extra / 2)
        )

        # Desenha o texto
        tela.blit(superficie_texto, rect_texto)

        # Cabeçalho da área de Pokémons (60%)
    area_pokemons_cabecalho_x = x_inicial
    area_pokemons_cabecalho_largura = x_linha_interna_esquerda - x_inicial
    area_pokemons_cabecalho_y = y_inicial
    area_pokemons_cabecalho_altura = linha_esquerda_y - y_inicial

    texto_pokemons = Fonte40.render("Pokemons do Baralho", True, (255, 255, 255))
    texto_pokemons_rect = texto_pokemons.get_rect(center=(
        area_pokemons_cabecalho_x + area_pokemons_cabecalho_largura // 2,
        area_pokemons_cabecalho_y + area_pokemons_cabecalho_altura // 2
    ))
    tela.blit(texto_pokemons, texto_pokemons_rect)

    # Cabeçalho da área de Itens (40%)
    area_itens_cabecalho_x = x_linha_interna_esquerda
    area_itens_cabecalho_largura = x_divisao - x_linha_interna_esquerda
    area_itens_cabecalho_y = y_inicial
    area_itens_cabecalho_altura = linha_esquerda_y - y_inicial

    texto_itens = Fonte40.render("Itens do Baralho", True, (255, 255, 255))
    texto_itens_rect = texto_itens.get_rect(center=(
        area_itens_cabecalho_x + area_itens_cabecalho_largura // 2,
        area_itens_cabecalho_y + area_itens_cabecalho_altura // 2
    ))
    tela.blit(texto_itens, texto_itens_rect)


    area_pokemons_x = x_inicial
    area_pokemons_y = linha_esquerda_y
    area_pokemons_largura = x_linha_interna_esquerda - x_inicial
    area_pokemons_altura = y_inicial + altura - linha_esquerda_y

    linhas = 2
    colunas = 6
    espacamento = 10

    largura_disponivel = area_pokemons_largura - (espacamento * (colunas + 1))
    altura_disponivel = area_pokemons_altura - (espacamento * (linhas + 1))

    lado_slot = min(largura_disponivel // colunas, altura_disponivel // linhas)    

    for i in range(12):
        linha = i // colunas
        coluna = i % colunas

        x_slot = area_pokemons_x + espacamento + coluna * (lado_slot + espacamento) + 10
        y_slot = area_pokemons_y + espacamento + linha * (lado_slot + espacamento)
        margem = int(lado_slot * 0.1)
        pygame.draw.rect(tela, (80, 80, 80), (x_slot + margem, y_slot + margem, lado_slot - 2 * margem, lado_slot - 2 * margem))

        if Criou_Areas_pokemon < 12:
            rect_slot = pygame.Rect(x_slot + margem, y_slot + margem, lado_slot - 2 * margem, lado_slot - 2 * margem)
            Areas_pokemon.append(rect_slot)
            Criou_Areas_pokemon += 1

    if EditorSelecionado == listaPokemon:
            # Detecta mudança no Baralho (pode usar id ou cópia direta para mais segurança)
        if Baralho_atual_pokemons != Baralho["pokemons"]:
            Baralho_atual_pokemons = list(Baralho["pokemons"])  # Faz uma cópia simples (pode usar deepcopy se precisar)
            Arrastaveis.clear()

            for i in range(12):
                linha = i // colunas
                coluna = i % colunas

                x_slot = area_pokemons_x + espacamento + coluna * (lado_slot + espacamento) + 10
                y_slot = area_pokemons_y + espacamento + linha * (lado_slot + espacamento)

                pokemon = Baralho["pokemons"][i]

                if pokemon is not None:
                    cor_fundo = cores_raridade.get(pokemon["raridade"], (200, 200, 200))
                    imagem_fundo = pygame.Surface((lado_slot, lado_slot), pygame.SRCALPHA)
                    imagem_fundo.fill(cor_fundo)

                    imagem_pokemon = ImagensPokemon.get(pokemon["nome"])
                    if imagem_pokemon:
                        imagem_redimensionada = pygame.transform.smoothscale(imagem_pokemon, (lado_slot, lado_slot))
                        imagem_fundo.blit(imagem_redimensionada, (0, 0))

                    arrastavel = Arrastavel(imagem_fundo, (x_slot, y_slot), pokemon, "pokemons", True, Executar)
                    Arrastaveis.append(arrastavel)

    else:
        
        for i in range(12):
            linha = i // colunas
            coluna = i % colunas

            x_slot = area_pokemons_x + espacamento + coluna * (lado_slot + espacamento) + 10
            y_slot = area_pokemons_y + espacamento + linha * (lado_slot + espacamento)

            pokemon = Baralho["pokemons"][i]

            if pokemon is not None:
                # Define a cor pelo nível de raridade
                cor_fundo = cores_raridade.get(pokemon["raridade"])  # padrão cinza claro se não encontrar
                pygame.draw.rect(tela, cor_fundo, (x_slot, y_slot, lado_slot, lado_slot))

                imagem_pokemon = ImagensPokemon.get(pokemon["nome"])
                if imagem_pokemon:
                    imagem_redimensionada = pygame.transform.smoothscale(imagem_pokemon, (lado_slot, lado_slot))
                    tela.blit(imagem_redimensionada, (x_slot, y_slot))

    
    area_itens_x = x_linha_interna_esquerda + 5
    area_itens_y = linha_esquerda_y
    area_itens_largura = x_divisao - x_linha_interna_esquerda
    area_itens_altura = y_inicial + altura - linha_esquerda_y

    linhas_itens = 3
    colunas_itens = 6
    espacamento_itens = 10

    largura_disponivel_itens = area_itens_largura - (espacamento_itens * (colunas_itens + 1))
    altura_disponivel_itens = area_itens_altura - (espacamento_itens * (linhas_itens + 1))

    lado_slot_item = min(largura_disponivel_itens // colunas_itens, altura_disponivel_itens // linhas_itens)

    for i in range(18):
        linha = i // colunas_itens
        coluna = i % colunas_itens

        x_slot = area_itens_x + espacamento_itens + coluna * (lado_slot_item + espacamento_itens)
        y_slot = area_itens_y + espacamento_itens + linha * (lado_slot_item + espacamento_itens)

        margem = int(lado_slot_item * 0.1)
        pygame.draw.rect(tela, (80, 80, 80), (x_slot + margem, y_slot + margem, lado_slot_item - 2 * margem, lado_slot_item - 2 * margem))

        if Criou_Areas_itens < 18:
            rect_slot = pygame.Rect(x_slot + margem, y_slot + margem, lado_slot_item - 2 * margem, lado_slot_item - 2 * margem)
            Areas_itens.append(rect_slot)
            Criou_Areas_itens += 1

    if EditorSelecionado == listaItens:
    # Detecta mudança na lista de itens
        if Baralho_atual_itens != Baralho["itens"]:
            Baralho_atual_itens = list(Baralho["itens"])  # Copia simples (pode usar deepcopy se quiser)
            Arrastaveis.clear()

            for i in range(18):
                linha = i // colunas_itens
                coluna = i % colunas_itens

                x_slot = area_itens_x + espacamento_itens + coluna * (lado_slot_item + espacamento_itens)
                y_slot = area_itens_y + espacamento_itens + linha * (lado_slot_item + espacamento_itens)

                item = Baralho["itens"][i]

                if item is not None:
                    cor_fundo = cores_raridade.get(item["raridade"], (200, 200, 200))
                    imagem_fundo = pygame.Surface((lado_slot_item, lado_slot_item), pygame.SRCALPHA)
                    imagem_fundo.fill(cor_fundo)

                    imagem_item = ImagensItens.get(item["nome"])
                    if imagem_item:
                        imagem_redimensionada = pygame.transform.smoothscale(imagem_item, (lado_slot_item, lado_slot_item))
                        imagem_fundo.blit(imagem_redimensionada, (0, 0))

                    arrastavel = Arrastavel(imagem_fundo, (x_slot, y_slot), item, "itens", True, Executar)
                    Arrastaveis.append(arrastavel)
    else:
        for i in range(18):
            linha = i // colunas_itens
            coluna = i % colunas_itens

            x_slot = area_itens_x + espacamento_itens + coluna * (lado_slot_item + espacamento_itens)
            y_slot = area_itens_y + espacamento_itens + linha * (lado_slot_item + espacamento_itens)

            item = Baralho["itens"][i]

            if item is not None:
                # Define a cor pela raridade do item
                cor_fundo = cores_raridade.get(item["raridade"])  # padrão cinza claro se não encontrar
                pygame.draw.rect(tela, cor_fundo, (x_slot, y_slot, lado_slot_item, lado_slot_item))

                imagem_item = ImagensItens.get(item["nome"])
                if imagem_item:
                    imagem_redimensionada = pygame.transform.smoothscale(imagem_item, (lado_slot_item, lado_slot_item))
                    tela.blit(imagem_redimensionada, (x_slot, y_slot))

            # Parâmetros dos círculos
    espacamento = 26
    diametro = 38  # Já calculado anteriormente
    raio = diametro // 2

    # Coordenadas iniciais do espaço onde desenharemos os círculos (canto inferior direito)
    x_circulos_inicial = x_divisao + 27  # Margem a partir de x_divisao
    y_circulos_inicial = y_inicial + altura - altura_extra + (altura_extra // 2) + 6  # Centralizando verticalmente

    for i in range(4):
        x_centro = x_circulos_inicial + i * (diametro + espacamento) + raio
        margem = 5  # Margem para o quadrado menor
        pygame.draw.rect(tela, (80, 80, 80), (x_centro - raio + margem, y_circulos_inicial - raio + margem, diametro - 2 * margem, diametro - 2 * margem))
        if Criou_Areas_energia < 4:
            rect_slot = pygame.Rect(x_centro - raio + margem, y_circulos_inicial - raio + margem, diametro - 2 * margem, diametro - 2 * margem)
            Areas_Energias.append(rect_slot)
            Criou_Areas_energia += 1

    if EditorSelecionado == listaEnergias:
        if Baralho_atual_energias != Baralho["energiasD"]:
            Baralho_atual_energias = list(Baralho["energiasD"])
            Arrastaveis.clear()
            
            for i in range(4):
                x_centro = x_circulos_inicial + i * (diametro + espacamento) + raio
                energia = Baralho["energiasD"][i]

                if energia and energia in energia_cores:
                    cor = energia_cores[energia]

                    # Cria uma superfície transparente com o tamanho do círculo
                    imagem_fundo = pygame.Surface((diametro, diametro), pygame.SRCALPHA)
                    pygame.draw.circle(imagem_fundo, cor, (raio, raio), raio)

                    # Cria o Arrastavel no ponto calculado (ajustado para o topo esquerdo da imagem)
                    arrastavel = Arrastavel(imagem_fundo, (x_centro - raio, y_circulos_inicial - raio), energia, "energiasD", True, Executar)
                    Arrastaveis.append(arrastavel)
        
    else:
        for i in range(4):
            x_centro = x_circulos_inicial + i * (diametro + espacamento) + raio
            energia = Baralho["energiasD"][i]

            # Desenha o círculo ou quadrado
            if energia and energia in energia_cores:
                cor = energia_cores[energia]
                pygame.draw.circle(tela, cor, (x_centro, y_circulos_inicial), raio)

            # Desenha a posição do círculo (D1, D2, D3, D4) acima do círculo
            texto_posicao = f"D{i+1}"
            texto_renderizado = Fonte25.render(texto_posicao, True, (255,255,255))  # Cor branca
            
            # Posição do texto acima do círculo
            texto_x = x_centro - texto_renderizado.get_width() // 2  # Centraliza o texto em relação ao círculo
            texto_y = y_circulos_inicial - raio + 12  # Posição acima do círculo

            tela.blit(texto_renderizado, (texto_x, texto_y))
    
def desenhaBotoesEditor(tela, eventos):    

    largura = 980
    altura = 560
    x = 470
    y = 450

    if EditorSelecionado == listaPokemon:
        linhas = 4
        colunas = 7
        espacamento = 12

        # Calcula o tamanho dos slots usando toda a área e respeitando os espaçamentos
        largura_disponivel = largura - (espacamento * (colunas + 1)) + 2
        altura_disponivel = altura - (espacamento * (linhas + 1))
        lado_slot = min(largura_disponivel // colunas, altura_disponivel // linhas)

        # Desenha a grade e cria os arrastáveis
        for i in range(min(len(listaPokemon), linhas * colunas)):
            linha = i // colunas
            coluna = i % colunas

            x_slot = x + espacamento + coluna * (lado_slot + espacamento) + 4
            y_slot = y + espacamento + linha * (lado_slot + espacamento)

            pokemon = listaPokemon[i]

            GV.Botao(
                tela, "", (x_slot, y_slot, lado_slot, lado_slot), PRETO, PRETO, PRETO,
                lambda p=pokemon: SelecionaPokemon(p),
                Fonte50, BG, 2, None, True, eventos
            )
    
        if PokemonSelecionado is not None:
            if EvoPokemon < EvoPokemonLim:
                GV.Botao(
                        tela, "", (355, 547, 40, 30), PRETO, PRETO, PRETO,
                        lambda : MudaForma(True),
                        Fonte50, BG, 2, None, True, eventos
                    ) 
            if EvoPokemon != 0:
                GV.Botao(
                        tela, "", (75, 547, 40, 30), PRETO, PRETO, PRETO,
                        lambda: MudaForma(False),
                        Fonte50, BG, 2, None, True, eventos
                    )
    
    if EditorSelecionado == listaItens:
        linhas = 5
        colunas = 10
        espacamento = 16

        largura_disponivel = largura - (espacamento * (colunas + 1))
        altura_disponivel = altura - (espacamento * (linhas + 1))
        lado_slot = min(largura_disponivel // colunas, altura_disponivel // linhas)

        for i in range(min(len(listaItens), linhas * colunas)):
            linha = i // colunas
            coluna = i % colunas

            x_slot = x + espacamento + coluna * (lado_slot + espacamento) + 2
            y_slot = y + espacamento + linha * (lado_slot + espacamento)

            item = listaItens[i]

            GV.Botao(
                tela, "", (x_slot, y_slot, lado_slot, lado_slot), PRETO, PRETO, PRETO,
                lambda i=item: SelecionaItem(i),
                Fonte50, BG, 2, None, True, eventos
            )

def desenhaEditor(tela, eventos):
    global EditorSelecionado, listaPokemon, Lista_atual_pokemons, ArrastaveisEditor, Lista_atual_itens, Lista_atual_energias

    desenhaBotoesEditor(tela, eventos)

    largura = 380
    altura = 415
    x = 1495
    y = 450
    retangulo = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, (50, 50, 50), retangulo)
    pygame.draw.rect(tela, (0, 0, 0), retangulo, 3)

    pygame.draw.line(tela, (0,0,0), (x, y + 45), (x + largura, y + 45), width=4)
    if EditorSelecionado == listaPokemon:
        texto = "Editor De Pokemons"
    elif EditorSelecionado == listaItens:
        texto = "Editor De Itens"
    elif EditorSelecionado == listaEnergias:
        texto = "Editor De Energias"
    else:
        texto = ""

    superficie_texto = Fonte40.render(texto, True, (250,250,250))

    rect_texto = superficie_texto.get_rect()
    rect_texto.center = (x + largura // 2, y + 46 // 2)

    tela.blit(superficie_texto, rect_texto)

    largura = 380
    altura = 560
    x = 45
    y = 450

    retangulo = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, (50, 50, 50), retangulo)
    pygame.draw.rect(tela, (0, 0, 0), retangulo, 3)

    pygame.draw.line(tela, (0,0,0), (x, y + 45), (x + largura, y + 45), width=4)

    # Define as dimensões e posição do retângulo principal do editor
    largura = 980
    altura = 560
    x = 470
    y = 450

    # Desenha o retângulo cinza escuro
    retangulo = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, (50, 50, 50), retangulo)

    # Desenha a borda preta
    pygame.draw.rect(tela, (0, 0, 0), retangulo, 3)

    # Se a aba selecionada for a lista de pokemons
    if EditorSelecionado == listaPokemon:
        if Lista_atual_pokemons != listaPokemon:
            Lista_atual_pokemons = list(listaPokemon)  # Faz uma cópia simples
            ArrastaveisEditor.clear()

            # Configuração da grade
            linhas = 4
            colunas = 7
            espacamento = 12

            # Calcula o tamanho dos slots usando toda a área e respeitando os espaçamentos
            largura_disponivel = largura - (espacamento * (colunas + 1)) + 2
            altura_disponivel = altura - (espacamento * (linhas + 1))
            lado_slot = min(largura_disponivel // colunas, altura_disponivel // linhas)

            # Desenha a grade e cria os arrastáveis
            for i in range(min(len(listaPokemon), linhas * colunas)):
                linha = i // colunas
                coluna = i % colunas

                x_slot = x + espacamento + coluna * (lado_slot + espacamento) + 4
                y_slot = y + espacamento + linha * (lado_slot + espacamento)

                pokemon = listaPokemon[i]

                if pokemon is not None:
                    cor_fundo = cores_raridade.get(pokemon["raridade"], (200, 200, 200))
                    imagem_fundo = pygame.Surface((lado_slot, lado_slot), pygame.SRCALPHA)
                    imagem_fundo.fill(cor_fundo)

                    imagem_pokemon = ImagensPokemon.get(pokemon["nome"])
                    if imagem_pokemon:
                        imagem_redimensionada = pygame.transform.smoothscale(imagem_pokemon, (lado_slot, lado_slot))
                        imagem_fundo.blit(imagem_redimensionada, (0, 0))

                    # Cria o arrastável, definindo categoria "pokemon", interno True e função Executar
                    arrastavel = Arrastavel(imagem_fundo, (x_slot, y_slot), pokemon, "pokemons", False, Executar)
                    ArrastaveisEditor.append(arrastavel)
    
    if EditorSelecionado == listaItens:
        if Lista_atual_itens != listaItens:
            Lista_atual_itens = list(listaItens)  # Copia simples
            ArrastaveisEditor.clear()

            linhas = 5
            colunas = 10
            espacamento = 16

            largura_disponivel = largura - (espacamento * (colunas + 1))
            altura_disponivel = altura - (espacamento * (linhas + 1))
            lado_slot = min(largura_disponivel // colunas, altura_disponivel // linhas)

            for i in range(min(len(listaItens), linhas * colunas)):
                linha = i // colunas
                coluna = i % colunas

                x_slot = x + espacamento + coluna * (lado_slot + espacamento) + 2
                y_slot = y + espacamento + linha * (lado_slot + espacamento)

                item = listaItens[i]

                if item is not None:
                    # Se quiser, pode adicionar cores diferentes por raridade/categoria de item
                    cor_fundo = cores_raridade.get(item["raridade"], (200, 200, 200))
                    imagem_fundo = pygame.Surface((lado_slot, lado_slot), pygame.SRCALPHA)
                    imagem_fundo.fill(cor_fundo)

                    imagem_item = ImagensItens.get(item["nome"])  # Use seu dicionário de imagens
                    if imagem_item:
                        imagem_redimensionada = pygame.transform.smoothscale(imagem_item, (lado_slot, lado_slot))
                        imagem_fundo.blit(imagem_redimensionada, (0, 0))

                    # Cria o arrastável no mesmo padrão, categoria "item"
                    arrastavel = Arrastavel(imagem_fundo, (x_slot, y_slot), item, "itens", False, Executar)
                    ArrastaveisEditor.append(arrastavel)

    if EditorSelecionado == listaEnergias:
        if Lista_atual_energias != listaEnergias:
            Lista_atual_energias = list(listaEnergias)  # Copia simples
            ArrastaveisEditor.clear()

            colunas = 7
            espacamento = 60

            largura_disponivel = largura - (espacamento * (colunas + 1))
            lado_slot = largura_disponivel // colunas  # Será quadrado, mas usaremos para o círculo dentro

            y_slot = y + espacamento + 2  # Linha única fixa

            for i in range(min(len(listaEnergias), colunas)):
                energia = listaEnergias[i]

                x_slot = x + espacamento + i * (lado_slot + espacamento)

                if energia and energia in energia_cores:
                    cor = energia_cores[energia]

                    # Cria uma superfície transparente para o círculo
                    superficie_circulo = pygame.Surface((lado_slot, lado_slot), pygame.SRCALPHA)
                    pygame.draw.circle(
                        superficie_circulo,
                        cor,
                        (lado_slot // 2, lado_slot // 2),
                        lado_slot // 2
                    )

                    # Cria o arrastável no mesmo padrão, categoria "energias"
                    arrastavel = Arrastavel(superficie_circulo, (x_slot, y_slot), energia, "energiasD", False, Executar)
                    ArrastaveisEditor.append(arrastavel)
    
    if EditorSelecionado == listaicones:
        colunas = 4
        linhas = 2
        espacamento = 60

        largura_disponivel = largura - (espacamento * (colunas + 1))
        lado_slot = largura_disponivel // colunas  # Quadrado dos botões

        for i, icone in enumerate(listaicones):
            linha = i // colunas
            coluna = i % colunas

            x_slot = x + espacamento + coluna * (lado_slot + espacamento)
            y_slot = y + espacamento + linha * (lado_slot + espacamento)

            # --- Desenha o botão ---
            GV.Botao(
                tela, "", (x_slot, y_slot, lado_slot, lado_slot), PRETO, PRETO, PRETO,
                lambda icone=icone: selecionaIcone(icone),
                Fonte50, BG, 2, None, True, eventos
            )

            # --- Desenha o ícone centralizado dentro do botão ---
            if icone in IconesDeckIMG:
                imagem_icone = IconesDeckIMG[icone]
                # Redimensiona para caber dentro do slot com leve margem
                margem = 10
                tamanho_icone = lado_slot - 2 * margem
                imagem_redimensionada = pygame.transform.smoothscale(imagem_icone, (tamanho_icone, tamanho_icone))

                # Calcula posição centralizada dentro do botão
                icone_x = x_slot + margem
                icone_y = y_slot + margem

                tela.blit(imagem_redimensionada, (icone_x, icone_y))

    if EditorSelecionado == listaPokemon:
        if PokemonSelecionado is not None:
            PokemonInfo((45,450),tela,PokemonSelecionado,EvoPokemon,EvoPokemonLim,ListaFormas, eventos, TiposEnergiaIMG)
    
    if EditorSelecionado == listaItens:
        if ItemSelecionado is not None:
            ItemInfo((45,450),tela,ItemSelecionado,ImagensItens)

def Abre(Editar):
    global Abrir, DeckSelecionado
    if Editar is False:
        NovoDeck = {
                "nome": "Novo Deck",
                "pokemons": [None] * 12,
                "itens": [None] * 18,
                "energiasD": [None] * 4,
                "ID":f"Deck{len(ListaDecks) + 1}",
                "icone": "icone5"
            }
        DeckSelecionado = NovoDeck
    Abrir = DeckSelecionado

def Quer_Apagar():
    global Aviso_Apagar
    if Aviso_Apagar == False:
        Aviso_Apagar = True
    else:
        Aviso_Apagar = False

def SelecionaEditor(lista):
    global EditorSelecionado
    EditorSelecionado = lista

def DesselecionaEditor():
    global EditorSelecionado
    EditorSelecionado = None

def SelecionaPokemon(pokemon):
    global PokemonSelecionado, ListaFormas, EvoPokemonLim, EvoPokemon
    PokemonSelecionado = pokemon
    ListaFormas = [pokemon]  # O próprio selecionado já na lista
    EvoPokemonLim = 0
    EvoPokemon = 0

    # Trata formas finais FF do próprio Pokémon inicial antes de explorar evoluções
    ff_inicial = pokemon.get("FF")
    if ff_inicial:
        if isinstance(ff_inicial, list):
            for forma in ff_inicial:
                if forma not in ListaFormas:
                    ListaFormas.append(forma)
        else:
            if ff_inicial not in ListaFormas:
                ListaFormas.append(ff_inicial)

    # Função interna recursiva que trata evoluções e FF delas
    def explorar(pokemon_atual):
        if pokemon_atual in ListaFormas:
            return
        ListaFormas.append(pokemon_atual)

        evolucao = pokemon_atual.get("evolução")
        if evolucao:
            if isinstance(evolucao, list):
                for e in evolucao:
                    explorar(e)
            else:
                explorar(evolucao)

        ff = pokemon_atual.get("FF")
        if ff:
            if isinstance(ff, list):
                for forma in ff:
                    if forma not in ListaFormas:
                        ListaFormas.append(forma)
            else:
                if ff not in ListaFormas:
                    ListaFormas.append(ff)

    # Começa explorando a partir das evoluções
    evolucao_inicial = pokemon.get("evolução")
    if evolucao_inicial:
        if isinstance(evolucao_inicial, list):
            for e in evolucao_inicial:
                explorar(e)
        else:
            explorar(evolucao_inicial)

    EvoPokemonLim = len(ListaFormas) - 1

def SelecionaItem(item):
    global ItemSelecionado
    ItemSelecionado = item

def selecionaIcone(icone):
    global DeckSelecionado
    DeckSelecionado["icone"] = icone

estadoDecks = {"selecionado_esquerdo": None}
estadoEditor = {"selecionado_esquerdo": None}

B1 = {"estado": False}

def TelaDecks(tela,eventos,estados):
    global ListaDecks
    global DeckSelecionado
    global Abrir

    largura_botao = 200
    altura_botao = 200
    espaçamento = 35
    largura_tela = 1920
    altura_inicial = 560
    espaçamento_linhas = 35

    # Cálculo do total de largura ocupada pelos 8 botões e espaços entre eles
    largura_ocupada = (largura_botao * 8) + (espaçamento * 7)
    
    for i, deck in enumerate(ListaDecks):
        linha = i // 8
        coluna = i % 8

        pos_x = (coluna * (largura_botao + espaçamento)) + (largura_tela - largura_ocupada) // 2
        pos_y = altura_inicial + (linha * (altura_botao + espaçamento_linhas))

        # Criação do botão
        GV.Botao_Selecao(
            tela, 
            (pos_x, pos_y, largura_botao, altura_botao),
            "", 
            Fonte30,
            cor_fundo=AZUL_CLARO, 
            cor_borda_normal=PRETO,
            cor_borda_esquerda=VERDE, 
            cor_borda_direita=None,
            cor_passagem=AMARELO, 
            id_botao=deck,   
            estado_global=estadoDecks, 
            eventos=eventos,
            funcao_esquerdo=lambda deck=deck: selecionaDeck(deck), 
            funcao_direito=None,
            desfazer_esquerdo=lambda: desselecionaDeck(), 
            desfazer_direito=None,
            tecla_esquerda=pygame.K_1, 
            tecla_direita=None
        )

        # --- Texto no topo do botão ---
        texto_surface = Fonte28.render(deck["nome"], True, PRETO)
        texto_rect = texto_surface.get_rect(center=(pos_x + largura_botao // 2, pos_y + texto_surface.get_height() // 2 + 5))
        tela.blit(texto_surface, texto_rect)

    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)
    
    GV.Botao(tela, "Criar Novo Baralho", (110, 450, 500, 80), AMARELO, PRETO, AZUL,
                lambda: Abre(False), Fonte50, B1, 3, None, True, eventos)
    if DeckSelecionado is not None:
        GV.Botao(tela, "Editar Baralho", (710, 450, 500, 80), VERDE, PRETO, AZUL,
                    lambda: Abre(True), Fonte50, B1, 3, None, True, eventos)
        
        GV.Botao(tela, "Apagar Baralho", (1310, 450, 500, 80), VERMELHO, PRETO, AZUL,
                    lambda: Quer_Apagar(), Fonte50, B1, 3, None, True, eventos)
        
        desenhaBaralho(tela, DeckSelecionado, eventos)

    else:
        GV.Botao(tela, "Editar Baralho", (710, 450, 500, 80), CINZA, PRETO, AZUL,
                    lambda: tocar("Bloq"), Fonte50, B1, 3, None, True, eventos)
        
        GV.Botao(tela, "Apagar Baralho", (1310, 450, 500, 80), CINZA, PRETO, AZUL,
                    lambda: tocar("Bloq"), Fonte50, B1, 3, None, True, eventos)

def TelaCriador(tela,eventos,estados):

    desenhaBaralho(tela, DeckSelecionado, eventos)

    GV.Botao_Selecao(
        tela, (120, 90, 842, 40),
        "", Fonte30,
        cor_fundo=None, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
        cor_passagem=AMARELO, id_botao="pokemons",   
        estado_global=estadoEditor, eventos=eventos,
        funcao_esquerdo=lambda: SelecionaEditor(listaPokemon), 
        funcao_direito=None,
        desfazer_esquerdo=lambda: DesselecionaEditor(), desfazer_direito=None,
        tecla_esquerda=None, tecla_direita=None, grossura=2)
    GV.Botao_Selecao(
        tela, (962, 90, 559, 40),
        "", Fonte30,
        cor_fundo=None, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
        cor_passagem=AMARELO, id_botao="Itens",   
        estado_global=estadoEditor, eventos=eventos,
        funcao_esquerdo=lambda: SelecionaEditor(listaItens), 
        funcao_direito=None,
        desfazer_esquerdo=lambda: DesselecionaEditor(), desfazer_direito=None,
        tecla_esquerda=None, tecla_direita=None, grossura=2)
    GV.Botao_Selecao(
        tela, (1521, 90, 280, 40),
        "", Fonte30,
        cor_fundo=None, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
        cor_passagem=AMARELO, id_botao="Treinador",   
        estado_global=estadoEditor, eventos=eventos,
        funcao_esquerdo=lambda: SelecionaEditor(listaTreinadores), 
        funcao_direito=None,
        desfazer_esquerdo=lambda: DesselecionaEditor(), desfazer_direito=None,
        tecla_esquerda=None, tecla_direita=None, grossura=2)
    GV.Botao_Selecao(
        tela, (1521, 350, 280, 15),
        "", Fonte30,
        cor_fundo=None, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
        cor_passagem=AMARELO, id_botao="Energias",   
        estado_global=estadoEditor, eventos=eventos,
        funcao_esquerdo=lambda: SelecionaEditor(listaEnergias), 
        funcao_direito=None,
        desfazer_esquerdo=lambda: DesselecionaEditor(), desfazer_direito=None,
        tecla_esquerda=None, tecla_direita=None, grossura=2)
    GV.Botao_Selecao(
        tela, (120, 10, 80, 80),
        "", Fonte30,
        cor_fundo=None, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
        cor_passagem=AMARELO, id_botao="icones",   
        estado_global=estadoEditor, eventos=eventos,
        funcao_esquerdo=lambda: SelecionaEditor(listaicones), 
        funcao_direito=None,
        desfazer_esquerdo=lambda: DesselecionaEditor(), desfazer_direito=None,
        tecla_esquerda=None, tecla_direita=None, grossura=2)

    desenhaEditor(tela, eventos)

    GV.Botao(tela, "Salvar Deck", (1495, 910, 380, 100), AMARELO_CLARO, PRETO, AZUL,
                lambda: salvar_dicionario_em_py(DeckSelecionado,DeckSelecionado["ID"],"Decks"), Fonte40, B1, 3, None, True, eventos)

def TelaAviso(tela,eventos,estados):
    global DeckSelecionado
    largura_tela, altura_tela = 1920, 1080

    # Tamanho do quadrado médio
    largura = 850
    altura = 350

    # Calcula posição central
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    # Desenha retângulo cinza escuro
    retangulo = pygame.Rect(x, y, largura, altura)
    pygame.draw.rect(tela, (50, 50, 50), retangulo)

    # Borda preta
    pygame.draw.rect(tela, (0, 0, 0), retangulo, 5)

    # Escreve mensagem no centro do retângulo

    texto = Fonte50.render(f"Tem certeza que quer apagar o {DeckSelecionado["nome"]}?", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=retangulo.center)
    tela.blit(texto, texto_rect)

    GV.Botao(tela, "Apagar", (585, 720, 350, 90), VERMELHO, PRETO, AZUL,
                    lambda: Apagar_Deck(DeckSelecionado["ID"],"Decks"), Fonte50, B1, 3, None, True, eventos)

    GV.Botao(tela, "Cancelar", (985, 720, 350, 90), VERMELHO, PRETO, AZUL,
                    lambda: Quer_Apagar(), Fonte50, B1, 3, None, True, eventos)

    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)

def IniciaDecks():
    global DeckSelecionado,Abrir,EditorSelecionado,Aviso_Apagar, ListaDecks
    global Areas_pokemon, Areas_itens, Areas_Energias, Criou_Areas_pokemon, Criou_Areas_itens, Criou_Areas_energia
    global estadoDecks, estadoEditor

    DeckSelecionado = None
    Abrir = None
    EditorSelecionado = None
    Aviso_Apagar = False

    estadoDecks = {"selecionado_esquerdo": None}
    estadoEditor = {"selecionado_esquerdo": None}

    Areas_pokemon = []
    Areas_itens = []
    Areas_Energias = []
    Criou_Areas_pokemon = 0
    Criou_Areas_itens = 0
    Criou_Areas_energia = 0

    carregar_decks("Decks",ListaDecks)

def Decks(tela,estados,relogio):
    global ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG
    global Baralho_atual_pokemons, Baralho_atual_itens, Lista_atual_pokemons, Lista_atual_itens, Baralho_atual_energias, Lista_atual_energias
    global EditorSelecionado, EditorSelecionado_atual

    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Decks.jpg", (1920,1080))
    ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG  = Carregar_Imagens2(ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG)

    pygame.mixer.music.load('Audio/Musicas/Decks.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    IniciaDecks()

    while estados["Rodando_Decks"]:
        tela.blit(Fundo_Menu, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN:
                for arrastavel in Arrastaveis + ArrastaveisEditor:
                    arrastavel.verificar_clique(evento.pos)

            if evento.type == pygame.MOUSEBUTTONUP:
                for arrastavel in Arrastaveis + ArrastaveisEditor:
                    arrastavel.soltar()

            if evento.type == pygame.MOUSEMOTION:
                for arrastavel in Arrastaveis + ArrastaveisEditor:
                        arrastavel.arrastar(evento.pos)

            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False
        
        if Aviso_Apagar is False:
            if Abrir is None:
                TelaDecks(tela,eventos,estados)
            else:
                TelaCriador(tela,eventos,estados)
        else:
            TelaAviso(tela,eventos,estados)

        Arrastado = None
        for arrastavel in Arrastaveis + ArrastaveisEditor:
            if arrastavel.arrastando is False:
                arrastavel.desenhar(tela)
            else:
                Arrastado = arrastavel
        
        if Arrastado is not None:
            Arrastado.desenhar(tela)

        if EditorSelecionado_atual != EditorSelecionado:
            EditorSelecionado_atual = EditorSelecionado
            Arrastaveis.clear()
            ArrastaveisEditor.clear()
            Baralho_atual_pokemons = None
            Baralho_atual_itens = None
            Lista_atual_pokemons = None
            Lista_atual_itens = None
            Baralho_atual_energias = None
            Lista_atual_energias = None

        pygame.display.update()
        relogio.tick(120)

