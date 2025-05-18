import Visual.GeradoresVisuais as GV

Size = 0

pokeiconsrecortados = {
    "Bulbasaur": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/bulbasaur.png", (Size, Size), "PNG"),
    "Ivysaur": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/ivysaur.png", (Size, Size), "PNG"),
    "Venusaur": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/venusaur.png", (Size, Size), "PNG"),
    "Charmander": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/charmander.png", (Size, Size), "PNG"),
    "Charmeleon": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/charmeleon.png", (Size, Size), "PNG"),
    "Charizard": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/charizard.png", (Size, Size), "PNG"),
    "Squirtle": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/squirtle.png", (Size, Size), "PNG"),
    "Wartortle": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/wartortle.png", (Size, Size), "PNG"),
    "Blastoise": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/blastoise.png", (Size, Size), "PNG"),
    "Machop": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/machop.png", (Size, Size), "PNG"),
    "Machoke": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/machoke.png", (Size, Size), "PNG"),
    "Machamp": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/machamp.png", (Size, Size), "PNG"),
    "Gastly": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/gastly.png", (Size, Size), "PNG"),
    "Haunter": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/haunter.png", (Size, Size), "PNG"),
    "Gengar": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/gengar.png", (Size, Size), "PNG"),
    "Geodude": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/geodude.png", (Size, Size), "PNG"),
    "Graveler": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/graveler.png", (Size, Size), "PNG"),
    "Golem": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/golem.png", (Size, Size), "PNG"),
    "Caterpie": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/caterpie.png", (Size, Size), "PNG"),
    "Metapod": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/metapod.png", (Size, Size), "PNG"),
    "Butterfree": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/butterfree.png", (Size, Size), "PNG"),
    "Abra": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/abra.png", (Size, Size), "PNG"),
    "Kadabra": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/kadabra.png", (Size, Size), "PNG"),
    "Alakazam": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/alakazam.png", (Size, Size), "PNG"),
    "Dratini": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/dratini.png", (Size, Size), "PNG"),
    "Dragonair": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/dragonair.png", (Size, Size), "PNG"),
    "Dragonite": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/dragonite.png", (Size, Size), "PNG"),
    "Zorua": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/zorua.png", (Size, Size), "PNG"),
    "Zoroark": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/zoroark.png", (Size, Size), "PNG"),
    "Pikachu": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/pikachu.png", (Size, Size), "PNG"),
    "Raichu": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/raichu.png", (Size, Size), "PNG"),
    "Magikarp": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/magikarp.png", (Size, Size), "PNG"),
    "Gyarados": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/gyarados.png", (Size, Size), "PNG"),
    "Jigglypuff": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/jigglypuff.png", (Size, Size), "PNG"),
    "Wigglytuff": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/wigglytuff.png", (Size, Size), "PNG"),
    "Magnemite": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/magnemite.png", (Size, Size), "PNG"),
    "Magneton": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/magneton.png", (Size, Size), "PNG"),
    "Snorlax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/snorlax.png", (Size, Size), "PNG"),
    "Aerodactyl": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/aerodactyl.png", (Size, Size), "PNG"),
    "Jynx": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/jynx.png", (Size, Size), "PNG"),
    "Mewtwo": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/mewtwo.png", (Size, Size), "PNG"),
    "Mega Aerodactyl": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/aerodactyl.png", (Size, Size), "PNG"),
    "Mega Alakazam": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/alakazam.png", (Size, Size), "PNG"),
    "Articuno": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/articuno.png", (Size, Size), "PNG"),
    "Beedrill": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/beedrill.png", (Size, Size), "PNG"),
    "Mega Beedrill": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/beedrill.png", (Size, Size), "PNG"),
    "Blastoise Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/blastoise.png", (Size, Size), "PNG"),
    "Mega Blastoise": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/blastoise.png", (Size, Size), "PNG"),
    "Butterfree Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/butterfree.png", (Size, Size), "PNG"),
    "Charizard Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/charizard.png", (Size, Size), "PNG"),
    "Mega Charizard X": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/charizard.png", (Size, Size), "PNG"),
    "Mega Charizard Y": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/charizard.png", (Size, Size), "PNG"),
    "Clefable": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/clefable.png", (Size, Size), "PNG"),
    "Clefairy": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/clefairy.png", (Size, Size), "PNG"),
    "Cloyster": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/cloyster.png", (Size, Size), "PNG"),
    "Cubone": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/cubone.png", (Size, Size), "PNG"),
    "Gengar Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/gengar.png", (Size, Size), "PNG"),
    "Mega Gengar": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/gengar.png", (Size, Size), "PNG"),
    "Golem-alola": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/golem.png", (Size, Size), "PNG"),
    "Mega Gyarados": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/gyarados.png", (Size, Size), "PNG"),
    "Kakuna": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/kakuna.png", (Size, Size), "PNG"),
    "Machamp Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/machamp.png", (Size, Size), "PNG"),
    "Marowak": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/marowak.png", (Size, Size), "PNG"),
    "Meowth": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/meowth.png", (Size, Size), "PNG"),
    "Meowth Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/meowth.png", (Size, Size), "PNG"),
    "Mega Mewtwo X": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/mewtwo.png", (Size, Size), "PNG"),
    "Mega Mewtwo Y": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/mewtwo.png", (Size, Size), "PNG"),
    "Moltres": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/moltres.png", (Size, Size), "PNG"),
    "Persian": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/persian.png", (Size, Size), "PNG"),
    "Pikachu Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/pikachu.png", (Size, Size), "PNG"),
    "Pinsir": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/pinsir.png", (Size, Size), "PNG"),
    "Mega Pinsir": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/pinsir.png", (Size, Size), "PNG"),
    "Raticate": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/raticate.png", (Size, Size), "PNG"),
    "Rattata": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/rattata.png", (Size, Size), "PNG"),
    "Shellder": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/shellder.png", (Size, Size), "PNG"),
    "Snorlax Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/snorlax.png", (Size, Size), "PNG"),
    "Venusaur Vmax": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/venusaur.png", (Size, Size), "PNG"),
    "Zapdos": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/zapdos.png", (Size, Size), "PNG"),
    "Weedle": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/weedle.png", (Size, Size), "PNG"),
    "Charizard V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/charizard.png", (Size, Size), "PNG"),
    "Blastoise V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/blastoise.png", (Size, Size), "PNG"),
    "Venusaur V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/venusaur.png", (Size, Size), "PNG"),
    "Machamp V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/machamp.png", (Size, Size), "PNG"),
    "Gengar V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/machoke.png", (Size, Size), "PNG"),
    "Butterfree V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/butterfree.png", (Size, Size), "PNG"),
    "Pikachu V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/pikachu.png", (Size, Size), "PNG"),
    "Meowth V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/meowth.png", (Size, Size), "PNG"),
    "Snorlax V": lambda: GV.Carregar_Imagem("imagens/pokeiconsrecortados/snorlax.png", (Size, Size), "PNG")
}

