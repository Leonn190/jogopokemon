import importlib
import random
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade

def Regular(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def Irregular(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta = I(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta)

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

DicionarioAtaques = {

    "Jato de Água": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_de_Agua,
    "Jato Duplo": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_Duplo,
    "Bolhas": lambda: importlib.import_module("Dados.Ataques.Agua").Bolhas,
    "Controle do Oceano": lambda: importlib.import_module("Dados.Ataques.Agua").Controle_do_Oceano,
    "Splash": lambda: importlib.import_module("Dados.Ataques.Agua").Splash,
    "Vasculhar no Rio": lambda: importlib.import_module("Dados.Ataques.Agua").Vasculhar_no_Rio,
    "Golpe de Concha": lambda: importlib.import_module("Dados.Ataques.Agua").Golpe_de_Concha,
    "Gota Pesada": lambda: importlib.import_module("Dados.Ataques.Agua").Gota_Pesada,
    "Bola de Água": lambda: importlib.import_module("Dados.Ataques.Agua").Bola_de_Agua,

    "Tapa": lambda: importlib.import_module("Dados.Ataques.Normal").Tapa,
    "Cabeçada": lambda: importlib.import_module("Dados.Ataques.Normal").Cabeçada,
    "Investida": lambda: importlib.import_module("Dados.Ataques.Normal").Investida,
    "Vasculhar": lambda: importlib.import_module("Dados.Ataques.Normal").Vasculhar,
    "Ataque Rápido": lambda: importlib.import_module("Dados.Ataques.Normal").Ataque_Rapido,
    "Provocar": lambda: importlib.import_module("Dados.Ataques.Normal").Provocar,
    "Energia": lambda: importlib.import_module("Dados.Ataques.Normal").Energia,
    "Arranhar": lambda: importlib.import_module("Dados.Ataques.Normal").Arranhar,

    "Sopro do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Sopro_do_Dragao,
    "Garra do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Garra_do_Dragao,
    "Ultraje": lambda: importlib.import_module("Dados.Ataques.Dragao").Ultraje,

    "Faisca": lambda: importlib.import_module("Dados.Ataques.Eletrico").Faisca,
    "Energizar": lambda: importlib.import_module("Dados.Ataques.Eletrico").Energizar,
    "Eletrólise Hidrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Eletrolise_Hidrica,
    "Choque do Trovão": lambda: importlib.import_module("Dados.Ataques.Eletrico").Choque_do_Trovao,
    "Onda Elétrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Onda_Eletrica,
    "Bola Elétrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Bola_Eletrica,

    "Queimar": lambda: importlib.import_module("Dados.Ataques.Fogo").Queimar,
    "Bola de Fogo": lambda: importlib.import_module("Dados.Ataques.Fogo").Bola_de_Fogo,
    "Superaquecer": lambda: importlib.import_module("Dados.Ataques.Fogo").Superaquecer,

    "Cristalizar": lambda: importlib.import_module("Dados.Ataques.Gelo").Cristalizar,

    "Brilho": lambda: importlib.import_module("Dados.Ataques.Fada").Brilho,
    "Vento Fada": lambda: importlib.import_module("Dados.Ataques.Fada").Vento_Fada,
    "Benção": lambda: importlib.import_module("Dados.Ataques.Fada").Bençao,

    "Mordida": lambda: importlib.import_module("Dados.Ataques.Inseto").Mordida,
    "Seda": lambda: importlib.import_module("Dados.Ataques.Inseto").Seda,
    "Picada": lambda: importlib.import_module("Dados.Ataques.Inseto").Picada,
    "Minhocagem": lambda: importlib.import_module("Dados.Ataques.Inseto").Minhocagem,

    "Assombrar": lambda: importlib.import_module("Dados.Ataques.Fantasma").Assombrar,
    "Lambida": lambda: importlib.import_module("Dados.Ataques.Fantasma").Lambida,

    "Soco": lambda: importlib.import_module("Dados.Ataques.Lutador").Soco,
    "Chamar para Briga": lambda: importlib.import_module("Dados.Ataques.Lutador").Chamar_para_Briga,
    "Punho Míssil": lambda: importlib.import_module("Dados.Ataques.Lutador").Punho_Missil,
    "Combate Próximo": lambda: importlib.import_module("Dados.Ataques.Lutador").Combate_Proximo,
    "Submissão": lambda: importlib.import_module("Dados.Ataques.Lutador").Submissão,
    "Treinar": lambda: importlib.import_module("Dados.Ataques.Lutador").Treinar,

    "Reforçar": lambda: importlib.import_module("Dados.Ataques.Metal").Reforçar,
    "Cauda de Ferro": lambda: importlib.import_module("Dados.Ataques.Metal").Cauda_de_Ferro,
    
    "Pedregulho": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedregulho,

    "Arremesso de Terra": lambda: importlib.import_module("Dados.Ataques.Terrestre").Arremesso_de_Terra,

    "Confusão": lambda: importlib.import_module("Dados.Ataques.Psiquico").Confusão,
    "Bola Psíquica": lambda: importlib.import_module("Dados.Ataques.Psiquico").Bola_Psiquica,
    "Teleporte": lambda: importlib.import_module("Dados.Ataques.Psiquico").Teleporte,
    "Ampliação Mental": lambda: importlib.import_module("Dados.Ataques.Psiquico").Ampliação_Mental,
    "Psíquico Desgastante": lambda: importlib.import_module("Dados.Ataques.Psiquico").Psiquico_Desgastante,

    "Nas Sombras": lambda: importlib.import_module("Dados.Ataques.Sombrio").Nas_Sombras,
    "Bola Sombria": lambda: importlib.import_module("Dados.Ataques.Sombrio").Bola_Sombria,

    "Voar": lambda: importlib.import_module("Dados.Ataques.Voador").Voar,

    "Envenenar": lambda: importlib.import_module("Dados.Ataques.Veneno").Envenenar,
    "Ácido": lambda: importlib.import_module("Dados.Ataques.Veneno").Acido,

    "Dreno": lambda: importlib.import_module("Dados.Ataques.Planta").Dreno,
    "Disparo de Semente": lambda: importlib.import_module("Dados.Ataques.Planta").Disparo_de_Semente,
    "Chicote de Vinha": lambda: importlib.import_module("Dados.Ataques.Planta").Chicote_de_Vinha,
    "Cura Natural": lambda: importlib.import_module("Dados.Ataques.Planta").Cura_Natural,
    "Raio Solar": lambda: importlib.import_module("Dados.Ataques.Planta").Raio_Solar,

}

def SelecionaAtaques(Seleçao):
    Sorteado = random.choice(Seleçao)
    return DicionarioAtaques[Sorteado]()