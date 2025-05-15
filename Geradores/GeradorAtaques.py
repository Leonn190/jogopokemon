import importlib
import random
from Jogo.Funções2 import VEstilo, VEfeitos, Vsteb, efetividade

def Regular(PokemonS,PokemonV,AlvoS,Alvos,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta,I):
    if Alvos is None:
        Alvos = [AlvoS]
    for Alvo in Alvos:
        Dano, Defesa = VEstilo(PokemonS,Alvo,Ataque)
        Dano = Vsteb(PokemonS,Dano,Ataque)

        if I is not None and I != False:
            Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta = I(Dano,Defesa,PokemonS,PokemonV,AlvoS,Alvo,player,inimigo,Ataque,Mapa,tela,Baralho,AlvoLoc,EstadoDaPergunta)

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
    "Cachoeira": lambda: importlib.import_module("Dados.Ataques.Agua").Cachoeira,
    "Jato Triplo": lambda: importlib.import_module("Dados.Ataques.Agua").Jato_Triplo,

    "Tapa": lambda: importlib.import_module("Dados.Ataques.Normal").Tapa,
    "Tapa Especial": lambda: importlib.import_module("Dados.Ataques.Normal").Tapa_Especial,
    "Cabeçada": lambda: importlib.import_module("Dados.Ataques.Normal").Cabeçada,
    "Investida": lambda: importlib.import_module("Dados.Ataques.Normal").Investida,
    "Vasculhar": lambda: importlib.import_module("Dados.Ataques.Normal").Vasculhar,
    "Ataque Rápido": lambda: importlib.import_module("Dados.Ataques.Normal").Ataque_Rapido,
    "Provocar": lambda: importlib.import_module("Dados.Ataques.Normal").Provocar,
    "Energia": lambda: importlib.import_module("Dados.Ataques.Normal").Energia,
    "Arranhar": lambda: importlib.import_module("Dados.Ataques.Normal").Arranhar,
    "Crescer": lambda: importlib.import_module("Dados.Ataques.Normal").Crescer,
    "Esbravejar": lambda: importlib.import_module("Dados.Ataques.Normal").Esbravejar,
    "Esmagar": lambda: importlib.import_module("Dados.Ataques.Normal").Esmagar,
    "Descansar": lambda: importlib.import_module("Dados.Ataques.Normal").Descansar,
    "Canto Alegre": lambda: importlib.import_module("Dados.Ataques.Normal").Canto_Alegre,

    "Sopro do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Sopro_do_Dragao,
    "Garra do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Garra_do_Dragao,
    "Ultraje": lambda: importlib.import_module("Dados.Ataques.Dragao").Ultraje,
    "Cauda Violenta": lambda: importlib.import_module("Dados.Ataques.Dragao").Cauda_Violenta,
    "Investida do Dragão": lambda: importlib.import_module("Dados.Ataques.Dragao").Investida_do_Dragao,

    "Faisca": lambda: importlib.import_module("Dados.Ataques.Eletrico").Faisca,
    "Energizar": lambda: importlib.import_module("Dados.Ataques.Eletrico").Energizar,
    "Eletrólise Hidrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Eletrolise_Hidrica,
    "Choque do Trovão": lambda: importlib.import_module("Dados.Ataques.Eletrico").Choque_do_Trovao,
    "Onda Elétrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Onda_Eletrica,
    "Bola Elétrica": lambda: importlib.import_module("Dados.Ataques.Eletrico").Bola_Eletrica,
    "Tempestade de Raios": lambda: importlib.import_module("Dados.Ataques.Eletrico").Tempestade_de_Raios,

    "Queimar": lambda: importlib.import_module("Dados.Ataques.Fogo").Queimar,
    "Bola de Fogo": lambda: importlib.import_module("Dados.Ataques.Fogo").Bola_de_Fogo,
    "Superaquecer": lambda: importlib.import_module("Dados.Ataques.Fogo").Superaquecer,
    "Brasa": lambda: importlib.import_module("Dados.Ataques.Fogo").Brasa,
    "Ondas de Calor": lambda: importlib.import_module("Dados.Ataques.Fogo").Ondas_de_Calor,
    "Raio de Fogo": lambda: importlib.import_module("Dados.Ataques.Fogo").Raio_de_Fogo,
    "Ataque de Chamas": lambda: importlib.import_module("Dados.Ataques.Fogo").Ataque_de_Chamas,
    "Laser Incandescente": lambda: importlib.import_module("Dados.Ataques.Fogo").Laser_Incandescente,

    "Cristalizar": lambda: importlib.import_module("Dados.Ataques.Gelo").Cristalizar,
    "Reinado de Gelo": lambda: importlib.import_module("Dados.Ataques.Gelo").Reinado_de_Gelo,
    "Magia de Gelo": lambda: importlib.import_module("Dados.Ataques.Gelo").Magia_de_Gelo,
    "Raio de Gelo": lambda: importlib.import_module("Dados.Ataques.Gelo").Raio_de_Gelo,
    "Gelo Verdadeiro": lambda: importlib.import_module("Dados.Ataques.Gelo").Gelo_Verdadeiro,

    "Brilho": lambda: importlib.import_module("Dados.Ataques.Fada").Brilho,
    "Vento Fada": lambda: importlib.import_module("Dados.Ataques.Fada").Vento_Fada,
    "Benção": lambda: importlib.import_module("Dados.Ataques.Fada").Bençao,
    "Busca Alegre": lambda: importlib.import_module("Dados.Ataques.Fada").Busca_Alegre,
    "Tapa das Fadas": lambda: importlib.import_module("Dados.Ataques.Fada").Tapa_das_Fadas,
    "Constelação Mágica": lambda: importlib.import_module("Dados.Ataques.Fada").Constelaçao_Magica,
    "Explosão Lunar": lambda: importlib.import_module("Dados.Ataques.Fada").Explosao_Lunar,

    "Mordida": lambda: importlib.import_module("Dados.Ataques.Inseto").Mordida,
    "Seda": lambda: importlib.import_module("Dados.Ataques.Inseto").Seda,
    "Picada": lambda: importlib.import_module("Dados.Ataques.Inseto").Picada,
    "Minhocagem": lambda: importlib.import_module("Dados.Ataques.Inseto").Minhocagem,
    "Coleta": lambda: importlib.import_module("Dados.Ataques.Inseto").Coleta,
    "Tesoura X": lambda: importlib.import_module("Dados.Ataques.Inseto").Tesoura_X,
    "Dor Falsa": lambda: importlib.import_module("Dados.Ataques.Inseto").Dor_Falsa,

    "Assombrar": lambda: importlib.import_module("Dados.Ataques.Fantasma").Assombrar,
    "Lambida": lambda: importlib.import_module("Dados.Ataques.Fantasma").Lambida,
    "Atravessar": lambda: importlib.import_module("Dados.Ataques.Fantasma").Atravessar,
    "Coleta Gananciosa": lambda: importlib.import_module("Dados.Ataques.Fantasma").Coleta_Gananciosa,
    "Mão Espectral": lambda: importlib.import_module("Dados.Ataques.Fantasma").Mao_Espectral,
    "Maldade": lambda: importlib.import_module("Dados.Ataques.Fantasma").Maldade,
    "Massacre Fantasmagórico": lambda: importlib.import_module("Dados.Ataques.Fantasma").Massacre_Fantasmagorico,
    "Vasculhada Trapaceira": lambda: importlib.import_module("Dados.Ataques.Fantasma").Vasculhada_Trapaceira,

    "Soco": lambda: importlib.import_module("Dados.Ataques.Lutador").Soco,
    "Chamar para Briga": lambda: importlib.import_module("Dados.Ataques.Lutador").Chamar_para_Briga,
    "Punho Míssil": lambda: importlib.import_module("Dados.Ataques.Lutador").Punho_Missil,
    "Combate Próximo": lambda: importlib.import_module("Dados.Ataques.Lutador").Combate_Proximo,
    "Submissão": lambda: importlib.import_module("Dados.Ataques.Lutador").Submissão,
    "Treinar": lambda: importlib.import_module("Dados.Ataques.Lutador").Treinar,

    "Reforçar": lambda: importlib.import_module("Dados.Ataques.Metal").Reforçar,
    "Cauda de Ferro": lambda: importlib.import_module("Dados.Ataques.Metal").Cauda_de_Ferro,
    "Projétil Metálico": lambda: importlib.import_module("Dados.Ataques.Metal").Projetil_Metalico,
    "Barragem": lambda: importlib.import_module("Dados.Ataques.Metal").Barragem,
    "Broca Perfuradora": lambda: importlib.import_module("Dados.Ataques.Metal").Broca_Perfuradora,
    
    "Pedregulho": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedregulho,
    "Pedra Especial": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedra_Especial,
    "Barragem Rochosa": lambda: importlib.import_module("Dados.Ataques.Pedra").Barragem_Rochosa,
    "Impacto Rochoso": lambda: importlib.import_module("Dados.Ataques.Pedra").Impacto_Rochoso,
    "Pedra Colossal": lambda: importlib.import_module("Dados.Ataques.Pedra").Pedra_Colossal,
    "Fúria Pétrea": lambda: importlib.import_module("Dados.Ataques.Pedra").Furia_Petrea,

    "Arremesso de Terra": lambda: importlib.import_module("Dados.Ataques.Terrestre").Arremesso_de_Terra,
    "Tremor": lambda: importlib.import_module("Dados.Ataques.Terrestre").Tremor,
    "Quebra Chão": lambda: importlib.import_module("Dados.Ataques.Terrestre").Quebra_Chao,
    "Afinidade Territorial": lambda: importlib.import_module("Dados.Ataques.Terrestre").Afinidade_Territorial,
    "Osso Veloz": lambda: importlib.import_module("Dados.Ataques.Terrestre").Osso_Veloz,
    "Golpe Territorial": lambda: importlib.import_module("Dados.Ataques.Terrestre").Golpe_Territorial,
    "Terremoto": lambda: importlib.import_module("Dados.Ataques.Terrestre").Terremoto,

    "Confusão": lambda: importlib.import_module("Dados.Ataques.Psiquico").Confusão,
    "Bola Psíquica": lambda: importlib.import_module("Dados.Ataques.Psiquico").Bola_Psiquica,
    "Teleporte": lambda: importlib.import_module("Dados.Ataques.Psiquico").Teleporte,
    "Ampliação Mental": lambda: importlib.import_module("Dados.Ataques.Psiquico").Ampliação_Mental,
    "Psíquico Desgastante": lambda: importlib.import_module("Dados.Ataques.Psiquico").Psiquico_Desgastante,
    "Mente Forte": lambda: importlib.import_module("Dados.Ataques.Psiquico").Mente_Forte,
    "Psicorte Duplo": lambda: importlib.import_module("Dados.Ataques.Psiquico").Psicorte_Duplo,
    "Corrosão Psíquica": lambda: importlib.import_module("Dados.Ataques.Psiquico").Corrosao_Psiquica,
    "Transferência Psíquica": lambda: importlib.import_module("Dados.Ataques.Psiquico").Transferencia_Psiquica,
    "Teletransporte": lambda: importlib.import_module("Dados.Ataques.Psiquico").Teletransporte,
    "Raio Psíquico": lambda: importlib.import_module("Dados.Ataques.Psiquico").Raio_Psiquico,
    "Agonia Mental": lambda: importlib.import_module("Dados.Ataques.Psiquico").Agonia_Mental,

    "Nas Sombras": lambda: importlib.import_module("Dados.Ataques.Sombrio").Nas_Sombras,
    "Bola Sombria": lambda: importlib.import_module("Dados.Ataques.Sombrio").Bola_Sombria,
    "Corte Noturno": lambda: importlib.import_module("Dados.Ataques.Sombrio").Corte_Noturno,
    "Confronto Trevoso": lambda: importlib.import_module("Dados.Ataques.Sombrio").Confronto_Trevoso,

    "Voar": lambda: importlib.import_module("Dados.Ataques.Voador").Voar,
    "Ataque de Asa": lambda: importlib.import_module("Dados.Ataques.Voador").Ataque_de_Asa,
    "Investida Aérea": lambda: importlib.import_module("Dados.Ataques.Voador").Investida_Aerea,
    "Rasante": lambda: importlib.import_module("Dados.Ataques.Voador").Rasante,
    "Bico Broca": lambda: importlib.import_module("Dados.Ataques.Voador").Bico_Broca,
    "Vento Forte": lambda: importlib.import_module("Dados.Ataques.Voador").Vento_Forte,

    "Envenenar": lambda: importlib.import_module("Dados.Ataques.Veneno").Envenenar,
    "Ácido": lambda: importlib.import_module("Dados.Ataques.Veneno").Acido,
    "Bomba de Lodo": lambda: importlib.import_module("Dados.Ataques.Veneno").Bomba_de_Lodo,
    "Extração": lambda: importlib.import_module("Dados.Ataques.Veneno").Extraçao,

    "Dreno": lambda: importlib.import_module("Dados.Ataques.Planta").Dreno,
    "Disparo de Semente": lambda: importlib.import_module("Dados.Ataques.Planta").Disparo_de_Semente,
    "Chicote de Vinha": lambda: importlib.import_module("Dados.Ataques.Planta").Chicote_de_Vinha,
    "Cura Natural": lambda: importlib.import_module("Dados.Ataques.Planta").Cura_Natural,
    "Raio Solar": lambda: importlib.import_module("Dados.Ataques.Planta").Raio_Solar,
    "Dança das Pétalas": lambda: importlib.import_module("Dados.Ataques.Planta").Dança_das_Petalas,
    "Mega Dreno": lambda: importlib.import_module("Dados.Ataques.Planta").Mega_Dreno,
    "Folha Navalha": lambda: importlib.import_module("Dados.Ataques.Planta").Folha_Navalha,
    "Morteiro de Pólem": lambda: importlib.import_module("Dados.Ataques.Planta").Morteiro_de_Polem,

}

def SelecionaAtaques(ataque):
    return DicionarioAtaques[ataque]()
