import Funções2 as FU
import random
import Gerador2 as G

def Curar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i, alvos_selecionados):
    valores = ataque["valores"][i]
    
    # Se não houver alvos, retorna
    if not alvos_selecionados:
        return
    
    # Garante que alvos_selecionados seja uma lista (caso venha um único alvo, torna-se uma lista)
    if not isinstance(alvos_selecionados, list):
        alvos_selecionados = [alvos_selecionados]
    
    # Aplica a cura em cada alvo
    for alvo_final in alvos_selecionados:
        if isinstance(valores, list):
            mult, atributo = valores
            if atributo == "Atk":
                cura = mult * pokemon.Atk
            elif atributo == "Atk sp":
                cura = mult * pokemon.Atk_sp
            elif atributo == "Vida":
                cura = mult * pokemon.Vida
            else:
                continue
            pokemon.curar(alvo_final, cura, player, tela)
        elif isinstance(valores, (int, float)):
            if valores < 2:
                pokemon.vampirismo = valores
            else:
                pokemon.curar(alvo_final, valores, player, tela)

def Efeito(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i, alvos_selecionados):
    efeito_dado = ataque["valores"][i]  # Agora é sempre ["efeito", duração]

    if not alvos_selecionados:
        return
    if not isinstance(alvos_selecionados, list):
        alvos_selecionados = [alvos_selecionados]

    efeito, duracao = efeito_dado
    for alvo_final in alvos_selecionados:
        if efeito in alvo_final.efeitosPosi:
            alvo_final.efeitosPosi[efeito] = duracao
        elif efeito in alvo_final.efeitosNega:
            alvo_final.efeitosNega[efeito] = duracao

def Status(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i, alvos_selecionados):
    atributo, quantidade = ataque["valores"][i]

    # Se não houver alvos, retorna
    if not alvos_selecionados:
        return

    # Garante que alvos_selecionados seja uma lista (caso venha um único alvo, torna-se uma lista)
    if not isinstance(alvos_selecionados, list):
        alvos_selecionados = [alvos_selecionados]

    # Aplica a mudança de status em cada alvo
    for alvo_final in alvos_selecionados:
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

def DanoExtra(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i, alvos_selecionados):
    if not alvos_selecionados:
        return

    # Garante que alvos_selecionados seja uma lista (caso venha um único alvo, transforma em lista)
    if not isinstance(alvos_selecionados, list):
        alvos_selecionados = [alvos_selecionados]

    # Obtem o valor do dano extra a ser aplicado
    valor = ataque["valores"][i]

    for alvo_final in alvos_selecionados:
        if valor < 2:
            dano_extra = dano * valor
        else:
            dano_extra = valor

        # Aplica o dano extra ao alvo
        alvo_final.atacado(dano_extra)


def DanoEscalar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i):
    atributo = ataque["valores"][i]

    if atributo == "Vida":
        dano = ataque["dano"] * pokemon.VidaMax
    elif atributo == "VidaPerdida":
        vida_perdida = pokemon.VidaMax - pokemon.Vida
        dano = ataque["dano"] * vida_perdida
    elif atributo == "Def":
        dano = ataque["dano"] * pokemon.Def
    elif atributo == "Def_sp":
        dano = ataque["dano"] * pokemon.Def_sp
    elif atributo == "vel":
        dano = ataque["dano"] * pokemon.vel
    # caso inválido, dano permanece o mesmo

    return defesa, dano

def AumentoCondicional(ataque, pokemon, alvo, player, inimigo, mapa, dano, defesa, i):
    base = ataque["valores"][i][0]
    condicao = ataque["valores"][i][1]
    aumento = ataque["valores"][i][2]

    def contar_itens(j):
        return sum(j.inventario.values()) + sum(j.captura.values())

    def contar_energias(j):
        return sum(j.energias.values())

    def contar_pokemons(j):
        return len(j.time)

    def contar_efeitos(dicionario):
        return sum(1 for v in dicionario.values() if v > 0)

    if base == "EfeitoAliado":
        nome_efeito = condicao
        if pokemon.efeitosPosi.get(nome_efeito, 0) > 0 or pokemon.efeitosNega.get(nome_efeito, 0) > 0:
            dano += aumento
    elif base == "EfeitoInimigo":
        if alvo:
            nome_efeito = condicao
            if alvo.efeitosPosi.get(nome_efeito, 0) > 0 or alvo.efeitosNega.get(nome_efeito, 0) > 0:
                dano += aumento
    else:
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
            if distancia is not None:
                alcance = ataque.get("alcance", 999)
                valor = max(0, alcance - distancia)
            else:
                valor = 0
        elif base == "VidaPerdida":
            valor = pokemon.VidaMax - pokemon.Vida
        elif base == "EfeitosNegaInimigo":
            valor = contar_efeitos(alvo.efeitosNega)
        elif base == "EfeitosPosiInimigo":
            valor = contar_efeitos(alvo.efeitosPosi)
        elif base == "EstagioInimigo":
            valor = alvo.estagio
        else:
            valor = 0

        if aumento > 2:
            if valor >= condicao:
                dano += aumento
        else:
            if condicao != 0:
                dano += (valor // condicao) * aumento

    return defesa, dano

def RemoverGanhar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa,i):
    alvo_real = player if ataque["alvo"] == "player" else inimigo
    tipo, valor = ataque["valores"][i]

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
    return defesa, dano

def Perfurar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i):
    if ataque["alvo"] is None:
        perfuraçao = 1 - ataque["valores"][i]
    else:
        if ataque["alvo"] == "Atk":
            perfuraçao = 1 - ataque["valores"] * pokemon.Atk
        elif ataque["alvo"] == "Atk sp":
            perfuraçao = 1 - ataque["valores"] * pokemon.Atk_sp
        elif ataque["alvo"] == "vel":
            perfuraçao = 1 - ataque["valores"] * pokemon.vel
        else:
            perfuraçao = 1  # nenhuma alteração se tipo não reconhecido

    defesa *= perfuraçao
    return defesa, dano

def Corroer(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i):
    defesa = 0
    dano = alvo.Vida * dano
    return defesa, dano

def Executar(ataque, pokemon, alvo, player, inimigo, mapa, tela, dano, defesa, i):
    Tipo = ataque["tipo"]
    mitigação = 100 / (100 + defesa) 
    dano_E = dano * FU.efetividade(Tipo,alvo.tipo,tela,alvo)
    dano_F = round(dano_E * mitigação,1)
    if alvo.Vida - dano_F < alvo.VidaMax / ataque["valores"][i]:
        dano = 1000
    return defesa, dano
