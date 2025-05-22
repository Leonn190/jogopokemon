import pygame
import math
import random
from Visual.Sonoridade import tocar
import Visual.GeradoresVisuais as GV

terreno = None
Mapa = None
x_terreno = 0
y_terreno = 0
largura_terreno = 0
altura_terreno = 0

B1 = {"estado": False}

class PecaArrastavel:
    def __init__(self, pokemon, camera, imagem):
        self.pokemon = pokemon
        self.tela = camera
        self.imagem = imagem  # imagem da peça arrastável (ex: círculo azul + ícone)
        self.arrastando = False
        self.offset_x = 0
        self.offset_y = 0
        self.pos_inicial = pokemon.local  # (x, y)
        self.moveu = False  # Controla se o movimento foi válido

    def iniciar_arraste(self, pos_mouse):
        if not self.pokemon.PodeMover:
            return False

        x_p, y_p = self.pokemon.local
        rect = self.imagem.get_rect(center=(int(x_p), int(y_p)))

        if rect.collidepoint(pos_mouse):
            self.arrastando = True
            self.offset_x = x_p - pos_mouse[0]
            self.offset_y = y_p - pos_mouse[1]
            self.pos_inicial = self.pokemon.local
            self.pokemon.local = (pos_mouse[0], pos_mouse[1])
            return True

        return False

    def atualizar_local_durante_arrasto(self, pos_mouse):
        if self.arrastando:
            novo_x = pos_mouse[0] + self.offset_x
            novo_y = pos_mouse[1] + self.offset_y

            x_ini, y_ini = self.pos_inicial
            distancia = math.hypot(novo_x - x_ini, novo_y - y_ini)
            raio_movimento = self.pokemon.vel * Mapa.Metros // 2 + self.pokemon.raio + 15

            if distancia > raio_movimento:
                # Muito longe: cancelar arrasto
                self.arrastando = False
                self.pokemon.local = self.pos_inicial
                tocar("Bloq")  # Som de bloqueio opcional
                GV.adicionar_mensagem("Distância de movimento excedida")
                return

            # Atualiza a posição do Pokémon em tempo real
            self.pokemon.local = (novo_x, novo_y)

    def soltar(self, pos_mouse):
        if not self.arrastando:
            return

        self.arrastando = False
        x_ini, y_ini = self.pos_inicial
        x_fim = pos_mouse[0] + self.offset_x
        y_fim = pos_mouse[1] + self.offset_y

        distancia = math.hypot(x_fim - x_ini, y_fim - y_ini)
        raio_movimento = self.pokemon.vel * Mapa.Metros // 2

        if distancia <= raio_movimento + self.pokemon.raio and self.pokemon.PodeMover == True:
            if not ponto_valido(x_fim, y_fim, self.pokemon):
                self.pokemon.local = self.pos_inicial
                return

            player = self.pokemon.dono
            custo = self.pokemon.custo
            if self.pokemon.efeitosNega.get("Encharcado"):
                custo += 2

            pagou = 0
            gastas = []
            for _ in range(custo):
                for cor in player.energiasDesc:
                    if player.energias.get(cor, 0) >= 1:
                        player.energias[cor] -= 1
                        gastas.append(cor)
                        pagou += 1
                        break

            if pagou == custo:
                Mapa.mudança = True
                self.pokemon.moveu = True
                self.pokemon.local = (x_fim, y_fim)
                return
            else:
                GV.adicionar_mensagem("Sem energias")
                for cor in gastas:
                    player.energias[cor] += 1

        # Caso inválido, volta ao início
        tocar("Bloq")
        self.pokemon.local = self.pos_inicial

    def desenhar_raio_velocidade(self):
        if not self.arrastando:
            return
        x_p, y_p = map(int, self.pos_inicial)
        raio = int((self.pokemon.vel//2) * Mapa.Metros + self.pokemon.raio)

        superficie = pygame.Surface((raio*2, raio*2), pygame.SRCALPHA)
        pygame.draw.circle(superficie, (0, 255, 0, 60), (raio, raio), raio)
        self.tela.blit(superficie, (x_p - raio, y_p - raio))

    def desenhar(self, pos_mouse=None):
        if self.arrastando and pos_mouse is not None:
            x_m, y_m = pos_mouse
            center = (x_m + self.offset_x, y_m + self.offset_y)
        else:
            x_p, y_p = map(int, self.pokemon.local)
            center = (x_p, y_p)

        rect = self.imagem.get_rect(center=center)

        # Desenha a borda verde se puder mover
        if self.pokemon.PodeMover:
            raio = max(rect.width, rect.height) // 2 + 3  # raio levemente maior que o da imagem
            pygame.draw.circle(self.tela, (0, 255, 0), center, raio, width=3)

        # Desenha a imagem da peça
        self.tela.blit(self.imagem, rect)

def verifica_colisao(x, y, pokemon):
    """Verifica se o círculo em (x, y) com raio do Pokémon colide com áreas ocupadas."""
    
    raio = int(pokemon.raio)
    novo_rect = pygame.Rect(x - raio, y - raio, raio * 2, raio * 2)

    for rect in Mapa.Ocupadas:
        # Ignora o próprio Pokémon, se estiver na lista
        if hasattr(pokemon, "rect") and rect == pokemon.rect:
            continue

        if rect.colliderect(novo_rect):
            return False  # Colidiu
    return True  # Espaço livre

def ponto_valido(x, y, pokemon, ignorar_limites=False, ignora_colisão=False):
    raio = int(pokemon.raio - 2)

    # Se não ignorar limites, verifica se o ponto está dentro do terreno e alfa > 0
    if not ignorar_limites:
        for dx in range(-raio, raio + 1):
            for dy in range(-raio, raio + 1):
                if dx * dx + dy * dy <= raio * raio:
                    px = x + dx
                    py = y + dy
                    local_x = px - x_terreno
                    local_y = py - y_terreno

                    # Verifica se está dentro dos limites do terreno
                    if not (0 <= local_x < largura_terreno and 0 <= local_y < altura_terreno):
                        return False

                    # Verifica se é terreno válido (alpha > 0)
                    if terreno.get_at((local_x, local_y)).a <= 0:
                        return False

    if not ignora_colisão:
        if not verifica_colisao(x, y, pokemon):
            return False

    return True

def Desenhar_Casas_Disponiveis(tela, mapa, player, inimigo, eventos, estadoAlvo, estadoVisualiza, selecionaAlvo, desselecionaAlvo, oculta, visualiza):
    global terreno, x_terreno, y_terreno, largura_terreno, altura_terreno, Mapa
    Mapa = mapa
    
    terreno = Mapa.terreno
    largura_terreno, altura_terreno = terreno.get_size()

    # Centralizar o terreno
    largura_tela, altura_tela = tela.get_size()
    x_terreno = (largura_tela - largura_terreno) // 2
    y_terreno = (altura_tela - altura_terreno) // 2

    # Desenhar borda preta
    margem = 3  # Tamanho da borda em pixels
    pygame.draw.rect(tela, (0, 0, 0), (x_terreno - margem, y_terreno - margem,
                                       largura_terreno + 2 * margem, altura_terreno + 2 * margem))

    # Desenhar o terreno sobre a borda
    tela.blit(terreno, (x_terreno, y_terreno))

    def criar_imagem_peca(pokemon, cor_circulo):
        raio = int(pokemon.raio)
        diametro = raio * 2

        superficie = pygame.Surface((diametro, diametro), pygame.SRCALPHA)

        # Círculo com a cor passada (azul ou vermelho)
        pygame.draw.circle(superficie, cor_circulo, (raio, raio), raio)

        icone = pokemon.icone.convert_alpha()
        largura_icone, altura_icone = icone.get_size()
        pos_icone = (raio - largura_icone // 2, raio - altura_icone // 2)
        superficie.blit(icone, pos_icone)

        return superficie

    def desenhar_pokemons(jogador, criar_pecas, cor_circulo, ):
        pokemons_validos = [pokemon for pokemon in jogador.pokemons if pokemon.local is not None and ponto_valido(*pokemon.local, pokemon, ignora_colisão=True)]

        if criar_pecas is True:
            if Mapa.Peças == []:
                for pokemon in pokemons_validos:
                    imagem_peca = criar_imagem_peca(pokemon, cor_circulo)
                    nova_peca = PecaArrastavel(pokemon, tela, imagem=imagem_peca)
                    Mapa.Peças.append(nova_peca)

        else:
            for pokemon in jogador.pokemons:
                if pokemon.local is not None:
                    x, y = pokemon.local
                    if ponto_valido(x, y, pokemon, ignora_colisão=True):
                        imagem_peca = criar_imagem_peca(pokemon, cor_circulo)
                        largura_img, altura_img = imagem_peca.get_size()
                        x_img = x - largura_img // 2
                        y_img = y - altura_img // 2

                        espaço = pygame.Rect(x_img + 1, y_img + 1, largura_img - 2, altura_img - 2)
                
                        GV.Botao_Selecao2(
                        tela, espaço,
                        "", GV.Fonte20,
                        cor_fundo=(180, 0, 0), cor_borda_normal=(0, 0, 0),
                        cor_borda_esquerda=GV.VERMELHO, cor_borda_direita=GV.AZUL,
                        cor_passagem=GV.AMARELO, id_botao=pokemon,
                        estado_global_esquerdo=estadoAlvo ,estado_global_direito=estadoVisualiza, eventos=eventos,
                        funcao_esquerdo=lambda poke=pokemon: selecionaAlvo(poke),
                        funcao_direito=lambda poke=pokemon: visualiza(poke),
                        desfazer_esquerdo=lambda: desselecionaAlvo(), desfazer_direito=lambda: oculta(),
                        tecla_esquerda=pygame.K_1, tecla_direita=None)

                        tela.blit(imagem_peca, (x_img, y_img))
                    else:
                        PosicionarGuardar(pokemon, 0)


    # No corpo principal da função:
    desenhar_pokemons(player, criar_pecas=True, cor_circulo=(0, 0, 255))  # azul para player
    desenhar_pokemons(inimigo, criar_pecas=False, cor_circulo=(255, 0, 0))  # vermelho para inimigos


def PosicionarGuardar(pokemon, tempo):
    if pokemon.local is None:
        tentativas = 500  # evita loop infinito

        for _ in range(tentativas):
            x = random.randint(x_terreno, x_terreno + largura_terreno - 1)
            y_min = y_terreno + int(altura_terreno * 0.75)
            y_max = y_terreno + altura_terreno - 1
            y = random.randint(y_min, y_max)

            if ponto_valido(x, y, pokemon):
                pokemon.local = (x, y)
                Mapa.mudança = True
                Mapa.Peças = []
                return
        
    else:
        Mapa.mudança = True
        pokemon.local = None
        pokemon.guardado = tempo

def mover(pokemon,pos):
    x, y = pos
    
    if ponto_valido(x,y,pokemon) == True:
        Mapa.mudança = True
        pokemon.local = (x, y)

def inverter_tabuleiro(player, inimigo):
    for treinador in [player, inimigo]:
        for poke in treinador.pokemons:
            if poke.local is not None:
                x, y = poke.local

                # Inverte posição no tabuleiro com base nas dimensões do terreno
                novo_x = x_terreno + (largura_terreno - 1) - (x - x_terreno)
                novo_y = y_terreno + (altura_terreno - 1) - (y - y_terreno)

                poke.local = (novo_x, novo_y)

    Mapa.mudança = True
    