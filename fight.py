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
    wait(3)
    clear()
    

    pass

def trainer_fight():
    pass

def fight_gui(my_pokemon: classes.Pokemon, enemy_name, enemy_pokemon: classes.Pokemon):
    print(my_pokemon.nickname + " vs ")
    print("-" * 60)
    for i in range(10):
        if i < len(options):
            print(f"""│ {f"{i + 1}. {options[i]}".ljust(56)} │""")
        else:
            print("│" + " " * 58 + "│")
    print("-" * 60)
    return input("Válasz: ") 

