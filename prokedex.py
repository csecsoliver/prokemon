import menu
import classes
from classes2 import clearscreen as clear
import time


def main(external=True):
    if external == False:
        clear()
        print("Prokemon kódex")
        time.sleep(0.5)
        input("Nyomjon meg egy gombot a folytatáshoz...")
        clear()
        mode = menu.generic_menu("Prokedex", ["Prokemonok böngészése", "Keresés", "Prokemonok összehasonlítása", "Új prokemon készítése", "Kilépés"])
    elif external is True:
        clear()
        mode = menu.generic_menu("Prokedex", ["Prokemonok böngészése", "Keresés", "Prokemonok összehasonlítása", "Új prokemon készítése", "Vissza a főmenübe"])
    elif external == "nope":
        clear()
        mode = menu.generic_menu("Prokedex", ["Prokemonok böngészése", "Keresés", "Prokemonok összehasonlítása", "Új prokemon készítése", "Kilépés"])
    
    match mode:
        case "1":
            clear()
            print("Prokemonok betöltése...")
            time.sleep(0.5)
            clear()
            browse()
        case "2":
            clear()
            search()
        case "3":
            clear()
            compare()
        case "4":
            clear()
            create()
        case "5":
            return
        case "0":
            clear()
            if external is not True:
                print("Kilépés...")
                time.sleep(0.5)
            return
        case _:
            print("Nem opció")
            time.sleep(0.5)
            main("nope")
        

def browse(num_of_first = 0):
    clear()
    choice = menu.generic_menu("Összes pokemon", ["Vissza","Fel", classes.osszespokemon[num_of_first + 0].name, classes.osszespokemon[num_of_first + 1].name, classes.osszespokemon[num_of_first + 2].name, classes.osszespokemon[num_of_first + 3].name, classes.osszespokemon[num_of_first + 4].name, classes.osszespokemon[num_of_first + 5].name, classes.osszespokemon[num_of_first + 6].name, "Tovább"])
    match choice:
        case "1":
            return True
        case "2":
            back = browse(num_of_first - 5)
            if back == True:
                return True
        case "10":
            back = browse(num_of_first + 5)
            if back == True:
                return True
        case _:
            if choice.isnumeric():
                if int(choice) in [3,4,5,6,7,8,9]:
                    view_prokemon(num_of_first + (int(choice)-3))







if __name__ == "__main__":
    main(False)