PokeGifs = {
    "Bulbasaur": lambda: GV.carregar_frames('imagens/gifs/bulbasaur_frames'),
    "Ivysaur": lambda: GV.carregar_frames('imagens/gifs/ivysaur_frames'),
    "Venusaur": lambda: GV.carregar_frames('imagens/gifs/venusaur_frames'),
    "Charmander": lambda: GV.carregar_frames('imagens/gifs/charmander_frames'),
    "Charmeleon": lambda: GV.carregar_frames('imagens/gifs/charmeleon_frames'),
    "Charizard": lambda: GV.carregar_frames('imagens/gifs/charizard_frames'),
    "Squirtle": lambda: GV.carregar_frames('imagens/gifs/squirtle_frames'),
    "Wartortle": lambda: GV.carregar_frames('imagens/gifs/wartortle_frames'),
    "Blastoise": lambda: GV.carregar_frames('imagens/gifs/blastoise_frames'),
    "Machop": lambda: GV.carregar_frames('imagens/gifs/machop_frames'),
    "Machoke": lambda: GV.carregar_frames('imagens/gifs/machoke_frames'),
    "Machamp": lambda: GV.carregar_frames('imagens/gifs/machamp_frames'),
    "Gastly": lambda: GV.carregar_frames('imagens/gifs/gastly_frames'),
    "Haunter": lambda: GV.carregar_frames('imagens/gifs/haunter_frames'),
    "Gengar": lambda: GV.carregar_frames('imagens/gifs/gengar_frames'),
    "Geodude": lambda: GV.carregar_frames('imagens/gifs/geodude_frames'),
    "Graveler": lambda: GV.carregar_frames('imagens/gifs/graveler_frames'),
    "Golem": lambda: GV.carregar_frames('imagens/gifs/golem_frames'),
    "Caterpie": lambda: GV.carregar_frames('imagens/gifs/caterpie_frames'),
    "Metapod": lambda: GV.carregar_frames('imagens/gifs/metapod_frames'),
    "Butterfree": lambda: GV.carregar_frames('imagens/gifs/butterfree_frames'),
    "Abra": lambda: GV.carregar_frames('imagens/gifs/abra_frames'),
    "Kadabra": lambda: GV.carregar_frames('imagens/gifs/kadabra_frames'),
    "Alakazam": lambda: GV.carregar_frames('imagens/gifs/alakazam_frames'),
    "Dratini": lambda: GV.carregar_frames('imagens/gifs/dratini_frames'),
    "Dragonair": lambda: GV.carregar_frames('imagens/gifs/dragonair_frames'),
    "Dragonite": lambda: GV.carregar_frames('imagens/gifs/dragonite_frames'),
    "Zorua": lambda: GV.carregar_frames('imagens/gifs/zorua_frames'),
    "Zoroark": lambda: GV.carregar_frames('imagens/gifs/zoroark_frames'),
    "Pikachu": lambda: GV.carregar_frames('imagens/gifs/pikachu_frames'),
    "Raichu": lambda: GV.carregar_frames('imagens/gifs/raichu_frames'),
    "Magikarp": lambda: GV.carregar_frames('imagens/gifs/magikarp_frames'),
    "Gyarados": lambda: GV.carregar_frames('imagens/gifs/gyarados_frames'),
    "Jigglypuff": lambda: GV.carregar_frames('imagens/gifs/jigglypuff_frames'),
    "Wigglytuff": lambda: GV.carregar_frames('imagens/gifs/wigglytuff_frames'),
    "Magnemite": lambda: GV.carregar_frames('imagens/gifs/magnemite_frames'),
    "Magneton": lambda: GV.carregar_frames('imagens/gifs/magneton_frames'),
    "Snorlax": lambda: GV.carregar_frames('imagens/gifs/snorlax_frames'),
    "Aerodactyl": lambda: GV.carregar_frames('imagens/gifs/aerodactyl_frames'),
    "Jynx": lambda: GV.carregar_frames('imagens/gifs/jynx_frames'),
    "Mewtwo": lambda: GV.carregar_frames('imagens/gifs/mewtwo_frames'),
    "Mega Aerodactyl": lambda: GV.carregar_frames('imagens/gifs/aerodactyl-mega_frames'),
    "Mega Alakazam": lambda: GV.carregar_frames('imagens/gifs/alakazam-mega_frames'),
    "Articuno": lambda: GV.carregar_frames('imagens/gifs/articuno_frames'),
    "Beedrill": lambda: GV.carregar_frames('imagens/gifs/beedrill_frames'),
    "Mega Beedrill": lambda: GV.carregar_frames('imagens/gifs/beedrill-mega_frames'),
    "Blastoise Vmax": lambda: GV.carregar_frames('imagens/gifs/blastoise-gigantamax_frames'),
    "Mega Blastoise": lambda: GV.carregar_frames('imagens/gifs/blastoise-mega_frames'),
    "Butterfree Vmax": lambda: GV.carregar_frames('imagens/gifs/butterfree-gigantamax_frames'),
    "Charizard Vmax": lambda: GV.carregar_frames('imagens/gifs/charizard-gigantamax_frames'),
    "Mega Venusaur": lambda: GV.carregar_frames('imagens/gifs/venusaur-mega_frames'),
    "Mega Charizard X": lambda: GV.carregar_frames('imagens/gifs/charizard-megax_frames'),
    "Mega Charizard Y": lambda: GV.carregar_frames('imagens/gifs/charizard-megay_frames'),
    "Clefable": lambda: GV.carregar_frames('imagens/gifs/clefable_frames'),
    "Clefairy": lambda: GV.carregar_frames('imagens/gifs/clefairy_frames'),
    "Cloyster": lambda: GV.carregar_frames('imagens/gifs/cloyster_frames'),
    "Cubone": lambda: GV.carregar_frames('imagens/gifs/cubone_frames'),
    "Gengar Vmax": lambda: GV.carregar_frames('imagens/gifs/gengar-gigantamax_frames'),
    "Mega Gengar": lambda: GV.carregar_frames('imagens/gifs/gengar-mega_frames'),
    "Golem-Alola": lambda: GV.carregar_frames('imagens/gifs/golem-alola_frames'),
    "Mega Gyarados": lambda: GV.carregar_frames('imagens/gifs/gyarados-mega_frames'),
    "Kakuna": lambda: GV.carregar_frames('imagens/gifs/kakuna_frames'),
    "Machamp Vmax": lambda: GV.carregar_frames('imagens/gifs/machamp-gigantamax_frames'),
    "Marowak": lambda: GV.carregar_frames('imagens/gifs/marowak_frames'),
    "Meowth": lambda: GV.carregar_frames('imagens/gifs/meowth_frames'),
    "Meowth Vmax": lambda: GV.carregar_frames('imagens/gifs/meowth-gigantamax_frames'),
    "Mega Mewtwo X": lambda: GV.carregar_frames('imagens/gifs/mewtwo-megax_frames'),
    "Mega Mewtwo Y": lambda: GV.carregar_frames('imagens/gifs/mewtwo-megay_frames'),
    "Moltres": lambda: GV.carregar_frames('imagens/gifs/moltres_frames'),
    "Persian": lambda: GV.carregar_frames('imagens/gifs/persian_frames'),
    "Pikachu Vmax": lambda: GV.carregar_frames('imagens/gifs/pikachu-gigantamax_frames'),
    "Pinsir": lambda: GV.carregar_frames('imagens/gifs/pinsir_frames'),
    "Mega Pinsir": lambda: GV.carregar_frames('imagens/gifs/pinsir-mega_frames'),
    "Raticate": lambda: GV.carregar_frames('imagens/gifs/raticate_frames'),
    "Rattata": lambda: GV.carregar_frames('imagens/gifs/rattata_frames'),
    "Shellder": lambda: GV.carregar_frames('imagens/gifs/shellder_frames'),
    "Snorlax Vmax": lambda: GV.carregar_frames('imagens/gifs/snorlax-gigantamax_frames'),
    "Venusaur Vmax": lambda: GV.carregar_frames('imagens/gifs/venusaur-gigantamax_frames'),
    "Zapdos": lambda: GV.carregar_frames('imagens/gifs/zapdos_frames'),
    "Weedle": lambda: GV.carregar_frames('imagens/gifs/weedle_frames'),
    "Charizard V": lambda: GV.carregar_frames('imagens/gifs/charizard_frames'),
    "Blastoise V": lambda: GV.carregar_frames('imagens/gifs/blastoise_frames'),
    "Venusaur V": lambda: GV.carregar_frames('imagens/gifs/venusaur_frames'),
    "Machamp V": lambda: GV.carregar_frames('imagens/gifs/machamp_frames'),
    "Gengar V": lambda: GV.carregar_frames('imagens/gifs/gengar_frames'),
    "Butterfree V": lambda: GV.carregar_frames('imagens/gifs/butterfree_frames'),
    "Pikachu V": lambda: GV.carregar_frames('imagens/gifs/pikachu_frames'),
    "Meowth V": lambda: GV.carregar_frames('imagens/gifs/meowth_frames'),
    "Snorlax V": lambda: GV.carregar_frames('imagens/gifs/snorlax_frames'),
    "Charizard Vstar": lambda: GV.carregar_frames('imagens/gifs/charizard_frames'),
    "Blastoise Vstar": lambda: GV.carregar_frames('imagens/gifs/blastoise_frames'),
    "Venusaur Vstar": lambda: GV.carregar_frames('imagens/gifs/venusaur_frames'),
    "Machamp Vstar": lambda: GV.carregar_frames('imagens/gifs/machamp_frames'),
    "Gengar Vstar": lambda: GV.carregar_frames('imagens/gifs/gengar_frames'),
    "Butterfree Vstar": lambda: GV.carregar_frames('imagens/gifs/butterfree_frames'),
    "Pikachu Vstar": lambda: GV.carregar_frames('imagens/gifs/pikachu_frames'),
    "Meowth Vstar": lambda: GV.carregar_frames('imagens/gifs/meowth_frames'),
    "Snorlax Vstar": lambda: GV.carregar_frames('imagens/gifs/snorlax_frames')
}

