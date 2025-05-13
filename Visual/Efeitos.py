import pygame
import Visual.GeradoresVisuais as GV
import os

efeitos_ativos = []

# Agora só guardamos o que muda
Parametros_Efeitos = {
    "Evoluindo": {"velocidade": 92, "duracao": 2800},
    "!None": {"velocidade": 100, "duracao": 1000},

    "LabaredaMultipla": {"velocidade": 32, "duracao": 2800},
    "Corte": {"velocidade": 98, "duracao": 1100},
    "BolhasVerdes": {"velocidade": 50, "duracao": 2100},
    "CorteDourado": {"velocidade": 92, "duracao": 1300},
    "ChuvaVermelha": {"velocidade": 32, "duracao": 3300},
    "ChuvaBrilhante": {"velocidade": 30, "duracao": 2500},
    "Agua": {"velocidade": 42, "duracao": 1500},
    "AtemporalRosa": {"velocidade": 25, "duracao": 3000},
    "BarreiraCelular": {"velocidade": 80, "duracao": 1200},
    "ChicoteMultiplo": {"velocidade": 72, "duracao": 1200},
    "CorteDuploRoxo": {"velocidade": 30, "duracao": 2700},
    "CorteMagico": {"velocidade": 40, "duracao": 1600},
    "CorteRicocheteadoRoxo": {"velocidade": 112, "duracao": 700},
    "CorteRosa": {"velocidade": 40, "duracao": 2200},
    "DomoVerde": {"velocidade": 85, "duracao": 1400},
    "EnergiaAzul": {"velocidade": 65, "duracao": 1100},
    "Engrenagem": {"velocidade": 115, "duracao": 900},
    "EspiralAzul": {"velocidade": 45, "duracao": 2200},
    "Estouro": {"velocidade": 97, "duracao": 750},
    "EstouroMagico": {"velocidade": 50, "duracao": 1800},
    "EstouroVermelho": {"velocidade": 46, "duracao": 1200},
    "Explosao": {"velocidade": 45, "duracao": 2000},
    "ExplosaoPedra": {"velocidade": 92, "duracao": 1400},
    "ExplosaoVerde": {"velocidade": 112, "duracao": 900},
    "ExplosaoVermelha": {"velocidade": 30, "duracao": 2200},
    "ExplosaoRoxa": {"velocidade": 105, "duracao": 1000},
    "FacasAzuis": {"velocidade": 28, "duracao": 3000},
    "FacasBrancas": {"velocidade": 38, "duracao": 2100},
    "FacasColoridas": {"velocidade": 32, "duracao": 2200},
    "FacasRosas": {"velocidade": 25, "duracao": 2700},
    "FeixeMagenta": {"velocidade": 42, "duracao": 1800},
    "FeixeRoxo": {"velocidade": 96, "duracao": 800},
    "FluxoAzul": {"velocidade": 65, "duracao": 2200},
    "Fogo": {"velocidade": 95, "duracao": 1000},
    "Fumaça": {"velocidade": 35, "duracao": 2200},
    "GasRoxo": {"velocidade": 78, "duracao": 1300},
    "Garra": {"velocidade": 80, "duracao": 900},
    "HexagonoLaminas": {"velocidade": 36, "duracao": 1300},
    "ImpactoRochoso": {"velocidade": 115, "duracao": 600},
    "Karate": {"velocidade": 90, "duracao": 1200},
    "LuaAmarela": {"velocidade": 18, "duracao": 3500},
    "MagiaAzul": {"velocidade": 26, "duracao": 3600},
    "MagiaMagenta": {"velocidade": 48, "duracao": 1900},
    "MarcaBrilhosa": {"velocidade": 38, "duracao": 2700},
    "MarcaAmarela": {"velocidade": 52, "duracao": 2600},
    "MarcaAzul": {"velocidade": 38, "duracao": 2500},
    "Mordida": {"velocidade": 115, "duracao": 800},
    "MultiplasFacas": {"velocidade": 36, "duracao": 2900},
    "OrbesRoxos": {"velocidade": 28, "duracao": 2500},
    "PedaçoColorido": {"velocidade": 38, "duracao": 2300},
    "RaioAzul": {"velocidade": 12, "duracao": 4700},
    "RajadaAmarela": {"velocidade": 35, "duracao": 2000},
    "RasgoMagenta": {"velocidade": 26, "duracao": 3200},
    "RasgosRosa": {"velocidade": 28, "duracao": 2900},
    "RedemoinhoAzul": {"velocidade": 38, "duracao": 1900},
    "RedemoinhoCosmico": {"velocidade": 95, "duracao": 1300},
    "SuperDescarga": {"velocidade": 82, "duracao": 1100},
    "SuperNova": {"velocidade": 32, "duracao": 3000},
    "TirosAmarelos": {"velocidade": 25, "duracao": 2900},
    "TornadoAgua": {"velocidade": 39, "duracao": 3900},
}

