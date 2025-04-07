import pygame
import sys

# Inicializa o pygame
pygame.init()

# Cores
BRANCO = (255, 255, 255)
CINZA = (200, 200, 200)
AZUL = (100, 100, 255)
PRETO = (0, 0, 0)

# Tela
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Botão com Pygame")

# Fonte
fonte = pygame.font.SysFont(None, 36)

# Função para desenhar o botão
def desenhar_botao(tela, texto, x, y, largura, altura, cor_normal, cor_hover, acao=None):
    mouse = pygame.mouse.get_pos()
    clique = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x + largura and y < mouse[1] < y + altura:
        pygame.draw.rect(tela, cor_hover, (x, y, largura, altura))
        if clique[0] == 1 and acao:
            acao()
    else:
        pygame.draw.rect(tela, cor_normal, (x, y, largura, altura))

    texto_renderizado = fonte.render(texto, True, PRETO)
    texto_rect = texto_renderizado.get_rect(center=(x + largura // 2, y + altura // 2))
    tela.blit(texto_renderizado, texto_rect)

# Exemplo de ação ao clicar
def exemplo_acao():
    print("Botão clicado!")

# Loop principal
relogio = pygame.time.Clock()
rodando = True
while rodando:
    tela.fill(BRANCO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Desenha o botão
    desenhar_botao(tela, "Clique aqui", 200, 150, 200, 60, CINZA, AZUL, exemplo_acao)

    pygame.display.update()
    relogio.tick(60)

pygame.quit()
sys.exit()