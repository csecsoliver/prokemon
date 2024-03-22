class Pokemon:
    def __init__(self, row: str) -> None:
        #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
        spltd = row.strip().split(',')
        self.name = spltd[1]
        self.type1 = spltd[2]
        self.type2 = spltd[3]
        self.hp = spltd[5]
        self.atk = spltd[6]
        self.defe = spltd[7]
        self.speed = spltd[10]
        


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
            return v[type_to_int(type2)-1]

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
        


print(osszespokemon)