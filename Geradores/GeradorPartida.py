import pygame
import os
import json
import re
from deepdiff import DeepDiff

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



class PartidaOnline:
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
        self.anterior = self.ToDic_Inic()

    def ToDic_Inic(self):
        return {
            "Turno": self.Turno,
            "tempo_restante": self.tempo_restante,
            "Centro": self.Centro,  # sem alteração, só copia a lista
            "Loja": self.Loja,      # idem
            "Baralho": self.Baralho.ToDic(),
            "Mapa": self.Mapa.ToDic(),
            "Jogador1": self.Jogador1.ToDic_Inicial(),
            "Jogador2": self.Jogador2.ToDic_Inicial(),
            "Vencedor": self.Vencedor,  # só copia (se for None ou nome ou id)
            "Perdedor": self.Perdedor,
        }
    
    def ToDic_Atualiza(self):
        return {
            "Turno": self.Turno,
            "tempo_restante": self.tempo_restante,
            "Centro": self.Centro,  # sem alteração, só copia a lista
            "Loja": self.Loja,      # idem
            "Baralho": self.Baralho.ToDic(),
            "Mapa": self.Mapa.ToDic(),
            "Jogador1": self.Jogador1.ToDic_Atualiza(),
            "Jogador2": self.Jogador2.ToDic_Atualiza(),
            "Vencedor": self.Vencedor,  # só copia (se for None ou nome ou id)
            "Perdedor": self.Perdedor,
        }
    
    def VerificaDiferença(self):
        
        atual = self.ToDic_Atualiza()

        diff = DeepDiff(self.anterior, atual, verbose_level=2)
        self.anterior = atual
        return diff.to_dict()
    
    def atualizar(self, diff):

        changes = diff.get("values_changed", {})

        for caminho, valores in changes.items():
            caminho_obj = caminho.replace("root", "self")
            caminho_obj = re.sub(r"\['(\w+)'\]", r".\1", caminho_obj)

            try:
                exec(f"{caminho_obj} = {repr(valores['new_value'])}")
            except:
                pass
        self.anterior = self.ToDic_Inic()


def GeraPartidaOnline(player1,player2,Baralho,Mapa):
    return PartidaOnline(player1,player2,Baralho,Mapa)
