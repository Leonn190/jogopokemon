import pygame
import os
import json
import re
from Geradores.GeradorPokemon import Gerador_Clone
from Geradores.GeradorOutros import GeraBaralhoClone, Gera_Mapa
from Geradores.GeradorPlayer import Gerador_player_clone
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



def navegar_e_setar(obj, caminho, valor):
    # Divide o caminho em partes (suporta ['chave'], [índice], .atributo)
    partes = re.findall(r"\['(.*?)'\]|\[(\d+)\]|\.([a-zA-Z_][\w]*)", caminho)

    atual = obj
    for i, parte in enumerate(partes[:-1]):
        chave = parte[0] or parte[1] or parte[2]

        # Caminho parcial para debug (opcional)
        # print(f"Passo {i}: {repr(atual)} >> {repr(chave)}")

        if parte[1]:  # índice de lista
            atual = atual[int(chave)]
        elif isinstance(atual, dict):
            atual = atual.get(chave)
        else:
            atual = getattr(atual, chave)

    # Última parte do caminho: onde o valor será atribuído
    parte_final = partes[-1]
    chave_final = parte_final[0] or parte_final[1] or parte_final[2]

    if parte_final[1]:  # é índice de lista
        atual[int(chave_final)] = valor
    elif isinstance(atual, dict):  # é dicionário
        atual[chave_final] = valor
    else:  # é atributo de objeto
        setattr(atual, chave_final, valor)

class PartidaOnline:
    def __init__(self,player1,player2,Baralho,Mapa,Dados=False):
    
        if Dados is False:
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
        else:
            self.Turno = 1
            self.tempo_restante = 0
            self.Centro = [None,None,None,None,None,None,None,None]
            self.Loja = [None,None,None,None]
            self.Baralho = GeraBaralhoClone(Dados["Baralho"])
            self.Mapa = Gera_Mapa(Dados["Mapa"])
            self.Jogador1 = Gerador_player_clone(Dados["Jogador1"])
            self.Jogador2 = Gerador_player_clone(Dados["Jogador2"])
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
        # Caso o diff contenha um novo dicionário completo do objeto (ex: Pokémon)
        if "new" in diff and isinstance(diff["new"], dict):
            try:
                clone = Gerador_Clone(diff["new"])
                self.__dict__.update(clone.__dict__)  # substitui todos os atributos do objeto atual
                self.anterior = self.ToDic_Inic()
                print("[INFO] Objeto substituído por um clone completo.")
                return
            except Exception as e:
                print(f"[ERRO] Ao gerar clone de objeto: {e}")

        # Caso o diff contenha mudanças parciais
        changes = diff.get("values_changed", {})

        for caminho, valores in changes.items():
            caminho_obj = caminho.replace("root", "")  # remove "root"
            try:
                navegar_e_setar(self, caminho_obj, valores["new_value"])
            except Exception as e:
                print(f"[ERRO] Ao atualizar {caminho_obj}: {e}")

        self.anterior = self.ToDic_Inic()

def GeraPartidaOnline(player1,player2,Baralho,Mapa):
    return PartidaOnline(player1,player2,Baralho,Mapa)

def GeraPartidaOnlineClone(Dados):
    return PartidaOnline(None,None,None,None,Dados)
