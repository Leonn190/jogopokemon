from Gerador2 import Gerador_final, caixa, coletor, pokebolas_disponiveis
from Sonoridade import tocar
from Partida import Mudar_estadio
import GeradoresVisuais as GV


class Jogador:
    def __init__(self, informaçoes):
        self.nome = informaçoes[0]
        self.pokemons = [Gerador_final(informaçoes[1],1,self)]
        self.inventario = []
        self.Captura = []
        self.energias = { "vermelha": 0, "azul": 0, "amarela": 0, "verde": 0, "roxa": 0, "rosa": 0, "laranja": 0,"marrom": 0, "preta": 0, "cinza": 0}
        self.energiasDesc = []
        self.ouro = 10
    
    def ganhar_item(self,item):
        self.inventario.append(item)
    
    def usar_item(self,indice,Pokemon,tela):
            item = self.inventario[indice] 
            if item["classe"] in ["pokebola", "fruta"]:
                tocar("Bloq")
                GV.adicionar_mensagem("Pokebolas e frutas são usadas no centro")
            else:
                if item["classe"] in ["poçao"] and Pokemon is not None:
                        if Pokemon.Vida > 0:
                            cura = item["cura"]
                            tocar("Usou")
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
                            else:
                                tocar("Usou")
                                self.inventario.remove(item)
                                Pokemon.amplificar(tipo,0.1,self)
                                return
                        else:
                            tocar("Bloq")
                            GV.adicionar_mensagem("Pokemons nocauteados não podem ser amplificados")
                elif item["classe"] in ["caixa","coletor"]:
                    compras = item["compra"]
                    if item["classe"] in ["caixa"]:
                        tocar("Usou")
                        self.inventario.remove(item)
                        for _ in range(compras):
                            item = caixa()
                            if item in pokebolas_disponiveis:
                                self.Captura.append(item)
                            else:
                                self.inventario.append(item)
                        return
                    elif item["classe"] in ["coletor"]:
                        tocar("Usou")
                        self.inventario.remove(item)
                        for _ in range(compras):
                            self.energias[coletor()] += 1
                        return
                elif item["classe"] == "estadio":
                    tocar("Usou")
                    Mudar_estadio(item["ST Code"])
                    self.inventario.remove(item)
                    return
                else:
                    tocar("Bloq")
                    GV.adicionar_mensagem("selecione um pokemon para usar um item")
    
    def ganhar_pokemon(self,pokemon):
        self.pokemons.append(pokemon)

    def muda_descarte(self,energia):
        if energia in self.energiasDesc:
            self.energiasDesc.remove(energia)
        else:
            self.energiasDesc.append(energia)

def Gerador_player(informaçoes):
    return Jogador(informaçoes)
