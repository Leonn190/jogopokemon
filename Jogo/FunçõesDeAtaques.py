import Funções2 as FU
import random
import Gerador2 as G

def Curar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    alvo_str = ataque["alvo"]
    valores = ataque["valores"]

    # Seleciona o(s) alvos com base no alvo_str, que pode retornar uma lista de alvos
    alvos_finais = FU.seleciona_alvo(pokemon, alvo_str, player, inimigo, mapa, alvo)
    
    # Se não houver alvos, retorna
    if not alvos_finais:
        return
    
    # Garante que alvos_finais seja uma lista (caso venha um único alvo, torna-se uma lista)
    if not isinstance(alvos_finais, list):
        alvos_finais = [alvos_finais]
    
    # Aplica a cura em cada alvo
    for alvo_final in alvos_finais:
        for valor in valores:
            if isinstance(valor, list):
                mult, atributo = valor
                if atributo == "Atk":
                    cura = mult * pokemon.Atk
                elif atributo == "Atk sp":
                    cura = mult * pokemon.Atk_sp
                elif atributo == "Vida":
                    cura = mult * pokemon.Vida
                else:
                    continue
                pokemon.curar(alvo_final, cura, player, tela)
            elif isinstance(valor, (int, float)):
                if valor < 2:
                    pokemon.vampirismo = valor
                else:
                    pokemon.curar(alvo_final, valor, player, tela)

