# === Início de Agua.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move, GuardarPosicionar
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

Jato_de_Agua = {
    "nome": "Jato De Agua",
    "tipo": ["agua"],   
    "custo": ["normal","azul"],
    "estilo": "E",
    "dano": 1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "EspiralAzul",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Jato_Duplo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Aumento = random.choice([True,False])

    if Aumento is True:
        Dano = Dano * 1.5
        Alvo.efeitosNega["Encharcado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Jato_Duplo = {
    "nome": "Jato Duplo",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 20,
    "precisão": 95, 
    "descrição": "Esse ataque tem 50% de chance de causar mais 50% de dano e deixar o oponente encharcado por 3 turnos",
    "efeito": "EspiralAzul",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Jato_Duplo
    }

def F_Bolhas(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    try:
        Dano = Dano * (1 + PokemonS.bolhas/5)
    except AttributeError:
        PokemonS.bolhas = 0
    
    PokemonS.bolhas += 1

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bolhas = {
    "nome": "Bolhas",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "N",
    "dano": 0.3,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Esse ataque causa mais 20% de dano por cada vez que o pokemon oponente foi atingido pelo ataque Bolhas",
    "efeito": "Agua",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bolhas
    }

def FF_Controle_do_Oceano(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
        
        linhaA, colunaA = Alvo.local["id"]

        if Escolha == "Norte":
            Move(Alvo,linhaA-2,colunaA,Mapa.Zona)
        elif Escolha == "Sul":
            Move(Alvo,linhaA+2,colunaA,Mapa.Zona)
        elif Escolha == "Leste":
            Move(Alvo,linhaA,colunaA+2,Mapa.Zona)
        elif Escolha == "Oeste":
            Move(Alvo,linhaA,colunaA-2,Mapa.Zona)

        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Controle_do_Oceano(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Controle_do_Oceano
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Norte","Sul","Leste","Oeste"]
    EstadoDaPergunta["estado"] = True

Controle_do_Oceano = {
    "nome": "Controle do Oceano",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 60,
    "precisão": 100, 
    "descrição": "Escolha para qual direçao irá mover o pokemon inimigo em 2 posições",
    "efeito": "TornadoAgua",
    "extra": "A",
    "funçao": F_Controle_do_Oceano,
    "irregularidade": False
    }

Splash = {
    "nome": "Splash",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "N",
    "dano": 0.5,
    "alcance": 15,
    "precisão": 50, 
    "descrição": "A precisão do ataque é 50% pois esse ataque tem 50% de chance de não fazer nada",
    "efeito": "Agua",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Vasculhar_no_Rio(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Vezes = random.choice([1,2])
    for i in range(Vezes):
        item = caixa()
        if item["classe"] in ["pokebola","Fruta"]:
            player.Captura.append(item)
        else:
            player.inventario.append(item)

Vasculhar_no_Rio = {
    "nome": "Vasculhar no Rio",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Vasculhe até 2 itens no rio",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Vasculhar_no_Rio,
    "irregularidade": False
    }

def F_Golpe_de_Concha(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano += PokemonS.Def * Ataque["dano"]
    Dano += PokemonS.Def_sp * Ataque["dano"]
    PokemonS.efeitosPosi["Reforçado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Golpe_de_Concha = {
    "nome": "Golpe de Concha",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul"],
    "estilo": "N",
    "dano": 0.5,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque causa dano baseado em defesa, defesa especial e em ataque, após esse ataque o pokemon perde o efeito reforçado caso tenha",
    "efeito": "HexagonoLaminas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Golpe_de_Concha
    }

def F_Gota_Pesada(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Encharcado"] = 4

Gota_Pesada = {
    "nome": "Gota Pesada",
    "tipo": ["agua"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 25,
    "precisão": 95, 
    "descrição": "Esse ataque deixa o oponente encharcado por 4 turnos mas sem dar dano nele",
    "efeito": "Agua",
    "extra": "A",
    "funçao": F_Gota_Pesada,
    "irregularidade": False
    }

def Alv_Bola_de_Agua(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bola_de_Agua(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_de_Agua = {
    "nome": "Bola de Água",
    "tipo": ["agua"],   
    "custo": ["azul","azul","azul"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "EspiralAzul",
    "alvos": Alv_Bola_de_Agua,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bola_de_Agua
    }

def F_Cachoeira(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 75:
        GuardarPosicionar(Alvo,player,3,Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Cachoeira = {
    "nome": "Cachoeira",
    "tipo": ["agua"],   
    "custo": ["normal","azul","azul","azul"],
    "estilo": "N",
    "dano": 1.55,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Uma manobra aquática poderosa que tem 25% de chance de fazer o pokemon alvo ser guardado por 3 turnos",
    "efeito": "TornadoAgua",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Cachoeira
    }

def F_Jato_Triplo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Aumento = random.randint(0,100)

    if Aumento > 70:
        Dano = Dano * 1.55
        Alvo.efeitosNega["Encharcado"] = 3
    elif Aumento > 20:
        Dano = Dano * 2.1
        Alvo.efeitosNega["Encharcado"] = 5

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Jato_Triplo = {
    "nome": "Jato Triplo",
    "tipo": ["agua"],   
    "custo": ["azul","azul","azul","azul"],
    "estilo": "E",
    "dano": 0.8,
    "alcance": 18,
    "precisão": 100, 
    "descrição": "Esse ataque tem 50% de chance de aumentar 55% de dano e deixar o alvo encharcado por 3 turnos e tem 30% de chance de aumentar 110% de dano e encharcar o alvo por 5 turnos, e 20% de chance de não fazer nada a mais",
    "efeito": "EspiralAzul",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Jato_Triplo
    }


# === Fim de Agua.py ===

# === Início de Dragao.py ===
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
    "alcance": 26,
    "precisão": 90, 
    "descrição": "O sopro do dragão é capaz de remover um efeito positivo com o padrão draconico do pokemon atingido",
    "efeito": "Fumaça",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Sopro_do_Dragao
    }

def FF_Garra_do_Dragao(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
        Alvo.efeitosNega[Escolha] = 3

        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Garra_do_Dragao(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Garra_do_Dragao
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Quebrado","Fragilizado"]
    EstadoDaPergunta["estado"] = True

Garra_do_Dragao = {
    "nome": "Garra do Dragão",
    "tipo": ["dragao"],   
    "custo": ["normal","vermelha","vermelha"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Escolha entre deixar o oponente fragilizado ou quebrado por 3 turnos",
    "efeito": "Garra",
    "extra": "A",
    "funçao": F_Garra_do_Dragao,
    "irregularidade": False
    }

def F_Ultraje(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.atacado(22,player,inimigo,tela,Mapa)
    
Ultraje = {
    "nome": "Ultraje",
    "tipo": ["dragao"],   
    "custo": ["normal","vermelha"],
    "estilo": "N",
    "dano": 1,
    "alcance": 25,
    "precisão": 95, 
    "descrição": "Esse ataque causa sempre 22 de dano independente de qualquer efeito ou atributo",
    "efeito": "Corte",
    "extra": "A",
    "funçao": F_Ultraje,
    "irregularidade": False
    }

Cauda_Violenta = {
    "nome": "Cauda Violenta",
    "tipo": ["dragao"],   
    "custo": ["normal","vermelha","vermelha"],
    "estilo": "N",
    "dano": 1.4,
    "alcance": 20,
    "precisão": 85, 
    "descrição": "Use sua cauda para atingir o oponente com força",
    "efeito": "CorteRosa",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Investida_do_Dragao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):

    PokemonS.atacado(40,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Investida_do_Dragao = {
    "nome": "Investida do Dragao",
    "tipo": ["dragao"],   
    "custo": ["vermelha","vermelha","vermelha","vermelha"],
    "estilo": "N",
    "dano": 2,
    "alcance": 16,
    "precisão": 100, 
    "descrição": "Esse ataque causa 36 de dano de perfuraçao em si mesmo",
    "efeito": "ExplosaoVermelha",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida_do_Dragao
    }


# === Fim de Dragao.py ===

# === Início de Eletrico.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular, Multi_Regular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Eletrolise_Hidrica(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Encharcado"] > 0:
        Dano = Dano * 2.25

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Eletrolise_Hidrica = {
    "nome": "Eletrólise Hidrica",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Se o alvo estiver encharcado esse ataque causará 125% a mais de dano",
    "efeito": "EnergiaAzul",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Eletrolise_Hidrica
    }

Faisca = {
    "nome": "Faisca",
    "tipo": ["eletrico"],   
    "custo": ["amarela"],
    "estilo": "N",
    "dano": 1,
    "alcance": 10,
    "precisão": 125, 
    "descrição": "Uma faisca certeira no oponente",
    "efeito": "RajadaAmarela",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Onda_Eletrica(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Paralisado"] = 3

Onda_Eletrica = {
    "nome": "Onda Elétrica",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 36,
    "precisão": 100, 
    "descrição": "Deixe o alvo paralisado por 3 turnos",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": F_Onda_Eletrica,
    "irregularidade": None
    }

def F_Choque_do_Trovao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 70:
        Alvo.efeitosNega["Paralisado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Choque_do_Trovao = {
    "nome": "Choque do Trovão",
    "tipo": ["eletrico"],   
    "custo": ["amarela","amarela","amarela","amarela"],
    "estilo": "E",
    "dano": 1.6,
    "alcance": 32,
    "precisão": 99, 
    "descrição": "Um grande raio que tem 30% de chance de paralisar o alvo por 3 turnos",
    "efeito": "SuperDescarga",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Choque_do_Trovao
    }

def F_Energizar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Energizado"] += 2
            return
 
    PokemonS.efeitosPosi["Energizado"] += 2

Energizar = {
    "nome": "Energizar",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 99, 
    "descrição": "Ganhe energizado por 2 turnos ou caso exista um pokemon aliado vizualisado, ele que ganhará o efeito",
    "efeito": "Estouro",
    "efeito2": "Estouro",
    "extra": "TV",
    "funçao": F_Energizar,
    "irregularidade": None
    }

def Alv_Bola_Eletrica(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bola_Eletrica(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Eletrica = {
    "nome": "Bola Elétrica",
    "tipo": ["eletrico"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "FacasBrancas",
    "alvos": Alv_Bola_Eletrica,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bola_Eletrica
    }

def Alv_Tempestade_de_Raios(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in inimigo.pokemons:
        if pokemon.efeitosNega["Encharcado"] > 0:
            alvos.append(pokemon)
    return alvos

Tempestade_de_Raios = {
    "nome": "Tempestade de Raios",
    "tipo": ["eletrico"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "E",
    "dano": 1.45,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Esse ataque atinge todos os pokemon encharcados inimigos",
    "efeito": "MarcaAmarela",
    "extra": "MA",
    "alvos": Alv_Tempestade_de_Raios,
    "funçao": Multi_Regular,
    "irregularidade": False
    }


# === Fim de Eletrico.py ===

# === Início de Fada.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa, coletor
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Brilho(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosPosi["Furtivo"] = 0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

def Alv_Brilho(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in inimigo.pokemons:
        if pokemon.efeitosPosi["Furtivo"] > 0:
            alvos.append(pokemon)
    return alvos

Brilho = {
    "nome": "Brilho",
    "tipo": ["fada"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ataca todos os pokemon com o efeito furtivo e remove esse efeito deles",
    "efeito": "MarcaBrilhosa",
    "extra": "MA",
    "alvos": Alv_Brilho,
    "funçao": Multi_Irregular,
    "irregularidade": F_Brilho
    }

Vento_Fada = {
    "nome": "Vento Fada",
    "tipo": ["fada"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Um vento fada ofensivo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Bençao(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonV.efeitosPosi["Abençoado"] = 3
    
Bençao = {
    "nome": "Benção",
    "tipo": ["fada"],   
    "custo": ["normal","roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Selecione um pokemon como vizualizado, ele será abençoado por 3 turnos",
    "efeito": "MarcaBrilhosa",
    "extra": "V",
    "funçao": F_Bençao,
    "irregularidade": False
    }

def FF_Busca_Alegre(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    num = int(Escolha)
    if PokemonV is not None:
        PokemonV.curar(4*num,player,tela)
    else:
        PokemonS.curar(4*num,player,tela)
    
    for i in range(5-num):
        player.energias[coletor()] += 1
    EstadoDaPergunta["estado"] = False

def F_Busca_Alegre(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Busca_Alegre
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["0","1","2","3"]
    EstadoDaPergunta["estado"] = True

Busca_Alegre = {
    "nome": "Busca Alegre",
    "tipo": ["fada"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 5 energias aleatorias, voce pode escolher descartar até 3 delas, para cada uma cure 4 de vida do pokemon visualizado ou de si mesmo",
    "efeito": "!None",
    "extra": "TV",
    "funçao": F_Busca_Alegre,
    "irregularidade": False
    }

def F_Tapa_das_Fadas(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    contador = 0
    for efeito in Alvo.efeitosPosi:
        if Alvo.efeitosPosi[efeito] > 1:
            contador += 1
    Dano = Dano * (1 + 0.3 * contador)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Tapa_das_Fadas = {
    "nome": "Tapa das Fadas",
    "tipo": ["agua"],   
    "custo": ["normal","roxa","roxa"],
    "estilo": "N",
    "dano": 0.95,
    "alcance": 9,
    "precisão": 100, 
    "descrição": "Esse ataque causa 30% de dano a mais para cada efeito positivo que o alvo tiver",
    "efeito": "FacasRosas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Tapa_das_Fadas
    }

def F_Constelaçao_Magica(PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for alvo in Alvo:
        alvo.efeitosPosi["Furtivo"] = 3

def Alv_Constelaçao_Magica(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in player.pokemons:
        if pokemon != PokemonS:
            alvos.append(pokemon)
    return alvos

Constelaçao_Magica = {
    "nome": "Constelação Mágica",
    "tipo": ["fada"],   
    "custo": ["roxa","roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Deixa todos os pokemon aliados menos a si mesmo em modo furtivo por 3 turnos",
    "efeito": "Fumaça",
    "extra": "MA",
    "alvos": Alv_Constelaçao_Magica,
    "funçao": F_Constelaçao_Magica,
    "irregularidade": False
    }

def Alv_Explosao_Lunar(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = [Alvo]
    for pokemon in inimigo.pokemons:
        if abs(pokemon.pos - Alvo.pos) == 1:
            alvos.append(pokemon)

    return alvos

def F_Explosao_Lunar(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.4

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Explosao_Lunar = {
    "nome": "Explosão Lunar",
    "tipo": ["agua"],   
    "custo": ["normal","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.4,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque causa 40% do dano original aos pokemons nas duas posiçoes adjacentes",
    "efeito": "CorteRosa",
    "alvos": Alv_Explosao_Lunar,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Explosao_Lunar
    }


# === Fim de Fada.py ===

# === Início de Fantasma.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Assombrar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    efeitos_disponiveis = list(Alvo.efeitosNega.keys())
    if efeitos_disponiveis:
        efeito_escolhido = random.choice(efeitos_disponiveis)
        Alvo.efeitosNega[efeito_escolhido] = 2

Assombrar = {
    "nome": "Assombrar",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 15,
    "precisão": 95, 
    "descrição": "Aplica um efeito negativo aleatorio por 2 turnos no alvo",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": F_Assombrar,
    "irregularidade": False
    }

def F_Lambida(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(Dano/15,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Lambida = {
    "nome": "Lambida",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Cure 15% do dano causado",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Lambida
    }

def F_Atravessar(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    for chave,valor in PokemonS.efeitosNega.items():
        PokemonS.efeitosNega[chave] = 0
        Alvo.efeitosNega[chave] = valor

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Atravessar = {
    "nome": "Atravessar",
    "tipo": ["fantasma"],   
    "custo": ["preta","preta"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 9,
    "precisão": 100, 
    "descrição": "Atravessa o alvo, removendo todos os efeitos negativos de si mesmo e passando para o alvo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Atravessar
    }

saldo = 1

def FF_Coleta_Gananciosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    global saldo
    if Escolha == "Mais":
        if random.randint(0,100) > saldo * 2:
            saldo += saldo
            EstadoDaPergunta["estado"] = False
            F_Coleta_Gananciosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta)
        else:   
            saldo = 0
            EstadoDaPergunta["estado"] = False
            return
    else:
        player.ouro += saldo
        saldo = 1
        EstadoDaPergunta["estado"] = False

def F_Coleta_Gananciosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I=None):
    
    EstadoDaPergunta["funçao"] = FF_Coleta_Gananciosa
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Mais","Parar"]
    EstadoDaPergunta["estado"] = True

Coleta_Gananciosa = {
    "nome": "Coleta Gananciosa",
    "tipo": ["fantasma"],   
    "custo": ["preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 1 de ouro, no entanto voce pode ganhar mais, porém toda vez que escolhe mais tem mais chance de perder tudo",
    "efeito": "!None",
    "extra": "TV",
    "funçao": F_Coleta_Gananciosa,
    "irregularidade": False
    }

def F_Mao_Espectral(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaS, colunaS = PokemonS.local["id"]
    linhaA, colunaA = Alvo.local["id"]

    if linhaS > linhaA:
        Move(Alvo,linhaS - 1, colunaS,Mapa.Zona)
    else:
        Move(Alvo,linhaS + 1, colunaS,Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Mao_Espectral = {
    "nome": "Mão Espectral",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta","preta"],
    "estilo": "E",
    "dano": 1,
    "alcance": 40,
    "precisão": 100, 
    "descrição": "Puxe o inimigo para perto de você",
    "efeito": "ExplosaoRoxa",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Mao_Espectral
    }

def FF_Maldade(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    Alvo.efeitosNega[Escolha] = 4
    EstadoDaPergunta["estado"] = False

def F_Maldade(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I=None):
    opçoes = []
    for chave in PokemonS.efeitosNega:
        opçoes.append(chave)

    EstadoDaPergunta["funçao"] = FF_Maldade
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = []
    EstadoDaPergunta["estado"] = True

    for i in range(4):
        EstadoDaPergunta["opçoes"].append(random.choice(opçoes))

Maldade = {
    "nome": "Maldade",
    "tipo": ["fantasma"],   
    "custo": ["normal","preta","preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 50,
    "precisão": 100, 
    "descrição": "Escolha entre 4 efeitos negativos aleatorios para colocar no alvo por 4 turnos",
    "efeito": "ChuvaVermelha",
    "extra": "A",
    "funçao": F_Maldade,
    "irregularidade": False
    }

def F_Massacre_Fantasmagorico(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    for chave in PokemonS.efeitosPosi:
        if Alvo.efeitosPosi[chave] > 1:
            return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

    Dano = Dano * 1.41
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Massacre_Fantasmagorico = {
    "nome": "Massacre Fantasmagórico",
    "tipo": ["fantasma"],   
    "custo": ["preta","preta","preta","preta"],
    "estilo": "E",
    "dano": 1.4,
    "alcance": 10,
    "precisão": 99, 
    "descrição": "Se o alvo não tiver nenhum efeito positivo, esse ataque irá causar mais 41% de dano",
    "efeito": "RasgosRosa",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Massacre_Fantasmagorico
    }



# === Fim de Fantasma.py ===

# === Início de Fogo.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores, distancia_entre_pokemons
import random

def F_Queimar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Queimado"] = 3

Queimar = {
    "nome": "Queimar",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 15,
    "precisão": 90, 
    "descrição": "Queime o pokemon inimigo por 3 turnos",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": F_Queimar,
    "irregularidade": False
    }

def Alv_Bola_de_Fogo(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bola_de_Fogo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_de_Fogo = {
    "nome": "Bola de Fogo",
    "tipo": ["fogo"],   
    "custo": ["vermelha","vermelha","vermelha"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "Fogo",
    "alvos": Alv_Bola_de_Fogo,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bola_de_Fogo
    }

def F_Superaquecer(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Queimado"] > 0:
        Alvo.efeitosNega["Queimado"] += 1
        Dano = Dano * 1.15
    if PokemonV in player.pokemons:
        PokemonV.efeitosNega["Congelado"] = 0
        PokemonV.efeitosNega["Encharcado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Superaquecer = {
    "nome": "Superaquecer",
    "tipo": ["fogo"],   
    "custo": ["vermelha","vermelha"],
    "estilo": "E",
    "dano": 0.5,
    "alcance": 20,
    "precisão": 99, 
    "descrição": "Caso o alvo ja esteja queimado, acrescente 1 contador no efeito e cause mais 15% de dano, selecione um pokemon aliado para remover o efeito congelado e encharcado",
    "efeito": "Fogo",
    "efeito2": "Fogo",
    "extra": "AV",
    "funçao": Irregular,
    "irregularidade": F_Superaquecer
    }

def F_Brasa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if random.randint(0,100) > 85:
        Alvo.efeitosNega["Queimado"] += 2

Brasa = {
    "nome": "Brasa",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "E",
    "dano": 1.05,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque tem 15% de chance de deixar o alvo queimado por 2 turnos",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Ondas_de_Calor(PokemonS,PokemonV,Alvo,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for alvo in Alvos:
        alvo.efeitosNega["Queimado"] = 4

def Alv_Ondas_de_Calor(PokemonS,Alvo,player,inimigo,Mapa):
    alvos = []
    for pokemon in inimigo.pokemons:
        dist = distancia_entre_pokemons(pokemon,PokemonS,Mapa.Metros)
        if random.randint(0,100) > dist + 5:
            alvos.append(pokemon)
    return alvos

Ondas_de_Calor = {
    "nome": "Ondas de Calor",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha","vermelha"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "qaunto mais perto os inimigos estiverem desse pokemon, mais chance eles tem de serem atingidos, todos os atingidos ficam queimados por 4 turnos",
    "efeito": "Fogo",
    "extra": "MA",
    "alvos": Alv_Ondas_de_Calor,
    "funçao": F_Ondas_de_Calor,
    "irregularidade": False
    }

def F_Raio_de_Fogo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Congelado"] = 0
    Alvo.efeitosNega["Encharcado"] = 0
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Raio_de_Fogo = {
    "nome": "Raio de Fogo",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha","vermelha","vermelha","vermelha"],
    "estilo": "E",
    "dano": 1.9,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Lança um raio de calor concentrado extremo que remove o efeito congelado e encharcado do oponente",
    "efeito": "LabaredaMultipla",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Raio_de_Fogo
    }

Ataque_de_Chamas = {
    "nome": "Ataque de Chamas",
    "tipo": ["fogo"],   
    "custo": ["normal","vermelha"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Uma manobra poderosa onde se utiliza fogo",
    "efeito": "Fogo",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Laser_Incandescente(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Congelado"] = 0
    Alvo.efeitosNega["Encharcado"] = 0
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Laser_Incandescente = {
    "nome": "Laser Incandescente",
    "tipo": ["fogo"],   
    "custo": ["vermelha","vermelha","vermelha","vermelha","vermelha"],
    "estilo": "E",
    "dano": 2,
    "alcance": 28,
    "precisão": 100, 
    "descrição": "Lança um laser de calor concentrado extremo que remove o efeito congelado e encharcado do oponente",
    "efeito": "LabaredaMultipla",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Laser_Incandescente
    }


# === Fim de Fogo.py ===

# === Início de Gelo.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Cristalizar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if Alvo.efeitosNega["Encharcado"] > 0:
        Alvo.efeitosNega["Congelado"] += Alvo.efeitosNega["Encharcado"] + 1
        Alvo.efeitosNega["Encharcado"] = 0

Cristalizar = {
    "nome": "Cristalizar",
    "tipo": ["gelo"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 30,
    "precisão": 100, 
    "descrição": "Se o pokemon inimigo estiver encharcado, ele perde esse efeito e ganha congelar por 1 turno a mais",
    "efeito": "FluxoAzul",
    "extra": "A",
    "funçao": F_Cristalizar,
    "irregularidade": False
    }

def F_Reinado_de_Gelo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    contador = 0
    for pokemon in player.pokemons + inimigo.pokemons:
        if pokemon.efeitosNega["Congelado"] > 0:
            contador += 1
    Dano = Dano * (1 + 0.5 * contador)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Reinado_de_Gelo = {
    "nome": "Reinado de Gelo",
    "tipo": ["gelo"],   
    "custo": ["normal","azul","azul"],
    "estilo": "E",
    "dano": 0.6,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% a mais de dano para cada pokemon congelado na partida",
    "efeito": "FacasAzuis",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Reinado_de_Gelo
    }

def FF_Magia_de_Gelo(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    Valor = int(Escolha)
    PokemonV.curar(20,player,tela)
    PokemonV.efeitosPosi["Regeneração"] = Valor
    PokemonV.efeitosPosi["Congelado"] = Valor
    EstadoDaPergunta["estado"] = False

def F_Magia_de_Gelo(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Magia_de_Gelo
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["2","3","4","5"]
    EstadoDaPergunta["estado"] = True

Magia_de_Gelo = {
    "nome": "Magia de Gelo",
    "tipo": ["gelo"],  
    "custo": ["normal","azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Cure 20 de vida do pokemon Visualizado e escolha quantos turnos ele vai ganhar o efeito cura e congelado",
    "efeito": "MagiaAzul",
    "efeito2": "MagiaAzul",
    "extra": "V",
    "funçao": F_Magia_de_Gelo,
    "irregularidade": False
    }

def F_Raio_de_Gelo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 80:
        Alvo.efeitosNega["Congelado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Raio_de_Gelo = {
    "nome": "Raio de Gelo",
    "tipo": ["gelo"],   
    "custo": ["normal","azul","azul","azul","azul"],
    "estilo": "E",
    "dano": 1.95,
    "alcance": 18,
    "precisão": 99, 
    "descrição": "Lança um raio de gelo extremamente potente que tem 20% de chance de congelar o alvo por 3 turnos",
    "efeito": "RaioAzul",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Raio_de_Gelo
    }

def F_Gelo_Verdadeiro(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Gelo_Verdadeiro = {
    "nome": "Gelo Verdadeiro",
    "tipo": ["gelo"],   
    "custo": ["azul","azul"],
    "estilo": "N",
    "dano": 1.15,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque ignora a defesa do pokemon inimigo",
    "efeito": "MarcaAzul",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Raio_de_Gelo
    }



# === Fim de Gelo.py ===

# === Início de Inseto.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move, GuardarPosicionar
from Geradores.GeradorOutros import caixa, coletor
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Mordida = {
    "nome": "Mordida",
    "tipo": ["inseto"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Morda seu oponente com força",
    "efeito": "Mordida",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Seda(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.Varvel_perm > -11:
        Alvo.Varvel_perm -= 12

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Seda = {
    "nome": "Seda",
    "tipo": ["inseto"],   
    "custo": ["verde"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 20,
    "precisão": 90, 
    "descrição": "Esse ataque diminue 12 de velocidade do oponente, caso ja tenha -12 de velocidade, não diminue mais",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Seda
    }

def F_Picada(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.choice([True,False]) == True:
        Alvo.efeitosNega["Envenenado"] += 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Picada = {
    "nome": "Picada",
    "tipo": ["inseto"],   
    "custo": ["verde"],
    "estilo": "N",
    "dano": 0.8,
    "alcance": 15,
    "precisão": 90, 
    "descrição": "Esse ataque tem 50% de chance de deixar o oponente envenenado por 3 turnos",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Picada
    }

def FF_Minhocagem(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
        if Escolha == "Roubar":
            if inimigo.energias["verde"] > 2:
                 inimigo.energias["verde"] -= 2
                 player.energias["verde"] += 2
            else:
                 player.energias["verde"] += inimigo.energias["verde"]
                 inimigo.energias["verde"] = 0
        else:
            GuardarPosicionar(PokemonS,player,3,Mapa.Zona)

        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Minhocagem(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Minhocagem
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["Guardar","Roubar"]
    EstadoDaPergunta["estado"] = True

Minhocagem = {
    "nome": "Minhocagem",
    "tipo": ["inseto"],   
    "custo": ["normal","normal","normal"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Com o movimento das minhocas voce pode escolher entre guardar esse pokemon ou roubar 2 energias verde do oponente",
    "efeito": "DomoVerde",
    "extra": "A",
    "funçao": F_Minhocagem,
    "irregularidade": False
    }

def F_Coleta(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for i in range(4):
        player.energias[coletor()] += 1

Coleta = {
    "nome": "Coleta",
    "tipo": ["inseto"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 4 energias aleatorias",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Coleta,
    "irregularidade": None
    }

Tesoura_X = {
    "nome": "Tesoura X",
    "tipo": ["inseto"],   
    "custo": ["verde","verde","verde"],
    "estilo": "N",
    "dano": 1.6,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Atinja com força o oponente",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Dor_Falsa(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosPosi["Regeneração"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Dor_Falsa = {
    "nome": "Dor Falsa",
    "tipo": ["inseto"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 1.7,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque aplica uma dor falsa no oponente pois deixa ele com regeneração por 3 turnos",
    "efeito": "ChicoteMultiplo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Dor_Falsa
    }


# === Fim de Inseto.py ===

# === Início de Lutador.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Chamar_para_Briga(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
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

Punho_Missil = {
    "nome": "Punho Missil",
    "tipo": ["lutador"],   
    "custo": ["normal","laranja"],
    "estilo": "E",
    "dano": 1.2,
    "alcance": 35,
    "precisão": 100, 
    "descrição": "Um construto de soco disparado no oponente",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Combate_Proximo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    aliados, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    if PokemonS in aliados:
        Dano = Dano * 1.7

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

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
    "funçao": Irregular,
    "irregularidade": F_Combate_Proximo
    }

def FF_Submissão(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
        
        if Escolha == "Sim":
            PokemonS.efeitosNega["Incapacitado"] = 3
            Alvo.efeitosNega["Incapacitado"] = 3
        elif Escolha == "Não":
            pass

        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        Mitigaçao = 100 / (100 + Defesa)
        DanoM = Dano * Mitigaçao
        DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)

        DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

        EstadoDaPergunta["estado"] = False
        Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Submissão(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Submissão
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
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

def F_Treinar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
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


# === Fim de Lutador.py ===

# === Início de Metal.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Reforçar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Reforçado"] = 3
            return
 
    PokemonS.efeitosPosi["Reforçado"] = 3

Reforçar = {
    "nome": "Reforçar",
    "tipo": ["metal"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 100,
    "precisão": 100, 
    "descrição": "Ganhe reforçado por 3 turnos, caso tenha um pokemon vizualisado aliado, ele que ganhará o efeito",
    "efeito": "Engrenagem",
    "efeito2": "Engrenagem",
    "extra": "TV",
    "funçao": F_Reforçar,
    "irregularidade": False
    }

def F_Cauda_de_Ferro(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.choice([True,False]) == True:
        Alvo.Def_spB -= 1

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Cauda_de_Ferro = {
    "nome": "Cauda de Ferro",
    "tipo": ["metal"],   
    "custo": ["azul","azul"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque tem 50% de chance de remover 1 de defesa normal permanente",
    "efeito": "Corte",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Cauda_de_Ferro
    }

Projetil_Metalico = {
    "nome": "Projétil Metálico",
    "tipo": ["metal"],   
    "custo": ["azul","azul"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 30,
    "precisão": 90, 
    "descrição": "Lança um projétil metalico intenso no oponente",
    "efeito": "Engrenagem",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Barragem(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    ganho = PokemonS.Atk_sp * 0.4
    if "metal" in PokemonS.tipo:
        ganho = ganho * 1.25
    PokemonS.barreira += ganho

Barragem = {
    "nome": "Barragem",
    "tipo": ["metal"],   
    "custo": ["azul"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe barreira equivalente a 40% do dano especial, caso esse pokemon seja do tipo Metal, ganhe mais 25%",
    "efeito": "Engrenagem",
    "efeito2": "Engrenagem",
    "extra": None,
    "funçao": F_Barragem,
    "irregularidade": False
    }

def F_Broca_Perfuradora(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.2

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Broca_Perfuradora = {
    "nome": "Broca Perfuradora",
    "tipo": ["metal"],   
    "custo": ["normal","azul","azul"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 9,
    "precisão": 100, 
    "descrição": "Esse ataque ignora 80% da armadura do Alvo",
    "efeito": "Corte",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Cauda_de_Ferro
    }


# === Fim de Metal.py ===

# === Início de Normal.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move, GuardarPosicionar
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Tapa = {
    "nome": "Tapa",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 0.8,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Um Tapa ofensivo no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Cabeçada = {
    "nome": "Cabeçada",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 1.0,
    "alcance": 9,
    "precisão": 90, 
    "descrição": "Uma cabeçada ofensiva no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Investida(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.Vida -= 10

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Investida = {
    "nome": "Investida",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 9,
    "precisão": 85, 
    "descrição": "Esse ataque causa 10 de dano a si mesmo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida
    }

def F_Vasculhar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    item = caixa()
    if item["classe"] in ["pokebola","Fruta"]:
        player.Captura.append(item)
    else:
        player.inventario.append(item)

Vasculhar = {
    "nome": "Vasculhar",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Vasculhe e ganhe 1 item aleatório",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Vasculhar,
    "irregularidade": False
    }

def F_Ataque_Rapido(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    
    if random.choice([True,False]) == True:
        PokemonS.atacou = False

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Ataque_Rapido = {
    "nome": "Ataque Rápido",
    "tipo": ["normal"],   
    "custo": ["normal","normal"],
    "estilo": "N",
    "dano": 1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Tem 50% de chance desse ataque não constar como um ataque e esse pokemon poder atacar novamente",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Ataque_Rapido
    }

def F_Provocar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Provocando"] = 3

Provocar = { 
    "nome": "Provocar",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Provoque os inimigos e ganhe Provocar por 3 turnos",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Provocar,
    "irregularidade": False
    }

Energia = {
    "nome": "Energia",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 20,
    "precisão": 95, 
    "descrição": "Libere energia contra o pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Arranhar = {
    "nome": "Arranhar",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Arranhe o alvo com vontade",
    "efeito": "Garra",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Crescer(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.Ganhar_XP(4,player)

Crescer = {
    "nome": "Crescer",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 4 de XP",
    "efeito": "BolhasVerdes",
    "extra": None,
    "funçao": F_Crescer,
    "irregularidade": False
    }

def F_Esbravejar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonS.Vida < PokemonS.VidaMax * 0.6:
        PokemonS.efeitosPosi["Ofensivo"] = 3

Esbravejar = {
    "nome": "Esbravejar",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Se esse pokemon estiver com menos de 60% da vida maxima, ele ganha Ofensivo por 3 turnos",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Esbravejar,
    "irregularidade": False
    }

Tapa_Especial = {
    "nome": "Tapa Especial",
    "tipo": ["normal"],   
    "custo": ["normal"],
    "estilo": "E",
    "dano": 0.8,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Um Tapa ofensivo no pokemon inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Esmagar(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    
    Dano = Dano + Dano * (1 + 0.1 * PokemonS.Peso // 100)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Esmagar = {
    "nome": "Esmagar",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal","normal","normal"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 9,
    "precisão": 99, 
    "descrição": "Esse ataque causa mais 10% de dano a cada 100kg que esse pokemon tiver",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Esmagar
    }

def F_Descansar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    GuardarPosicionar(PokemonS,player,4,Mapa.Zona)
    cura = (PokemonS.VidaMax - PokemonS.Vida) * 0.3
    PokemonS.curar(cura,player,tela)

Descansar = {
    "nome": "Descansar",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Esse pokemon é guardado por 4 turnos mas regenera 30% da vida perdida",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Descansar,
    "irregularidade": False
    }

def F_Canto_Alegre(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for efeito in PokemonV.efeitosNega:
        PokemonV.efeitosNega[efeito] = 0
 
Canto_Alegre = {
    "nome": "Canto Alegre",
    "tipo": ["normal"],   
    "custo": ["normal","normal","normal"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Remove todos os efeitos negativos do pokemon visualizado",
    "efeito": "FeixeMagenta",
    "extra": "V",
    "funçao": F_Canto_Alegre,
    "irregularidade": False
    }


# === Fim de Normal.py ===

# === Início de Pedra.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

Pedregulho = {
    "nome": "Pedregulho",
    "tipo": ["pedra"],   
    "custo": ["laranja"],
    "estilo": "N",
    "dano": 0.9,
    "alcance": 30,
    "precisão": 90, 
    "descrição": "Lança um pedregulho no inimigo",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

Pedra_Especial = {
    "nome": "Pedra Especial",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja"],
    "estilo": "E",
    "dano": 1.5,
    "alcance": 20,
    "precisão": 50, 
    "descrição": "Lança uma pedra especial no inimigo",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Barragem_Rochosa(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.barreira += (PokemonS.Def + PokemonS.Def_sp) * 0.2

Barragem_Rochosa = {
    "nome": "Barragem Rochosa",
    "tipo": ["pedra"],   
    "custo": ["cinza"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe 20% das somas das defesas como barreira",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Barragem_Rochosa,
    "irregularidade": False
    }

def F_Impacto_Rochoso(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano = PokemonS.Def * Ataque["dano"]
    PokemonS.efeitosNega["Quebrado"] = 2

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Impacto_Rochoso = {
    "nome": "Impacto Rochoso",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja","laranja"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 9,
    "precisão": 100, 
    "descrição": "Esse ataque causa dano baseado apenas na Defesa, após esse ataque, esse pokemon fica quebrado por 2 turnos",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Impacto_Rochoso
    }

def F_Pedra_Colossal(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if inimigo.inventario != []:  
        item = random.choice(inimigo.inventario)
        inimigo.inventario.remove(item)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Pedra_Colossal = {
    "nome": "Pedra Colossal",
    "tipo": ["pedra"],   
    "custo": ["normal","laranja","laranja","laranja"],
    "estilo": "N",
    "dano": 1.55,
    "alcance": 15,
    "precisão": 95, 
    "descrição": "Esse ataque remove um item do inventário do oponente",
    "efeito": "ImpactoRochoso",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Pedra_Colossal
    }

def FF_Furia_Petrea(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,Escolha):
    Valor = int(Escolha)
    
    PokemonS.efeitosPosi["Imortal"] = 2
    PokemonS.atacado(Valor * 35,player,inimigo,tela,Mapa)

    Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
    Dano = Vsteb(PokemonS,Dano,Ataque)

    Dano = Dano * (1 + 0.35 * Valor)

    Mitigaçao = 100 / (100 + Defesa)
    DanoM = Dano * Mitigaçao
    DanoF = DanoM * efetividade(Ataque["tipo"],Alvo.tipo,tela,AlvoLoc)
    
    DanoF = VEfeitos(PokemonS,Alvo,player,inimigo,DanoF,Ataque["estilo"],tela)

    EstadoDaPergunta["estado"] = False
    Alvo.atacado(DanoF,player,inimigo,tela,Mapa)

def F_Furia_Petrea(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    
    EstadoDaPergunta["funçao"] = FF_Furia_Petrea
    EstadoDaPergunta["info"] = PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc
    EstadoDaPergunta["opçoes"] = ["1","2","3","4"]
    EstadoDaPergunta["estado"] = True

Furia_Petrea = {
    "nome": "Fúria Pétrea",
    "tipo": ["pedra"],  
    "custo": ["normal","laranja","laranja","laranja","laranja"],
    "estilo": "N",
    "dano": 1,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Ganhe importal por 2 turnos, Escolha um nivel de fúria, esse ataque causa 35% de dano a mais e 35 de dano a si mesmo como perfuraçao a cada nivel de fúria",
    "efeito": "ImpactoRochoso",
    "efeito2": "ImpactoRochoso",
    "extra": "A",
    "funçao": F_Furia_Petrea,
    "irregularidade": False
    }


# === Fim de Pedra.py ===

# === Início de Planta.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Dreno(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(15,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Dreno = {
    "nome": "Dreno",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "estilo": "E",
    "dano": 0.8,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque cura 15 de vida de si mesmo",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Dreno
    }

def F_Chicote_de_Vinha(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.randint(0,100) > 40:
        Dano = Dano * 1.2

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Chicote_de_Vinha = {
    "nome": "Chicote de Vinha",
    "tipo": ["planta"],   
    "custo": ["verde","verde"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 25,
    "precisão": 75, 
    "descrição": "Esse ataque tem 60% de chance de causar mais 20% de dano",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Chicote_de_Vinha
    }

Disparo_de_Semente = {
    "nome": "Disparo de Semente",
    "tipo": ["planta"],   
    "custo": ["normal","verde"],
    "estilo": "N",
    "dano": 0.9,
    "alcance": 38,
    "precisão": 100, 
    "descrição": "Lança um jato de agua intenso no oponente",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Cura_Natural(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    if PokemonV is not None:
        if PokemonV in player.pokemons:
            PokemonV.efeitosPosi["Regeneração"] += 3
            return
 
    PokemonS.efeitosPosi["Regeneração"] += 3

Cura_Natural = {
    "nome": "Cura Natural",
    "tipo": ["planta"],   
    "custo": ["verde"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe regeneração por 3 turnos, caso tenha um pokemon visualizado aliado, ele que ganhará o efeito",
    "efeito": "DomoVerde",
    "efeito2": "DomoVerde",
    "extra": "TV",
    "funçao": F_Cura_Natural,
    "irregularidade": False
    }

Raio_Solar = {
    "nome": "Raio Solar",
    "tipo": ["planta"],   
    "custo": ["normal","verde","verde","verde","verde"],
    "estilo": "E",
    "dano": 1.8,
    "alcance": 32,
    "precisão": 100, 
    "descrição": "Lança um raio canalisado pelo sol",
    "efeito": "BarreiraCelular",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def Alv_Dança_das_Petalas(PokemonS,Alvo,player,inimigo,Mapa):
    aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
    return aliados + [PokemonS]

def F_Dança_das_Petalas(PokemonS,PokemonV,Alvo,Alvos,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    for alvo in Alvos:
        cura = (alvo.VidaMax - alvo.Vida) * 0.15
        alvo.curar(cura,player,tela)
        alvo.efeitosPosi["Velocista"] = 3

Dança_das_Petalas = {
    "nome": "Dança das Pétalas",
    "tipo": ["planta"],   
    "custo": ["normal","verde","verde"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Num raio de 2 casas adjacentes, cure 15% da vida perdida dos aliados e deixe eles com o efeito velocista",
    "efeito": "DomoVerde",
    "extra": "MA",
    "alvos": Alv_Dança_das_Petalas,
    "funçao": F_Dança_das_Petalas,
    "irregularidade": None
    }

def F_Mega_Dreno(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.curar(PokemonS.Atk_sp * 0.45,player,tela)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Mega_Dreno = {
    "nome": "Mega Dreno",
    "tipo": ["planta"],   
    "custo": ["verde","verde","verde"],
    "estilo": "N",
    "dano": 1.15,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque cura 45% do seu dano especial",
    "efeito": "ExplosaoVerde",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Dreno
    }

Folha_Navalha = {
    "nome": "Folha Navalha",
    "tipo": ["planta"],   
    "custo": ["normal","verde","verde"],
    "estilo": "N",
    "dano": 1.5,
    "alcance": 25,
    "precisão": 90, 
    "descrição": "Uma folha capaz de cortar como uma navalha, atirada no alvo",
    "efeito": "DomoVerde",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def Alv_Morteiro_de_Polem(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Morteiro_de_Polem(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Morteiro_de_Polem = {
    "nome": "Morteiro de Pólem",
    "tipo": ["planta"],   
    "custo": ["verde","verde","verde","verde","verde"],
    "estilo": "E",
    "dano": 1.45,
    "alcance": 70,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "Explosao",
    "alvos": Alv_Morteiro_de_Polem,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Morteiro_de_Polem
    }


# === Fim de Planta.py ===

# === Início de Psiquico.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move, GuardarPosicionar
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Confusão(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Confuso"] = 3

Confusão = {
    "nome": "Confusão",
    "tipo": ["psiquico"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 35,
    "precisão": 90, 
    "descrição": "Deixe o inimigo confuso por 3 turnos",
    "efeito": "FeixeRoxo",
    "extra": "A",
    "funçao": F_Confusão,
    "irregularidade": False
    }

def Alv_Bola_Psíquica(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bola_Psiquica(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Psiquica = {
    "nome": "Bola Psíquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "ExplosaoRoxa",
    "alvos": Alv_Bola_Psíquica,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bola_Psiquica
    }

def F_Teleporte(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaA, colunaA = Alvo.local["id"]
    linhaS, colunaS = PokemonS.local["id"]
    
    GuardarPosicionar(Alvo,player,1,Mapa.Zona)
    GuardarPosicionar(Alvo,player,1,Mapa.Zona)
    Move(PokemonS,linhaA,colunaA,Mapa.Zona)
    Move(Alvo,linhaS,colunaS,Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Teleporte = {
    "nome": "Teleporte",
    "tipo": ["psiquico"],   
    "custo": ["roxa"],
    "estilo": "N",
    "dano": 0.4,
    "alcance": 45,
    "precisão": 100, 
    "descrição": "Troque de lugar com o alvo",
    "efeito": "FeixeMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Teleporte
    }

def F_Ampliação_Mental(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    for efeito in PokemonS.efeitosNega:
        if Alvo.efeitosNega[efeito] > 0:
            Alvo.efeitosNega[efeito] += 1

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Ampliação_Mental = {
    "nome": "Ampliação Mental",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 0.85,
    "alcance": 15,
    "precisão": 80, 
    "descrição": "Aumente 1 de todos os contadores de efeitos negativos do pokemon atingido",
    "efeito": "FeixeRoxo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Ampliação_Mental
    }

def F_Psiquico_Desgastante(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.efeitosNega["Incapacitado"] += 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Psiquico_Desgastante = {
    "nome": "Psiquico Desgastante",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 1.45,
    "alcance": 20,
    "precisão": 85, 
    "descrição": "Esse pokemon agora está incapacitado por 3 turnos",
    "efeito": "CorteRicocheteadoRoxo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Psiquico_Desgastante
    }

def F_Mente_Forte(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if random.choice([True,False]) ==  True:
        PokemonS.efeitosPosi["Focado"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Mente_Forte = {
    "nome": "Mente Forte",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa"],
    "estilo": "N",
    "dano": 1.15,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque tem 50% de chance de te deixar focado",
    "efeito": "CorteRicocheteadoRoxo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Mente_Forte
    }

def F_Corrosao_Psiquica(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano = Dano * Alvo.Vida // 100

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Corrosao_Psiquica = {
    "nome": "Corrosão Psíquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "O dano desse ataque é a % da vida do inimigo",
    "efeito": "OrbesRoxos",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Corrosao_Psiquica
    }

def F_Psicorte_Duplo(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.7
    aliados, inimigos = pokemons_nos_arredores(Alvo,player,inimigo,2,Mapa.Zona)
    if PokemonV in inimigos:
        mitigação = 100 / (100 + PokemonV.Def)
        DanoV = Dano * mitigação
        PokemonV.atacado(DanoV,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Psicorte_Duplo = {
    "nome": "Psicorte Duplo",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa","roxa","roxa","roxa"],
    "estilo": "N",
    "dano": 1.5,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Esse ataque causa dano a um oponente selecionado caso esteja ate 2 casas adjacentes do alvo principal, esse ataque ignora 40% das defesas inimigas",
    "efeito": "CorteDuploRoxo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Psicorte_Duplo
    }

def F_Transferencia_Psiquica(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    for efeito in PokemonV.efeitosNega:
        if PokemonV.efeitosNega[efeito] >= 1:
            Alvo.efeitosNega[efeito] += PokemonV.efeitosNega[efeito]
            PokemonV.efeitosNega[efeito] = 0
            break

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Transferencia_Psiquica = {
    "nome": "Tranferência Psíquica",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 0.7,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Transfere um efeito negativo aleatorio do pokemon visualizado para o alvo",
    "efeito": "FeixeMagenta",
    "efeito2": "FluxoAzul",
    "extra": "AV",
    "funçao": Irregular,
    "irregularidade": F_Transferencia_Psiquica
    }

def F_Teletransporte(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaA, colunaA = Alvo.local["id"]
    linhaS, colunaS = PokemonV.local["id"]
    
    GuardarPosicionar(Alvo,player,1,Mapa.Zona)
    GuardarPosicionar(Alvo,player,1,Mapa.Zona)
    Move(PokemonV,linhaA,colunaA,Mapa.Zona)
    Move(Alvo,linhaS,colunaS,Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Teletransporte = {
    "nome": "Teletransporte",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa"],
    "estilo": "E",
    "dano": 0.6,
    "alcance": 50,
    "precisão": 100, 
    "descrição": "O pokemon visualizado troca de lugar com o alvo",
    "efeito": "FeixeMagenta",
    "efeito2": "FeixeMagenta",
    "extra": "AV",
    "funçao": Irregular,
    "irregularidade": F_Teletransporte
    }

def F_Raio_Psiquico(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    contador = 0
    for efeito in Alvo.efeitosNega:
        if Alvo.efeitosNega[efeito] > 0:
            contador += 1
    for efeito in Alvo.efeitosPosi:
        if Alvo.efeitosPosi[efeito] > 0:
            contador += 1
    Dano = Dano * (1 - 0.1 * contador)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Raio_Psiquico = {
    "nome": "Raio Psíquico",
    "tipo": ["psiquico"],   
    "custo": ["normal","roxa","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 2.1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Esse ataque causa menos 10% de dano a cada efeito que o pokemon inimigo tiver",
    "efeito": "RasgoMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Raio_Psiquico
    }

def F_Agonia_Mental(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Incapacitado"] = 5

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Agonia_Mental = {
    "nome": "Agonia Mental",
    "tipo": ["psiquico"],   
    "custo": ["roxa","roxa","roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1.35,
    "alcance": 40,
    "precisão": 100, 
    "descrição": "Esse ataque deixa o alvo incapacitado por 5 turnos",
    "efeito": "OrbesRoxos",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Agonia_Mental
    }


# === Fim de Psiquico.py ===

# === Início de Sombrio.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Nas_Sombras(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Furtivo"] = 5

Nas_Sombras = {
    "nome": "Nas Sombras",
    "tipo": ["sombrio"],   
    "custo": ["preta","preta"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "entre nas sombras e ganhe o efeito furtivo por 5 turnos",
    "efeito": "ChuvaBrilhante",
    "extra": None,
    "funçao": F_Nas_Sombras,
    "irregularidade": False
    }

def Alv_Bola_Sombria(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 1, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bola_Sombria(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo != AlvoS:
        Dano = Dano * 0.5

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bola_Sombria = {
    "nome": "Bola Sombria",
    "tipo": ["sombrio"],   
    "custo": ["preta","preta","preta"],
    "estilo": "E",
    "dano": 1.3,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa 50% do dano original aos pokemons inimigos adjacentes",
    "efeito": "ChuvaBrilhante",
    "alvos": Alv_Bola_Sombria,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bola_Sombria
    }

def F_Corte_Noturno(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaS, colunaS = PokemonS.local["id"]
    linhaA, colunaA = Alvo.local["id"]

    if linhaS == linhaA - 1:
        Dano = Dano * 1.7

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Corte_Noturno = {
    "nome": "Corte Noturno",
    "tipo": ["sombrio"],   
    "custo": ["normal","preta","preta"],
    "estilo": "N",
    "dano": 0.95,
    "alcance": 5,
    "precisão": 100, 
    "descrição": "Esse ataque causa 70% a mais de dano caso voce esteja atras do pokemon",
    "efeito": "CorteDourado",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Corte_Noturno
    }

def F_Confronto_Trevoso(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    PokemonS.efeitosPosi["Provocando"] = 3
    Alvo.efeitosPosi["Provocando"] = 3

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Confronto_Trevoso = {
    "nome": "Confronto Trevoso",
    "tipo": ["sombrio"],   
    "custo": ["normal","preta","preta"],
    "estilo": "N",
    "dano": 1.05,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Deixe a si mesmo e o alvo provocando por 3 turnos",
    "efeito": "RedemoinhoCosmico",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Confronto_Trevoso
    }


# === Fim de Sombrio.py ===

# === Início de Terrestre.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Regular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

Arremesso_de_Terra = {
    "nome": "Arremesso de Terra",
    "tipo": ["terrestre"],   
    "custo": ["amarela"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 30,
    "precisão": 65, 
    "descrição": "Lança terra ofensiva com força no oponente",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def Alv_Tremor(PokemonS,Alvo,player,inimigo,Mapa):

    aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
    return inimigos  

Tremor = {
    "nome": "Tremor",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela"],
    "estilo": "E",
    "dano": 0.9,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Atinge todos os inimigos que estiverem até 2 casas adjacentes, não precisa de alvo",
    "efeito": "ExplosaoPedra",
    "extra": "MA",
    "alvos": Alv_Tremor,
    "funçao": Multi_Regular,
    "irregularidade": False
    }

def Alv_Quebra_Chao(PokemonS,Alvo,player,inimigo,Mapa):
    if PokemonS.vel >= 30:
        aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,3,Mapa.Zona)
        return inimigos
    else:
        aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
        return inimigos

def F_Quebra_Chao(Dano,Defesa,PokemonS,PokemonV,AlvoS,alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Dano = Dano * PokemonS.Vida / 100
    PokemonS.atacado(Dano*0.15,player,inimigo,tela,Mapa)

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Quebra_Chao = {
    "nome": "Quebra Chão",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "N",
    "dano": 0.7,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "A cada 1 de vida esse ataque causa mais 1% de dano, esse ataque atinge todos os inimigos ate 2 casas nos arredores e caso esse pokemon tenha mais de 30 de velocidade, atinge até 3 casas nos arredores. Esse ataque causa 15% do dano a si mesmo como perfuração",
    "efeito": "ImpactoRochoso",
    "extra": "MA",
    "alvos": Alv_Quebra_Chao,
    "funçao": Multi_Irregular,
    "irregularidade": F_Quebra_Chao
    }

def F_Afinidade_Territorial(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Velocista"] = 3
    aliados, inimigos = pokemons_nos_arredores(PokemonS,player,inimigo,2,Mapa.Zona)
    if inimigos == []:
        PokemonS.atacou = False

Afinidade_Territorial = {
    "nome": "Afinidade Territorial",
    "tipo": ["terrestre"],   
    "custo": ["amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Ganhe o efeito velocista por 3 turnos, se não tiver nenhum inimigo até 2 casas adjacentes esse pokemon poderá atacar novamente",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Afinidade_Territorial,
    "irregularidade": False
    }

Osso_Veloz = {
    "nome": "Osso Veloz",
    "tipo": ["terrestre"],   
    "custo": ["amarela","amarela","amarela"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 55,
    "precisão": 75, 
    "descrição": "Lança um osso ofensivo com força no oponente, podendo viajar por muitos metros",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Regular,
    "irregularidade": False
    }

def F_Golpe_Territorial(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Provocando"] > 0:
        Dano = Dano * 1.2
        if Alvo.efeitosPosi["Provocando"] > 0:
            Dano = Dano * 1.1
            Alvo.efeitosPosi["Provocando"] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Golpe_Territorial = {
    "nome": "Golpe Territorial",
    "tipo": ["terrestre"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "N",
    "dano": 1.1,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Se esse pokemon estiver com o efeito provocando, esse ataque causará mais 20% de dano e caso o alvo também esteja provocando, esse golpe causa ainda mais 10% e remove o efeito de provocando do alvo",
    "efeito": "ExplosaoPedra",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Golpe_Territorial
    }

def Alv_Tremorr(PokemonS,Alvo,player,inimigo,Mapa):
    return inimigo.pokemons

Terremoto = {
    "nome": "Terremoto",
    "tipo": ["terrestre"],   
    "custo": ["normal","amarela","amarela","amarela","amarela"],
    "estilo": "N",
    "dano": 1.2,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Esse ataque atinge todos os pokemon inimigos",
    "efeito": "ExplosaoPedra",
    "extra": "MA",
    "alvos": Alv_Tremorr,
    "funçao": Multi_Regular,
    "irregularidade": False
    }


# === Fim de Terrestre.py ===

# === Início de Veneno.py ===
from Geradores.GeradorAtaques import Regular, Irregular, Multi_Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade, pokemons_nos_arredores
import random

def F_Envenenar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    Alvo.efeitosNega["Envenenado"] = 3

Envenenar = {
    "nome": "Envenenar",
    "tipo": ["venenoso"],   
    "custo": ["roxa"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 25,
    "precisão": 80, 
    "descrição": "deixe o pokemon inimigo envenenado por 3 turnos",
    "efeito": "GasRoxo",
    "extra": "A",
    "funçao": F_Envenenar,
    "irregularidade": False
    }

def F_Acido(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.8
    if random.choice([True,False]) == True:
        Alvo.Def_spB -= 1

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Acido = {
    "nome": "Acido",
    "tipo": ["venenoso"],   
    "custo": ["roxa","roxa"],
    "estilo": "E",
    "dano": 1,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque ignora 20% da defesa especial e tem 50% de chance de remover 1 de defesa especial permanente",
    "efeito": "MagiaMagenta",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Acido
    }

def Alv_Bomba_de_Lodo(PokemonS,Alvo,player,inimigo,Mapa):
    _, inimigos = pokemons_nos_arredores(Alvo, player, inimigo, 2, Mapa.Zona)
    inimigos.append(Alvo)
    return inimigos

def F_Bomba_de_Lodo(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Alvo.efeitosNega["Envenenado"] = 3
    if Alvo != AlvoS:
        Dano = Dano * 0.0

    return Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bomba_de_Lodo = {
    "nome": "Bomba de Lodo",
    "tipo": ["venenoso"],   
    "custo": ["roxa","roxa","roxa"],
    "estilo": "E",
    "dano": 1,
    "alcance": 20,
    "precisão": 100, 
    "descrição": "Esse ataque causa envenenamento por 3 turnos aos pokemons inimigos adjacentes até 2 casas",
    "efeito": "Fogo",
    "alvos": Alv_Bomba_de_Lodo,
    "extra": "MAA",
    "funçao": Multi_Irregular,
    "irregularidade": F_Bomba_de_Lodo
    }

def F_Extraçao(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if Alvo.efeitosNega["Envenenado"] > 0:
        PokemonS.curar(14 * Alvo.efeitosNega["Envenenado"],player,tela)
        Alvo.efeitosNega["Envenenado"] = 0

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Extraçao = {
    "nome": "Extração",
    "tipo": ["venenoso"],   
    "custo": ["normal","roxa"],
    "estilo": "N",
    "dano": 1.05,
    "alcance": 10,
    "precisão": 100, 
    "descrição": "Esse ataque remove o efeito envenenar do oponente, para cada turno restante no efeito, cure 14 de vida",
    "efeito": "Mordida",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Extraçao
    }


# === Fim de Veneno.py ===

# === Início de Voador.py ===
from Geradores.GeradorAtaques import Regular, Irregular
from Jogo.Tabuleiro import Move
from Geradores.GeradorOutros import caixa
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade
import random

def F_Voar(PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta,I):
    PokemonS.efeitosPosi["Voando"] = 3

Voar = {
    "nome": "Voar",
    "tipo": ["voador"],   
    "custo": ["amarela"],
    "estilo": "S",
    "dano": 0.0,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "voe e ganhe o efeito voando por 3 turnos",
    "efeito": "!None",
    "extra": None,
    "funçao": F_Voar,
    "irregularidade": False
    }

def F_Ataque_de_Asa(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Voando"] > 0:
        Dano = Dano * 0.8
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Ataque_de_Asa = {
    "nome": "Ataque de Asa",
    "tipo": ["voador"],   
    "custo": ["normal","amarela","amarela"],
    "estilo": "N",
    "dano": 1.45,
    "alcance": 15,
    "precisão": 100, 
    "descrição": "Esse ataque causa -25% de dano caso esse pokemon esteja voando",
    "efeito": "ChicoteMultiplo",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Ataque_de_Asa
    }

def F_Investida_Aerea(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    if PokemonS.efeitosPosi["Voando"] > 0:
        Dano = Dano * 1.25
    PokemonS.atacado(15,player,inimigo,tela,Mapa)
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Investida_Aerea = {
    "nome": "Investida Aérea",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "N",
    "dano": 1.25,
    "alcance": 10,
    "precisão": 95, 
    "descrição": "Esse ataque causa 15 de dano a si mesmo, caso esse pokemon esteja voando esse ataque causará mais 25% de dano",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida_Aerea
    }

def F_Rasante(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    DanoV = PokemonS.vel * 1.35 * 0.9
    DanoN = PokemonS.Atk * 1.35 * 0.1
    Dano = DanoV + DanoN
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Rasante = {
    "nome": "Rasante",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "N",
    "dano": 1.35,
    "alcance": 15,
    "precisão": 110, 
    "descrição": "Esse ataque escala apenas 10% com o dano o resto é com velocidade (90%)",
    "efeito": "FacasBrancas",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Investida_Aerea
    }

def F_Bico_Broca(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    Defesa = Defesa * 0.49
    
    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Bico_Broca = {
    "nome": "Bico Broca",
    "tipo": ["voador"],   
    "custo": ["normal","amarela"],
    "estilo": "N",
    "dano": 1.05,
    "alcance": 0,
    "precisão": 100, 
    "descrição": "Bique seu oponente como uma verdadeira broca, ignorando 51% da defesa dele",
    "efeito": "Corte",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Bico_Broca
    }

def F_Vento_Forte(Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta):
    linhaS, colunaS = PokemonS.local["id"]
    linhaA, colunaA = Alvo.local["id"]

    intensidade = 2 if Alvo.Peso < 200 else 1

    deslocamento_linha = 0
    deslocamento_coluna = 0

    if colunaS == colunaA:

        if linhaA > linhaS:
            deslocamento_linha = intensidade  
        else:
            deslocamento_linha = -intensidade  

    elif linhaS == linhaA:
        if colunaA > colunaS:
            deslocamento_coluna = intensidade  
        else:
            deslocamento_coluna = -intensidade  

    else:

        if linhaA > linhaS:
            deslocamento_linha = intensidade  
        else:
            deslocamento_linha = -intensidade 

        if colunaA > colunaS:
            deslocamento_coluna = intensidade  
        else:
            deslocamento_coluna = -intensidade  

    nova_linha = linhaA + deslocamento_linha
    nova_coluna = colunaA + deslocamento_coluna

    Move(Alvo, nova_linha, nova_coluna, Mapa.Zona)

    return Dano,Defesa,PokemonS,PokemonV,Alvo,player,inimigo,Ataque,Mapa,tela,AlvoLoc,EstadoDaPergunta

Vento_Forte = {
    "nome": "Vento Forte",
    "tipo": ["voador"],   
    "custo": ["amarela","amarela"],
    "estilo": "E",
    "dano": 1.1,
    "alcance": 25,
    "precisão": 100, 
    "descrição": "Mova o alvo 2 casas para longe, caso ele tenha mais de 200kg mova apenas 1 casa",
    "efeito": "Estouro",
    "extra": "A",
    "funçao": Irregular,
    "irregularidade": F_Vento_Forte
    }


# === Fim de Voador.py ===

