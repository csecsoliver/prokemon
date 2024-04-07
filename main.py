import classes
import classes2
import menu
from classes import clearscreen as clear
from time import sleep as wait
import prokedex

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
    
    match choice:
        case "1":
            player = new_game()
            
        case "2":
            player = classes.load_a_save() # ez még nincs megírva
        case "3":
            return True
    if choice == "1":
        clear()
        print(f"Üdvözöllek {player.name}!")
        wait(1)
        clear()
        print("Ez egy pokemon játék.")
        wait(1)
        clear()
        print("A játék célja, hogy minél erősebb prokemonokat gyűjts össze, és legyőzd a legerősebb ellenfeleket is.")
        wait(1)
        clear()
        print("A játékban a pokemontokat prokelabdákkal gyűjtheted össze.")
        wait(1)
        clear()
        print("A prokemontokat a harcokban használhatod.")
        wait(1)
        clear()
        print("A játékban a prokemontokat a Prokedexben tudod megnézni.")
        wait(1)
        clear()
        print("A prokedex elindítható a főmenüből, vagy a külön fájllal is.")
        
            
def new_game():
    clear()
    name = input("Add meg a neved: ")
    return classes2.Player(name, [], [])










if __name__ == "__main__":
    main()