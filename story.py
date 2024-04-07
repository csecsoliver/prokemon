import classes
import classes2
import random
from fight import *
from time import sleep as wait



'''
PLSSSSS EGY KIS VISSZAJELZÉS HOGY MEGFELEL E

4 + 1 biom 

Bármelyik biomból bármelyikbe lehet menni kivéve a végsőbe ott csak ha már az összes boss megvan automatikusan átkerül a játékos
és vége lesz a játéknak ha legyőzi

Minden biomban 3 megállóhely egy shop egy puszta és egy minibossal tallkoás ami annak a biomnak a trainer minibossa a minibossok 
nyilván egy nagy boss irányítása alatt vannak aki meg akarja szerezni magának az összes pokemont ami nekünk nem jó és ezt kell 
megakadályozni hogy mindet legyőzzük nekünk van egy segítőnk (akinek még nincs neve) gyakorlatilag narrátor megy velünk
végig és meséli hogy mi merre hány méter vakon megbízunk benne de a legvégén kiderül ő mozgatja a szálakat és őt is le kell győznünk

Bossok pokemonjai 25-tel több hp-val és a többi statból 5-tel többel kezdenek mint a pokemonok alapverziója 
(fix ne legyen túl önnyű legyőzni őket)

- Grassy biom (Normal, Grass, Water, Ground, Poison)
    - boss pokemonjai: 
        - Bulbasaur, Pidgey, Psyduck

- Cloud biom (Electric, Ice, Flying, Bug)
    - boss pokemonjai:
        - Raichu, Scyther, Zubat

- Mountain biom (Rock, Fighting)
    - boss pokemonjai:
        - Aerodactyl, Kabuto, Mankey

- Underworld biom (Fire, Psychic, Ghost, Dragon)
    - boss pokemonjai:
        - Arcanine, Dratini, Charmander

- Boss biom (itt már bármilyen pokemon lehet és csak a végső harcra lehet átjutni)
    - boss pokemonjai: 
        - Dragonite, Charmeleon, Ivysaur
    - Volt segítő pokemonjai:
        - Charizard, Mewtwo, Articuno
'''


def puszta(type1, type2, type3, type4, type5):
    typeslist: list = [type1, type2, type3, type4, type5]
    print('Megérkeztél egy puszta területre')
    wait(2)
    wild_fight('player', typeslist)
    

def grassy_biom(player):
    print('(story)')
    input('Tovább...')
    puszta('Normal', 'Grass', 'Water', 'Ground', 'Poison')
    print('(story szöveg)')
    input('Tovább...')
    puszta('Normal', 'Grass', 'Water', 'Ground', 'Poison')
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta('Normal', 'Grass', 'Water', 'Ground', 'Poison')
            pass
        else: 
            break

    trainer_fight()
    print('story')


def cloud_biom(player):
    print('(story)')
    input('Tovább...')
    puszta('Electric', 'Ice', 'Flying', 'Bug')
    print('(story szöveg)')
    input('Tovább...')
    puszta('Electric', 'Ice', 'Flying', 'Bug')
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta('Electric', 'Ice', 'Flying', 'Bug')
            pass
        else: 
            break

    trainer_fight()
    print('story')

def mountain_biom(player):
    print('(story)')
    input('Tovább...')
    puszta('Rock', 'Fighting')
    print('(story szöveg)')
    input('Tovább...')
    puszta('Rock', 'Fighting')
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta('Rock', 'Fighting')
            pass
        else: 
            break

    trainer_fight()
    print('story')

def underworld_biom(player):
    print('(story)')
    input('Tovább...')
    puszta('Fire', 'Psychic', 'Ghost', 'Dragon')
    print('(story szöveg)')
    input('Tovább...')
    puszta('Fire', 'Psychic', 'Ghost', 'Dragon')
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta('Fire', 'Psychic', 'Ghost', 'Dragon')
            pass
        else: 
            break

    trainer_fight()
    print('story')