def Carrega_Icone_pokemon(nome,S):
    global Size
    Size = S
    imagem = pokeiconsrecortados[nome]()
    return imagem

def Carrega_Gif_pokemon(nome):
    frames = PokeGifs[nome]()
    return frames

def Carregar_Imagens_Partida(ImagensPokemonIcons,PokeGifs,OutrosIMG,FundosIMG,EfeitosIMG,ImagensPokemonCentro,ImagensItens,TiposEnergiaIMG):

    RegeneraçãoIMG = GV.Carregar_Imagem("imagens/icones/regeneraçao.png", (24, 24), "PNG")
    ConfusoIMG = GV.Carregar_Imagem("imagens/icones/confuso.png", (24, 24), "PNG")
    BloqueadoIMG = GV.Carregar_Imagem("imagens/icones/bloqueado.png", (24, 24), "PNG")
    EnvenenadoIMG = GV.Carregar_Imagem("imagens/icones/envenenado.png", (24, 24), "PNG")
    TóxicoIMG = GV.Carregar_Imagem("imagens/icones/toxico.png", (24, 24), "PNG")
    FragilizadoIMG = GV.Carregar_Imagem("imagens/icones/fragilizado.png", (24, 24), "PNG")
    QuebradoIMG = GV.Carregar_Imagem("imagens/icones/quebrado.png", (24, 24), "PNG")
    CongeladoIMG = GV.Carregar_Imagem("imagens/icones/congelado.png", (24, 24), "PNG")
    QueimadoIMG = GV.Carregar_Imagem("imagens/icones/queimado.png", (24, 24), "PNG")
    ParalisadoIMG = GV.Carregar_Imagem("imagens/icones/paralisado.png", (24, 24), "PNG")
    EncharcadoIMG = GV.Carregar_Imagem("imagens/icones/encharcado.png", (24, 24), "PNG")
    VampiricoIMG = GV.Carregar_Imagem("imagens/icones/vampirico.png", (24, 24), "PNG")
    DescarregadoIMG = GV.Carregar_Imagem("imagens/icones/descarregado.png", (24, 24), "PNG")
    EnfraquecidoIMG = GV.Carregar_Imagem("imagens/icones/enfraquecido.png", (24, 24), "PNG")
    IncapacitadoIMG = GV.Carregar_Imagem("imagens/icones/incapacitado.png", (24, 24), "PNG")
    ImuneIMG = GV.Carregar_Imagem("imagens/icones/imune.png", (24, 24), "PNG")
    PreparadoIMG = GV.Carregar_Imagem("imagens/icones/preparado.png", (24, 24), "PNG")
    ProvocandoIMG = GV.Carregar_Imagem("imagens/icones/provocando.png", (24, 24), "PNG")
    FurtivoIMG = GV.Carregar_Imagem("imagens/icones/furtivo.png", (24, 24), "PNG")
    VoandoIMG = GV.Carregar_Imagem("imagens/icones/voando.png", (24, 24), "PNG")
    OfensivoIMG = GV.Carregar_Imagem("imagens/icones/ofensivo.png", (24, 24), "PNG")
    ReforçadoIMG = GV.Carregar_Imagem("imagens/icones/reforçado.png", (24, 24), "PNG")
    ImortalIMG = GV.Carregar_Imagem("imagens/icones/imortal.png", (24, 24), "PNG")
    RefletirIMG = GV.Carregar_Imagem("imagens/icones/refletir.png", (24, 24), "PNG")
    FocadoIMG = GV.Carregar_Imagem("imagens/icones/focado.png", (24, 24), "PNG")
    VelocistaIMG = GV.Carregar_Imagem("imagens/icones/velocista.png", (24, 24), "PNG")
    EnergizadoIMG = GV.Carregar_Imagem("imagens/icones/energizado.png", (24, 24), "PNG")
    AbençoadoIMG = GV.Carregar_Imagem("imagens/icones/abençoado.png", (24, 24), "PNG")

    Fundo = GV.Carregar_Imagem("imagens/fundos/fundo3.jpg", (1920,1080))
    MerFundo = GV.Carregar_Imagem("imagens/fundos/Mer.jpg", (1920, 1080))
    ShivreFundo = GV.Carregar_Imagem("imagens/fundos/Shivre.png", (1920, 1080))
    KalosFundo = GV.Carregar_Imagem("imagens/fundos/Kalos.jpg", (1920, 1080))
    PortoFundo = GV.Carregar_Imagem("imagens/fundos/Porto.jpg", (1920, 1080))
    SkyloftFundo = GV.Carregar_Imagem("imagens/fundos/Skyloft.jpg", (1920, 1080))
    AuromaFundo = GV.Carregar_Imagem("imagens/fundos/Auroma.jpg", (1920, 1080))

    InventárioIMG = GV.Carregar_Imagem("imagens/icones/inventario.png", (60,60),"PNG")
    energiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (50,50),"PNG")
    CentroIMG = GV.Carregar_Imagem("imagens/icones/centro.png", (70,70),"PNG")
    LojasIMG = GV.Carregar_Imagem("imagens/icones/Loja.png", (50,50),"PNG")
    EstadiosIMG = GV.Carregar_Imagem("imagens/icones/Mapa.png", (55,55),"PNG")
    TreinadorIMG = GV.Carregar_Imagem("imagens/icones/Treinador.png", (50,50),"PNG")
    LojaPokebolasIMG = GV.Carregar_Imagem("imagens/icones/Poke.png", (70,70),"PNG")
    LojaAmplificadoresIMG = GV.Carregar_Imagem("imagens/icones/amplificadores.png", (70,70),"PNG")
    LojaEnergiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (60,60),"PNG")
    LojaEstTreIMG = GV.Carregar_Imagem("imagens/icones/EstTre.png", (70,70),"PNG")
    LojaBloqIMG = GV.Carregar_Imagem("imagens/icones/cadeado.png", (68,68),"PNG")
    AtaqueIMG = GV.Carregar_Imagem("imagens/icones/atacar.png", (40,40),"PNG")
    NocauteIMG  = GV.Carregar_Imagem("imagens/icones/KO.png", (50,50),"PNG")
    GuardadoIMG = GV.Carregar_Imagem("imagens/icones/guardado.png", (40,40),"PNG") 

    Alvo = GV.carregar_frames('imagens/efeitos/Alvo_frames')

    EsmeraldaIMG = GV.Carregar_Imagem("imagens/itens/esmeralda.png", (62, 62), "PNG")
    CitrinoIMG = GV.Carregar_Imagem("imagens/itens/citrino.png", (62, 62), "PNG")
    RubiIMG = GV.Carregar_Imagem("imagens/itens/rubi.png", (62, 62), "PNG")
    SafiraIMG = GV.Carregar_Imagem("imagens/itens/safira.png", (62, 62), "PNG")
    AmetistaIMG = GV.Carregar_Imagem("imagens/itens/ametista.png", (62, 62), "PNG")
    RubelitaIMG = GV.Carregar_Imagem("imagens/itens/rubelita.png", (62, 62), "PNG")
    DiamanteIMG = GV.Carregar_Imagem("imagens/itens/diamante.png", (62, 62), "PNG")
    ColetorIMG = GV.Carregar_Imagem("imagens/itens/coletor.png", (62, 62), "PNG")
    CaixaIMG = GV.Carregar_Imagem("imagens/itens/caixa.png", (62, 62), "PNG")
    CaixoteIMG = GV.Carregar_Imagem("imagens/itens/caixote.png", (62, 62), "PNG")
    PocaoIMG = GV.Carregar_Imagem("imagens/itens/poçao.png", (62, 62), "PNG")
    SuperPocaoIMG = GV.Carregar_Imagem("imagens/itens/super_poçao.png", (62, 62), "PNG")
    HiperPocaoIMG = GV.Carregar_Imagem("imagens/itens/hiper_poçao.png", (62, 62), "PNG")
    MegaPocaoIMG = GV.Carregar_Imagem("imagens/itens/mega_poçao.png", (62, 62), "PNG")
    PokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (62, 62), "PNG")
    GreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (62, 62), "PNG")
    UltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (62, 62), "PNG")
    MasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (62, 62), "PNG")
    FramboIMG = GV.Carregar_Imagem("imagens/itens/frambo.png", (62, 62), "PNG")
    FramboDouradaIMG = GV.Carregar_Imagem("imagens/itens/frambo_dourada.png", (62, 62), "PNG")
    CaxiIMG = GV.Carregar_Imagem("imagens/itens/caxi.png", (62, 62), "PNG")
    CaxiPrateadaIMG = GV.Carregar_Imagem("imagens/itens/caxi_prateada.png", (62, 62), "PNG")
    EstadioIMG = GV.Carregar_Imagem("imagens/itens/TP.png", (62, 62), "PNG")
    MegaIMG = GV.Carregar_Imagem("imagens/itens/mega.png", (62, 62), "PNG")
    VMaxIMG = GV.Carregar_Imagem("imagens/itens/Vmax.png", (62, 62), "PNG")
    VStarIMG = GV.Carregar_Imagem("imagens/itens/VStar.png", (62, 62), "PNG")
    TrocadorAtaqueIMG = GV.Carregar_Imagem("imagens/itens/TrocadorAtaque.png", (62, 62), "PNG")
    RemovedorIMG = GV.Carregar_Imagem("imagens/itens/removedor.png", (62, 62), "PNG")
    CompraEnergia = GV.Carregar_Imagem("imagens/icones/CompraEnergia.png", (28, 28), "PNG")
    UPokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (55,55),"PNG")
    UGreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (55,55),"PNG")
    UUltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (55,55),"PNG")
    UMasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (55,55),"PNG")
    UFramboIMG = GV.Carregar_Imagem("imagens/itens/frambo.png", (48, 48), "PNG")
    UFramboDouradaIMG = GV.Carregar_Imagem("imagens/itens/frambo_dourada.png", (48, 48), "PNG")
    UCaxiIMG = GV.Carregar_Imagem("imagens/itens/caxi.png", (48, 48), "PNG")
    UCaxiPrateadaIMG = GV.Carregar_Imagem("imagens/itens/caxi_prateada.png", (48, 48), "PNG")

    MbulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (88, 88), "PNG")
    McharmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (88, 88), "PNG")
    MsquirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (88, 88), "PNG")
    MmachopIMG = GV.Carregar_Imagem("imagens/pokemons/machop.png", (88, 88), "PNG")
    MgastlyIMG = GV.Carregar_Imagem("imagens/pokemons/gastly.png", (88, 88), "PNG")
    MgeodudeIMG = GV.Carregar_Imagem("imagens/pokemons/geodude.png", (88, 88), "PNG")
    McaterpieIMG = GV.Carregar_Imagem("imagens/pokemons/caterpie.png", (88, 88), "PNG")
    MabreIMG = GV.Carregar_Imagem("imagens/pokemons/abra.png", (88, 88), "PNG")
    MdratiniIMG = GV.Carregar_Imagem("imagens/pokemons/dratini.png", (88, 88), "PNG")
    MzoruaIMG = GV.Carregar_Imagem("imagens/pokemons/zorua.png", (88, 88), "PNG")
    MpikachuIMG = GV.Carregar_Imagem("imagens/pokemons/pikachu.png", (88, 88), "PNG")
    MmagikarpIMG = GV.Carregar_Imagem("imagens/pokemons/magikarp.png", (88, 88), "PNG")
    MjigglypuffIMG = GV.Carregar_Imagem("imagens/pokemons/jigglypuff.png", (88, 88), "PNG")
    MmagnemiteIMG = GV.Carregar_Imagem("imagens/pokemons/magnemite.png", (88, 88), "PNG")
    MsnorlaxIMG = GV.Carregar_Imagem("imagens/pokemons/snorlax.png", (88, 88), "PNG")
    MaerodactylIMG = GV.Carregar_Imagem("imagens/pokemons/aerodactyl.png", (88, 88), "PNG")
    MjynxIMG = GV.Carregar_Imagem("imagens/pokemons/jynx.png", (88, 88), "PNG")
    MmewtwoIMG = GV.Carregar_Imagem("imagens/pokemons/mewtwo.png", (88, 88), "PNG")
    MmeowthIMG = GV.Carregar_Imagem("imagens/pokemons/meowth.png", (88, 88), "PNG")
    McuboneIMG = GV.Carregar_Imagem("imagens/pokemons/cubone.png", (88, 88), "PNG")
    MshellderIMG = GV.Carregar_Imagem("imagens/pokemons/shellder.png", (88, 88), "PNG")
    MarticunoIMG = GV.Carregar_Imagem("imagens/pokemons/articuno.png", (88, 88), "PNG")
    MmoltresIMG = GV.Carregar_Imagem("imagens/pokemons/moltres.png", (88, 88), "PNG")
    MzapdosIMG = GV.Carregar_Imagem("imagens/pokemons/zapdos.png", (88, 88), "PNG")
    MclefairyIMG = GV.Carregar_Imagem("imagens/pokemons/clefairy.png", (88, 88), "PNG")
    MrattataIMG = GV.Carregar_Imagem("imagens/pokemons/rattata.png", (88, 88), "PNG")
    MweedleIMG = GV.Carregar_Imagem("imagens/pokemons/weedle.png", (88, 88), "PNG")
    MpinsirIMG = GV.Carregar_Imagem("imagens/pokemons/pinsir.png", (88, 88), "PNG")

    Efogo = GV.Carregar_Imagem("imagens/icones/fogo.png", (30,30), "PNG")
    Eagua = GV.Carregar_Imagem("imagens/icones/agua.png", (30,30), "PNG")
    Eplanta = GV.Carregar_Imagem("imagens/icones/planta.png", (30,30), "PNG")
    Eeletrico = GV.Carregar_Imagem("imagens/icones/eletrico.png", (30,30), "PNG")
    Epsiquico = GV.Carregar_Imagem("imagens/icones/psiquico.png", (30,30), "PNG")
    Efantasma = GV.Carregar_Imagem("imagens/icones/fantasma.png", (30,30), "PNG")
    Epedra = GV.Carregar_Imagem("imagens/icones/pedra.png", (30,30), "PNG")
    Eterrestre = GV.Carregar_Imagem("imagens/icones/terrestre.png", (30,30), "PNG")
    Evoador = GV.Carregar_Imagem("imagens/icones/voador.png", (30,30), "PNG")
    Enormal = GV.Carregar_Imagem("imagens/icones/normal.png", (30,30), "PNG")
    Evenenoso = GV.Carregar_Imagem("imagens/icones/venenoso.png", (30,30), "PNG")
    Einseto = GV.Carregar_Imagem("imagens/icones/inseto.png", (30,30), "PNG")
    Elutador = GV.Carregar_Imagem("imagens/icones/lutador.png", (30,30), "PNG")
    Edragao = GV.Carregar_Imagem("imagens/icones/dragao.png", (30,30), "PNG")
    Egelo = GV.Carregar_Imagem("imagens/icones/gelo.png", (30,30), "PNG")
    Efada = GV.Carregar_Imagem("imagens/icones/fada.png", (30,30), "PNG")
    Emetal = GV.Carregar_Imagem("imagens/icones/metal.png", (30,30), "PNG")
    Esombrio = GV.Carregar_Imagem("imagens/icones/sombrio.png", (30,30), "PNG")

    TiposEnergiaIMG = {
    "fogo": Efogo,
    "agua": Eagua,
    "planta": Eplanta,
    "eletrico": Eeletrico,
    "psiquico": Epsiquico,
    "fantasma": Efantasma,
    "pedra": Epedra,
    "terrestre": Eterrestre,
    "voador": Evoador,
    "normal": Enormal,
    "venenoso": Evenenoso,
    "inseto": Einseto,
    "lutador": Elutador,
    "dragao": Edragao,
    "gelo": Egelo,
    "fada": Efada,
    "metal": Emetal,
    "sombrio": Esombrio
}
    
    ImagensItens = {
    "Esmeralda": EsmeraldaIMG,
    "Citrino": CitrinoIMG,
    "Rubi": RubiIMG,
    "Safira": SafiraIMG,
    "Ametista": AmetistaIMG,
    "Rubelita": RubelitaIMG,
    "Diamante": DiamanteIMG,
    "Coletor": ColetorIMG,
    "Caixa": CaixaIMG,
    "Caixote": CaixoteIMG,
    "Poção": PocaoIMG,
    "Super Poção": SuperPocaoIMG,
    "Hiper Poção": HiperPocaoIMG,
    "Mega Poção": MegaPocaoIMG,
    "Pokebola": PokeballIMG,
    "Greatball": GreatBallIMG,
    "Ultraball": UltraBallIMG,
    "Masterball": MasterBallIMG,
    "Fruta Frambo": FramboIMG,
    "Fruta Frambo Dourada": FramboDouradaIMG,
    "Fruta Caxi": CaxiIMG,
    "Fruta Caxi Prateada": CaxiPrateadaIMG,
    "Energia Mega": MegaIMG,
    "Energia Vstar": VStarIMG,
    "Energia GigantaMax": VMaxIMG,
    "Trocador de Ataque": TrocadorAtaqueIMG,
    "Removedor": RemovedorIMG,
    "Estádio Mer": EstadioIMG,
    "Cidade Shivre": EstadioIMG,
    "Parque Auroma": EstadioIMG,
    "Estádio Kalos": EstadioIMG,
    "Skyloft": EstadioIMG,
    "Porto Molgera": EstadioIMG,
    "CompraEnergia": CompraEnergia,
    "Pokebola": UPokeballIMG,
    "Greatball": UGreatBallIMG,
    "Ultraball": UUltraBallIMG,
    "Masterball": UMasterBallIMG,
    "Fruta Frambo": UFramboIMG,
    "Fruta Frambo Dourada": UFramboDouradaIMG,
    "Fruta Caxi": UCaxiIMG,
    "Fruta Caxi Prateada": UCaxiPrateadaIMG}

    ImagensPokemonCentro = {
    "Bulbasaur": MbulbasaurIMG,
    "Charmander": McharmanderIMG,
    "Squirtle": MsquirtleIMG,
    "Machop": MmachopIMG,
    "Gastly": MgastlyIMG,
    "Geodude": MgeodudeIMG,
    "Caterpie": McaterpieIMG,
    "Abra": MabreIMG,
    "Dratini": MdratiniIMG,
    "Zorua": MzoruaIMG,
    "Pikachu": MpikachuIMG,
    "Magikarp": MmagikarpIMG,
    "Jigglypuff": MjigglypuffIMG,
    "Magnemite": MmagnemiteIMG,
    "Snorlax": MsnorlaxIMG,
    "Aerodactyl": MaerodactylIMG,
    "Jynx": MjynxIMG,
    "Mewtwo": MmewtwoIMG,
    "Meowth": MmeowthIMG,
    "Cubone": McuboneIMG,
    "Shellder": MshellderIMG,
    "Articuno": MarticunoIMG,
    "Moltres": MmoltresIMG,
    "Zapdos": MzapdosIMG,
    "Clefairy": MclefairyIMG,
    "Rattata": MrattataIMG,
    "Weedle": MweedleIMG,
    "Pinsir": MpinsirIMG
}

    EfeitosIMG = {
    "Confuso": ConfusoIMG,
    "Bloqueado": BloqueadoIMG,
    "Envenenado": EnvenenadoIMG,
    "Tóxico": TóxicoIMG,
    "Fragilizado": FragilizadoIMG,
    "Quebrado": QuebradoIMG,
    "Congelado": CongeladoIMG,
    "Queimado": QueimadoIMG,
    "Paralisado": ParalisadoIMG,
    "Encharcado": EncharcadoIMG,
    "Vampirico": VampiricoIMG,
    "Descarregado": DescarregadoIMG,
    "Enfraquecido": EnfraquecidoIMG,
    "Incapacitado": IncapacitadoIMG,
    "Regeneração": RegeneraçãoIMG,
    "Abençoado": AbençoadoIMG,
    "Imune": ImuneIMG,
    "Preparado": PreparadoIMG,
    "Provocando": ProvocandoIMG,
    "Furtivo": FurtivoIMG,
    "Voando": VoandoIMG,
    "Ofensivo": OfensivoIMG,
    "Reforçado": ReforçadoIMG,
    "Imortal": ImortalIMG,
    "Refletir": RefletirIMG,
    "Focado": FocadoIMG,
    "Velocista": VelocistaIMG,
    "Energizado": EnergizadoIMG
    }

    OutrosIMG = [InventárioIMG,energiasIMG,CentroIMG,EstadiosIMG,LojaPokebolasIMG,LojaAmplificadoresIMG,LojaEnergiasIMG,AtaqueIMG,NocauteIMG,LojaEstTreIMG,LojaBloqIMG,GuardadoIMG,LojasIMG,TreinadorIMG,Alvo]

    FundosIMG = [Fundo,MerFundo,ShivreFundo,AuromaFundo,KalosFundo,SkyloftFundo,PortoFundo]

    return ImagensPokemonIcons,PokeGifs,OutrosIMG,FundosIMG,EfeitosIMG,ImagensPokemonCentro,ImagensItens,TiposEnergiaIMG

