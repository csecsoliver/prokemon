from classes import *
from classes2 import *
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
    

def grassy_biom(player: Player):
    typeslist = ['Normal', 'Grass', 'Water', 'Ground', 'Poison']
    aaron_pokemons = ['Bulbasaur', 'Pidgey', 'Psyduck']
    print(f'Max: Üdvözöllek {player.name}! Szükségem lenne a segítségedre mert Gloria át akarja venni az uralmat az összes pokemon felett és ezt nem hagyhatjuk!\n Látom benned a potenciált ott is van egy füves puszta el is kezdhetsz gyakorolni és pokemonokat szerezni!')
    input('Tovább...')
    clearscreen()
    print(f"Kapsz egy pokemont és egy pokelabdát, hogy segítsen utadon!")
    input("Tovább...")
    clearscreen()
    
    puszta(player, typeslist)
    print('Max: Ez egész ügyes volt de mielőtt találkozol az elő igazi ellenfeleddel rádfér mégegy kör!')
    input('Tovább...')
    clearscreen()
    puszta(player, typeslist)
    print('Max: Ennek a területnek a mestere Aaron. Még rajta át kell magad verekedned hogy továbbmehess.')
    wait(4)
    while True:
        input_ = input('Max: Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Aaron', aaron_pokemons)
    print('Max: Az első mester akit legyőztél! Remélem jó érzés. Szerintem indulhatunk is tovább')
    wait(4)
    clearscreen()


def cloud_biom(player):
    typeslist = ['Electric', 'Ice', 'Flying', 'Bug']
    lyra_pokemons = ['Raichu', 'Scyther', 'Zubat']
    print('MAx: Ooo igen a felhős vidék, gondolom érzed ezt a csodás friss levegőt! Tökéletes idő új pokeonok befogására!')
    input('Tovább...')
    clearscreen()
    puszta(player, typeslist)
    print('Max: Igen itt már újabb fajta pokemonok találhatók úgyhogy csak óvatosan az ellenfeleiddel!')
    input('Tovább...')
    clearscreen()
    puszta(player, typeslist)
    print('Max: Már csak Lyra nagymestert kell legyőzni de vigyzz vele mert Electic és Flying típusokat is használ!')
    wait(4)
    while True:
        input_ = input('Max: Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Lyra', lyra_pokemons)
    print('Max: Legyőzted! Büszke vagyok! Gyorsan nincs több vesztegetni való időnk')
    wait(4)
    clearscreen()

def mountain_biom(player):
    typeslist = ['Rock', 'Fighting']
    dawn_pokemons = ['Aerodactyl', 'Kabuto', 'Mankey']
    print('Max: Utálom a hegyvidéket! És ezzel együtt itt található a legkevesebb pokemon. Na mindegy túl kell esnünk rajta mert az összes mestert le kell győznünk.')
    input('Tovább...')
    clearscreen()
    puszta(player, typeslist)
    print('Max: Akármennyire is nem szeretem ezt a területet meglehetősen erősek itt a pokemonok szóval próbálj minél többet szerezni!')
    input('Tovább...')
    clearscreen()
    
    while True:
        input_ = input('Max: Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Dawn', dawn_pokemons)
    print('Max: Nem gondoltam volna hogy le tudod győzni elég erős ellenfél volt de végig neked szurkoltam!')
    wait(4)
    clearscreen()
def underworld_biom(player):
    typeslist = ['Fire', 'Psychic', 'Ghost', 'Dragon']
    whitney_pokemons = ['Arcanine', 'Dratini', 'Charmander']
    print('Max: Már csak egy mester van de előbb ismerkedj meg az új biommal!')
    input('Tovább...')
    clearscreen()
    puszta(player, typeslist)
    print('Max: Nem is megy rosszul na de ez még nem elég egy nagymester ellen!')
    input('Tovább...')
    clearscreen()
    puszta(player, typeslist)
    print('Elérkeztél most közelebb vagyunk a végéhez mint valaha is voltunk!')
    wait(4)
    clearscreen()
    while True:
        input_ = input('Szeretnél visszafordulni és visszamenni a puszta területre? Ha nem akkor a boss harccal fogod folytatni. i/n')
        if input_ == 'i':
            puszta(player, typeslist)
            pass
        else: 
            break

    trainer_fight(player, 'Whitney', whitney_pokemons)
    print('Max: Legyőzted Whitney-t el se hiszem! Ő volt az utolsó nagyhatalmú pokemon mester! Már csak Gloria választ el a célunktól.')
    wait(5)
    clearscreen()

def boss_biom(player):
    max_pokemons = ['Charizard', 'Mewtwo', 'Articuno']
    gloria_pokemons = ['Dragonite', 'Charmeleon', 'Ivysaur']
    clearscreen()
    print('Max: Végre elérkeztünk ide és le tudjuk győzni Gloria-t és megakadályozhatjuk hogy övé legyen a hatalom!')
    wait(5)
    clearscreen()
    print('Gloria: Már régóta vártalak kölyök! Már csak téged kell eltakarítanom az utamból! Állj ki ellenem és küzdjünk meg a hatalomért!')
    input('Harc...')
    clearscreen()
    trainer_fight(player, 'Gloria', gloria_pokemons)
    clearscreen()
    print('Max: Én.. Én nem hiszem el hogy tényleg legyőzted nekem Gloria-t! Hát ez hihetetlen most pedig enyém a világ végre!!!')
    wait(5)
    clearscreen()
    trainer_fight(player, 'Max', max_pokemons)