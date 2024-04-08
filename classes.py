import platform
import os

class Pokemon:
    def __init__(self, row: str) -> None:
        #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
        spltd = row.strip().split(',')
        self.name = spltd[1]
        self.type1 = spltd[2]
        self.type2 = spltd[3]
        self.hp = int(spltd[5])
        self.atk = int(spltd[6])
        self.defe = int(spltd[7])
        self.speed = int(spltd[10])
        
class Player:
    def __init__(self, name, items: list, pokemons: list) -> None:
        self.name = name
        self.items = items
        self.pokemons = pokemons

osszespokemon: list[Pokemon] = []
type_list: list = []
type_dict: dict = {}



def load_from_file(filename: str, classname, listname: list):
    '''Sima file beolvasás három parameterrel: 
    1. a file neve
    2. a listbe felvett elemek classa
    3. lista neve'''
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for f in file:
        listname.append(classname(f.strip()))

load_from_file('pokemon.csv', Pokemon, osszespokemon)







def types():
    load_from_file('type.csv', str, type_list)
    for i, t in enumerate(type_list):
        splitted = str(t).split(';')
        typename = splitted[0]
        typestats = splitted[1:]
        
        if typename not in type_dict.keys():
            type_dict[str(typename)] = typestats

def fordito(type1: str, type2: str) -> int:
    '''Két parameter:

    type1: támadó pokemon type
    type2: védekező pokemon type

    lefuttatja a type() függvényt ezáltal beolvassa a pokemonok statjait a type.csv-ből majd visszaadja a támadás szorzóját'''
    types()
    for k, v in type_dict.items():
        if k == type1:
            return float(v[type_to_int(type2)-1])

def type_to_int(type: str) -> int:
    '''Normal;Fire;Water;Electric;Grass;Ice;Fighting;Poison;Ground;Flying;Psychic;Bug;Rock;Ghost;Dragon'''
    match type:
        case 'Normal':
            return 1
        case 'Fire':
            return 2
        case 'Water':
            return 3
        case 'Electric':
            return 4
        case 'Grass':
            return 5
        case 'Ice':
            return 6
        case 'Fighting':
            return 7
        case 'Poison':
            return 8
        case 'Ground':
            return 9
        case 'Flying':
            return 10
        case 'Psychic':
            return 11
        case 'Bug':
            return 12
        case 'Rock':
            return 13
        case 'Ghost':
            return 14
        case 'Dragon':
            return 15
        

def clearscreen():
    match platform.system():
        case "Windows":
            os.system("cls")
        case "Linus":
            print("WTF are you doing?")
        case "Linux":
            os.system("clear")
        case "Darwin":
            os.system("clear")
        case "Java":
            print("Why? Cannot clear the screen.")
        case _:
            print("Incompatible system, cannot clear the screen")

#player_pokemons = [("Pikachu", osszespokemon[25], 100, 100), ("Charmander", osszespokemon[4], 100, 100), ("Squirtle", osszespokemon[7], 100, 100)]
#player = Player("Péter",'', player_pokemons)
    

def save(player: Player) -> bool:
    
    nameinput = input('Add meg a mentés nevét! ')
    file = open(nameinput + '.csv', 'w', encoding='utf8')
    file.write(f'{player.name}\n')
    for i in player.items:
         file.write(f'{i}\n')
    file.write('POKEMONS\n')
    for p in player.pokemons:
        file.write(f'{p}\n')
    saveend = input('A mentés sikeres! Folytatja a játékot? ')
    match saveend:
        case 'i':
            return True
        case 'n':
            return False
        case _:
            print('Írj már be valami olyat amit kértem légysziiii, ezt akkor egy nemnek veszem csáá')
            return False
        

#save(player)
# print(osszespokemon)