def Carregar_Imagens_Decks(ImagensItens,ImagensPokemonCentro,TiposEnergiaIMG,DeckIconesIMG,ImagensTreinadores):
    
    EsmeraldaIMG = GV.Carregar_Imagem("imagens/itens/esmeralda.png", (79, 79), "PNG")
    CitrinoIMG = GV.Carregar_Imagem("imagens/itens/citrino.png", (79, 79), "PNG")
    RubiIMG = GV.Carregar_Imagem("imagens/itens/rubi.png", (79, 79), "PNG")
    SafiraIMG = GV.Carregar_Imagem("imagens/itens/safira.png", (79, 79), "PNG")
    AmetistaIMG = GV.Carregar_Imagem("imagens/itens/ametista.png", (79, 79), "PNG")
    RubelitaIMG = GV.Carregar_Imagem("imagens/itens/rubelita.png", (79, 79), "PNG")
    DiamanteIMG = GV.Carregar_Imagem("imagens/itens/diamante.png", (79, 79), "PNG")
    ColetorIMG = GV.Carregar_Imagem("imagens/itens/coletor.png", (79, 79), "PNG")
    CaixaIMG = GV.Carregar_Imagem("imagens/itens/caixa.png", (79, 79), "PNG")
    CaixoteIMG = GV.Carregar_Imagem("imagens/itens/caixote.png", (79, 79), "PNG")
    PocaoIMG = GV.Carregar_Imagem("imagens/itens/poçao.png", (79, 79), "PNG")
    SuperPocaoIMG = GV.Carregar_Imagem("imagens/itens/super_poçao.png", (79, 79), "PNG")
    HiperPocaoIMG = GV.Carregar_Imagem("imagens/itens/hiper_poçao.png", (79, 79), "PNG")
    MegaPocaoIMG = GV.Carregar_Imagem("imagens/itens/mega_poçao.png", (79, 79), "PNG")
    PokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (79, 79), "PNG")
    GreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (79, 79), "PNG")
    UltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (79, 79), "PNG")
    MasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (79, 79), "PNG")
    FramboIMG = GV.Carregar_Imagem("imagens/itens/frambo.png", (79, 79), "PNG")
    FramboDouradaIMG = GV.Carregar_Imagem("imagens/itens/frambo_dourada.png", (79, 79), "PNG")
    CaxiIMG = GV.Carregar_Imagem("imagens/itens/caxi.png", (79, 79), "PNG")
    CaxiPrateadaIMG = GV.Carregar_Imagem("imagens/itens/caxi_prateada.png", (79, 79), "PNG")
    EstadioIMG = GV.Carregar_Imagem("imagens/itens/TP.png", (79, 79), "PNG")
    MegaIMG = GV.Carregar_Imagem("imagens/itens/mega.png", (79, 79), "PNG")
    VMaxIMG = GV.Carregar_Imagem("imagens/itens/Vmax.png", (79, 79), "PNG")
    VStarIMG = GV.Carregar_Imagem("imagens/itens/VStar.png", (79, 79), "PNG")
    TrocadorAtaqueIMG = GV.Carregar_Imagem("imagens/itens/TrocadorAtaque.png", (79, 79), "PNG")
    RemovedorIMG = GV.Carregar_Imagem("imagens/itens/removedor.png", (79, 79), "PNG")
    UPokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (79,79),"PNG")
    UGreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (79,79),"PNG")
    UUltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (79,79),"PNG")
    UMasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (79,79),"PNG")
    UFramboIMG = GV.Carregar_Imagem("imagens/itens/frambo.png", (79, 79), "PNG")
    UFramboDouradaIMG = GV.Carregar_Imagem("imagens/itens/frambo_dourada.png", (79, 79), "PNG")
    UCaxiIMG = GV.Carregar_Imagem("imagens/itens/caxi.png", (79, 79), "PNG")
    UCaxiPrateadaIMG = GV.Carregar_Imagem("imagens/itens/caxi_prateada.png", (79, 79), "PNG")

    MbulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (128, 128), "PNG")
    McharmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (128, 128), "PNG")
    MsquirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (128, 128), "PNG")
    MmachopIMG = GV.Carregar_Imagem("imagens/pokemons/machop.png", (128, 128), "PNG")
    MgastlyIMG = GV.Carregar_Imagem("imagens/pokemons/gastly.png", (128, 128), "PNG")
    MgeodudeIMG = GV.Carregar_Imagem("imagens/pokemons/geodude.png", (128, 128), "PNG")
    McaterpieIMG = GV.Carregar_Imagem("imagens/pokemons/caterpie.png", (128, 128), "PNG")
    MabreIMG = GV.Carregar_Imagem("imagens/pokemons/abra.png", (128, 128), "PNG")
    MdratiniIMG = GV.Carregar_Imagem("imagens/pokemons/dratini.png", (128, 128), "PNG")
    MzoruaIMG = GV.Carregar_Imagem("imagens/pokemons/zorua.png", (128, 128), "PNG")
    MpikachuIMG = GV.Carregar_Imagem("imagens/pokemons/pikachu.png", (128, 128), "PNG")
    MmagikarpIMG = GV.Carregar_Imagem("imagens/pokemons/magikarp.png", (128, 128), "PNG")
    MjigglypuffIMG = GV.Carregar_Imagem("imagens/pokemons/jigglypuff.png", (128, 128), "PNG")
    MmagnemiteIMG = GV.Carregar_Imagem("imagens/pokemons/magnemite.png", (128, 128), "PNG")
    MsnorlaxIMG = GV.Carregar_Imagem("imagens/pokemons/snorlax.png", (128, 128), "PNG")
    MaerodactylIMG = GV.Carregar_Imagem("imagens/pokemons/aerodactyl.png", (128, 128), "PNG")
    MjynxIMG = GV.Carregar_Imagem("imagens/pokemons/jynx.png", (128, 128), "PNG")
    MmewtwoIMG = GV.Carregar_Imagem("imagens/pokemons/mewtwo.png", (128, 128), "PNG")
    MmeowthIMG = GV.Carregar_Imagem("imagens/pokemons/meowth.png", (128, 128), "PNG")
    McuboneIMG = GV.Carregar_Imagem("imagens/pokemons/cubone.png", (128, 128), "PNG")
    MshellderIMG = GV.Carregar_Imagem("imagens/pokemons/shellder.png", (128, 128), "PNG")
    MarticunoIMG = GV.Carregar_Imagem("imagens/pokemons/articuno.png", (128, 128), "PNG")
    MmoltresIMG = GV.Carregar_Imagem("imagens/pokemons/moltres.png", (128, 128), "PNG")
    MzapdosIMG = GV.Carregar_Imagem("imagens/pokemons/zapdos.png", (128, 128), "PNG")
    MclefairyIMG = GV.Carregar_Imagem("imagens/pokemons/clefairy.png", (128, 128), "PNG")
    MrattataIMG = GV.Carregar_Imagem("imagens/pokemons/rattata.png", (128, 128), "PNG")
    MweedleIMG = GV.Carregar_Imagem("imagens/pokemons/weedle.png", (128, 128), "PNG")
    MpinsirIMG = GV.Carregar_Imagem("imagens/pokemons/pinsir.png", (128, 128), "PNG")

    Efogo = GV.Carregar_Imagem("imagens/icones/fogo.png", (30,30), "PNG")
    Eagua = GV.Carregar_Imagem("imagens/icones/agua.png", (30,30), "PNG")
    Eplanta = GV.Carregar_Imagem("imagens/icones/planta.png", (30,30), "PNG")
    Eeletrico = GV.Carregar_Imagem("imagens/icones/eletrico.png", (30,30), "PNG")
    Epsiquico = GV.Carregar_Imagem("imagens/icones/psiquico.png", (30,30), "PNG")
    Efantasma = GV.Carregar_Imagem("imagens/icones/fantasma.png", (30,30), "PNG")
    Epedra = GV.Carregar_Imagem("imagens/icones/pedra.png", (30,30), "PNG")
    Eterrestre = GV.Carregar_Imagem("imagens/icones/terrestre.png", (30,30), "PNG")
    Evoador = GV.Carregar_Imagem("imagens/icones/voador.png", (30,30), "PNG")
    Enormal = GV.Carregar_Imagem("imagens/icones/normal.png", (30,30), "PNG")
    Evenenoso = GV.Carregar_Imagem("imagens/icones/venenoso.png", (30,30), "PNG")
    Einseto = GV.Carregar_Imagem("imagens/icones/inseto.png", (30,30), "PNG")
    Elutador = GV.Carregar_Imagem("imagens/icones/lutador.png", (30,30), "PNG")
    Edragao = GV.Carregar_Imagem("imagens/icones/dragao.png", (30,30), "PNG")
    Egelo = GV.Carregar_Imagem("imagens/icones/gelo.png", (30,30), "PNG")
    Efada = GV.Carregar_Imagem("imagens/icones/fada.png", (30,30), "PNG")
    Emetal = GV.Carregar_Imagem("imagens/icones/metal.png", (30,30), "PNG")
    Esombrio = GV.Carregar_Imagem("imagens/icones/sombrio.png", (30,30), "PNG")

    Icon1 = GV.Carregar_Imagem("imagens/Deck_icones/icon1.png", (80, 80), "PNG")
    Icon2 = GV.Carregar_Imagem("imagens/Deck_icones/icon2.png", (80, 80), "PNG")
    Icon3 = GV.Carregar_Imagem("imagens/Deck_icones/icon3.png", (80, 80), "PNG")
    Icon4 = GV.Carregar_Imagem("imagens/Deck_icones/icon4.png", (80, 80), "PNG")
    Icon5 = GV.Carregar_Imagem("imagens/Deck_icones/icon5.png", (80, 80), "PNG")
    Icon6 = GV.Carregar_Imagem("imagens/Deck_icones/icon6.png", (80, 80), "PNG")
    Icon7 = GV.Carregar_Imagem("imagens/Deck_icones/icon7.png", (80, 80), "PNG")
    Icon8 = GV.Carregar_Imagem("imagens/Deck_icones/icon8.png", (80, 80), "PNG")

    AshIMG = GV.Carregar_Imagem("imagens/Treinadores/Ash.png", (230, 160), "PNG")
    BrockIMG = GV.Carregar_Imagem("imagens/Treinadores/Brock.png", (230, 160), "PNG")
    MistyIMG = GV.Carregar_Imagem("imagens/Treinadores/Misty.png", (230, 160), "PNG")
    GiovanniIMG = GV.Carregar_Imagem("imagens/Treinadores/Giovanni.png", (230, 160), "PNG")
    JessieIMG = GV.Carregar_Imagem("imagens/Treinadores/Jessie.png", (230, 160), "PNG")
    JamesIMG = GV.Carregar_Imagem("imagens/Treinadores/James.png", (230, 160), "PNG")
    CarvalhoIMG = GV.Carregar_Imagem("imagens/Treinadores/Carvalho.png", (230, 160), "PNG")
    RedIMG = GV.Carregar_Imagem("imagens/Treinadores/Red.png", (230, 160), "PNG")

    ImagensTreinadores = {
        "Ash": AshIMG,
        "Brock": BrockIMG,
        "Misty": MistyIMG,
        "Giovanni": GiovanniIMG,
        "Jessie": JessieIMG,
        "James": JamesIMG,
        "Professor Carvalho": CarvalhoIMG,
        "Red": RedIMG,
}

    DeckIconesIMG = {
    "icone1": Icon1,
    "icone2": Icon2,
    "icone3": Icon3,
    "icone4": Icon4,
    "icone5": Icon5,
    "icone6": Icon6,
    "icone7": Icon7,
    "icone8": Icon8,
}

    TiposEnergiaIMG = {
    "fogo": Efogo,
    "agua": Eagua,
    "planta": Eplanta,
    "eletrico": Eeletrico,
    "psiquico": Epsiquico,
    "fantasma": Efantasma,
    "pedra": Epedra,
    "terrestre": Eterrestre,
    "voador": Evoador,
    "normal": Enormal,
    "venenoso": Evenenoso,
    "inseto": Einseto,
    "lutador": Elutador,
    "dragao": Edragao,
    "gelo": Egelo,
    "fada": Efada,
    "metal": Emetal,
    "sombrio": Esombrio
}
    
    ImagensItens = {
    "Esmeralda": EsmeraldaIMG,
    "Citrino": CitrinoIMG,
    "Rubi": RubiIMG,
    "Safira": SafiraIMG,
    "Ametista": AmetistaIMG,
    "Rubelita": RubelitaIMG,
    "Diamante": DiamanteIMG,
    "Coletor": ColetorIMG,
    "Caixa": CaixaIMG,
    "Caixote": CaixoteIMG,
    "Poção": PocaoIMG,
    "Super Poção": SuperPocaoIMG,
    "Hiper Poção": HiperPocaoIMG,
    "Mega Poção": MegaPocaoIMG,
    "Pokebola": PokeballIMG,
    "Greatball": GreatBallIMG,
    "Ultraball": UltraBallIMG,
    "Masterball": MasterBallIMG,
    "Fruta Frambo": FramboIMG,
    "Fruta Frambo Dourada": FramboDouradaIMG,
    "Fruta Caxi": CaxiIMG,
    "Fruta Caxi Prateada": CaxiPrateadaIMG,
    "Energia Mega": MegaIMG,
    "Energia Vstar": VStarIMG,
    "Energia GigantaMax": VMaxIMG,
    "Trocador de Ataque": TrocadorAtaqueIMG,
    "Removedor": RemovedorIMG,
    "Estádio Mer": EstadioIMG,
    "Cidade Shivre": EstadioIMG,
    "Parque Auroma": EstadioIMG,
    "Estádio Kalos": EstadioIMG,
    "Skyloft": EstadioIMG,
    "Porto Molgera": EstadioIMG,
    "Pokebola": UPokeballIMG,
    "Greatball": UGreatBallIMG,
    "Ultraball": UUltraBallIMG,
    "Masterball": UMasterBallIMG,
    "Fruta Frambo": UFramboIMG,
    "Fruta Frambo Dourada": UFramboDouradaIMG,
    "Fruta Caxi": UCaxiIMG,
    "Fruta Caxi Prateada": UCaxiPrateadaIMG}

    ImagensPokemonCentro = {
    "Bulbasaur": MbulbasaurIMG,
    "Charmander": McharmanderIMG,
    "Squirtle": MsquirtleIMG,
    "Machop": MmachopIMG,
    "Gastly": MgastlyIMG,
    "Geodude": MgeodudeIMG,
    "Caterpie": McaterpieIMG,
    "Abra": MabreIMG,
    "Dratini": MdratiniIMG,
    "Zorua": MzoruaIMG,
    "Pikachu": MpikachuIMG,
    "Magikarp": MmagikarpIMG,
    "Jigglypuff": MjigglypuffIMG,
    "Magnemite": MmagnemiteIMG,
    "Snorlax": MsnorlaxIMG,
    "Aerodactyl": MaerodactylIMG,
    "Jynx": MjynxIMG,
    "Mewtwo": MmewtwoIMG,
    "Meowth": MmeowthIMG,
    "Cubone": McuboneIMG,
    "Shellder": MshellderIMG,
    "Articuno": MarticunoIMG,
    "Moltres": MmoltresIMG,
    "Zapdos": MzapdosIMG,
    "Clefairy": MclefairyIMG,
    "Rattata": MrattataIMG,
    "Weedle": MweedleIMG,
    "Pinsir": MpinsirIMG
}

    return ImagensItens,ImagensPokemonCentro, TiposEnergiaIMG, DeckIconesIMG, ImagensTreinadores

