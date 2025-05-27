import pygame
import re
import os
import time

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

class GifCondicional:
    def __init__(self, frames, pos, intervalo, loop=True):
        self.frames = frames
        self.index = 0
        self.tempo_entre_frames = intervalo
        self.ultimo_tempo = pygame.time.get_ticks()
        self.pos = pos
        self.ativo = True
        self.loop = loop
        self.direcao = 1  # 1 para frente, -1 para trás

    def atualizar(self, tela):
        if not self.ativo:
            return

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tempo > self.tempo_entre_frames:
            self.ultimo_tempo = tempo_atual

            # Atualização de índice com base no modo de loop
            if self.loop:
                self.index = (self.index + 1) % len(self.frames)
            else:
                self.index += self.direcao
                # Inverte a direção ao atingir as extremidades
                if self.index >= len(self.frames):
                    self.index = len(self.frames) - 2
                    self.direcao = -1
                elif self.index < 0:
                    self.index = 1
                    self.direcao = 1

        # Desenha o frame atual centralizado
        if 0 <= self.index < len(self.frames):
            frame = self.frames[self.index]
            largura = frame.get_width()
            altura = frame.get_height()
            pos_x = self.pos[0] - largura // 2
            pos_y = self.pos[1] - altura // 2
            tela.blit(frame, (pos_x, pos_y))

    def apagar(self):
        self.ativo = False

Fonte40 = pygame.font.SysFont(None, 40)
Carregamento = True

def TelaCarregamento(tela, relogio, config, Surface):
    global Carregamento

    Carregando_Frames = carregar_frames("imagens/Efeitos/!Loading_frames")
    Gif = GifCondicional(Carregando_Frames, (tela.get_width() // 2, tela.get_height() // 2), 62)
    Carregamento = True

    pontos = [".", "..", "..."]
    indice_pontos = 0
    tempo_pontos = time.time()

    # Loop de carregamento
    while Carregamento:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        tela.fill((0, 0, 0))

        Gif.atualizar(tela)

        if time.time() - tempo_pontos > 0.5:
            indice_pontos = (indice_pontos + 1) % len(pontos)
            tempo_pontos = time.time()

        texto = Fonte40.render("Carregando" + pontos[indice_pontos], True, (255, 255, 255))
        rect = texto.get_rect(center=(tela.get_width() // 2, tela.get_height() // 2 + 150))
        tela.blit(texto, rect)

        pygame.display.update()
        relogio.tick(config["FPS"])