import pygame
import Visual.GeradoresVisuais as GV

efeitos_ativos = []

Lista_Efeitos = {
    "Evoluir": lambda:GV.carregar_frames('imagens/Efeitos/Evoluindo_frames')
}

class GifAtivo:
    def __init__(self, frames, posicao, velocidade, duracao, ao_terminar=None):
        self.frames = frames
        self.posicao = posicao
        self.velocidade = velocidade  # ms por frame
        self.duracao = duracao        # duração total em ms
        self.ao_terminar = ao_terminar

        self.inicio = pygame.time.get_ticks()
        self.tempo_ultimo_frame = self.inicio
        self.frame_atual = 0

    def desenhar(self, tela):
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_frame >= self.velocidade:
            self.frame_atual += 1
            self.tempo_ultimo_frame = agora

        if self.frame_atual < len(self.frames):
            tela.blit(self.frames[self.frame_atual], self.posicao)

    def finalizado(self):
        return pygame.time.get_ticks() - self.inicio >= self.duracao

def adicionar_efeito(efeito, posicao, velocidade=95, duracao=2600,ao_terminar=None):
    frames = Lista_Efeitos[efeito]()

    efeitos_ativos.append(GifAtivo(frames, posicao, velocidade, duracao, ao_terminar))

    del frames

def atualizar_efeitos(tela):
    for gif in efeitos_ativos[:]:
        gif.desenhar(tela)
        if gif.finalizado():
            if gif.ao_terminar:
                gif.ao_terminar()
            efeitos_ativos.remove(gif)
