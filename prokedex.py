import menu
import classes
from classes import clearscreen as clear
from time import sleep as wait


def main(external=True):
    if external == False:
        clear()
        print("Prokemon kódex")
        wait(0.5)
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
            wait(0.5)
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
                wait(0.5)
            return
        case _:
            print("Nem opció")
            wait(0.5)
            main("nope")
        

def browse(num_of_first = 0, to_browse=classes.osszespokemon):
    clear()
    choice = menu.generic_menu("Összes pokemon", ["Vissza","Fel", to_browse[num_of_first + 0].name, to_browse[num_of_first + 1].name, to_browse[num_of_first + 2].name, to_browse[num_of_first + 3].name, to_browse[num_of_first + 4].name, to_browse[num_of_first + 5].name, to_browse[num_of_first + 6].name, "Tovább"])
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

def view_prokemon(num):
    prokemon = classes.osszespokemon[num]
    clear()
    choice = menu.generic_menu(prokemon.name, [f"Típusa: {prokemon.type1} {prokemon.type2}", f"Életpontok: {prokemon.hp}", f"Támadás: {prokemon.atk}", f"Védekezés: {prokemon.defe}", f"Sebessége: {prokemon.speed}", f"vissza"]) 
    filtered = []
    match choice:
        case "6":
            return
        case "1":
            for i in classes.osszespokemon:
                if i.type1 == prokemon.type1 or i.type2 == prokemon.type1 or i.type1 == prokemon.type2 or i.type2 == prokemon.type2:
                    filtered.append(i)
            browse(0, filtered)
        case "2":
            for i in classes.osszespokemon:
                if i.hp == prokemon.hp or (i.hp - prokemon.hp < 10 and i.hp - prokemon.hp > -10):
                    filtered.append(i)
            browse(0, filtered)
        case "3":
            for i in classes.osszespokemon:
                if i.atk == prokemon.atk or (i.atk - prokemon.atk < 10 and i.atk - prokemon.atk > -10):
                    filtered.append(i)
            browse(0, filtered)
        case "4":
            for i in classes.osszespokemon:
                if i.defe == prokemon.defe or (i.defe - prokemon.defe < 10 and i.defe - prokemon.defe > -10):
                    filtered.append(i)
            browse(0, filtered)
        case "5":
            for i in classes.osszespokemon:
                if i.speed == prokemon.speed or (i.speed - prokemon.speed < 10 and i.speed - prokemon.speed > -10):
                    filtered.append(i)
            browse(0, filtered)
        case _:
            print("Nem opció")
            wait(1)
            view_prokemon(num)



def search():
    clear()
    query = input("Keresés: ")
    results = []
    for i, p in enumerate(classes.osszespokemon):
        if query.lower() in p.name.lower():
            results.append(p)
    if len(results) == 0:
        print("Nincs találat")
        wait(1)
        search()
    else:
        browse(0, results)
    wait(1)
    search()

if __name__ == "__main__":
    main(False)