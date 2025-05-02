from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Sopro_do_Dragao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):

    efeitos_ativos = [chave for chave, valor in Alvo.efeitosPosi.items() if valor > 0]

    if efeitos_ativos:
        efeito_removido = random.choice(efeitos_ativos)
        Alvo.efeitosPosi[efeito_removido] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Sopro_do_Dragao = {
    "nome": "Sopro do Dragão",
    "tipo": ["dragao"],   
    "custo": ["vermelha"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 28,
    "precisão": 90, 
    "descrição": "O sopro do dragão é capaz de remover um efeito positivo com o padrão draconico do pokemon atingido",
    "efeito": "Fumaça",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Sopro_do_Dragao
    }