def Carregar_Imagens_Pré_Partida(ImagensPokemonInicial,IconesDeckIMG):

    MbulbasaurIMG = GV.Carregar_Imagem("imagens/pokemons/bulbasaur.png", (235, 235), "PNG")
    McharmanderIMG = GV.Carregar_Imagem("imagens/pokemons/charmander.png", (235, 235), "PNG")
    MsquirtleIMG = GV.Carregar_Imagem("imagens/pokemons/squirtle.png", (235, 235), "PNG")
    MmachopIMG = GV.Carregar_Imagem("imagens/pokemons/machop.png", (235, 235), "PNG")
    MgastlyIMG = GV.Carregar_Imagem("imagens/pokemons/gastly.png", (235, 235), "PNG")
    MgeodudeIMG = GV.Carregar_Imagem("imagens/pokemons/geodude.png", (235, 235), "PNG")
    McaterpieIMG = GV.Carregar_Imagem("imagens/pokemons/caterpie.png", (235, 235), "PNG")
    MmagikarpIMG = GV.Carregar_Imagem("imagens/pokemons/magikarp.png", (235, 235), "PNG")
    MjigglypuffIMG = GV.Carregar_Imagem("imagens/pokemons/jigglypuff.png", (235, 235), "PNG")
    MmagnemiteIMG = GV.Carregar_Imagem("imagens/pokemons/magnemite.png", (235, 235), "PNG")
    MmeowthIMG = GV.Carregar_Imagem("imagens/pokemons/meowth.png", (235, 235), "PNG")
    McuboneIMG = GV.Carregar_Imagem("imagens/pokemons/cubone.png", (235, 235), "PNG")
    MclefairyIMG = GV.Carregar_Imagem("imagens/pokemons/clefairy.png", (235, 235), "PNG")
    MrattataIMG = GV.Carregar_Imagem("imagens/pokemons/rattata.png", (235, 235), "PNG")
    MweedleIMG = GV.Carregar_Imagem("imagens/pokemons/weedle.png", (235, 235), "PNG")

    Icon1 = GV.Carregar_Imagem("imagens/Deck_icones/icon1.png", (80, 80), "PNG")
    Icon2 = GV.Carregar_Imagem("imagens/Deck_icones/icon2.png", (80, 80), "PNG")
    Icon3 = GV.Carregar_Imagem("imagens/Deck_icones/icon3.png", (80, 80), "PNG")
    Icon4 = GV.Carregar_Imagem("imagens/Deck_icones/icon4.png", (80, 80), "PNG")
    Icon5 = GV.Carregar_Imagem("imagens/Deck_icones/icon5.png", (80, 80), "PNG")
    Icon6 = GV.Carregar_Imagem("imagens/Deck_icones/icon6.png", (80, 80), "PNG")
    Icon7 = GV.Carregar_Imagem("imagens/Deck_icones/icon7.png", (80, 80), "PNG")
    Icon8 = GV.Carregar_Imagem("imagens/Deck_icones/icon8.png", (80, 80), "PNG")

    ImagensPokemonInicial = {
    "Bulbasaur": MbulbasaurIMG,
    "Charmander": McharmanderIMG,
    "Squirtle": MsquirtleIMG,
    "Machop": MmachopIMG,
    "Gastly": MgastlyIMG,
    "Geodude": MgeodudeIMG,
    "Caterpie": McaterpieIMG,
    "Magikarp": MmagikarpIMG,
    "Jigglypuff": MjigglypuffIMG,
    "Magnemite": MmagnemiteIMG,
    "Meowth": MmeowthIMG,
    "Cubone": McuboneIMG,
    "Clefairy": MclefairyIMG,
    "Rattata": MrattataIMG,
    "Weedle": MweedleIMG,
}
    
    DeckIconesIMG = {
    "icone1": Icon1,
    "icone2": Icon2,
    "icone3": Icon3,
    "icone4": Icon4,
    "icone5": Icon5,
    "icone6": Icon6,
    "icone7": Icon7,
    "icone8": Icon8,
}
    
    return ImagensPokemonInicial, DeckIconesIMG
