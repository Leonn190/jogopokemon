import GeradoresVisuais as GV

def Carregar_Imagens(ImagensPokemonIcons,ImagensPokemonCentro,PokeGifs,ImagensCaptura,ImagensItens,OutrosIMG,FundosIMG,TiposEnergiaIMG,EfeitosIMG):


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

    Gbulbasaur = GV.carregar_frames('imagens/gifs/bulbasaur_frames')
    Givysaur = GV.carregar_frames('imagens/gifs/ivysaur_frames')
    Gvenusaur = GV.carregar_frames('imagens/gifs/venusaur_frames')
    Gcharmander = GV.carregar_frames('imagens/gifs/charmander_frames')
    Gcharmeleon = GV.carregar_frames('imagens/gifs/charmeleon_frames')
    Gcharizard = GV.carregar_frames('imagens/gifs/charizard_frames')
    Gsquirtle = GV.carregar_frames('imagens/gifs/squirtle_frames')
    Gwartortle = GV.carregar_frames('imagens/gifs/wartortle_frames')
    Gblastoise = GV.carregar_frames('imagens/gifs/blastoise_frames')
    Gmachop = GV.carregar_frames('imagens/gifs/machop_frames')
    Gmachoke = GV.carregar_frames('imagens/gifs/machoke_frames')
    Gmachamp = GV.carregar_frames('imagens/gifs/machamp_frames')
    Ggastly = GV.carregar_frames('imagens/gifs/gastly_frames')
    Ghaunter = GV.carregar_frames('imagens/gifs/haunter_frames')
    Ggengar = GV.carregar_frames('imagens/gifs/gengar_frames')
    Ggeodude = GV.carregar_frames('imagens/gifs/geodude_frames')
    Ggraveler = GV.carregar_frames('imagens/gifs/graveler_frames')
    Ggolem = GV.carregar_frames('imagens/gifs/golem_frames')
    Gcaterpie = GV.carregar_frames('imagens/gifs/caterpie_frames')
    Gmetapod = GV.carregar_frames('imagens/gifs/metapod_frames')
    Gbutterfree = GV.carregar_frames('imagens/gifs/butterfree_frames')
    Gabra = GV.carregar_frames('imagens/gifs/abra_frames')
    Gkadabra = GV.carregar_frames('imagens/gifs/kadabra_frames')
    Galakazam = GV.carregar_frames('imagens/gifs/alakazam_frames')
    Gdratini = GV.carregar_frames('imagens/gifs/dratini_frames')
    Gdragonair = GV.carregar_frames('imagens/gifs/dragonair_frames')
    Gdragonite = GV.carregar_frames('imagens/gifs/dragonite_frames')
    Gzorua = GV.carregar_frames('imagens/gifs/zorua_frames')
    Gzoroark = GV.carregar_frames('imagens/gifs/zoroark_frames')
    Gpikachu = GV.carregar_frames('imagens/gifs/pikachu_frames')
    Graichu = GV.carregar_frames('imagens/gifs/raichu_frames')
    Gmagikarp = GV.carregar_frames('imagens/gifs/magikarp_frames')
    Ggyarados = GV.carregar_frames('imagens/gifs/gyarados_frames')
    Gjigglypuff = GV.carregar_frames('imagens/gifs/jigglypuff_frames')
    Gwigglytuff = GV.carregar_frames('imagens/gifs/wigglytuff_frames')
    Gmagnemite = GV.carregar_frames('imagens/gifs/magnemite_frames')
    Gmagneton = GV.carregar_frames('imagens/gifs/magneton_frames')
    Gsnorlax = GV.carregar_frames('imagens/gifs/snorlax_frames')
    Gaerodactyl = GV.carregar_frames('imagens/gifs/aerodactyl_frames')
    Gjynx = GV.carregar_frames('imagens/gifs/jynx_frames')
    Gmewtwo = GV.carregar_frames('imagens/gifs/mewtwo_frames')
    Gmewtwo = GV.carregar_frames('imagens/gifs/mewtwo_frames')
    Gaerodactyl_mega = GV.carregar_frames('imagens/gifs/aerodactyl-mega_frames')
    Galakazam_mega = GV.carregar_frames('imagens/gifs/alakazam-mega_frames')
    Garticuno = GV.carregar_frames('imagens/gifs/articuno_frames')
    Gbeedrill = GV.carregar_frames('imagens/gifs/beedrill_frames')
    Gbeedrill_mega = GV.carregar_frames('imagens/gifs/beedrill-mega_frames')
    Gblastoise_gigantamax = GV.carregar_frames('imagens/gifs/blastoise-gigantamax_frames')
    Gblastoise_mega = GV.carregar_frames('imagens/gifs/blastoise-mega_frames')
    Gbutterfree_gmax = GV.carregar_frames('imagens/gifs/butterfree-gigantamax_frames')
    Gcharizard_gmax = GV.carregar_frames('imagens/gifs/charizard-gigantamax_frames')
    Gcharizard_megax = GV.carregar_frames('imagens/gifs/charizard-megax_frames')
    Gcharizard_megay = GV.carregar_frames('imagens/gifs/charizard-megay_frames')
    Gclefable = GV.carregar_frames('imagens/gifs/clefable_frames')
    Gclefairy = GV.carregar_frames('imagens/gifs/clefairy_frames')
    Gcloyster = GV.carregar_frames('imagens/gifs/cloyster_frames')
    Gcubone = GV.carregar_frames('imagens/gifs/cubone_frames')
    Ggengar_gigantamax = GV.carregar_frames('imagens/gifs/gengar-gigantamax_frames')
    Ggengar_mega = GV.carregar_frames('imagens/gifs/gengar-mega_frames')
    Ggolem_alola = GV.carregar_frames('imagens/gifs/golem-mega_frames')
    Ggyarados_mega = GV.carregar_frames('imagens/gifs/gyarados-mega_frames')
    Gweedle = GV.carregar_frames('imagens/gifs/weedle_frames')
    Gkakuna = GV.carregar_frames('imagens/gifs/kakuna_frames')
    Gmachamp_gigantamax = GV.carregar_frames('imagens/gifs/machamp-gigantamax_frames')
    Gmarowak = GV.carregar_frames('imagens/gifs/marowak_frames')
    Gmeowth = GV.carregar_frames('imagens/gifs/meowth_frames')
    Gmeowth_gigantamax = GV.carregar_frames('imagens/gifs/meowth-gigantamax_frames')
    Gmewtwo_megax = GV.carregar_frames('imagens/gifs/mewtwo-megax_frames')
    Gmewtwo_megay = GV.carregar_frames('imagens/gifs/mewtwo-megay_frames')
    Gmoltres = GV.carregar_frames('imagens/gifs/moltres_frames')
    Gzapdos = GV.carregar_frames('imagens/gifs/zapdos_frames')
    Gpersian = GV.carregar_frames('imagens/gifs/persian_frames')
    Gpikachu_gigantamax = GV.carregar_frames('imagens/gifs/pikachu-gigantamax_frames')
    Gpinsir = GV.carregar_frames('imagens/gifs/pinsir_frames')
    Gpinsir_mega = GV.carregar_frames('imagens/gifs/pinsir-mega_frames')
    Graticate = GV.carregar_frames('imagens/gifs/raticate_frames')
    Grattata = GV.carregar_frames('imagens/gifs/rattata_frames')
    Gshellder = GV.carregar_frames('imagens/gifs/shellder_frames')
    Gsnorlax_gigantamax = GV.carregar_frames('imagens/gifs/snorlax-gigantamax_frames')
    Gvenusaur_gigantamax = GV.carregar_frames('imagens/gifs/venusaur-gigantamax_frames')

    IbulbasaurIMG = GV.Carregar_Imagem("imagens/pokeicons/bulbasaur.png", (41,41), "PNG")
    IivysaurIMG = GV.Carregar_Imagem("imagens/pokeicons/ivysaur.png", (41,41), "PNG")
    IvenusaurIMG = GV.Carregar_Imagem("imagens/pokeicons/venusaur.png", (41,41), "PNG")
    IcharmanderIMG = GV.Carregar_Imagem("imagens/pokeicons/charmander.png", (41,41), "PNG")
    IcharmeleonIMG = GV.Carregar_Imagem("imagens/pokeicons/charmeleon.png", (41,41), "PNG")
    IcharizardIMG = GV.Carregar_Imagem("imagens/pokeicons/charizard.png", (41,41), "PNG")
    IsquirtleIMG = GV.Carregar_Imagem("imagens/pokeicons/squirtle.png", (41,41), "PNG")
    IwartortleIMG = GV.Carregar_Imagem("imagens/pokeicons/wartortle.png", (41,41), "PNG")
    IblastoiseIMG = GV.Carregar_Imagem("imagens/pokeicons/blastoise.png", (41,41), "PNG")
    ImachopIMG = GV.Carregar_Imagem("imagens/pokeicons/machop.png", (41,41), "PNG")
    ImachokeIMG = GV.Carregar_Imagem("imagens/pokeicons/machoke.png", (41,41), "PNG")
    ImachampIMG = GV.Carregar_Imagem("imagens/pokeicons/machamp.png", (41,41), "PNG")
    IgastlyIMG = GV.Carregar_Imagem("imagens/pokeicons/gastly.png", (41,41), "PNG")
    IhaunterIMG = GV.Carregar_Imagem("imagens/pokeicons/haunter.png", (41,41), "PNG")
    IgengarIMG = GV.Carregar_Imagem("imagens/pokeicons/gengar.png", (41,41), "PNG")
    IgeodudeIMG = GV.Carregar_Imagem("imagens/pokeicons/geodude.png", (41,41), "PNG")
    IgravelerIMG = GV.Carregar_Imagem("imagens/pokeicons/graveler.png", (41,41), "PNG")
    IgolemIMG = GV.Carregar_Imagem("imagens/pokeicons/golem.png", (41,41), "PNG")
    IcaterpieIMG = GV.Carregar_Imagem("imagens/pokeicons/caterpie.png", (41,41), "PNG")
    ImetapodIMG = GV.Carregar_Imagem("imagens/pokeicons/metapod.png", (41,41), "PNG")
    IbutterfreeIMG = GV.Carregar_Imagem("imagens/pokeicons/butterfree.png", (41,41), "PNG")
    IabraIMG = GV.Carregar_Imagem("imagens/pokeicons/abra.png", (41,41), "PNG")
    IkadabraIMG = GV.Carregar_Imagem("imagens/pokeicons/kadabra.png", (41,41), "PNG")
    IalakazamIMG = GV.Carregar_Imagem("imagens/pokeicons/alakazam.png", (41,41), "PNG")
    IdratiniIMG = GV.Carregar_Imagem("imagens/pokeicons/dratini.png", (41,41), "PNG")
    IdragonairIMG = GV.Carregar_Imagem("imagens/pokeicons/dragonair.png", (41,41), "PNG")
    IdragoniteIMG = GV.Carregar_Imagem("imagens/pokeicons/dragonite.png", (41,41), "PNG")
    IzoruaIMG = GV.Carregar_Imagem("imagens/pokeicons/zorua.png", (41,41), "PNG")
    IzoroarkIMG = GV.Carregar_Imagem("imagens/pokeicons/zoroark.png", (41,41), "PNG")
    IpikachuIMG = GV.Carregar_Imagem("imagens/pokeicons/pikachu.png", (41,41), "PNG")
    IraichuIMG = GV.Carregar_Imagem("imagens/pokeicons/raichu.png", (41,41), "PNG")
    ImagikarpIMG = GV.Carregar_Imagem("imagens/pokeicons/magikarp.png", (41,41), "PNG")
    IgyaradosIMG = GV.Carregar_Imagem("imagens/pokeicons/gyarados.png", (41,41), "PNG")
    IjigglypuffIMG = GV.Carregar_Imagem("imagens/pokeicons/jigglypuff.png", (41,41), "PNG")
    IwigglytuffIMG = GV.Carregar_Imagem("imagens/pokeicons/wigglytuff.png", (41,41), "PNG")
    ImagnemiteIMG = GV.Carregar_Imagem("imagens/pokeicons/magnemite.png", (41,41), "PNG")
    ImagnetonIMG = GV.Carregar_Imagem("imagens/pokeicons/magneton.png", (41,41), "PNG")
    IsnorlaxIMG = GV.Carregar_Imagem("imagens/pokeicons/snorlax.png", (41,41), "PNG")
    IaerodactylIMG = GV.Carregar_Imagem("imagens/pokeicons/aerodactyl.png", (41,41), "PNG")
    IjynxIMG = GV.Carregar_Imagem("imagens/pokeicons/jynx.png", (41,41), "PNG")
    ImewtwoIMG = GV.Carregar_Imagem("imagens/pokeicons/mewtwo.png", (41,41), "PNG")
    IarticunoIMG = GV.Carregar_Imagem("imagens/pokeicons/articuno.png", (41,41), "PNG")
    IbeedrillIMG = GV.Carregar_Imagem("imagens/pokeicons/beedrill.png", (41,41), "PNG")
    IclefableIMG = GV.Carregar_Imagem("imagens/pokeicons/clefable.png", (41,41), "PNG")
    IclefairyIMG = GV.Carregar_Imagem("imagens/pokeicons/clefairy.png", (41,41), "PNG")
    IcloysterIMG = GV.Carregar_Imagem("imagens/pokeicons/cloyster.png", (41,41), "PNG")
    IcuboneIMG = GV.Carregar_Imagem("imagens/pokeicons/cubone.png", (41,41), "PNG")
    IkakunaIMG = GV.Carregar_Imagem("imagens/pokeicons/kakuna.png", (41,41), "PNG")
    ImarowakIMG = GV.Carregar_Imagem("imagens/pokeicons/marowak.png", (41,41), "PNG")
    ImeowthIMG = GV.Carregar_Imagem("imagens/pokeicons/meowth.png", (41,41), "PNG")
    ImoltresIMG = GV.Carregar_Imagem("imagens/pokeicons/moltres.png", (41,41), "PNG")
    IpersianIMG = GV.Carregar_Imagem("imagens/pokeicons/persian.png", (41,41), "PNG")
    IpinsirIMG = GV.Carregar_Imagem("imagens/pokeicons/pinsir.png", (41,41), "PNG")
    IraticateIMG = GV.Carregar_Imagem("imagens/pokeicons/raticate.png", (41,41), "PNG")
    IrattataIMG = GV.Carregar_Imagem("imagens/pokeicons/rattata.png", (41,41), "PNG")
    IshellderIMG = GV.Carregar_Imagem("imagens/pokeicons/shellder.png", (41,41), "PNG")
    IzapdosIMG = GV.Carregar_Imagem("imagens/pokeicons/zapdos.png", (41,41), "PNG")
    IweedleIMG = GV.Carregar_Imagem("imagens/pokeicons/weedle.png", (41,41), "PNG")


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



    EsmeraldaIMG = GV.Carregar_Imagem("imagens/itens/esmeralda.png", (62, 62), "PNG")
    CitrinoIMG = GV.Carregar_Imagem("imagens/itens/citrino.png", (62, 62), "PNG")
    RubiIMG = GV.Carregar_Imagem("imagens/itens/rubi.png", (62, 62), "PNG")
    SafiraIMG = GV.Carregar_Imagem("imagens/itens/safira.png", (62, 62), "PNG")
    AmetistaIMG = GV.Carregar_Imagem("imagens/itens/ametista.png", (62, 62), "PNG")
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
    VMaxIMG = GV.Carregar_Imagem("imagens/itens/Vstar.png", (62, 62), "PNG")
    VStarIMG = GV.Carregar_Imagem("imagens/itens/Vmax.png", (62, 62), "PNG")


    UPokeballIMG = GV.Carregar_Imagem("imagens/itens/PokeBall.png", (55,55),"PNG")
    UGreatBallIMG = GV.Carregar_Imagem("imagens/itens/GreatBall.png", (55,55),"PNG")
    UUltraBallIMG = GV.Carregar_Imagem("imagens/itens/UltraBall.png", (55,55),"PNG")
    UMasterBallIMG = GV.Carregar_Imagem("imagens/itens/MasterBall.png", (55,55),"PNG")
    UFramboIMG = GV.Carregar_Imagem("imagens/itens/frambo.png", (48, 48), "PNG")
    UFramboDouradaIMG = GV.Carregar_Imagem("imagens/itens/frambo_dourada.png", (48, 48), "PNG")
    UCaxiIMG = GV.Carregar_Imagem("imagens/itens/caxi.png", (48, 48), "PNG")
    UCaxiPrateadaIMG = GV.Carregar_Imagem("imagens/itens/caxi_prateada.png", (48, 48), "PNG")

    InventárioIMG = GV.Carregar_Imagem("imagens/icones/inventario.png", (60,60),"PNG")
    energiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (50,50),"PNG")
    CentroIMG = GV.Carregar_Imagem("imagens/icones/centro.png", (70,70),"PNG")
    LojaPokebolasIMG = GV.Carregar_Imagem("imagens/icones/Poke.png", (70,70),"PNG")
    LojaItensIMG = GV.Carregar_Imagem("imagens/icones/itens.png", (70,70),"PNG")
    LojaAmplificadoresIMG = GV.Carregar_Imagem("imagens/icones/amplificadores.png", (70,70),"PNG")
    LojaEnergiasIMG = GV.Carregar_Imagem("imagens/icones/energias.png", (60,60),"PNG")
    LojaEstTreIMG = GV.Carregar_Imagem("imagens/icones/EstTre.png", (70,70),"PNG")
    LojaBloqIMG = GV.Carregar_Imagem("imagens/icones/cadeado.png", (68,68),"PNG")
    AtaqueIMG = GV.Carregar_Imagem("imagens/icones/atacar.png", (40,40),"PNG")
    NocauteIMG  = GV.Carregar_Imagem("imagens/icones/KO.png", (50,50),"PNG")
    GuardadoIMG = GV.Carregar_Imagem("imagens/icones/guardado.png", (40,40),"PNG") 

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
    "velocista": VelocistaIMG,
    "Energizado": EnergizadoIMG
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

    PokeGifs = {
    "Bulbasaur": Gbulbasaur,
    "Ivysaur": Givysaur,
    "Venusaur": Gvenusaur,
    "Charmander": Gcharmander,
    "Charmeleon": Gcharmeleon,
    "Charizard": Gcharizard,
    "Squirtle": Gsquirtle,
    "Wartortle": Gwartortle,
    "Blastoise": Gblastoise,
    "Machop": Gmachop,
    "Machoke": Gmachoke,
    "Machamp": Gmachamp,
    "Gastly": Ggastly,
    "Haunter": Ghaunter,
    "Gengar": Ggengar,
    "Geodude": Ggeodude,
    "Graveler": Ggraveler,
    "Golem": Ggolem,
    "Caterpie": Gcaterpie,
    "Metapod": Gmetapod,
    "Butterfree": Gbutterfree,
    "Abra": Gabra,
    "Kadabra": Gkadabra,
    "Alakazam": Galakazam,
    "Dratini": Gdratini,
    "Dragonair": Gdragonair,
    "Dragonite": Gdragonite,
    "Zorua": Gzorua,
    "Zoroark": Gzoroark,
    "Pikachu": Gpikachu,
    "Raichu": Graichu,
    "Magikarp": Gmagikarp,
    "Gyarados": Ggyarados,
    "Jigglypuff": Gjigglypuff,
    "Wigglytuff": Gwigglytuff,
    "Magnemite": Gmagnemite,
    "Magneton": Gmagneton,
    "Snorlax": Gsnorlax,
    "Aerodactyl": Gaerodactyl,
    "Jynx": Gjynx,
    "Mewtwo": Gmewtwo,
    "Aerodactyl-Mega": Gaerodactyl_mega,
    "Alakazam-Mega": Galakazam_mega,
    "Articuno": Garticuno,
    "Beedrill": Gbeedrill,
    "Beedrill-Mega": Gbeedrill_mega,
    "Blastoise-Gigantamax": Gblastoise_gigantamax,
    "Blastoise-Mega": Gblastoise_mega,
    "Butterfree-gigantamax": Gbutterfree_gmax,
    "Charizard-gigantamax": Gcharizard_gmax,
    "Charizard-MegaX": Gcharizard_megax,
    "Charizard-MegaY": Gcharizard_megay,
    "Clefable": Gclefable,
    "Clefairy": Gclefairy,
    "Cloyster": Gcloyster,
    "Cubone": Gcubone,
    "Gengar-Gigantamax": Ggengar_gigantamax,
    "Gengar-Mega": Ggengar_mega,
    "Golem-Alola": Ggolem_alola,
    "Gyarados-Mega": Ggyarados_mega,
    "Kakuna": Gkakuna,
    "Machamp-Gigantamax": Gmachamp_gigantamax,
    "Marowak": Gmarowak,
    "Meowth": Gmeowth,
    "Meowth-Gigantamax": Gmeowth_gigantamax,
    "Mewtwo-MegaX": Gmewtwo_megax,
    "Mewtwo-MegaY": Gmewtwo_megay,
    "Moltres": Gmoltres,
    "Persian": Gpersian,
    "Pikachu-Gigantamax": Gpikachu_gigantamax,
    "Pinsir": Gpinsir,
    "Pinsir-Mega": Gpinsir_mega,
    "Raticate": Graticate,
    "Rattata": Grattata,
    "Shellder": Gshellder,
    "Snorlax-Gigantamax": Gsnorlax_gigantamax,
    "Venusaur-Gigantamax": Gvenusaur_gigantamax,
    "Zapdos": Gzapdos,
    "Weedle": Gweedle,
    "Charizard V": Gcharizard,
    "Blastoise V": Gblastoise,
    "Venusaur V": Gvenusaur,
    "Machamp V": Gmachamp,
    "Gengar V": Gmachoke,
    "Butterfree V": Gbutterfree,
    "Pikachu V": Gpikachu,
    "Meowth V": Gmeowth,
    "Snorlax V": Gsnorlax
    }

    ImagensPokemonIcons = {
    "Bulbasaur": IbulbasaurIMG,
    "Ivysaur": IivysaurIMG,
    "Venusaur": IvenusaurIMG,
    "Charmander": IcharmanderIMG,
    "Charmeleon": IcharmeleonIMG,
    "Charizard": IcharizardIMG,
    "Squirtle": IsquirtleIMG,
    "Wartortle": IwartortleIMG,
    "Blastoise": IblastoiseIMG,
    "Machop": ImachopIMG,
    "Machoke": ImachokeIMG,
    "Machamp": ImachampIMG,
    "Gastly": IgastlyIMG,
    "Haunter": IhaunterIMG,
    "Gengar": IgengarIMG,
    "Geodude": IgeodudeIMG,
    "Graveler": IgravelerIMG,
    "Golem": IgolemIMG,
    "Caterpie": IcaterpieIMG,
    "Metapod": ImetapodIMG,
    "Butterfree": IbutterfreeIMG,
    "Abra": IabraIMG,
    "Kadabra": IkadabraIMG,
    "Alakazam": IalakazamIMG,
    "Dratini": IdratiniIMG,
    "Dragonair": IdragonairIMG,
    "Dragonite": IdragoniteIMG,
    "Zorua": IzoruaIMG,
    "Zoroark": IzoroarkIMG,
    "Pikachu": IpikachuIMG,
    "Raichu": IraichuIMG,
    "Magikarp": ImagikarpIMG,
    "Gyarados": IgyaradosIMG,
    "Jigglypuff": IjigglypuffIMG,
    "Wigglytuff": IwigglytuffIMG,
    "Magnemite": ImagnemiteIMG,
    "Magneton": ImagnetonIMG,
    "Snorlax": IsnorlaxIMG,
    "Aerodactyl": IaerodactylIMG,
    "Jynx": IjynxIMG,
    "Mewtwo": ImewtwoIMG,
    "Aerodactyl-mega": IaerodactylIMG,
    "Alakazam-mega": IalakazamIMG,
    "Articuno": IarticunoIMG,
    "Beedrill": IbeedrillIMG,
    "Beedrill-mega": IbeedrillIMG,
    "Blastoise-gigantamax": IblastoiseIMG,
    "Blastoise-mega": IblastoiseIMG,
    "Butterfree-gigantamax": IbutterfreeIMG,
    "Charizard-gigantamax": IcharizardIMG,
    "Charizard-mega-x": IcharizardIMG,
    "Charizard-mega-y": IcharizardIMG,
    "Clefable": IclefableIMG,
    "Clefairy": IclefairyIMG,
    "Cloyster": IcloysterIMG,
    "Cubone": IcuboneIMG,
    "Gengar-gigantamax": IgengarIMG,
    "Gengar-mega": IgengarIMG,
    "Golem-alola": IgolemIMG,
    "Gyarados-mega": IgyaradosIMG,
    "Kakuna": IkakunaIMG,
    "Machamp-gigantamax": ImachampIMG,
    "Marowak": ImarowakIMG,
    "Meowth": ImeowthIMG,
    "Meowth-gigantamax": ImeowthIMG,
    "Mewtwo-mega-x": ImewtwoIMG,
    "Mewtwo-mega-y": ImewtwoIMG,
    "Moltres": ImoltresIMG,
    "Persian": IpersianIMG,
    "Pikachu-gigantamax": IpikachuIMG,
    "Pinsir": IpinsirIMG,
    "Pinsir-mega": IpinsirIMG,
    "Raticate": IraticateIMG,
    "Rattata": IrattataIMG,
    "Shellder": IshellderIMG,
    "Snorlax-gigantamax": IsnorlaxIMG,
    "Venusaur-gigantamax": IvenusaurIMG,
    "Zapdos": IzapdosIMG,
    "Weedle": IweedleIMG,
    "Charizard V": IcharizardIMG,
    "Blastoise V": IblastoiseIMG,
    "Venusaur V": IvenusaurIMG,
    "Machamp V": ImachampIMG,
    "Gengar V": ImachokeIMG,
    "Butterfree V": IbutterfreeIMG,
    "Pikachu V": IpikachuIMG,
    "Meowth V": ImeowthIMG,
    "Snorlax V": IsnorlaxIMG

}



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



    ImagensCaptura = {
    "Pokebola": UPokeballIMG,
    "Greatball": UGreatBallIMG,
    "Ultraball": UUltraBallIMG,
    "Masterball": UMasterBallIMG,
    "Fruta Frambo": UFramboIMG,
    "Fruta Frambo Dourada": UFramboDouradaIMG,
    "Fruta Caxi": UCaxiIMG,
    "Fruta Caxi Prateada": UCaxiPrateadaIMG
    }


    ImagensItens = {
    "Esmeralda": EsmeraldaIMG,
    "Citrino": CitrinoIMG,
    "Rubi": RubiIMG,
    "Safira": SafiraIMG,
    "Ametista": AmetistaIMG,
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
    "estadio": EstadioIMG,
    "Energia Mega": MegaIMG,
    "Energia Vstar": VStarIMG,
    "Energia GigantaMax": VMaxIMG
    
    }

    OutrosIMG = [InventárioIMG,energiasIMG,CentroIMG,LojaItensIMG,LojaPokebolasIMG,LojaAmplificadoresIMG,LojaEnergiasIMG,AtaqueIMG,NocauteIMG,LojaEstTreIMG,LojaBloqIMG,GuardadoIMG]

    FundosIMG = [Fundo,MerFundo,ShivreFundo,AuromaFundo,KalosFundo,SkyloftFundo,PortoFundo]

    return ImagensPokemonIcons,ImagensPokemonCentro,PokeGifs,ImagensCaptura,ImagensItens,OutrosIMG,FundosIMG,TiposEnergiaIMG,EfeitosIMG