def Efeito(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    alvo_str = ataque["alvo"]
    valores = ataque["valores"]

    # Seleciona o(s) alvos com base no alvo_str, que pode retornar uma lista de alvos
    alvos_finais = FU.seleciona_alvo(pokemon, alvo_str, player, inimigo, mapa, alvo)
    
    # Se não houver alvos, retorna
    if not alvos_finais:
        return
    
    # Garante que alvos_finais seja uma lista (caso venha um único alvo, torna-se uma lista)
    if not isinstance(alvos_finais, list):
        alvos_finais = [alvos_finais]
    
    # Aplica os efeitos em cada alvo
    for alvo_final in alvos_finais:
        for efeito, duracao in valores:
            if efeito in alvo_final.efeitosPosi:
                alvo_final.efeitosPosi[efeito] = duracao
            elif efeito in alvo_final.efeitosNega:
                alvo_final.efeitosNega[efeito] = duracao

def Status(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    alvo_str = ataque["alvo"]
    atributo, quantidade = ataque["valores"]

    # Seleciona o(s) alvos com base no alvo_str, que pode retornar uma lista de alvos
    alvos_finais = FU.seleciona_alvo(pokemon, alvo_str, player, inimigo, mapa, alvo)

    # Se não houver alvos, retorna
    if not alvos_finais:
        return

    # Garante que alvos_finais seja uma lista (caso venha um único alvo, torna-se uma lista)
    if not isinstance(alvos_finais, list):
        alvos_finais = [alvos_finais]

    # Aplica a mudança de status em cada alvo
    for alvo_final in alvos_finais:
        if atributo == "Atk":
            alvo_final.Atk += quantidade
        elif atributo == "Atk_sp":
            alvo_final.Atk_sp += quantidade
        elif atributo == "Def":
            alvo_final.Def += quantidade
        elif atributo == "Def_sp":
            alvo_final.Def_sp += quantidade
        elif atributo == "vel":
            alvo_final.vel += quantidade
        elif atributo == "Xp":
            alvo_final.xp_atu += quantidade


def DanoExtra(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    # Encontrar o alvo usando a função auxiliar seleciona_alvo
    alvo_selecionado = FU.seleciona_alvo(pokemon, ataque["alvo"], player, inimigo, mapa, alvo)

    if alvo_selecionado:
        # Obter o valor do dano extra a ser aplicado
        dano_extra = ataque["valores"][0]

        # Se o dano extra for menor que 2, usamos ele como um multiplicador
        if dano_extra < 2:
            # Aplica o multiplicador ao dano existente, mas não altera o valor do dano original
            dano_extra = dano * dano_extra
        else:
            # Se o valor de dano for maior ou igual a 2, aplica o dano diretamente
            dano_extra = dano_extra

        # Aplica o dano extra ao alvo selecionado
        alvo_selecionado.atacado(dano_extra)

def DanoEscalar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    atributo = ataque["valores"]

    if atributo == "Vida":
        return ataque["dano"] * pokemon.VidaMax
    
    elif atributo == "VidaPerdida":
        vida_perdida = pokemon.VidaMax - pokemon.Vida
        return ataque["dano"] * vida_perdida

    elif atributo == "Def":
        return ataque["dano"] * pokemon.Def

    elif atributo == "Def_sp":
        return ataque["dano"] * pokemon.Def_sp

    elif atributo == "vel":
        return ataque["dano"] * pokemon.vel

    else:
        return dano  # Mantém o dano original caso atributo inválido

def AumentoCondicional(ataque, pokemon, alvo, player, inimigo, mapa, dano, defesa):
    
    base = ataque["valores"][0]
    condicao = ataque["valores"][1]
    aumento = ataque["valores"][2]

    def contar_itens(j):
        return sum(j.inventario.values()) + sum(j.captura.values())

    def contar_energias(j):
        return sum(j.energias.values())

    def contar_pokemons(j):
        return len(j.time)

    def contar_efeitos(dicionario):
        return sum(1 for v in dicionario.values() if v > 0)

    # Se a base for efeito direto (EfeitoAliado/Inimigo), trataremos separadamente
    if base == "EfeitoAliado":
        nome_efeito = condicao
        if pokemon.efeitosPosi.get(nome_efeito, 0) > 0 or pokemon.efeitosNega.get(nome_efeito, 0) > 0:
            return aumento
        else:
            return 0

    elif base == "EfeitoInimigo":
        if not alvo:
            return 0
        nome_efeito = condicao
        if alvo.efeitosPosi.get(nome_efeito, 0) > 0 or alvo.efeitosNega.get(nome_efeito, 0) > 0:
            return aumento
        else:
            return 0

    # Demais bases seguem aqui
    if base == "Ouro":
        valor = player.ouro
    elif base == "Xp":
        valor = pokemon.XP
    elif base == "Itens":
        valor = contar_itens(player)
    elif base == "Energias":
        valor = contar_energias(player)
    elif base == "Pokemons":
        valor = contar_pokemons(player)
    elif base == "Xpinimigo":
        valor = alvo.XP
    elif base == "EnergiasInimigo":
        valor = contar_energias(inimigo)
    elif base == "ItensInimigo":
        valor = contar_itens(inimigo)
    elif base == "OuroInimigo":
        valor = inimigo.ouro
    elif base == "PokemonsInimigo":
        valor = contar_pokemons(inimigo)
    elif base == "Distancia":
        valor = FU.distancia_entre_pokemons(pokemon, alvo, mapa.Metros)
    elif base == "Proximidade":
        distancia = FU.distancia_entre_pokemons(pokemon, alvo, mapa.Metros)
        if distancia is None:
            return 0
        alcance = ataque.get("alcance", 999)
        valor = max(0, alcance - distancia)
    elif base == "VidaPerdida":
        valor = pokemon.VidaMax - pokemon.vida
    elif base == "EfeitosNegaInimigo":
        valor = contar_efeitos(alvo.efeitosNega)
    elif base == "EfeitosPosiInimigo":
        valor = contar_efeitos(alvo.efeitosPosi)
    elif base == "EstagioInimigo":
        valor = alvo.estagio
    else:
        valor = 0

    # Escalar ou fixo?
    if aumento > 2:
        if valor >= condicao:
            return aumento
        else:
            return 0
    else:
        if condicao == 0:
            return 0  # evitar divisão por zero
        else:
            return (valor // condicao) * aumento

def RemoverGanhar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    alvo_real = player if ataque["alvo"] == "player" else inimigo
    tipo, valor = ataque["valores"]

    if tipo == "Ouro":
        alvo_real.ouro += valor
        alvo_real.ouro = max(0, alvo_real.ouro)

    elif tipo == "Energia":
        if valor >= 0:
            G.coletor(alvo_real, valor)
        else:
            for _ in range(abs(valor)):
                energias = [k for k in alvo_real.energias if alvo_real.energias[k] > 0]
                if energias:
                    escolhida = random.choice(energias)
                    alvo_real.energias[escolhida] -= 1

    elif tipo == "Item":
        if valor >= 0:
            for _ in range(valor):
                G.caixa(alvo_real)
        else:
            for _ in range(abs(valor)):
                itens_inventario = [item for item in alvo_real.inventario]
                itens_captura = [item for item in alvo_real.captura]
                todos_itens = itens_inventario + itens_captura
                if todos_itens:
                    escolhida = random.choice(todos_itens)
                    if escolhida in alvo_real.inventario and alvo_real.inventario[escolhida] > 0:
                        alvo_real.inventario[escolhida] -= 1
                    elif escolhida in alvo_real.captura and alvo_real.captura[escolhida] > 0:
                        alvo_real.captura[escolhida] -= 1

def Perfurar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    if ataque["alvo"] is None:
        perfuraçao = 1 - ataque["valores"]
    else:
        if ataque["alvo"] ==  "Atk":
            perfuraçao = 1 - ataque["valores"] * pokemon.Atk
        elif ataque["alvo"] ==  "Atk sp":
            perfuraçao = 1 - ataque["valores"] * pokemon.Atk_sp
        elif ataque["alvo"] ==  "vel":
            perfuraçao = 1 - ataque["valores"] * pokemon.vel
    
    defesa = defesa * perfuraçao
    return defesa

def Corroer(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa):
    defesa = 0
    dano = alvo.Vida * dano

    return 
