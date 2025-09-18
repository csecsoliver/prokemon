import menu
import classes
import classes2
from classes import clearscreen as clear
import random
from time import sleep as wait
def wild_fight(player: classes.Player, opponent_types: list):
    """
    Improved wild pokemon battle system
    player: a játékos adatai
    opponent_types: a lehetséges ellenséges pokemontípusok
    """
    # Select random opponent of the specified types
    opponent = None
    attempts = 0
    while opponent == None and attempts < 100:  # Prevent infinite loop
        opponent_num = random.randint(0, len(classes.osszespokemon) - 1)
        pokemon = classes.osszespokemon[opponent_num]
        if (pokemon.type1 in opponent_types) or (pokemon.type2 in opponent_types):
            opponent = pokemon
        attempts += 1
    
    if opponent == None:
        print("Nem található megfelelő ellenfél!")
        wait(2)
        return player
    
    clear()
    print(f"🌟 Egy vad {opponent.name} jelent meg! 🌟")
    print(f"Típus: {opponent.type1}" + (f"/{opponent.type2}" if opponent.type2 else ""))
    opponent_health = opponent.hp
    wait(3)
    
    # Check if player has any usable Pokemon
    if not player.pokemons or all(p.health <= 0 for p in player.pokemons):
        print("Nincs használható prokemonod!")
        wait(2)
        return player
    
    # Find first healthy Pokemon
    selected_pokemon = 0
    for i, pokemon in enumerate(player.pokemons):
        if pokemon.health > 0:
            selected_pokemon = i
            break
    
    ongoing = True
    message = None
    
    while ongoing:
        # Check if all player's Pokemon are fainted
        if all(p.health <= 0 for p in player.pokemons):
            clear()
            print("💀 Minden prokemonod harcképtelen! 💀")
            wait(3)
            # Heal one Pokemon to continue
            player.pokemons[selected_pokemon].heal_hp(player.pokemons[selected_pokemon].pokemon.hp)
            print(f"🏥 {player.pokemons[selected_pokemon].nickname} magához tért!")
            wait(2)
            return player
        
        # Make sure selected Pokemon is healthy
        if player.pokemons[selected_pokemon].health <= 0:
            for i, pokemon in enumerate(player.pokemons):
                if pokemon.health > 0:
                    selected_pokemon = i
                    break
        
        # Check if opponent is defeated
        if opponent_health <= 0:
            clear()
            print(f"🎉 {opponent.name} legyőzve! 🎉")
            exp_gained = random.randint(10, 25)
            print(f"💫 {player.pokemons[selected_pokemon].nickname} {exp_gained} tapasztalatot szerzett!")
            wait(3)
            return player
        
        return_value = fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
        message = None  # Reset message after displaying
        
        match return_value:
            case "1":  # Attack
                damage, message = calculate_attack_damage(player.pokemons[selected_pokemon], opponent)
                
                # Check if opponent attacks first (speed-based)
                if opponent.speed > player.pokemons[selected_pokemon].pokemon.speed and random.randint(0, 2) == 0:
                    enemy_damage, enemy_msg = calculate_attack_damage_reverse(opponent, player.pokemons[selected_pokemon])
                    player.pokemons[selected_pokemon].damage(enemy_damage)
                    message = f"⚡ {opponent.name} gyorsabb volt! {enemy_msg}"
                    if player.pokemons[selected_pokemon].health <= 0:
                        message += f"\n💀 {player.pokemons[selected_pokemon].nickname} harcképtelen!"
                else:
                    opponent_health -= damage
                    
            case "2":  # Wait  
                message = f"⏳ {player.pokemons[selected_pokemon].nickname} várakozik..."
                # Opponent might attack
                if random.randint(0, 1) == 0:
                    enemy_damage, enemy_msg = calculate_attack_damage_reverse(opponent, player.pokemons[selected_pokemon])
                    player.pokemons[selected_pokemon].damage(enemy_damage)
                    message += f"\n🔥 {opponent.name} támadott! {enemy_msg}"
                    
            case "3":  # Defend
                defense_boost = 0.5
                message = f"🛡️ {player.pokemons[selected_pokemon].nickname} védekezik!"
                # Reduced damage if opponent attacks
                if random.randint(0, 1) == 0:
                    enemy_damage, enemy_msg = calculate_attack_damage_reverse(opponent, player.pokemons[selected_pokemon])
                    reduced_damage = max(1, int(enemy_damage * defense_boost))
                    player.pokemons[selected_pokemon].damage(reduced_damage)
                    message += f"\n🔒 Csökkentett sebzés: {reduced_damage} ({enemy_msg})"
                    
            case "4":  # Use item
                if player.items:
                    # Simplified item usage
                    item_choice = player.pokemons[selected_pokemon].pick_item(player)
                    if item_choice is not None:
                        message = "🧪 Tárgy használva!"
                    else:
                        message = "❌ Nem használtál tárgyat"
                else:
                    message = "📦 Nincsenek tárgyaid!"
                    
            case "5":  # Switch Pokemon
                new_pokemon = switch_pokemon(player, selected_pokemon)
                if new_pokemon != selected_pokemon:
                    selected_pokemon = new_pokemon
                    message = f"🔄 {player.pokemons[selected_pokemon].nickname} a csatatérre!"
                else:
                    message = "🚫 Nem váltottál prokemot"
                    
            case "6":  # Run away
                if random.randint(0, 2) == 0:  # 33% chance to escape
                    print("🏃 Sikeresen megszöktél!")
                    wait(2)
                    return player
                else:
                    message = "❌ Nem sikerült megszökni!"
                    # Opponent gets a free attack
                    enemy_damage, enemy_msg = calculate_attack_damage_reverse(opponent, player.pokemons[selected_pokemon])
                    player.pokemons[selected_pokemon].damage(enemy_damage)
                    message += f"\n🔥 {opponent.name} támadott közben! {enemy_msg}"
                    
            case "7":  # Use Pokeball
                capture_chance = max(0.1, (opponent.hp - opponent_health) / opponent.hp * 0.6)
                if random.random() < capture_chance:
                    print(f"🎉 {opponent.name} elfogva!")
                    new_pokemon = classes2.Player_pokemon(opponent.name, opponent, opponent_health, 100)
                    player.pokemons.append(new_pokemon)
                    wait(3)
                    return player
                else:
                    message = f"💥 {opponent.name} kitört a prokelabdából!"
                    # Opponent gets angry and attacks
                    enemy_damage, enemy_msg = calculate_attack_damage_reverse(opponent, player.pokemons[selected_pokemon])
                    player.pokemons[selected_pokemon].damage(int(enemy_damage * 1.2))  # Bonus damage
                    message += f"\n😡 {opponent.name} dühös! {enemy_msg}"
                    
            case _:
                message = "❓ Érvénytelen választás!"
                wait(1)

