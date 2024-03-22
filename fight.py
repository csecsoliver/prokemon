import menu
import classes
from classes import clearscreen as clear
import random
from time import sleep as wait
def wild_fight(player, opponent_types: list):
    """
    player: a játékos adatai
    opponent_types: a lehetséges ellenséges pokemontípusok
    """
    opponent = None
    while opponent == None:
        oppontent_num = random.randint(0, len(classes.osszespokemon))
        if (classes.osszespokemon[oppontent_num].type1 in opponent_types) or (classes.osszespokemon[oppontent_num].type2 in opponent_types):
            opponent = classes.osszespokemon[oppontent_num]
    
    print()
    clear()
    print(f"A wild {opponent.name} appeared!")


    pass

def trainer_fight():
    pass

def fight_gui():
    pass

