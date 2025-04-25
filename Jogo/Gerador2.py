import pygame
from Visual.Sonoridade import tocar
from Geradores.GeradorPokemon import Gerador_final
from Geradores.GeradorPlayer import Gerador_player
import Visual.GeradoresVisuais as GV
from Geradores.GeradorOutros import pokebolas_disponiveis,itens_disponiveis,amplificadores_disponiveis,Estadios_disponiveis,caixa,coletor,gera_item,spawn_do_centro,Gera_Mapa


pygame.init()
pygame.mixer.init()

Energias = ["vermelha", "azul", "amarela", "verde", "roxa", "rosa", "laranja", "marrom", "cinza", "preta"]
