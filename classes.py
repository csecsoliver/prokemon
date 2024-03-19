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
type_dict2: dict = {}


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
            if typename not in type_dict2.keys():
                    type_dict2[str(typename)] = float(typestats[i])
        type_dict[str(typename)] = type_dict2




types()
print(type_dict)