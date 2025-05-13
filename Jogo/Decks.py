import pygame
import os
import importlib
import Visual.GeradoresVisuais as GV
import PygameAções as A
from Visual.Imagens import Carregar_Imagens2
from Geradores.GeradorOutros import Amplificadores_Todos,Frutas_Todas,Pokebolas_Todas,Poçoes_Todas,Estadios_Todos,Outros_Todos,Pokemons_Todos
from Visual.Sonoridade import tocar
from Visual.GeradoresVisuais import (
    Fonte15, Fonte20, Fonte30, Fonte40, Fonte50,Fonte70,
    PRETO, BRANCO, CINZA, AZUL, AZUL_CLARO,AZUL_SUPER_CLARO,
    AMARELO, AMARELO_CLARO, VERMELHO,VERMELHO_CLARO, VERDE, VERDE_CLARO,
    LARANJA, ROXO, ROSA, DOURADO, PRATA,)

pygame.init()
pygame.mixer.init()

DeckSelecionado = None
Abrir = None
ListaDecks = []

ImagensPokemon = {}
ImagensItens = {}

def salvar_dicionario_em_py(dicionario, nome_arquivo, pasta_destino):
    """Salva um dicionário em um arquivo .py no formato Python."""
    # Garante que a pasta existe
    os.makedirs(pasta_destino, exist_ok=True)

    # Monta o caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta_destino, f"{nome_arquivo}.py")

    # Abre e escreve o dicionário em formato Python legível
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(f"# Arquivo gerado automaticamente\n\n")
        arquivo.write(f"{nome_arquivo} = {repr(dicionario)}\n")

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
                    Decks.append(valor)
                    break

