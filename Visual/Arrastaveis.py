import pygame

class DraggableImagem:
    def __init__(self, imagem, pos_inicial, areas_destino, funcoes_sucesso, funcao_clique=None):
        self.imagem = imagem
        self.rect = self.imagem.get_rect(topleft=pos_inicial)
        self.pos_inicial = pos_inicial
        self.areas_destino = areas_destino
        self.funcoes_sucesso = funcoes_sucesso
        self.funcao_clique = funcao_clique  # Nova função de clique
        self.arrastando = False
        self.offset_x = 0
        self.offset_y = 0

    def handle_event(self, event, outros_itens=[]):
        """
        Handle de eventos para o item arrastável e função de clique simples.
        
        :param event: Evento Pygame
        :param outros_itens: Lista de outros itens arrastáveis a serem verificados.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3 and self.rect.collidepoint(event.pos):  # Botão direito
                print("Clique direito detectado!")

                # Executa a função de clique simples (sem arrastar)
                if self.funcao_clique:
                    print("Executando função de clique.")
                    self.funcao_clique()

                # Apenas inicia arrasto se nenhum outro está arrastando
                if not any(item.arrastando for item in outros_itens):
                    self.arrastando = True
                    self.offset_x = self.rect.x - event.pos[0]
                    self.offset_y = self.rect.y - event.pos[1]

        elif event.type == pygame.MOUSEBUTTONUP:
            if self.arrastando:
                print("Arraste finalizado!")
                sucesso = False
                for i, area in enumerate(self.areas_destino):
                    if area.colliderect(self.rect):
                        print(f"Item solto na área {i}")
                        self.funcoes_sucesso[i]()  # Chama a função de sucesso
                        sucesso = True
                        break
                if not sucesso:
                    print("Não colidiu com nenhuma área, retornando à posição inicial.")
                    self.rect.topleft = self.pos_inicial
                self.arrastando = False

        elif event.type == pygame.MOUSEMOTION and self.arrastando:
            print(f"Movendo para: {event.pos}")
            self.rect.x = event.pos[0] + self.offset_x
            self.rect.y = event.pos[1] + self.offset_y

    def atualiza_posicao(self, pos_mouse):
        if self.arrastando:
            self.rect.x = pos_mouse[0] + self.offset_x
            self.rect.y = pos_mouse[1] + self.offset_y

    def desenha(self, surface):
        surface.blit(self.imagem, self.rect)



def Gera_Arrastavel(imagem, pos_inicial, areas_destino, funcoes_sucesso, fun):
    return DraggableImagem(imagem, pos_inicial, areas_destino, funcoes_sucesso, fun)