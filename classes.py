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

def l_f_f(filename):
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for f in file:
        osszespokemon.append(Pokemon(f))

l_f_f('pokemon.csv')




type_dict: dict = {}
Typestat = []

def typestat(filename):
    file = open(filename, 'r', encoding='utf8')
    file.readline()
    for f in file:
        Typestat.append(f)

typestat('type.csv')
print(Typestat)