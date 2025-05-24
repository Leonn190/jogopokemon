import pygame

class Partida:
    def __init__(self,player1,player2,Baralho,Mapa):
        self.Turno = 1
        self.tempo_restante = 0
        self.Centro = [None,None,None,None,None,None,None,None]
        self.Loja = [None,None,None,None]
        self.Baralho = Baralho
        self.Mapa = Mapa
        self.Jogador1 = player1
        self.Jogador2 = player2
        self.Vencedor = None
        self.Perdedor = None

def GeraPartida(player1,player2,Baralho,Mapa):
    return Partida(player1,player2,Baralho,Mapa)
