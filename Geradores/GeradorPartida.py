import pygame
import os
import copy
import json
import re
from Jogo.Funções2 import verificar_serializabilidade
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
        self.online = False
    
def GeraPartida(player1,player2,Baralho,Mapa):
    return Partida(player1,player2,Baralho,Mapa)

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
            self.online = True
            self.anterior = self.ToDic_Inic()

        else:

                        # Demais atributos simples
            self.Turno = Dados["Turno"]
            self.tempo_restante = Dados["tempo_restante"]
            self.Centro = Dados["Centro"]
            self.Loja = Dados["Loja"]
            self.Vencedor = Dados["Vencedor"]
            self.Perdedor = Dados["Perdedor"]
            self.online = True

            # Inicializações com prints resumidos
            try:
                self.Baralho = GeraBaralhoClone(Dados["Baralho"])
            except Exception as e:
                print("Erro ao gerar Baralho:", e)

            try:
                self.Mapa = Gera_Mapa(Dados["Mapa"]["Code"])
            except Exception as e:
                print("Erro ao gerar Mapa:", e)

            try:
                self.Jogador1 = Gerador_player_clone(Dados["Jogador1"])
            except Exception as e:
                print("Erro ao gerar Jogador1:", e)
            print (self.Jogador1.pokemons[0].Atk)

            try:
                self.Jogador2 = Gerador_player_clone(Dados["Jogador2"])
            except Exception as e:
                print("Erro ao gerar Jogador2:", e)

            # Conversão final para dicionário
            self.anterior = self.ToDic_Inic()
            print("Partida inicializada e convertida para dicionário com sucesso.")

    def ToDic_Inic(self):
        erros = []

        dicionario = {
            "Turno": self.Turno,
            "tempo_restante": self.tempo_restante,
            "Centro": self.Centro,
            "Loja": self.Loja,
            "Vencedor": self.Vencedor,
            "Perdedor": self.Perdedor,
        }

        try:
            dicionario["Baralho"] = self.Baralho.ToDic()
        except Exception:
            erros.append("Baralho")

        try:
            dicionario["Mapa"] = self.Mapa.ToDic()
        except Exception:
            erros.append("Mapa")

        try:
            dicionario["Jogador1"] = self.Jogador1.ToDic()
        except Exception:
            erros.append("Jogador1")


        dicionario["Jogador2"] = self.Jogador2.ToDic()


        if erros:
            print(f"ERRO ao converter para dicionário: falhou em {', '.join(erros)}")
        else:
            print("ToDic_Inic: Tudo passado para o dicionário com sucesso.")

        verificar_serializabilidade(dicionario)
        return dicionario

def GeraPartidaOnline(player1,player2,Baralho,Mapa):
    return PartidaOnline(player1,player2,Baralho,Mapa)

def GeraPartidaOnlineClone(Dados,ID):
    P = PartidaOnline(None,None,None,None,Dados)
    P.ID = ID
    return P

