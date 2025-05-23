import pygame
import os
import importlib
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Config import aplicar_claridade
from Infos import PokemonInfo, ItemInfo, TreinadorInfo
from Visual.Arrastaveis import Arrastavel
from Visual.Imagens import Carregar_Imagens_Decks
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
Baralho_atual_treinador = None

Lista_atual_pokemons = None
Lista_atual_itens = None
Lista_atual_energias = None
Lista_atual_treinadores = None

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
TreinadorSelecionado = None

Aviso_Apagar = False

ImagensPokemon = {}
ImagensItens = {}
TiposEnergiaIMG = {}
IconesDeckIMG = {}
ImagensTreinadores = {}
ImagensFichas = {}

Areas_pokemon = []
Areas_itens = []
Areas_Energias = []
Criou_Areas_pokemon = 0
Criou_Areas_itens = 0
Criou_Areas_energia = 0
AreaEditor = pygame.Rect(470,450,980,560)
AreaTreinador = pygame.Rect(1585, 165, 150, 150)

EvoPokemon = 0
EvoPokemonLim = 0
ListaFormas = []

#Botao generico
BG = {"estado": False}

def VerificaDeck(Deck):

    if None in Deck["pokemons"]:
        return 1
    if None in Deck["itens"]:
        return 1
    if Deck["treinador"] == None:
        return 1

    contagem_raridades = {
    "Comum": 0,
    "Incomum": 0,
    "Raro": 0,
    "Epico": 0,
    "Mitico": 0,
    "Lendario": 0}
    for pokemon in Deck["pokemons"]:
        raridade = pokemon.get("raridade", "")
        if raridade in contagem_raridades:
            contagem_raridades[raridade] += 1
    
    if contagem_raridades["Lendario"] > 2:
        return 0
    if contagem_raridades["Mitico"] > 2:
        return 0
    
    for pokemon in Deck["pokemons"][:3]:
        if pokemon["raridade"] not in ["Comum","Incomum"]:
            return 0
    
    if len(Deck["pokemons"]) != len(set([poke["nome"] for poke in Deck["pokemons"]])):
        return 0
    
    contagem_raridades = {
    "Comum": 0,
    "Incomum": 0,
    "Raro": 0,
    "Epico": 0,
    "Mitico": 0,
    "Lendario": 0}
    for item in Deck["itens"]:
        raridade = item.get("raridade", "")
        if raridade in contagem_raridades:
            contagem_raridades[raridade] += 1
    
    if contagem_raridades["Lendario"] > 3:
        return 0
    if contagem_raridades["Mitico"] > 3:
        return 0
    
    return 2

def TrocaTexto(t):
    global selecionadoTXT, DeckSelecionado
    selecionadoTXT = False
    DeckSelecionado["nome"] = t

def Trocar(Idx1,Idx2,categoria):
    DeckSelecionado[categoria][Idx1],DeckSelecionado[categoria][Idx2] = DeckSelecionado[categoria][Idx2],DeckSelecionado[categoria][Idx1]

def Executar(pos,dados,categoria,interno):    
    global Arrastaveis

    if categoria == "pokemons":
        if interno == True:
            for i,area in enumerate(Areas_pokemon):
                if area.collidepoint(pos):
                    Trocar(DeckSelecionado[categoria].index(dados),i,categoria)
                    tocar("Encaixe")
                    break
            if AreaEditor.collidepoint(pos):
                DeckSelecionado[categoria][DeckSelecionado[categoria].index(dados)] = None
        
        if interno == False:
            for i,area in enumerate(Areas_pokemon):
                 if area.collidepoint(pos):
                     DeckSelecionado[categoria][i] = dados
                     tocar("Encaixe")
                     break
                 
    if categoria == "itens":
        if interno == True:
            for i,area in enumerate(Areas_itens):
                if area.collidepoint(pos):
                    Trocar(DeckSelecionado[categoria].index(dados),i,categoria)
                    tocar("Encaixe")
                    break
            if AreaEditor.collidepoint(pos):
                DeckSelecionado[categoria][DeckSelecionado[categoria].index(dados)] = None
        
        if interno == False:
            for i,area in enumerate(Areas_itens):
                 if area.collidepoint(pos):
                     DeckSelecionado[categoria][i] = dados
                     tocar("Encaixe")
                     break
                 
    if categoria == "energiasD":
        if interno == True:
            for i,area in enumerate(Areas_Energias):
                if area.collidepoint(pos):
                    Trocar(DeckSelecionado[categoria].index(dados),i,categoria)
                    tocar("Encaixe")
                    break
            if AreaEditor.collidepoint(pos):
                DeckSelecionado[categoria][DeckSelecionado[categoria].index(dados)] = None
        
        if interno == False:
            for i,area in enumerate(Areas_Energias):
                 if area.collidepoint(pos):
                     DeckSelecionado[categoria][i] = dados
                     tocar("Encaixe")
                     break
    
    if categoria == "treinador":
        if interno == True:
            if AreaEditor.collidepoint(pos):
                DeckSelecionado[categoria] = None
                Arrastaveis.clear()
        if interno == False:
            if AreaTreinador.collidepoint(pos):
                DeckSelecionado[categoria] = dados
                tocar("Encaixe")
                 
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
    
    tocar("Salvou")

    IniciaDecks()

