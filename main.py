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
        grassy_biom(player)
        ingamemenu(player)
        cloud_biom(player)
        ingamemenu(player)
        mountain_biom(player)
        ingamemenu(player)
        underworld_biom(player)
        ingamemenu(player)
        boss_biom(player)
        print('Gratulálok sikeresen végigjátszottad a játékot!')
        b()
        
            
def new_game():
    clear()
    name = input("Add meg a neved: ")
    return classes2.Player(name, [], [])

def ingamemenu(player):
    print('1 - Tovább a következő biomra')
    print('2 - Irány valamelyik puszta')
    print("3 - Mentés")
    valasz = input('Válasz: ')
    match valasz:
        case '1':
            return
        case '2':
            print('1 - Füves biom')
            print('1 - Felhő biom')
            print('1 - Hegyvidék biom')
            print('1 - Alvilág biom')
            valasz2 = input('Válasz: ')
            match valasz2:
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
        case "3":
            classes.save(player)
        case _:
            print('Nem opció')
            wait(1)
            ingamemenu(player)








if __name__ == "__main__":
    main()