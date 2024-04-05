import menu
import classes
import classes2 as classes
from classes import clearscreen as clear
import random
from time import sleep as wait
def wild_fight(player: classes.Player, opponent_types: list):
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
    opponent_health = opponent.health
    wait(3)
    clear()
    ongoing = True
    message = None
    selected_pokemon = 0
    while ongoing:
        return_value = fight_gui(player.pokemons, opponent.name, opponent, opponent_health, message)
        match return_value:
            case "1":
                effectiveness = classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type1)
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type2)
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type2)
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type1)
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                
                damage = round(player.pokemons[selected_pokemon].pokemon.atk * effectiveness)
                if damage == 0:
                    message = "Nem hatásos"
                if effectiveness > 2:
                    message = "Nagyon hatásos!"
                if effectiveness < 1:
                    message = "Nem nagyon hatásos"
                if effectiveness == 1:
                    message = "Sikeres támadás"
                
                if opponent.speed > player.pokemons[selected_pokemon].pokemon.speed and random.randint(0, 3) == 0:
                    message = "Az ellenfél gyorsabb, ezért ő támad először: "
                    
                    effectiveness = classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1)
                    if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                        effectiveness = effectiveness * classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2)
                        effectiveness = round(effectiveness, 2)
                    elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                        effectiveness = effectiveness * classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1)
                        effectiveness = round(effectiveness, 2)
                    elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                        effectiveness = effectiveness * classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2)
                        effectiveness = round(effectiveness, 2)
                    
                    effectiveness *= random.uniform(0.85, 1.15)
                    
                    if damage == 0:
                        message += "Nem hatásos"
                    if effectiveness > 1:
                        message += "Nagyon hatásos!"
                    if effectiveness < 1:
                        message = "Nem nagyon hatásos"
                    if effectiveness == 1:
                        message += "Sikeres támadás"
                    
                    damage = round(opponent.atk * effectiveness)
                    player.pokemons[selected_pokemon].damage(damage)
                    
                else:
                    opponent_health -= damage
                    
                
            case "2":
                message = "Várakozol, eközben az ellenfél támad: "
                
                effectiveness = classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1)
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2)
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1)
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2)
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                
                if damage == 0:
                    message += "Nem hatásos"
                if effectiveness > 1:
                    message += "Nagyon hatásos!"
                if effectiveness < 1:
                    message = "Nem nagyon hatásos"
                if effectiveness == 1:
                    message += "Sikeres támadás"
                
                damage = round(opponent.atk * effectiveness)
                player.pokemons[selected_pokemon].damage(damage)
                
                player.pokemons[selected_pokemon].use_energy(random.randint(-40, -17))
                
            case "3":
                message = "Védekező pozíciót veszel föl, eközben az ellenfél támad: "
                
                effectiveness = classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1)
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2)
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1)
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2)
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                effectiveness *= random.uniform(0, 0.4)
                if damage < 0.3:
                    message += "Sikesesen kivédted"
                if effectiveness > 1:
                    message += "Nagyon hatásos!"
                if effectiveness < 1:
                    message = "Nem nagyon hatásos"
                if effectiveness == 1:
                    message += "Sikeres támadás"
                
                damage = round(opponent.atk * effectiveness)
                player.pokemons[selected_pokemon].damage(damage)
                
                player.pokemons[selected_pokemon].use_energy(random.randint(-20, -5))
            case "4":
                classes.pick_item(player, 0)
                
                
                
                
            case "5":
                pass
            case "6":
                pass
            case _:
                pass
        
    

    pass

def trainer_fight():
    pass

def fight_gui(my_pokemon: classes.Player_pokemon, enemy_name, enemy_pokemon: classes.Pokemon, opponent_health: int, what_happened: str = None):
    print(my_pokemon.nickname + " vs " + enemy_pokemon.name)
    print("-" * 60)
    options = ["",f"Ellenség, {enemy_name} életpontjai: {opponent_health} / {enemy_pokemon.health}", f"{my_pokemon.nickname} életpontjai: {my_pokemon.health} / {my_pokemon.pokemon.health}", "1. Támadás","2. Várakozás", "3. Védekezés", "4. Tárgy használata", "5. Prokemon csere", "6. Menekülés"]
    if what_happened != None:
        options[0] = what_happened
    for i in range(10):
        if i < len(options):
            print(f"""│ {f"{options[i]}".ljust(56)} │""")
        else:
            print("│" + " " * 58 + "│")
    print("-" * 60)
    return input("Válasz: ") 

