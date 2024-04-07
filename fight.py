import menu
import classes
import classes2
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
    opponent_health = opponent.hp
    wait(3)
    clear()
    ongoing = True
    message = None
    selected_pokemon = 0
    while ongoing:
        clear()
        return_value = fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
        
        
        match return_value:
            case "1":
                effectiveness = (classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type1))
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type1))
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                
                damage = round(player.pokemons[selected_pokemon].pokemon.atk * effectiveness * 0.3)
                if effectiveness == 0:
                    message = "Nem hatásos"
                if effectiveness > 2:
                    message = "Nagyon hatásos!"
                if effectiveness < 1:
                    message = "Nem nagyon hatásos"
                if effectiveness == 1:
                    message = "Sikeres támadás"
                
                if opponent.speed > player.pokemons[selected_pokemon].pokemon.speed and random.randint(0, 3) == 0:
                    message = "Az ellenfél gyorsabb, ezért ő támad először: "
                    
                    effectiveness = (classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1))
                    if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                        effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                        effectiveness = round(effectiveness, 2)
                    elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                        effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                        effectiveness = round(effectiveness, 2)
                    elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                        effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                        effectiveness = round(effectiveness, 2)
                    
                    effectiveness *= random.uniform(0.85, 1.15)
                    
                    if effectiveness == 0:
                        message += "Nem hatásos"
                    if effectiveness > 1:
                        message += "Nagyon hatásos!"
                    if effectiveness < 1:
                        message += "Nem nagyon hatásos"
                    if effectiveness == 1:
                        message += "Sikeres támadás"
                    
                    damage = round(opponent.atk * effectiveness * 0.3)
                    player.pokemons[selected_pokemon].damage(damage)
                    
                else:
                    opponent_health -= damage
                
                player.pokemons[selected_pokemon].use_energy(random.randint(12, 26))
                passs = False
                
            case "2":
                message = "Várakozol, eközben az ellenfél támad: "
                
                effectiveness = (classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1))
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                
                if effectiveness == 0:
                    message += "Nem hatásos"
                if effectiveness > 1:
                    message += "Nagyon hatásos!"
                if effectiveness < 1:
                    message += "Nem nagyon hatásos"
                if effectiveness == 1:
                    message += "Sikeres támadás"
                
                damage = round(opponent.atk * effectiveness * 0.3)
                player.pokemons[selected_pokemon].damage(damage)
                
                player.pokemons[selected_pokemon].use_energy(random.randint(-40, -17))
                
                passs = True
            case "3":
                message = "Védekező pozíciót veszel föl, eközben az ellenfél támad: "
                
                effectiveness = classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1)
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                effectiveness *= random.uniform(0, 0.4)
                if effectiveness < 0.3:
                    message += "Sikesesen kivédted"
                if effectiveness > 1:
                    message += "Nagyon hatásos!"
                if effectiveness < 1:
                    message += "Nem nagyon hatásos"
                if effectiveness == 1:
                    message += "Sikeres támadás"
                
                damage = round(opponent.atk * effectiveness * 0.3)
                player.pokemons[selected_pokemon].damage(damage)
                
                player.pokemons[selected_pokemon].use_energy(random.randint(-20, -5))
                
                passs = True
            case "4":
                message = player.pokemons[selected_pokemon].pick_item(player, 0)
                
                
                
                
            case "5":
                picked_pokemon = classes2.pick_pokemon(player, 0)
                if picked_pokemon == None:
                    pass
                else:
                    selected_pokemon = picked_pokemon
                    message = f"{player.pokemons[selected_pokemon].nickname}-t választottad!"
                passs = True
            case "6":
                chance = random.randint(0, 2)
                if chance != 0:
                    ongoing = False
                    clear()
                    print("Sikeresen megléptél a harcból!")
                    wait(3)
                    clear()
                    return player
            case "7":
                for i in player.items:
                    if i.name == "Pokeball":
                        if random.randint(0, 2) == 0:
                            ongoing = False
                            clear()
                            print("Sikeresen elkapta a wild pokemont!")
                            wait(3)
                            clear()
                            player.pokemons.append(classes2.Player_pokemon("Wild " + opponent.name, opponent, opponent.hp, 100))
                            return player
                        else:
                            clear()
                            print("A wild pokemon meglépett!")
                            wait(3)
                            clear()
                            return player
            case _:
                passs = True
        
        if opponent_health <= 0:
            ongoing = False
            opponent_health = 0
            clear()
            fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
            player.pokemons[selected_pokemon].heal_hp(player.pokemons[selected_pokemon].pokemon.hp)
            clear()
            print(f"{player.pokemons[selected_pokemon].nickname} legyőzte {opponent.name}-t!")
            wait(3)
            clear()
            return player
        
        if player.pokemons[selected_pokemon].health <= 0:
            
            clear()
            print(f"{player.pokemons[selected_pokemon].nickname} harcképtelenné vált!")
            wait(3)
            clear()
            djshfkd = False
            while djshfkd == False:
                picked_pokemon = classes2.pick_pokemon(player, 0)
                if picked_pokemon == None:
                    pass
                else:
                    selected_pokemon = picked_pokemon
                    if player.pokemons[selected_pokemon].health > 0:
                        message = f"{player.pokemons[selected_pokemon].nickname}-t választottad!"
                        djshfkd = True
                
            
        
        if passs == False:
            fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
            message = "Az ellenfél támad: "
                
            effectiveness = (classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1))
            if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                effectiveness = round(effectiveness, 2)
            elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                effectiveness = round(effectiveness, 2)
            elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                effectiveness = round(effectiveness, 2)
            
            effectiveness *= random.uniform(0.85, 1.15)
            
            if effectiveness == 0:
                message += "Nem hatásos"
            if effectiveness > 1:
                message += "Nagyon hatásos!"
            if effectiveness < 1:
                message += "Nem nagyon hatásos"
            if effectiveness == 1:
                message += "Sikeres támadás"
            
            damage = round(opponent.atk * effectiveness * 0.3)
            player.pokemons[selected_pokemon].damage(damage)



