import classes
import classes2
import random
from fight import *
from time import sleep as wait
from os import system


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


def puszta(player, typeslist):
    print('Megérkeztél egy puszta területre')
    wait(2)
    wild_fight(player, typeslist)
    

def grassy_biom(player):
    typeslist = ['Normal', 'Grass', 'Water', 'Ground', 'Poison']
    aaron_pokemons = ['Bulbasaur', 'Pidgey', 'Psyduck']
    print('(story)')
    input('Tovább...')
    puszta(player, typeslist)
    print('(story szöveg)')
    input('Tovább...')
    puszta(player, typeslist)
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Aaron', aaron_pokemons)
    print('story')


def cloud_biom(player):
    typeslist = ['Electric', 'Ice', 'Flying', 'Bug']
    lyra_pokemons = ['Raichu', 'Scyther', 'Zubat']
    print('(story)')
    input('Tovább...')
    puszta(player, typeslist)
    print('(story szöveg)')
    input('Tovább...')
    puszta(player, typeslist)
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Lyra', lyra_pokemons)
    print('story')

def mountain_biom(player):
    typeslist = ['Rock', 'Fighting']
    dawn_pokemons = ['Aerodactyl', 'Kabuto', 'Mankey']
    print('(story)')
    input('Tovább...')
    puszta(player, typeslist)
    print('(story szöveg)')
    input('Tovább...')
    puszta(player, typeslist)
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Dawn', dawn_pokemons)
    print('story')

def underworld_biom(player):
    typeslist = ['Fire', 'Psychic', 'Ghost', 'Dragon']
    whitney_pokemons = ['Arcanine', 'Dratini', 'Charmander']
    print('(story)')
    input('Tovább...')
    puszta(player, typeslist)
    print('(story szöveg)')
    input('Tovább...')
    puszta(player, typeslist)
    print('story')
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Whitney', whitney_pokemons)
    print('Max: Legyőzted Whitney-t el se hiszem! Ő volt az utolsó nagyhatalmú pokemon mester! Már csak Gloria választ el a célunktól.')
    wait('5')
    system('cls')

def boss_biom(player):
    max_pokemons = ['Charizard', 'Mewtwo', 'Articuno']
    gloria_pokemons = ['Dragonite', 'Charmeleon', 'Ivysaur']
    system('cls')
    print('Max: Végre elérkeztünk ide és le tudjuk győzni Gloria-t és megakadályozhatjuk hogy övé legyen a hatalom!')
    wait('5')
    system('cls')
    print('Gloria: Már régóta vártalak kölyök! Már csak téged kell eltakarítanom az utamból! Állj ki ellenem és küzdjünk meg a hatalomért!')
    input('Harc...')
    system('cls')
    trainer_fight(player, 'Gloria', gloria_pokemons)
    system('cls')
    print('Max: Én.. Én nem hiszem el hogy tényleg legyőzted nekem Gloria-t! Hát ez hihetetlen most pedig enyém a világ végre!!!')
    wait('5')
    system('cls')
    trainer_fight(player, 'Max', max_pokemons)