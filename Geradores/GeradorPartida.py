import pygame

class Partida:
    def __init__(self,player1,player2):
        self.Turno = 0
        self.Centro = []
        self.Loja = []
        self.Baralho = player1.deck + player2.deck
        self.Mapa = None
        self.player1 = player1
        self.player2 = player2
