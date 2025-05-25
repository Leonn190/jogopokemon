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

            # Demais atributos simples
            self.Turno = 1
            self.tempo_restante = 0
            self.Centro = [None,None,None,None,None,None,None,None]
            self.Loja = [None,None,None,None]
            self.Vencedor = None
            self.Perdedor = None
            self.ID = 2

            print("DEBUG: Criando Baralho...")
            self.Baralho = GeraBaralhoClone(Dados["Baralho"])
            print("DEBUG: Baralho criado com sucesso.")

            print("DEBUG: Gerando Mapa...")
            self.Mapa = Gera_Mapa(Dados["Mapa"]["Code"])
            print("DEBUG: Mapa gerado com sucesso.")

            print("DEBUG: Gerando Jogador 1...")
            self.Jogador1 = Gerador_player_clone(Dados["Jogador1"])
            print("DEBUG: Jogador 1 criado com sucesso.")

            print("DEBUG: Gerando Jogador 2...")
            self.Jogador2 = Gerador_player_clone(Dados["Jogador2"])
            print("DEBUG: Jogador 2 criado com sucesso.")

            print("DEBUG: Convertendo partida para dicionário...")
            self.anterior = self.ToDic_Inic()
            print("DEBUG: Conversão para dicionário finalizada com sucesso.")

    def ToDic_Inic(self):
        print("DEBUG ToDic_Inic: Convertendo Turno, tempo, Centro, Loja, Vencedor e Perdedor...")
        dicionario = {
            "Turno": self.Turno,
            "tempo_restante": self.tempo_restante,
            "Centro": self.Centro,
            "Loja": self.Loja,
            "Vencedor": self.Vencedor,
            "Perdedor": self.Perdedor,
        }

        print("DEBUG ToDic_Inic: Convertendo Baralho...")
        try:
            dicionario["Baralho"] = self.Baralho.ToDic()
            print("DEBUG ToDic_Inic: Baralho convertido com sucesso.")
        except Exception as e:
            print("ERRO em Baralho.ToDic():", e)

        print("DEBUG ToDic_Inic: Convertendo Mapa...")
        try:
            dicionario["Mapa"] = self.Mapa.ToDic()
            print("DEBUG ToDic_Inic: Mapa convertido com sucesso.")
        except Exception as e:
            print("ERRO em Mapa.ToDic():", e)

        print("DEBUG ToDic_Inic: Convertendo Jogador1...")
        try:
            dicionario["Jogador1"] = self.Jogador1.ToDic()
            print("DEBUG ToDic_Inic: Jogador1 convertido com sucesso.")
        except Exception as e:
            print("ERRO em Jogador1.ToDic_Inicial():", e)

        print("DEBUG ToDic_Inic: Convertendo Jogador2...")
        try:
            dicionario["Jogador2"] = self.Jogador2.ToDic()
            print("DEBUG ToDic_Inic: Jogador2 convertido com sucesso.")
        except Exception as e:
            print("ERRO em Jogador2.ToDic_Inicial():", e)

        return dicionario
    
    def ToDic_Atualiza(self):
        return {
            "Turno": self.Turno,
            "tempo_restante": self.tempo_restante,
            "Centro": self.Centro,  # sem alteração, só copia a lista
            "Loja": self.Loja,      # idem
            "Baralho": self.Baralho.ToDic(),
            "Mapa": self.Mapa.ToDic(),
            "Jogador1": self.Jogador1.ToDic(),
            "Jogador2": self.Jogador2.ToDic(),
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

def GeraPartidaOnlineClone(Dados,ID):
    P = PartidaOnline(None,None,None,None,Dados)
    P.ID = ID
    return P
