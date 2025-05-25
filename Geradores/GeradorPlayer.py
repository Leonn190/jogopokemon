from Geradores.GeradorPokemon import Gerador_final, Gerador_Clone
from Visual.Sonoridade import tocar
from Jogo.Abas import Trocar_Ataque_Pergunta
from Dados.Treinadores import Derrotas,Vitorias,Passivas,Habilidades
import Visual.GeradoresVisuais as GV
import random

class Jogador:
    def __init__(self, informaçoes, Dados=False):
        
        if Dados is False:
            self.nome = informaçoes[0]
            if informaçoes[1] is not None:
                self.pokemons = [Gerador_final(informaçoes[1]["code"],1,self)]
            else:
                informaçoes[1] = informaçoes[2]["pokemons"][random.choice([0,1,2])]
                self.pokemons = [Gerador_final(informaçoes[1]["code"],1,self)]
            self.inventario = []
            self.energias = {"vermelha": 0, "azul": 0, "amarela": 0, "verde": 0, "roxa": 0, "laranja": 0, "preta": 0}
            self.energiasMax = 15
            self.energiasDesc = []
            self.ouro = 10
            self.deck = informaçoes[2]
            self.treinador = informaçoes[2]["treinador"]
            self.tempo = self.treinador["tempo"]
            self.AtivaPassiva = self.treinador["ativaTurno"]
            self.ContaPassiva = self.treinador["ativaTurno"]
            self.PoderCaptura = self.treinador["Poder"]
            self.Derrota = Derrotas[self.treinador["nome"]]
            self.Vitoria = Vitorias[self.treinador["nome"]]
            self.Passiva = Passivas[self.treinador["nome"]]
            self.Habilidade = Habilidades[self.treinador["nome"]]
            self.NocautesSofridos = 0
            self.NocautesRealizados = 0
            self.PokemonsNocauteados = 0
            self.PokemonsCapturados = 0
            self.PontosSofridos = 0
            self.Pontos = 0
            self.PontosVitoria = self.treinador["Vitoria"]
            self.PontosDerrota = self.treinador["Derrota"]
            self.Megas = 0
            self.Ultras = 0
            self.Vstars = 0
            self.Vmaxs = 0
            self.MultiplicaIV = 1

            for energia in self.deck["energiasD"]:
                if energia is not None:
                    self.energiasDesc.append(energia)
        else:
            self.nome = Dados["nome"]
            self.pokemons = [Gerador_Clone(p) for p in Dados["pokemons"]]
            self.inventario = Dados["inventario"]
            self.energias = Dados["energias"]
            self.energiasMax = Dados["energiasMax"]
            self.ouro = Dados["ouro"]
            self.deck = Dados["deck"]
            self.treinador = Dados["treinador"]
            self.tempo = Dados["tempo"]
            self.AtivaPassiva = Dados["AtivaPassiva"]
            self.ContaPassiva = Dados["ContaPassiva"]
            self.PoderCaptura = Dados["PoderCaptura"]
            self.NocautesSofridos = Dados["NocautesSofridos"]
            self.NocautesRealizados = Dados["NocautesRealizados"]
            self.PokemonsNocauteados = Dados["PokemonsNocauteados"]
            self.PokemonsCapturados = Dados["PokemonsCapturados"]
            self.PontosSofridos = Dados["PontosSofridos"]
            self.Pontos = Dados["Pontos"]
            self.PontosVitoria = Dados["PontosVitoria"]
            self.PontosDerrota = Dados["PontosDerrota"]
            self.Megas = Dados["Megas"]
            self.Ultras = Dados["Ultras"]
            self.Vstars = Dados["Vstars"]
            self.Vmaxs = Dados["Vmaxs"]
    
    def usar_item(self,item,Pokemon,tela,Mapa,ataque,EstadoDaPergunta, Baralho):
            if item["classe"] in ["pokebola", "fruta"]:
                tocar("Bloq")
                GV.adicionar_mensagem("Pokebolas e frutas são usadas no centro")
            else:
                if item["classe"] in ["poçao"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            cura = item["cura"]
                            tocar("Usou")
                            if not item.get("extra"):
                                Baralho.devolve_item(item)
                            self.inventario.remove(item)
                            Pokemon.curar(cura,self,tela)
                            return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser curados")
                elif item["classe"] in ["amplificador"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            tipo = item["aumento"]
                            if tipo == "Evolucional":
                                Pokemon.FormaFinal(item,self)
                            elif tipo == "XP":
                                Pokemon.Ganhar_XP(5,self)
                                GV.adicionar_mensagem(f"{Pokemon.nome} Ganhou 5 de XP")
                                if not item.get("extra"):
                                    Baralho.devolve_item(item)
                                self.inventario.remove(item)
                                return
                            elif Pokemon.amplificações > 5:
                                GV.adicionar_mensagem("Esse pokemon já atingiu 6 amplificações")
                                return
                            else:
                                tocar("Usou")
                                if not item.get("extra"):
                                    Baralho.devolve_item(item)
                                self.inventario.remove(item)
                                Pokemon.amplificar(tipo,tela,self)
                                return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser amplificados")
                elif item["classe"] == "estadio":
                    tocar("Usou")
                    Mapa.MudarEstagio(item["ST Code"])
                    if not item.get("extra"):
                        Baralho.devolve_item(item)
                    self.inventario.remove(item)
                    return
                elif item["classe"] == "Outros":
                    if item["nome"] == "Trocador de Ataque":
                        if ataque is not None:
                            tocar("Usou")
                            Trocar_Ataque_Pergunta(Pokemon,ataque,EstadoDaPergunta)
                            if not item.get("extra"):
                                Baralho.devolve_item(item)
                            self.inventario.remove(item)
                            return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("selecione um ataque para usar um item")
                    else:
                        if Pokemon is not None:
                            if not getattr(self, "RemoveuPokemon", None):
                                GV.adicionar_mensagem(f"seu {Pokemon.nome} foi embora")
                                self.pokemons.remove(Pokemon)
                                self.RemoveuPokemon = True
                                if not item.get("extra"):
                                    Baralho.devolve_item(item)
                                self.inventario.remove(item)
                            else:
                                tocar("Bloq")
                                GV.adicionar_mensagem("Não é possivel usar esse item novamente")
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("selecione um pokemon para usar um item")
                else:
                    tocar("Bloq")
                    GV.adicionar_mensagem("selecione um pokemon para usar um item")
    
    def vender_item(self,item,Baralho):
        self.ouro += item["preço"] // 2
        self.inventario.remove(item)
        Baralho.devolve_item(item)

    def ganhar_pokemon(self,pokemon):
        self.pokemons.append(pokemon)

    def muda_descarte(self,energia):
        if energia in self.energiasDesc:
            self.energiasDesc.remove(energia)
        else:
            self.energiasDesc.append(energia)

    def ganhar_item(self,item,Baralho):
            if len(self.inventario) < 13:
                self.inventario.append(item)
                return True
            else:
                GV.adicionar_mensagem("Inventário cheio")
                self.ouro += item["preço"]
                Baralho.devolve_item(item)
                return False

    def ToDic(self):
        return {
            "nome": self.nome,
            "pokemons": [p.ToDic() for p in self.pokemons],
            "inventario": self.inventario,
            "energias": self.energias.copy(),
            "energiasMax": self.energiasMax,
            "ouro": self.ouro,
            "deck": self.deck,
            "treinador": self.treinador,
            "tempo": self.tempo,
            "AtivaPassiva": self.AtivaPassiva,
            "ContaPassiva": self.ContaPassiva,
            "PoderCaptura": self.PoderCaptura,
            "NocautesSofridos": self.NocautesSofridos,
            "NocautesRealizados": self.NocautesRealizados,
            "PokemonsNocauteados": self.PokemonsNocauteados,
            "PokemonsCapturados": self.PokemonsCapturados,
            "PontosSofridos": self.PontosSofridos,
            "Pontos": self.Pontos,
            "PontosVitoria": self.PontosVitoria,
            "PontosDerrota": self.PontosDerrota,
            "Megas": self.Megas,
            "Ultras": self.Ultras,
            "Vstars": self.Vstars,
            "Vmaxs": self.Vmaxs,
        }
    

def Gerador_player(informaçoes):
    return Jogador(informaçoes)

def Gerador_player_clone(dados):
    return Jogador(None,dados)
