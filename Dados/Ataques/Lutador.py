from Geradores.GeradorAtaques import Regular
from Jogo.Mapa import mover
from Geradores.GeradorOutros import Gera_item
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Chamar_para_Briga(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Provocando"] = 3
    PokemonS.efeitosPosi["Preparado"] = 3

Chamar_para_Briga = {
    "nome": "Chamar para Briga",
    "tipo": ["lutador"],   
    "custo": ["normal","laranja"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe preparado e provocar por 3 turnos",
    "efeito": "Karate",
    "extra": None,
    "funçao": F_Chamar_para_Briga,
    "irregularidade": False
    }

Soco = {
    "nome": "Soco",
    "tipo": ["lutador"],   
    "custo": ["laranja"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Um soco firme",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def V_Punho_Missil(alcance,assertividade,PokemonS,AlvoS,Ataque):
     alcance += PokemonS.Atk_sp // 5
     return alcance,assertividade

Punho_Missil = {
    "nome": "Punho Missil",
    "tipo": ["lutador"],   
    "custo": ["normal","laranja"],
    "estilo": "E",
    "dano": 1.2,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Um construto de soco disparado no oponente, aumenta 1 de alcance a cada 5 de dano especial",
    "var": V_Punho_Missil,
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def FI_Combate_Proximo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta):
    aliados, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    if PokemonS in aliados:
        Dano = Dano * 1.7

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta

Combate_Proximo = {
    "nome": "Combate Proximo",
    "tipo": ["lutador"],   
    "custo": ["normal","laranja","laranja","laranja"],
    "estilo": "N",
    "dano": 1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque causa mais 70% de dano caso voce esteja grudado no alvo",
    "efeito": "Karate",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": FI_Combate_Proximo
    }

def FF_Submissão(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,Escolha):
        
        if Escolha == "Sim":
            PokemonS.efeitosNega["Incapacitado"] = 3
            AlvoS.efeitosNega["Incapacitado"] = 3
        elif Escolha == "Não":
            pass

        Dano, Defesa = VEstilo(PokemonS,AlvoS,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],AlvoS.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,AlvoS,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        AlvoS.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Submissão(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Submissão
    EstadoDaPergunta["info"] = PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Sim","Não"]
    EstadoDaPergunta["estado"] = True

Submissão = {
    "nome": "Submissão",
    "tipo": ["lutador"],   
    "custo": ["normal","laranja","laranja"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Você pode optar por Incapacitar a si mesmo e o pokemon oponente ou não",
    "efeito": "ChicoteMultiplo",
    "extra": "A",
    "funçao": F_Submissão,
    "irregularidade": False
    }

def F_Treinar(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.Ganhar_XP(3,player)
    vezes = PokemonS.vel // 12
    for i in range(vezes):
         Atributo = random.choice([PokemonS.Varvel_perm,PokemonS.VarDef_perm,PokemonS.VarDef_sp_perm,PokemonS.VarAtk_perm,PokemonS.VarAtk_sp_perm])
         Atributo += 1

Treinar = {
    "nome": "Treinar",
    "tipo": ["lutador"],   
    "custo": ["laranja"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 3 de XP e aumente 1 de seus atributos aleatoriamente para cada 12 de velocidade que esse pokemon tiver",
    "efeito": "Karate",
    "extra": None,
    "funçao": F_Treinar,
    "irregularidade": False
    }