def Apagar_Deck(nome_arquivo, pasta):
    caminho_arquivo = os.path.join(pasta, f"{nome_arquivo}.py")
    os.remove(caminho_arquivo)
    tocar("Apagou")
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
    
    return ListaDecks

def MudaForma(sentido):
    global EvoPokemon
    if sentido is True:
        EvoPokemon += 1
    else:
        EvoPokemon -= 1

def desenhaBaralho(tela, Baralho, eventos):
    global Arrastaveis, Baralho_atual_pokemons, Baralho_atual_itens, Baralho_atual_energias, Baralho_atual_treinador
    global Areas_pokemon, Areas_itens, Areas_Energias, Criou_Areas_pokemon, Criou_Areas_itens, Criou_Areas_energia
    global selecionadoTXT, TextoBara

    x_inicial = 120
    y_inicial = 90
    largura = 1680
    altura = 320
    largura_extra = 280
    altura_extra = 55

    cor_fundo = (50, 50, 50)
    cor_fundo2 = (25, 25, 25)
    cor_borda = (0, 0, 0)
    cor_linha = (0, 0, 0)

    # Desenha o fundo principal
    pygame.draw.rect(tela, cor_fundo, (x_inicial, y_inicial, largura, altura))

    # NOVO: Desenha a extensão superior direita centralizada
    barra_largura = largura_extra + 52
    barra_x = x_inicial + (largura - barra_largura) // 2
    barra_y = y_inicial - altura_extra
    pygame.draw.rect(tela, cor_fundo2, (barra_x, barra_y, barra_largura, altura_extra))

    # Desenha a borda ao redor (ajustado para conectar ao novo posicionamento da barra superior)
    pontos = [
        (x_inicial, y_inicial),
        (x_inicial + largura, y_inicial),
        (x_inicial + largura, y_inicial + altura),
        (x_inicial, y_inicial + altura)
    ]
    pygame.draw.polygon(tela, cor_borda, pontos, width=5)

    # Desenha o ícone à esquerda
    largura_icon = 80
    altura_icon = 80
    x_icon = x_inicial - largura_icon + 80
    y_icon = y_inicial - altura_icon
    pygame.draw.rect(tela, cor_fundo2, (x_icon, y_icon, largura_icon, altura_icon))
    pygame.draw.rect(tela, cor_borda, (x_icon, y_icon, largura_icon, altura_icon), width=4)
    icone_img = IconesDeckIMG[Baralho["icone"]]
    icone_redimensionado = pygame.transform.smoothscale(icone_img, (75, 75))
    icone_x = x_icon + (largura_icon - 75) // 2
    icone_y = y_icon + (altura_icon - 75) // 2
    tela.blit(icone_redimensionado, (icone_x, icone_y))

    # === Desenha o ícone à direita ===
    largura_icon = 80
    altura_icon = 80
    x_icon_direita = x_inicial + largura - largura_icon
    y_icon_direita = y_inicial - altura_icon
    pygame.draw.rect(tela, cor_fundo2, (x_icon_direita, y_icon_direita, largura_icon, altura_icon))
    pygame.draw.rect(tela, cor_borda, (x_icon_direita, y_icon_direita, largura_icon, altura_icon), width=4)
    icone_img = IconesDeckIMG[Baralho["icone"]]
    icone_redimensionado = pygame.transform.smoothscale(icone_img, (75, 75))
    icone_x_direita = x_icon_direita + (largura_icon - 75) // 2
    icone_y_direita = y_icon_direita + (altura_icon - 75) // 2
    tela.blit(icone_redimensionado, (icone_x_direita, icone_y_direita))

    # Linhas internas e divisões
    x_divisao = x_inicial + largura - largura_extra
    pygame.draw.line(tela, cor_linha, (x_divisao, y_inicial), (x_divisao, y_inicial + altura), width=4)
    pygame.draw.line(tela, cor_linha, (barra_x, y_inicial), (barra_x + barra_largura, y_inicial), width=4)
    y_linha_inferior = y_inicial - altura_extra + 70
    pygame.draw.line(tela, cor_linha, (x_divisao, y_linha_inferior + 25), (x_inicial + largura, y_linha_inferior + 25), width=4)
    y_linha_inferior = y_inicial - altura_extra + 290
    pygame.draw.line(tela, cor_linha, (x_divisao, y_linha_inferior + 25), (x_inicial + largura, y_linha_inferior + 25), width=4)
    y_linha_inferior = y_inicial - altura_extra + 305
    pygame.draw.line(tela, cor_linha, (x_divisao, y_linha_inferior + 25), (x_inicial + largura, y_linha_inferior + 25), width=4)
    linha_esquerda_y = y_inicial + 40
    pygame.draw.line(tela, cor_linha, (x_inicial, linha_esquerda_y), (x_divisao, linha_esquerda_y), width=4)

    # Faixa inferior do setor direito
    faixa_y_inicial = y_inicial
    faixa_y_final = y_linha_inferior + 287
    faixa_altura = faixa_y_final - faixa_y_inicial
    texto_faixa = "Prédefinições de descarte"
    superficie_texto_faixa = Fonte20.render(texto_faixa, True, (255, 255, 255))
    rect_texto_faixa = superficie_texto_faixa.get_rect(center=(x_divisao + largura_extra // 2, faixa_y_inicial + faixa_altura // 2))
    tela.blit(superficie_texto_faixa, rect_texto_faixa)

    # Faixa superior do setor direito
    faixa_y_final = y_linha_inferior - 207
    faixa_altura = faixa_y_final - faixa_y_inicial
    texto_faixa = "Treinador"
    superficie_texto_faixa = Fonte40.render(texto_faixa, True, (255, 255, 255))
    rect_texto_faixa = superficie_texto_faixa.get_rect(center=(x_divisao + largura_extra // 2, faixa_y_inicial + faixa_altura // 2))
    tela.blit(superficie_texto_faixa, rect_texto_faixa)

    # Nova linha vertical dentro do setor esquerdo dividindo em 60% / 40%
    largura_esquerda = x_divisao - x_inicial
    x_linha_interna_esquerda = x_inicial + int(largura_esquerda * 0.6)
    pygame.draw.line(tela, cor_linha, (x_linha_interna_esquerda, y_inicial), (x_linha_interna_esquerda, y_inicial + altura), width=4)

    # Barra de texto dentro da área superior centralizada
    if Abrir is not None:
        TextoBara, selecionadoTXT = GV.Barra_De_Texto(
            tela, (barra_x, barra_y, barra_largura, altura_extra),
            Fonte50, (50,50,50), PRETO, BRANCO, eventos, TextoBara,
            TrocaTexto, AZUL, selecionadoTXT
        )

    if selecionadoTXT == False:
        texto = Baralho["nome"]
        cor_texto = (255, 255, 255)
        superficie_texto = Fonte50.render(texto, True, cor_texto)
        rect_texto = superficie_texto.get_rect(center=(
            barra_x + barra_largura // 2,
            barra_y + altura_extra // 2
        ))
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
                        imagem_fundo.blit(imagem_pokemon, (0, 0))

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
                    tela.blit(imagem_pokemon, (x_slot, y_slot))

    
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
                        imagem_fundo.blit(imagem_item, (0, 0))

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
                    tela.blit(imagem_item, (x_slot, y_slot))

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
    
    # Faixa superior do setor direito
    faixa_y_final = y_linha_inferior - 207
    faixa_altura = faixa_y_final - faixa_y_inicial
    texto_faixa = "Treinador"
    superficie_texto_faixa = Fonte40.render(texto_faixa, True, (255, 255, 255))
    rect_texto_faixa = superficie_texto_faixa.get_rect(center=(x_divisao + largura_extra // 2, faixa_y_inicial + faixa_altura // 2))
    tela.blit(superficie_texto_faixa, rect_texto_faixa)

    # Desenha a área do treinador (centralizada entre as faixas superior e inferior)
    area_treinador_topo = faixa_y_inicial + 55
    area_treinador_base = y_linha_inferior + 25
    area_treinador_centro_y = (area_treinador_topo + area_treinador_base - 30) // 2
    area_treinador_centro_x = x_divisao + largura_extra // 2

    # Primeiro o quadrado cinza claro (150x150) atrás
    tamanho_quadrado = 150
    rect_cinza = pygame.Rect(0, 0, tamanho_quadrado, tamanho_quadrado)
    rect_cinza.center = (area_treinador_centro_x, area_treinador_centro_y)
    pygame.draw.rect(tela, (80, 80, 80), rect_cinza)

    if Baralho["treinador"] is not None:
        img_treinador = ImagensTreinadores[Baralho["treinador"]["nome"]]

        if EditorSelecionado == listaTreinadores:
            if Baralho_atual_treinador != Baralho["treinador"]:
                Baralho_atual_treinador = Baralho["treinador"]
                Arrastaveis.clear()
                # Calcula o topleft correto baseado no centro
                rect_temp = img_treinador.get_rect(center=(area_treinador_centro_x, area_treinador_centro_y))
                pos_topleft = rect_temp.topleft

                arrastavel = Arrastavel(img_treinador, pos_topleft, Baralho["treinador"], "treinador", True, Executar)
                Arrastaveis.append(arrastavel)
        else:
            # Apenas exibe imagem fixa no centro
            rect_img = img_treinador.get_rect(center=(area_treinador_centro_x, area_treinador_centro_y))
            tela.blit(img_treinador, rect_img)

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
                        tela, "", (355, 560, 40, 30), PRETO, PRETO, PRETO,
                        lambda : MudaForma(True),
                        Fonte50, BG, 2, None, True, eventos
                    ) 
            if EvoPokemon != 0:
                GV.Botao(
                        tela, "", (75, 560, 40, 30), PRETO, PRETO, PRETO,
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

    if EditorSelecionado == listaTreinadores:
            linhas = 2
            colunas = 4
            espacamento = 12

            largura_treinador = 230
            altura_treinador = 160

            # Calcula área útil considerando o número de colunas/linhas e o tamanho fixo dos treinadores
            largura_disponivel = largura - (espacamento * (colunas + 1))
            altura_disponivel = altura - (espacamento * (linhas + 1))

            # Calcula a margem inicial para centralizar a grid se desejar
            x_inicial = x + (largura_disponivel - (colunas * largura_treinador)) // 2 + espacamento
            y_inicial = y + (altura_disponivel - (linhas * altura_treinador)) // 2 + espacamento

            for i in range(min(len(listaTreinadores), linhas * colunas)):
                linha = i // colunas
                coluna = i % colunas

                x_slot = x_inicial + coluna * (largura_treinador + espacamento)
                y_slot = y_inicial + linha * (altura_treinador + espacamento)

                treinador = listaTreinadores[i]

                GV.Botao(
                tela, "", (x_slot, y_slot, largura_treinador, altura_treinador), PRETO, PRETO, PRETO,
                lambda i=treinador: SelecionaTreinador(i),
                Fonte50, BG, 2, None, True, eventos
            )

def desenhaEditor(tela, eventos):
    global EditorSelecionado, listaPokemon, Lista_atual_pokemons, ArrastaveisEditor, Lista_atual_itens, Lista_atual_energias, Lista_atual_treinadores

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
        regras = [
            "- As 3 primeiras casas são reservadas para os inciais",
            "- Para o pokemon ser inicial ele deve ter raridade incomum ou inferior",
            "- Deve haver ao menos 1 pokemon de cada raridade",
            "- Não pode colocar mais de 2 lendários ou Miticos",
            "- Se alguma das regras não for cumprida o baralho não poderá entrar em jogo"
        ]
    elif EditorSelecionado == listaItens:
        texto = "Editor De Itens"
        regras = [
            "- Não pode ter mais de 2 cópias do item",
            "- Deve haver pelo menos 2 itens de cada raridade",
            "- Não pode colocar mais de 3 itens lendários ou Miticos",
            "- Se alguma das regras não for cumprida o baralho não poderá entrar em jogo"
        ]
    elif EditorSelecionado == listaEnergias:
        texto = "Editor De Energias"
        regras = ["- Sem regras para as energias"]
    elif EditorSelecionado == listaicones:
        texto = "Editor de Icones"
        regras = ["- Sem regras para os Icones"]
    elif EditorSelecionado == listaTreinadores:
        texto = "Editor de Treinadores"
        regras = ["- Sem regras para os Treinadores"]
    else:
        texto = ""
        regras = []

    # --- Texto do título ---
    superficie_texto = Fonte40.render(texto, True, (250,250,250))
    rect_texto = superficie_texto.get_rect(center=(x + largura // 2, y + 46 // 2))
    tela.blit(superficie_texto, rect_texto)

    # --- Função para quebrar linha ---
    def quebra_linha(texto, fonte, max_largura):
        palavras = texto.split()
        linhas = []
        linha_atual = ""
        for palavra in palavras:
            teste_linha = linha_atual + ("" if linha_atual == "" else " ") + palavra
            if fonte.size(teste_linha)[0] <= max_largura:
                linha_atual = teste_linha
            else:
                if linha_atual != "":
                    linhas.append(linha_atual)
                linha_atual = palavra
        if linha_atual:
            linhas.append(linha_atual)
        return linhas

    # --- Regras com quebra de linha ---
    margem_superior = rect_texto.bottom + 30  # Iniciar abaixo do título
    espacamento_linha = 25
    espacamento_regra = 50
    y_atual = margem_superior

    for regra in regras:
        linhas_regra = quebra_linha(regra, Fonte25, 360)
        for linha in linhas_regra:
            superficie_regra = Fonte25.render(linha, True, (230,230,230))
            rect_regra = superficie_regra.get_rect(center=(x + largura // 2, y_atual))
            tela.blit(superficie_regra, rect_regra)
            y_atual += espacamento_linha
        y_atual += espacamento_regra - espacamento_linha  # Espaço entre regras (já contou a última linha)
    
    if TreinadorSelecionado is None:
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
                        imagem_fundo.blit(imagem_pokemon, (0, 0))

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
                        imagem_fundo.blit(imagem_item, (0, 0))

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
                tela, "", (x_slot, y_slot, lado_slot, lado_slot), AZUL_CLARO, PRETO, AMARELO,
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
    
    if EditorSelecionado == listaTreinadores:
        if Lista_atual_treinadores != listaTreinadores:
            Lista_atual_treinadores = list(listaTreinadores)  # Cópia simples
            ArrastaveisEditor.clear()

            linhas = 2
            colunas = 4
            espacamento = 12

            largura_treinador = 230
            altura_treinador = 160

            # Calcula área útil considerando o número de colunas/linhas e o tamanho fixo dos treinadores
            largura_disponivel = largura - (espacamento * (colunas + 1))
            altura_disponivel = altura - (espacamento * (linhas + 1))

            # Calcula a margem inicial para centralizar a grid se desejar
            x_inicial = x + (largura_disponivel - (colunas * largura_treinador)) // 2 + espacamento
            y_inicial = y + (altura_disponivel - (linhas * altura_treinador)) // 2 + espacamento

            for i in range(min(len(listaTreinadores), linhas * colunas)):
                linha = i // colunas
                coluna = i % colunas

                x_slot = x_inicial + coluna * (largura_treinador + espacamento)
                y_slot = y_inicial + linha * (altura_treinador + espacamento)

                treinador = listaTreinadores[i]
                imagem_treinador = ImagensTreinadores.get(treinador["nome"])  # Imagem original sem redimensionar

                if imagem_treinador:
                    arrastavel = Arrastavel(imagem_treinador, (x_slot, y_slot), treinador, "treinador", False, Executar)
                    ArrastaveisEditor.append(arrastavel)

    if EditorSelecionado == listaPokemon:
        if PokemonSelecionado is not None:
            PokemonInfo((45,450),tela,PokemonSelecionado,EvoPokemon,EvoPokemonLim,ListaFormas, eventos, TiposEnergiaIMG)
    
    if EditorSelecionado == listaItens:
        if ItemSelecionado is not None:
            ItemInfo((45,450),tela,ItemSelecionado,ImagensItens)

    if EditorSelecionado == listaTreinadores:
        if TreinadorSelecionado is not None:
            TreinadorInfo((45,450),tela,TreinadorSelecionado,ImagensFichas, "D")

def Abre(Editar):
    global Abrir, DeckSelecionado
    tocar("Clique2")
    if Editar is False:
        for i in range(1, 17):
            if f"Deck{i}" not in [deck["ID"] for deck in ListaDecks]:
                ID = f"Deck{i}"
                break
        NovoDeck = {
                "nome": "Novo Deck",
                "pokemons": [None] * 12,
                "itens": [None] * 18,
                "energiasD": [None] * 4,
                "ID":ID,
                "treinador": None,
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
    global EditorSelecionado, PokemonSelecionado, ItemSelecionado, TreinadorSelecionado
    EditorSelecionado = lista
    tocar("Seleciona")
    PokemonSelecionado = None
    ItemSelecionado = None
    TreinadorSelecionado = None


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

def SelecionaTreinador(treinador):
    global TreinadorSelecionado
    TreinadorSelecionado = treinador

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
    	
        Valido = VerificaDeck(deck)
        if Valido == 0:
            cor = VERMELHO_CLARO
        elif Valido == 1:
            cor = AMARELO_CLARO
        else:
            cor = VERDE_CLARO

        # Criação do botão
        GV.Botao_Selecao(
            tela, 
            (pos_x, pos_y, largura_botao, altura_botao),
            "", 
            Fonte30,
            cor_fundo=cor, 
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

            # --- Imagem do ícone no centro ---
        if deck["icone"] in IconesDeckIMG:
            icone_original = IconesDeckIMG[deck["icone"]]
            icone_redimensionado = pygame.transform.smoothscale(icone_original, (110, 110))

            # Centralizar horizontalmente no botão
            icone_x = pos_x + (largura_botao - 110) // 2

            # Ajuste para ficar abaixo do texto ou centralizado no botão
            # Exemplo centralizado no espaço restante abaixo do texto:
            icone_y = texto_rect.bottom + 15  # 5 pixels abaixo do texto

            # Evitar que a imagem ultrapasse o botão (opcional: ajuste automático)
            if icone_y + 110 > pos_y + altura_botao:
                icone_y = pos_y + (altura_botao - 110) // 2

            tela.blit(icone_redimensionado, (icone_x, icone_y))


    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)
    
    if len(ListaDecks) < 16:
        GV.Botao(tela, "Criar Novo Baralho", (110, 450, 500, 80), AMARELO, PRETO, AZUL,
                    lambda: Abre(False), Fonte50, B1, 3, None, True, eventos)
    else:
        GV.Botao(tela, "Criar Novo Baralho", (110, 450, 500, 80), CINZA, PRETO, AZUL,
                    lambda: tocar("Bloq"), Fonte50, B1, 3, None, True, eventos)
        
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
    GV.Botao_Selecao(
        tela, (1720, 10, 80, 80),
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

    GV.Botao(tela, "Cancelar", (985, 720, 350, 90), AMARELO_CLARO, PRETO, AZUL,
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

def Decks(tela,estados,relogio,Config):
    global ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG, ImagensTreinadores, ImagensFichas
    global Baralho_atual_pokemons, Baralho_atual_itens, Lista_atual_pokemons, Lista_atual_itens, Baralho_atual_energias, Lista_atual_energias
    global EditorSelecionado, EditorSelecionado_atual, Lista_atual_treinadores, Baralho_atual_treinador

    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Decks.jpg", (1920,1080))
    ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG,ImagensTreinadores, ImagensFichas = Carregar_Imagens_Decks(
    ImagensItens,ImagensPokemon,TiposEnergiaIMG,IconesDeckIMG, ImagensTreinadores, ImagensFichas)

    pygame.mixer.music.load('Audio/Musicas/Decks.ogg')  
    pygame.mixer.music.set_volume(Config["Volume"])
    pygame.mixer.music.play(-1)

    IniciaDecks()

    while estados["Rodando_Decks"]:
        tela.blit(Fundo_Menu, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False
                estados["Rodando_Decks"] = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                for arrastavel in Arrastaveis + ArrastaveisEditor:
                    arrastavel.verificar_clique(evento.pos)

            if evento.type == pygame.MOUSEBUTTONUP:
                for arrastavel in Arrastaveis + ArrastaveisEditor:
                    arrastavel.soltar()

            if evento.type == pygame.MOUSEMOTION:
                for arrastavel in Arrastaveis + ArrastaveisEditor:
                        arrastavel.arrastar(evento.pos)
        
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
            Baralho_atual_treinador = None
            Lista_atual_treinadores = None

        aplicar_claridade(tela,Config["Claridade"])
        pygame.display.update()
        relogio.tick(Config["FPS"])
