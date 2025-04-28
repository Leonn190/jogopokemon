import pygame
import Visual.GeradoresVisuais as GV

efeitos_ativos = []

# Agora só guardamos o que muda
Parametros_Efeitos = {
    "Evoluindo": {"velocidade": 95, "duracao": 2600},
    "LabaredaMultipla": {"velocidade": 50, "duracao": 1500},
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

        # Calculando 80% da duração total
        self.tempo_80_porcento = self.inicio + (self.duracao * 0.8)

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

    def finalizado(self):
        # Verifica se o efeito atingiu os 80% do tempo
        if pygame.time.get_ticks() >= self.tempo_80_porcento:
            # Chama a função de término (se houver)
            if self.ao_terminar:
                self.ao_terminar()
            return True  # Retorna True quando o efeito alcançou os 80%
        return False

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
