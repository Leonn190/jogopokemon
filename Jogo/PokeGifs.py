import pygame

Gifs_ativos = []

def VerificaGIF(PokeGifs,player,inimigo):
    global Gifs_ativos

        # Ao capturar um novo Pokémon (exemplo)
    for i in range(len(player.pokemons)):
        nome = player.pokemons[i].nome

        # Verifica se o Pokémon ainda não foi adicionado
        if nome not in [gif["nome"] for gif in Gifs_ativos]:
            Gifs_ativos.append({
                "nome": nome,
                "frames": PokeGifs[nome],
                "frame_atual": 0,
                "tempo_anterior": pygame.time.get_ticks(),
                "intervalo": 25  # Pode ser ajustado para cada Pokémon se necessário
            })
    for i in range(len(inimigo.pokemons)):
        nome = inimigo.pokemons[i].nome

        # Verifica se o Pokémon ainda não foi adicionado
        if nome not in [gif["nome"] for gif in Gifs_ativos]:
            Gifs_ativos.append({
                "nome": nome,
                "frames": PokeGifs[nome],
                "frame_atual": 0,
                "tempo_anterior": pygame.time.get_ticks(),
                "intervalo": 25  # Pode ser ajustado para cada Pokémon se necessário
            })
