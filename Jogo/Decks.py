import pygame
import os
import importlib
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.Arrastaveis import Arrastavel
from Visual.Imagens import Carregar_Imagens2
from Geradores.GeradorOutros import Amplificadores_Todos,Frutas_Todas,Pokebolas_Todas,Poçoes_Todas,Estadios_Todos,Outros_Todos,Pokemons_Todos
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte25, Fonte30, Fonte40, Fonte50, Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA, cores_raridade, energia_cores)

pygame.init()
pygame.mixer.init()

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

DeckSelecionado = None
Abrir = None
ListaDecks = []
EditorSelecionado = None
EditorSelecionado_atual = None

Aviso_Apagar = False

ImagensPokemon = {}
ImagensItens = {}
TiposEnergiaIMG ={}

Areas_pokemon = []
Areas_itens = []
Areas_Energias = []
Criou_Areas_pokemon = 0
Criou_Areas_itens = 0
Criou_Areas_energia = 0
AreaEditor = pygame.Rect(470,450,980,560)

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

def carregar_decks(pasta):
    global ListaDecks
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

def desenhaBaralho(tela, Baralho):
    global Arrastaveis, Baralho_atual_pokemons, Baralho_atual_itens, Baralho_atual_energias
    global Areas_pokemon, Areas_itens, Areas_Energias, Criou_Areas_pokemon, Criou_Areas_itens, Criou_Areas_energia

    x_inicial = 120
    y_inicial = 75
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

    # Nova linha vertical dentro do setor esquerdo dividindo em 60% / 40%
    largura_esquerda = x_divisao - x_inicial
    x_linha_interna_esquerda = x_inicial + int(largura_esquerda * 0.6)
    pygame.draw.line(tela, cor_linha, (x_linha_interna_esquerda, y_inicial), (x_linha_interna_esquerda, y_inicial + altura), width=4)

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
    diametro = 35  # Já calculado anteriormente
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
            texto_renderizado = Fonte25.render(texto_posicao, True, (0, 0, 0))  # Cor preta
            
            # Posição do texto acima do círculo
            texto_x = x_centro - texto_renderizado.get_width() // 2  # Centraliza o texto em relação ao círculo
            texto_y = y_circulos_inicial - raio + 12  # Posição acima do círculo

            tela.blit(texto_renderizado, (texto_x, texto_y))

def desenhaEditor(tela):
    global EditorSelecionado, listaPokemon, Lista_atual_pokemons, ArrastaveisEditor, Lista_atual_itens

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
        # Se a lista atual não for a mesma da lista original, atualiza e gera os arrastáveis
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

def Abre(Editar):
    global Abrir, DeckSelecionado
    if Editar is False:
        NovoDeck = {
                "nome": "Novo Deck",
                "pokemons": [None] * 12,
                "itens": [None] * 18,
                "energiasD": [None] * 4,
                "ID":f"Deck{len(ListaDecks) + 1}"
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
        # Cálculo da posição x para o botão
        linha = i // 8  # Determine em qual linha o botão estará
        coluna = i % 8  # Determine em qual coluna o botão estará

        # Calcula a posição horizontal para o botão (de acordo com a coluna)
        pos_x = (coluna * (largura_botao + espaçamento)) + (largura_tela - largura_ocupada) // 2
        
        # Calcula a posição vertical para o botão (de acordo com a linha)
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

    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)
    
    GV.Botao(tela, "Criar Novo Baralho", (110, 450, 500, 80), AMARELO, PRETO, AZUL,
                lambda: Abre(False), Fonte50, B1, 3, None, True, eventos)
    if DeckSelecionado is not None:
        GV.Botao(tela, "Editar Baralho", (710, 450, 500, 80), VERDE, PRETO, AZUL,
                    lambda: Abre(True), Fonte50, B1, 3, None, True, eventos)
        
        GV.Botao(tela, "Apagar Baralho", (1310, 450, 500, 80), VERMELHO, PRETO, AZUL,
                    lambda: Quer_Apagar(), Fonte50, B1, 3, None, True, eventos)
        
        desenhaBaralho(tela, DeckSelecionado)

    else:
        GV.Botao(tela, "Editar Baralho", (710, 450, 500, 80), CINZA, PRETO, AZUL,
                    lambda: tocar("Bloq"), Fonte50, B1, 3, None, True, eventos)
        
        GV.Botao(tela, "Apagar Baralho", (1310, 450, 500, 80), CINZA, PRETO, AZUL,
                    lambda: tocar("Bloq"), Fonte50, B1, 3, None, True, eventos)

def TelaCriador(tela,eventos,estados):

    desenhaBaralho(tela, DeckSelecionado)

    GV.Botao_Selecao(
        tela, (120, 75, 843, 40),
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
        tela, (963, 75, 558, 40),
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
        tela, (1521, 75, 280, 260),
        "", Fonte30,
        cor_fundo=None, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
        cor_passagem=AMARELO, id_botao="Apoiador",   
        estado_global=estadoEditor, eventos=eventos,
        funcao_esquerdo=lambda: SelecionaEditor(), 
        funcao_direito=None,
        desfazer_esquerdo=lambda: DesselecionaEditor(), desfazer_direito=None,
        tecla_esquerda=None, tecla_direita=None, grossura=2)
    GV.Botao_Selecao(
        tela, (1521, 335, 280, 15),
        "", Fonte30,
        cor_fundo=None, cor_borda_normal=PRETO,
        cor_borda_esquerda=VERMELHO, cor_borda_direita=None,
        cor_passagem=AMARELO, id_botao="Energias",   
        estado_global=estadoEditor, eventos=eventos,
        funcao_esquerdo=lambda: SelecionaEditor(listaEnergias), 
        funcao_direito=None,
        desfazer_esquerdo=lambda: DesselecionaEditor(), desfazer_direito=None,
        tecla_esquerda=None, tecla_direita=None, grossura=2)

    desenhaEditor(tela)

    GV.Botao(tela, "Salvar Deck", (1470, 910, 330, 100), AMARELO_CLARO, PRETO, AZUL,
                lambda: salvar_dicionario_em_py(DeckSelecionado,DeckSelecionado["ID"],"Decks"), Fonte40, B1, 3, None, True, eventos)

    GV.Botao(tela, "Voltar", (0, 1020, 200, 60), CINZA, PRETO, AZUL,
                lambda: A.Voltar(estados), Fonte40, B1, 3, None, True, eventos)

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
    global DeckSelecionado,Abrir,EditorSelecionado,Aviso_Apagar
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

    carregar_decks("Decks")

def Decks(tela,estados,relogio):
    global ImagensItens,ImagensPokemon,TiposEnergiaIMG
    global Baralho_atual_pokemons, Baralho_atual_itens, Lista_atual_pokemons, Lista_atual_itens, Baralho_atual_energias, Lista_atual_energias
    global EditorSelecionado, EditorSelecionado_atual

    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Decks.jpg", (1920,1080))
    ImagensItens,ImagensPokemon,TiposEnergiaIMG = Carregar_Imagens2(ImagensItens,ImagensPokemon,TiposEnergiaIMG)

    pygame.mixer.music.load('Audio/Musicas/Decks.ogg')  
    pygame.mixer.music.set_volume(0.0)
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
        relogio.tick(100)

