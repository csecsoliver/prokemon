import classes
import classes2
import menu
from classes import clearscreen as clear
from time import sleep as wait
import prokedex
from story import *
from bulbasaur import bulbasaur_image as b

def main():
    clear()
    match menu.title_screen():
        case "1":
            game()
            main()
        case "2":
            prokedex.main(True)
            main()
        case "3":
            clear()
            print("Viszlát!")
            wait(1)
            clear()
            return

def game():
    clear()
    choice = menu.generic_menu("Játék", ["Új játék", "Folytatás", "Kilépés"])
    
    player = None
    try:
        match choice:
            case "1":
                player = new_game()
                # Show tutorial for new players
                show_tutorial(player)
            case "2":
                player = classes2.load_a_save()
            case "3":
                return
            case _:
                print("Érvénytelen választás!")
                wait(1)
                return game()
        
        if player:
            # Start the main game progression
            start_game_progression(player)
            
    except FileNotFoundError:
        print("A mentés fájl nem található!")
        wait(2)
        return game()
    except Exception as e:
        print(f"Hiba történt: {e}")
        wait(2)
        return game()

def show_tutorial(player):
    """Show tutorial for new players"""
    clear()
    print(f"Üdvözöllek {player.name}!")
    input('Tovább...')
    clear()
    print("Ez egy pokemon játék.")
    input('Tovább...')
    clear()
    print("A játék célja, hogy minél erősebb prokemonokat gyűjts össze, és legyőzd a legerősebb ellenfeleket is.")
    input('Tovább...')
    clear()
    print("A játékban a pokemontokat prokelabdákkal gyűjtheted össze.")
    input('Tovább...')
    clear()
    print("A prokemontokat a harcokban használhatod.")
    input('Tovább...')
    clear()
    print("A játékban a prokemontokat a Prokedexben tudod megnézni.")
    input('Tovább...')
    clear()
    print("A prokedex elindítható a főmenüből, vagy a külön fájllal is.")
    input('Tovább...')
    clear()

def start_game_progression(player):
    """Start the main game progression through all biomes"""
    biomes = [
        ("Füves biom", grassy_biom),
        ("Felhő biom", cloud_biom), 
        ("Hegyvidék biom", mountain_biom),
        ("Alvilág biom", underworld_biom),
        ("Végső biom", boss_biom)
    ]
    
    for i, (biome_name, biome_func) in enumerate(biomes):
        print(f"Belépés: {biome_name}")
        wait(1)
        biome_func(player)
        
        # Don't show menu after the final boss
        if i < len(biomes) - 1:
            menu_result = ingamemenu(player)
            if menu_result == "exit_to_main":
                return
    
    print('Gratulálok! Sikeresen végigjátszottad a játékot!')
    wait(3)
    b()
        
            
def new_game():
    """Create a new game with starter Pokemon selection"""
    clear()
    print("🌟 Új kaland kezdődik! 🌟")
    print()
    name = input("Add meg a neved: ")
    
    clear()
    print(f"Üdvözöllek a prokemon világában, {name}!")
    print()
    print("🎯 Válassz egy kezdő prokemot:")
    
    # Starter Pokemon options (Bulbasaur, Charmander, Squirtle)
    starters = [
        classes.osszespokemon[0],   # Bulbasaur
        classes.osszespokemon[3],   # Charmander  
        classes.osszespokemon[6]    # Squirtle
    ]
    
    starter_options = []
    for i, starter in enumerate(starters, 1):
        starter_options.append(f"{starter.name} - {starter.type1}" + 
                             (f"/{starter.type2}" if starter.type2 else ""))
    
    choice = menu.generic_menu("Válassz kezdő prokemot", starter_options)
    
    selected_starter = starters[int(choice) - 1]
    starter_nickname = input(f"Add meg a(z) {selected_starter.name} becenevét (vagy hagyd üresen): ").strip()
    
    if not starter_nickname:
        starter_nickname = selected_starter.name
    
    # Create starter Pokemon with full health
    starter_pokemon = classes2.Player_pokemon(
        starter_nickname, 
        selected_starter, 
        selected_starter.hp, 
        100
    )
    
    # Give player some starting items
    starting_items = []
    if hasattr(classes2, 'all_items') and classes2.all_items:
        # Add some healing items if available
        try:
            starting_items = [classes2.all_items[0]] * 3  # 3 healing items
        except:
            pass
    
    player = classes2.Player(name, starting_items, [starter_pokemon])
    
    clear()
    print(f"🎉 Sikeresen kiválasztottad: {starter_nickname}!")
    print(f"💚 Életerő: {starter_pokemon.health}/{starter_pokemon.pokemon.hp}")
    print(f"⚔️ Támadás: {starter_pokemon.pokemon.atk}")
    print(f"🛡️ Védekezés: {starter_pokemon.pokemon.defe}")
    print(f"💨 Sebesség: {starter_pokemon.pokemon.speed}")
    input("Nyomj Enter-t a folytatáshoz...")
    
    return player

def ingamemenu(player):
    """In-game menu with navigation options"""
    while True:
        clear()
        choice = menu.generic_menu("Játék menü", [
            "Tovább a következő biomra", 
            "Irány valamelyik puszta", 
            "Mentés",
            "Prokemonok megtekintése",
            "Kilépés a főmenübe"
        ])
        
        match choice:
            case '1':
                return
            case '2':
                biome_choice = menu.generic_menu("Válassz egy biomot", [
                    "Füves biom", 
                    "Felhő biom", 
                    "Hegyvidék biom", 
                    "Alvilág biom",
                    "Vissza"
                ])
                match biome_choice:
                    case '1':
                        puszta(player, ['Normal', 'Grass', 'Water', 'Ground', 'Poison'])
                        return
                    case '2':
                        puszta(player, ['Electric', 'Ice', 'Flying', 'Bug'])
                        return
                    case '3':
                        puszta(player, ['Rock', 'Fighting'])
                        return
                    case '4':
                        puszta(player, ['Fire', 'Psychic', 'Ghost', 'Dragon'])
                        return
                    case '5':
                        continue  # Go back to main menu
                    case _:
                        print('Érvénytelen választás!')
                        wait(1)
            case "3":
                try:
                    classes.save(player)
                except Exception as e:
                    print(f"Mentés sikertelen: {e}")
                    wait(2)
            case "4":
                # Show player's pokemons
                if player.pokemons:
                    show_player_pokemons(player)
                else:
                    print("Még nincsenek prokemonaid!")
                    wait(2)
            case "5":
                confirm = input("Biztosan ki akarsz lépni a főmenübe? (i/n): ").lower()
                if confirm == 'i':
                    return "exit_to_main"
            case _:
                print('Érvénytelen választás!')
                wait(1)

def show_player_pokemons(player):
    """Display player's current pokemons"""
    clear()
    print("=== PROKEMONAID ===")
    print("-" * 40)
    if not player.pokemons:
        print("Még nincsenek prokemonaid!")
    else:
        for i, pokemon in enumerate(player.pokemons, 1):
            print(f"{i}. {pokemon.nickname} ({pokemon.pokemon.name})")
            print(f"   Típus: {pokemon.pokemon.type1} {pokemon.pokemon.type2}".strip())
            print(f"   Életerő: {pokemon.health}/{pokemon.pokemon.hp}")
            print(f"   Energia: {pokemon.energy}/100")
            print("-" * 40)
    input("Nyomj Enter-t a folytatáshoz...")








if __name__ == "__main__":
    main()