def trainer_fight(player, trainer_name, trainer_pokemons: list):
    
    clear()
    print(f"{trainer_name} kihív egy párbajra!")
    wait(3)
    clear()
    opponent = trainer_pokemons[0]
    opponent_health = opponent.hp
    ongoing = True
    message = None
    selected_pokemon = 0
        
    
    
    while ongoing:
        clear()
        return_value = fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
        
        
        match return_value:
            case "1":
                effectiveness = (classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type1))
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type1))
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                
                damage = round(player.pokemons[selected_pokemon].pokemon.atk * effectiveness * 0.3)
                if effectiveness == 0:
                    message = "Nem hatásos"
                if effectiveness > 2:
                    message = "Nagyon hatásos!"
                if effectiveness < 1:
                    message = "Nem nagyon hatásos"
                if effectiveness == 1:
                    message = "Sikeres támadás"
                
                if opponent.speed > player.pokemons[selected_pokemon].pokemon.speed and random.randint(0, 3) == 0:
                    message = "Az ellenfél gyorsabb, ezért ő támad először: "
                    
                    effectiveness = (classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1))
                    if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                        effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                        effectiveness = round(effectiveness, 2)
                    elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                        effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                        effectiveness = round(effectiveness, 2)
                    elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                        effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                        effectiveness = round(effectiveness, 2)
                    
                    effectiveness *= random.uniform(0.85, 1.15)
                    
                    if effectiveness == 0:
                        message += "Nem hatásos"
                    if effectiveness > 1:
                        message += "Nagyon hatásos!"
                    if effectiveness < 1:
                        message += "Nem nagyon hatásos"
                    if effectiveness == 1:
                        message += "Sikeres támadás"
                    
                    damage = round(opponent.atk * effectiveness * 0.3)
                    player.pokemons[selected_pokemon].damage(damage)
                    
                else:
                    opponent_health -= damage
                
                player.pokemons[selected_pokemon].use_energy(random.randint(12, 26))
                passs = False
                
            case "2":
                message = "Várakozol, eközben az ellenfél támad: "
                
                effectiveness = (classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1))
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                
                if effectiveness == 0:
                    message += "Nem hatásos"
                if effectiveness > 1:
                    message += "Nagyon hatásos!"
                if effectiveness < 1:
                    message += "Nem nagyon hatásos"
                if effectiveness == 1:
                    message += "Sikeres támadás"
                
                damage = round(opponent.atk * effectiveness * 0.3)
                player.pokemons[selected_pokemon].damage(damage)
                
                player.pokemons[selected_pokemon].use_energy(random.randint(-40, -17))
                
                passs = True
            case "3":
                message = "Védekező pozíciót veszel föl, eközben az ellenfél támad: "
                
                effectiveness = classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1)
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                    effectiveness = round(effectiveness, 2)
                elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                effectiveness *= random.uniform(0, 0.4)
                if effectiveness < 0.3:
                    message += "Sikesesen kivédted"
                if effectiveness > 1:
                    message += "Nagyon hatásos!"
                if effectiveness < 1:
                    message += "Nem nagyon hatásos"
                if effectiveness == 1:
                    message += "Sikeres támadás"
                
                damage = round(opponent.atk * effectiveness * 0.3)
                player.pokemons[selected_pokemon].damage(damage)
                
                player.pokemons[selected_pokemon].use_energy(random.randint(-20, -5))
                
                passs = True
            case "4":
                message = player.pokemons[selected_pokemon].pick_item(player, 0)
                
                
                
                
            case "5":
                picked_pokemon = classes2.pick_pokemon(player, 0)
                if picked_pokemon == None:
                    pass
                else:
                    selected_pokemon = picked_pokemon
                    message = f"{player.pokemons[selected_pokemon].nickname}-t választottad!"
                passs = True
            case "6":
                clear()
                print("Ez itt nem lehetséges!")
                wait(3)
                clear()
                passs = True
            case _:
                passs = True
        
        if opponent_health <= 0:
            fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
            print(f"{player.pokemons[selected_pokemon].nickname} legyőzte {opponent.name}-t!")
            wait(3)
            clear()
            if trainer_pokemons.index(opponent) < len(trainer_pokemons) - 1:
                opponent = trainer_pokemons[trainer_pokemons.index(opponent) + 1]
                opponent_health = opponent.hp
                clear()
                message = f"{trainer_name} beküldi {opponent.name}-t!"
                wait(3)
                clear()
            else:
                ongoing = False
                
                opponent_health = 0
                clear()
                fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
                player.pokemons[selected_pokemon].heal_hp(player.pokemons[selected_pokemon].pokemon.hp)
                clear()
                return player
        
        if player.pokemons[selected_pokemon].health <= 0:
            
            clear()
            print(f"{player.pokemons[selected_pokemon].nickname} harcképtelenné vált!")
            wait(3)
            clear()
            picked_successfully = False
            while picked_successfully == False:
                picked_pokemon = classes2.pick_pokemon(player, 0)
                if picked_pokemon == None:
                    pass
                else:
                    selected_pokemon = picked_pokemon
                    if player.pokemons[selected_pokemon].health > 0:
                        message = f"{player.pokemons[selected_pokemon].nickname}-t választottad!"
                        picked_successfully = True
                
            
        
        if passs == False:
            fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
            message = "Az ellenfél támad: "
                
            effectiveness = (classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1))
            if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                effectiveness = round(effectiveness, 2)
            elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                effectiveness = round(effectiveness, 2)
            elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                effectiveness = round(effectiveness, 2)
            
            effectiveness *= random.uniform(0.85, 1.15)
            
            if effectiveness == 0:
                message += "Nem hatásos"
            if effectiveness > 1:
                message += "Nagyon hatásos!"
            if effectiveness < 1:
                message += "Nem nagyon hatásos"
            if effectiveness == 1:
                message += "Sikeres támadás"
            
            damage = round(opponent.atk * effectiveness * 0.3)
            player.pokemons[selected_pokemon].damage(damage)