def calculate_attack_damage(attacker: classes2.Player_pokemon, defender: classes.Pokemon):
    """Calculate attack damage with type effectiveness"""
    effectiveness = classes.fordito(attacker.pokemon.type1, defender.type1)
    
    # Handle dual types
    if attacker.pokemon.type2 and defender.type2:
        effectiveness *= classes.fordito(attacker.pokemon.type2, defender.type2)
    
    # Add some randomness
    effectiveness *= random.uniform(0.85, 1.15)
    
    # Calculate damage
    damage = max(1, round(attacker.pokemon.atk * effectiveness * 0.3))
    
    # Generate message based on effectiveness
    if effectiveness == 0:
        message = "Nem hatásos"
    elif effectiveness > 2:
        message = "Nagyon hatásos!"
    elif effectiveness < 1:
        message = "Nem nagyon hatásos"
    else:
        message = "Sikeres támadás"
    
    return damage, f"{message} ({damage} sebzés)"

def calculate_attack_damage_reverse(attacker: classes.Pokemon, defender: classes2.Player_pokemon):
    """Calculate attack damage when wild Pokemon attacks player's Pokemon"""
    effectiveness = classes.fordito(attacker.type1, defender.pokemon.type1)
    
    # Handle dual types  
    if attacker.type2 and defender.pokemon.type2:
        effectiveness *= classes.fordito(attacker.type2, defender.pokemon.type2)
    
    # Add some randomness
    effectiveness *= random.uniform(0.85, 1.15)
    
    # Calculate damage
    damage = max(1, round(attacker.atk * effectiveness * 0.3))
    
    # Generate message based on effectiveness
    if effectiveness == 0:
        message = "Nem hatásos"
    elif effectiveness > 2:
        message = "Nagyon hatásos!"
    elif effectiveness < 1:
        message = "Nem nagyon hatásos"
    else:
        message = "Sikeres támadás"
    
    return damage, f"{message} ({damage} sebzés)"