def desenhaBaralho(tela, ImagensPokemon, ImagensItens, Baralho):
    # Configurações do fundo do baralho
    x_inicial = 120
    y_inicial = 75
    largura = 1680
    altura = 320
    largura_extra = 280  # Largura da extensão
    altura_extra = 55    # Altura da extensão

    cor_fundo = (50, 50, 50)
    cor_borda = (0, 0, 0)
    cor_linha = (0, 0, 0)

    # Desenha o fundo principal
    pygame.draw.rect(tela, cor_fundo, (x_inicial, y_inicial, largura, altura))

    # Desenha a extensão superior direita
    pygame.draw.rect(tela, cor_fundo, (x_inicial + largura - largura_extra, y_inicial - altura_extra, largura_extra, altura_extra))

    # Desenha a borda ao redor
    pontos = [
        (x_inicial, y_inicial),
        (x_inicial + largura - largura_extra, y_inicial),
        (x_inicial + largura - largura_extra, y_inicial - altura_extra),
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
    pygame.draw.line(tela, cor_linha, (x_divisao, y_inicial), (x_inicial + largura, y_inicial), width=4)

    # Linha horizontal 280px abaixo da linha horizontal superior, dentro do setor direito
    y_linha_inferior = y_inicial - altura_extra + 280
    pygame.draw.line(tela, cor_linha, (x_divisao, y_linha_inferior + 25), (x_inicial + largura, y_linha_inferior + 25), width=4)

    # Linha horizontal dentro do setor esquerdo dividindo 120px em cima e 200px em baixo
    linha_esquerda_y = y_inicial + 40
    pygame.draw.line(tela, cor_linha, (x_inicial, linha_esquerda_y), (x_divisao, linha_esquerda_y), width=4)

    # Nova linha vertical dentro do setor esquerdo dividindo em 60% / 40%
    largura_esquerda = x_divisao - x_inicial
    x_linha_interna_esquerda = x_inicial + int(largura_esquerda * 0.6)
    pygame.draw.line(tela, cor_linha, (x_linha_interna_esquerda, y_inicial), (x_linha_interna_esquerda, y_inicial + altura), width=4)

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

    if Abrir is None:
         # Área útil para os pokémons (60% da esquerda, abaixo da linha de 40px)
        area_pokemons_x = x_inicial
        area_pokemons_y = linha_esquerda_y
        area_pokemons_largura = x_linha_interna_esquerda - x_inicial
        area_pokemons_altura = y_inicial + altura - linha_esquerda_y

        # Configuração dos slots
        linhas = 2
        colunas = 6
        espacamento = 10

        # Calcular o tamanho do quadrado com base na largura disponível e espaçamento
        largura_disponivel = area_pokemons_largura - (espacamento * (colunas + 1))
        altura_disponivel = area_pokemons_altura - (espacamento * (linhas + 1))

        lado_slot = min(largura_disponivel // colunas, altura_disponivel // linhas)

        for i in range(12):
            linha = i // colunas
            coluna = i % colunas

            x_slot = area_pokemons_x + espacamento + coluna * (lado_slot + espacamento) + 10
            y_slot = area_pokemons_y + espacamento + linha * (lado_slot + espacamento)

            pokemon = Baralho["pokemons"][i]

            if pokemon is not None:
                # Slot com Pokémon
                pygame.draw.rect(tela, (200, 200, 0), (x_slot, y_slot, lado_slot, lado_slot))
                imagem_pokemon = ImagensPokemon.get(pokemon["nome"])
                if imagem_pokemon:
                    imagem_redimensionada = pygame.transform.smoothscale(imagem_pokemon, (lado_slot, lado_slot))
                    tela.blit(imagem_redimensionada, (x_slot, y_slot))
            else:
                # Slot vazio (um pouco menor e cinza)
                margem = int(lado_slot * 0.1)
                pygame.draw.rect(tela, (80, 80, 80), (x_slot + margem, y_slot + margem, lado_slot - 2 * margem, lado_slot - 2 * margem))
        
        # === ITENS (REESTRUTURADO PARA 18 slots: 3x6) ===
        area_itens_x = x_linha_interna_esquerda
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

            item = Baralho["itens"][i]

            if item is not None:
                pygame.draw.rect(tela, (100, 220, 100), (x_slot, y_slot, lado_slot_item, lado_slot_item))
                imagem_item = ImagensItens.get(item["nome"])
                if imagem_item:
                    imagem_redimensionada = pygame.transform.smoothscale(imagem_item, (lado_slot_item, lado_slot_item))
                    tela.blit(imagem_redimensionada, (x_slot, y_slot))
            else:
                margem = int(lado_slot_item * 0.1)
                pygame.draw.rect(tela, (80, 80, 80), (x_slot + margem, y_slot + margem, lado_slot_item - 2 * margem, lado_slot_item - 2 * margem))

teste = {
    "nome": "Baralho foda",
    "pokemons": [Pokemons_Todos[4],None,Pokemons_Todos[27],Pokemons_Todos[24],Pokemons_Todos[11],Pokemons_Todos[16],None,Pokemons_Todos[5],None,Pokemons_Todos[20],Pokemons_Todos[9],Pokemons_Todos[8]],
    "itens": [None,None,None,None,None,None,None,None,None,None,Amplificadores_Todos[2],None,None,None,None,None,None,None,None,None,None,]
}

estadoDecks = {"selecionado_esquerdo": None}

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

    ListaDecks1 = [teste]

    # Cálculo do total de largura ocupada pelos 8 botões e espaços entre eles
    largura_ocupada = (largura_botao * 8) + (espaçamento * 7)
    
    for i, deck in enumerate(ListaDecks1):
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
                lambda: A.Voltar(estados), Fonte50, B1, 3, None, True, eventos)
    if DeckSelecionado is not None:
        GV.Botao(tela, "Editar Baralho", (710, 450, 500, 80), VERDE, PRETO, AZUL,
                    lambda: A.Voltar(estados), Fonte50, B1, 3, None, True, eventos)
        
        GV.Botao(tela, "Apagar Baralho", (1310, 450, 500, 80), VERMELHO, PRETO, AZUL,
                    lambda: A.Voltar(estados), Fonte50, B1, 3, None, True, eventos)
        
        desenhaBaralho(tela, ImagensPokemon, ImagensItens, DeckSelecionado)

    else:
        GV.Botao(tela, "Editar Baralho", (710, 450, 500, 80), CINZA, PRETO, AZUL,
                    lambda: tocar("Bloq"), Fonte50, B1, 3, None, True, eventos)
        
        GV.Botao(tela, "Apagar Baralho", (1310, 450, 500, 80), CINZA, PRETO, AZUL,
                    lambda: tocar("Bloq"), Fonte50, B1, 3, None, True, eventos)

def TelaCriador(tela,eventos,estados):
    pass

def Decks(tela,estados,relogio):
    global ImagensItens,ImagensPokemon

    Fundo_Menu = GV.Carregar_Imagem("imagens/fundos/Decks.jpg", (1920,1080))
    ImagensItens,ImagensPokemon = Carregar_Imagens2(ImagensItens,ImagensPokemon)

    pygame.mixer.music.load('Audio/Musicas/Decks.ogg')  
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    carregar_decks("Decks")

    while estados["Rodando_Decks"]:
        tela.blit(Fundo_Menu, (0, 0))
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                estados["Rodando_Menu"] = False
                estados["Rodando_Jogo"] = False

        if Abrir is None:
            TelaDecks(tela,eventos,estados)
        else:
            TelaCriador(tela,eventos,estados)

        pygame.display.update()
        relogio.tick(60)