def fight_gui(my_pokemon: classes2.Player_pokemon, enemy_name, enemy_pokemon: classes.Pokemon, opponent_health: int, what_happened: str = None):
    print(my_pokemon.nickname + " vs " + enemy_pokemon.name)
    print("-" * 60)
    options = ["",f"Ellenség, {enemy_name} életpontjai: {opponent_health} / {enemy_pokemon.hp}", f"{my_pokemon.nickname} életpontjai: {my_pokemon.health} / {my_pokemon.pokemon.hp}",f"Energia: {my_pokemon.energy}" , "1. Támadás","2. Várakozás", "3. Védekezés", "4. Tárgy használata", "5. Prokemon csere", "6. Menekülés"]
    if what_happened != None:
        options[0] = what_happened
    for i in range(10):
        if i < len(options):
            print(f"""│ {f"{options[i]}".ljust(56)} │""")
        else:
            print("│" + " " * 58 + "│")
    print("-" * 60)
    return input("Válasz: ") 

if __name__ == "__main__":
    player = classes.Player("Péter", [classes2.Item([1,"heal", "Életpontok teljesen feltöltve", 0,0,0,2102012012])], [classes2.Player_pokemon("Pikachu", classes.osszespokemon[25], 100, 100), classes2.Player_pokemon("Charmander", classes.osszespokemon[4], 100, 100), classes2.Player_pokemon("Squirtle", classes.osszespokemon[7], 100, 100)])
    wild_fight(player, ["Grass", "Water", "Fire", "Electric"])