def switch_pokemon(player: classes.Player, current_index: int):
    """Allow player to switch to a different Pokemon"""
    clear()
    print("🔄 Prokemon csere")
    print("-" * 40)
    
    available_pokemon = []
    for i, pokemon in enumerate(player.pokemons):
        if pokemon.health > 0 and i != current_index:
            available_pokemon.append((i, pokemon))
    
    if not available_pokemon:
        print("Nincs más használható prokemon!")
        wait(2)
        return current_index
    
    options = ["Mégse"] + [f"{p.nickname} ({p.health}/{p.pokemon.hp} HP)" for _, p in available_pokemon]
    choice = menu.generic_menu("Válassz prokemot", options)
    
    if choice == "1":  # Cancel
        return current_index
    else:
        choice_num = int(choice) - 2  # Adjust for "Mégse" option
        if 0 <= choice_num < len(available_pokemon):
            return available_pokemon[choice_num][0]
        else:
            return current_index
    wait(3)
    clear()
    opponent = trainer_pokemons[0]
    for i in classes.osszespokemon:
        if i.name == trainer_pokemons[0]:
            opponent = i
        
    opponent_health = opponent.hp
    ongoing = True
    message = None
    selected_pokemon = 0
    opponent_selected_pokemon = 0
        
    
    
    while ongoing:
        clear()
        fainted_pokemon = 0
        for i in player.pokemons:
            if i.health <= 0:
                fainted_pokemon += 1
        if fainted_pokemon == len(player.pokemons):
            clear()
            print("Legyőzött az ellenfeled!")
            player.pokemons[selected_pokemon].heal_hp(player.pokemons[selected_pokemon].pokemon.hp)
            wait(3)
            clear()
            return player
        return_value = fight_gui(player.pokemons[selected_pokemon], opponent.name, opponent, opponent_health, message)
        
        
        match return_value:
            case "1":
                effectiveness = (classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type1))
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type2))
                    effectiveness = round(effectiveness, 2)
                # elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                #     effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type1, opponent.type2))
                #     effectiveness = round(effectiveness, 2)
                # elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                #     effectiveness = effectiveness * (classes.fordito(player.pokemons[selected_pokemon].pokemon.type2, opponent.type1))
                #     effectiveness = round(effectiveness, 2)
                
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
                    # elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                    #     effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                    #     effectiveness = round(effectiveness, 2)
                    # elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                    #     effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                    #     effectiveness = round(effectiveness, 2)
                    
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
                # elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                #     effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                #     effectiveness = round(effectiveness, 2)
                # elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                #     effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                #     effectiveness = round(effectiveness, 2)
                
                effectiveness *= random.uniform(0.85, 1.15)
                
                if effectiveness == 0:
                    message += "Nem hatásos"
                if effectiveness > 1:
                    message += "Nagyon hatásos!"
                if effectiveness < 1:
                    message += "Nem nagyon hatásos"
                if effectiveness == 1:
                    message += "Sikeres támadás"
                
                damage = round(opponent.atk * effectiveness * 0.3 - player.pokemons[selected_pokemon].pokemon.defe / 10)
                player.pokemons[selected_pokemon].damage(damage)
                
                player.pokemons[selected_pokemon].use_energy(random.randint(-40, -17))
                
                passs = True
            case "3":
                message = "Védekező pozíciót veszel föl, eközben az ellenfél támad: "
                
                effectiveness = classes.fordito( opponent.type1, player.pokemons[selected_pokemon].pokemon.type1)
                if (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 != ""):
                    effectiveness = effectiveness * (classes.fordito( opponent.type2, player.pokemons[selected_pokemon].pokemon.type2))
                    effectiveness = round(effectiveness, 2)
                # elif (player.pokemons[selected_pokemon].pokemon.type2 == "") and (opponent.type2 != ""):
                #     effectiveness = effectiveness * (classes.fordito(opponent.type2, player.pokemons[selected_pokemon].pokemon.type1))
                #     effectiveness = round(effectiveness, 2)
                # elif (player.pokemons[selected_pokemon].pokemon.type2 != "") and (opponent.type2 == ""):
                #     effectiveness = effectiveness * (classes.fordito(opponent.type1, player.pokemons[selected_pokemon].pokemon.type2))
                #     effectiveness = round(effectiveness, 2)
                
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
                
                damage = round(opponent.atk * effectiveness * 0.3 - player.pokemons[selected_pokemon].pokemon.defe / 10)
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
            case "7":
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
            if trainer_pokemons.index(opponent.name) < len(trainer_pokemons) - 1:
                
                for i in classes.osszespokemon:
                    if i.name == trainer_pokemons[opponent_selected_pokemon + 1]:
                        opponent = i
                        opponent_selected_pokemon += 1
                        break
                        
        

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
            
            damage = round(opponent.atk * effectiveness * 0.3 - player.pokemons[selected_pokemon].pokemon.defe / 10)
            player.pokemons[selected_pokemon].damage(damage)