class GifAtivo:
    def __init__(self, frames, posicao, velocidade, duracao, ao_terminar=None):
        self.frames = frames
        self.posicao = posicao
        self.velocidade = velocidade
        self.duracao = duracao
        self.ao_terminar = ao_terminar

        self.inicio = pygame.time.get_ticks()
        self.tempo_ultimo_frame = self.inicio
        self.frame_atual = 0

        self.tempo_80_porcento = self.inicio + (self.duracao * 0.76)
        self.termino = self.inicio + self.duracao

        self.funcao_chamada = False  # <- novo controle

    def desenhar(self, tela):
        agora = pygame.time.get_ticks()

        # Avança o frame se o tempo de velocidade já tiver passado
        if agora - self.tempo_ultimo_frame >= self.velocidade:
            self.frame_atual += 1
            self.tempo_ultimo_frame = agora

        # Desenha o frame atual da animação
        if self.frame_atual < len(self.frames):
            imagem = self.frames[self.frame_atual]
            rect = imagem.get_rect(center=self.posicao)
            tela.blit(imagem, rect)
        else:
            # Se o frame atual passou o número de frames, fixa no último
            imagem = self.frames[-1]
            rect = imagem.get_rect(center=self.posicao)
            tela.blit(imagem, rect)

    def finalizado(self):
        agora = pygame.time.get_ticks()

        # Quando atingir 80% do tempo, chama a função só uma vez
        if not self.funcao_chamada and agora >= self.tempo_80_porcento:
            if self.ao_terminar:
                self.ao_terminar()
            self.funcao_chamada = True  # Marca que já chamou

        # Finaliza apenas após 100% do tempo
        return agora >= self.termino

def adicionar_efeito(efeito, posicao, ao_terminar=None):
    # Gera o caminho automaticamente
    caminho = f'imagens/Efeitos/{efeito}_frames'
    frames = GV.carregar_frames(caminho)

    parametros = Parametros_Efeitos[efeito]

    efeitos_ativos.append(GifAtivo(
        frames=frames,
        posicao=posicao,
        velocidade=parametros["velocidade"],
        duracao=parametros["duracao"],
        ao_terminar=ao_terminar
    ))

    del frames

def atualizar_efeitos(tela):
    for gif in efeitos_ativos[:]:
        gif.desenhar(tela)
        if gif.finalizado():
            efeitos_ativos.remove(gif)


class GifCondicional:
    def __init__(self, frames, pos, intervalo):
        self.frames = frames
        self.index = 0
        self.tempo_entre_frames = intervalo
        self.ultimo_tempo = pygame.time.get_ticks()
        self.pos = pos  # A posição de destino (onde você quer que o gif fique)
        self.ativo = True  # Continua sendo ativo

    def atualizar(self, tela):
        if not self.ativo:
            return

        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_tempo > self.tempo_entre_frames:
            self.index += 1
            self.ultimo_tempo = tempo_atual

            # Redefine o índice para criar o efeito de repetição infinita
            if self.index >= len(self.frames):
                self.index = 0  # Volta ao primeiro frame

        # Desenha o frame atual centralizado
        if self.index < len(self.frames):
            largura = self.frames[self.index].get_width()
            altura = self.frames[self.index].get_height()

            # Calculando a posição de modo que o gif fique centralizado
            pos_x = self.pos[0] - largura // 2
            pos_y = self.pos[1] - altura // 2

            tela.blit(self.frames[self.index], (pos_x, pos_y))  # Desenha o gif

    def apagar(self):
        self.ativo = False  # Caso precise parar manualmente em algum momento

def gerar_gif(frames, posicao, intervalo=80):
    return GifCondicional(frames, posicao, intervalo)
