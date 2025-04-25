import pygame

mensagens_passageiras = []

class MensagemPassageira:
    def __init__(self, mensagem, cor, fonte, posicao, duracao=350, deslocamento=50):
        self.mensagem = mensagem
        self.cor = cor
        self.fonte = fonte
        self.posicao_inicial = posicao
        self.duracao = duracao
        self.deslocamento = deslocamento
        self.frame_atual = 0
        self.ativa = True

    def atualizar(self):
        self.frame_atual += 1
        if self.frame_atual >= self.duracao:
            self.ativa = False

    def desenhar(self, tela):
        if not self.ativa:
            return

        alpha = max(0, 255 - int((self.frame_atual / self.duracao) * 255))
        y_offset = int((self.frame_atual / self.duracao) * self.deslocamento)

        texto_surface = self.fonte.render(self.mensagem, True, self.cor)
        texto_surface = texto_surface.convert_alpha()
        texto_surface.set_alpha(alpha)

        x, y = self.posicao_inicial
        x_texto = x
        y_texto = y - y_offset

        largura = texto_surface.get_width() + 20
        altura = texto_surface.get_height() + 10

        # Cria a superfície com canal alpha
        fundo = pygame.Surface((largura, altura), pygame.SRCALPHA)
        
        # Cor branca com transparência proporcional
        cor_fundo = (255, 255, 255, min(200, alpha))  # branco semi-transparente

        # Desenha retângulo arredondado
        pygame.draw.rect(fundo, cor_fundo, fundo.get_rect(), border_radius=10)

        # Posiciona retângulo levemente centralizado em relação ao texto
        tela.blit(fundo, (x_texto - 10, y_texto - 5))
        tela.blit(texto_surface, (x_texto, y_texto))

def adicionar_mensagem_passageira(mensagens, texto, cor, fonte, posicao, duracao=200, deslocamento=90):
    nova_mensagem = MensagemPassageira(texto, cor, fonte, posicao, duracao, deslocamento)
    mensagens_passageiras.append(nova_mensagem)