def fight_gui(my_pokemon: classes2.Player_pokemon, enemy_name, enemy_pokemon: classes.Pokemon, opponent_health: int, what_happened: str = None):
    """Enhanced fight GUI with better visual presentation"""
    clear()
    
    # Battle header
    print("=" * 70)
    print(f"  ⚔️  {my_pokemon.nickname} VS {enemy_pokemon.name}  ⚔️")
    print("=" * 70)
    
    # Status information
    print(f"🔥 Ellenfél: {enemy_name}")
    enemy_hp_percent = (opponent_health / enemy_pokemon.hp) * 100
    enemy_hp_bar = create_hp_bar(opponent_health, enemy_pokemon.hp)
    print(f"   💚 Életerő: {enemy_hp_bar} {opponent_health}/{enemy_pokemon.hp} HP ({enemy_hp_percent:.1f}%)")
    
    print()
    
    print(f"👤 Saját prokemon: {my_pokemon.nickname}")
    my_hp_percent = (my_pokemon.health / my_pokemon.pokemon.hp) * 100
    my_hp_bar = create_hp_bar(my_pokemon.health, my_pokemon.pokemon.hp)
    print(f"   💚 Életerő: {my_hp_bar} {my_pokemon.health}/{my_pokemon.pokemon.hp} HP ({my_hp_percent:.1f}%)")
    
    energy_percent = my_pokemon.energy
    energy_bar = create_energy_bar(energy_percent)
    print(f"   ⚡ Energia: {energy_bar} {my_pokemon.energy}/100 PP")
    
    # What happened in the last turn
    if what_happened:
        print()
        print("📢 Mi történt:")
        print(f"   {what_happened}")
    
    print()
    print("-" * 70)
    
    # Battle options
    options = [
        "⚔️  Támadás",
        "⏳ Várakozás", 
        "🛡️  Védekezés",
        "🧪 Tárgy használata",
        "🔄 Prokemon csere",
        "🏃 Menekülés",
        "🔴 Prokelabda használata"
    ]
    
    for i, option in enumerate(options, 1):
        print(f"│ {i}. {option.ljust(62)} │")
    
    # Fill remaining space
    for i in range(len(options), 10):
        print("│" + " " * 68 + "│")
    
    print("-" * 70)
    
    while True:
        try:
            choice = input("Válassz akciót (1-7): ").strip()
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                return choice
            else:
                print("❌ Kérlek válassz 1 és 7 között!")
        except (ValueError, KeyboardInterrupt):
            print("❌ Érvénytelen bemenet!")

def create_hp_bar(current_hp: int, max_hp: int, bar_length: int = 20) -> str:
    """Create a visual HP bar"""
    if max_hp <= 0:
        return "❌ [" + "░" * bar_length + "]"
    
    percentage = current_hp / max_hp
    filled_length = int(bar_length * percentage)
    
    # Choose color based on HP percentage
    if percentage > 0.6:
        fill_char = "█"  # Green
        color = "🟢"
    elif percentage > 0.3:
        fill_char = "█"  # Yellow  
        color = "🟡"
    else:
        fill_char = "█"  # Red
        color = "🔴"
    
    bar = fill_char * filled_length + "░" * (bar_length - filled_length)
    return f"{color} [{bar}]"

def create_energy_bar(energy: int, bar_length: int = 15) -> str:
    """Create a visual energy bar"""
    percentage = energy / 100
    filled_length = int(bar_length * percentage)
    
    # Choose color based on energy level
    if percentage > 0.7:
        color = "🔵"  # Blue
    elif percentage > 0.3:
        color = "🟠"  # Orange
    else:
        color = "🔴"  # Red
    
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return f"{color} [{bar}]" 

if __name__ == "__main__":
    player = classes.Player("Péter", [classes2.Item([1,"heal", "Életpontok teljesen feltöltve", 0,0,0,2102012012])], [classes2.Player_pokemon("Pikachu", classes.osszespokemon[25], 100, 100), classes2.Player_pokemon("Charmander", classes.osszespokemon[4], 100, 100), classes2.Player_pokemon("Squirtle", classes.osszespokemon[7], 100, 100)])
    wild_fight(player, ["Grass", "Water", "Fire", "Electric"])