from Geradores.GeradorPokemon import Gerador_final
from Visual.Sonoridade import tocar
from Jogo.Abas import Trocar_Ataque_Pergunta
from Geradores.GeradorOutros import Pokebolas_disponiveis,coletor
import Visual.GeradoresVisuais as GV

class Jogador:
    def __init__(self, informaçoes):
        self.nome = informaçoes[0]
        self.pokemons = [Gerador_final(informaçoes[1]["code"],1,self)]
        self.inventario = []
        self.energias = {"vermelha": 0, "azul": 0, "amarela": 0, "verde": 0, "roxa": 0, "laranja": 0, "preta": 0}
        self.energiasDesc = []
        self.ouro = 10
        self.deck = informaçoes[2]

        for energia in self.deck["energiasD"]:
            if energia is not None:
                self.energiasDesc.append(energia)
    
    def usar_item(self,item,Pokemon,tela,Mapa,ataque,EstadoDaPergunta, Baralho):
            if item["classe"] in ["pokebola", "fruta"]:
                tocar("Bloq")
                GV.adicionar_mensagem("Pokebolas e frutas são usadas no centro")
            else:
                if item["classe"] in ["poçao"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            cura = item["cura"]
                            tocar("Usou")
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
                                Baralho.devolve_item(item)
                                self.inventario.remove(item)
                                return
                            elif Pokemon.amplificações > 5:
                                GV.adicionar_mensagem("Esse pokemon já atingiu 6 amplificações")
                                return
                            else:
                                tocar("Usou")
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
                    Baralho.devolve_item(item)
                    self.inventario.remove(item)
                    return
                elif item["classe"] == "Outros":
                    if item["nome"] == "Trocador de Ataque" and ataque is not None:
                        tocar("Usou")
                        Trocar_Ataque_Pergunta(Pokemon,ataque,EstadoDaPergunta)
                        Baralho.devolve_item(item)
                        self.inventario.remove(item)
                        return
                    else:
                        tocar("Bloq")
                        GV.adicionar_mensagem("selecione um ataque para usar um item")
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

def Gerador_player(informaçoes):
    return Jogador(informaçoes)
