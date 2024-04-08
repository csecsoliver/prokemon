import menu
import classes
import classes2
from classes import clearscreen as clear
from time import sleep as wait


def main(external=True):
    if external == False:
        clear()
        print("Prokemon kódex")
        wait(0.5)
        input("Nyomjon meg egy gombot a folytatáshoz...")
        clear()
        mode = menu.generic_menu("Prokedex", ["Prokemonok böngészése", "Keresés", "Fejlett keresés", "Új prokemon készítése", "Kilépés"])
    elif external is True:
        clear()
        mode = menu.generic_menu("Prokedex", ["Prokemonok böngészése", "Keresés", "Fejlett keresés", "Új prokemon készítése", "Vissza a főmenübe"])
    elif external == "nope":
        clear()
        mode = menu.generic_menu("Prokedex", ["Prokemonok böngészése", "Keresés", "Fejlett keresés", "Új prokemon készítése", "Kilépés"])
    
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
            adv_search()
        case "4":
            clear()
            create()
        case "5":
            clear()
            if external is not True:
                print("Kilépés...")
                wait(0.5)
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
        

def browse(num_of_first = 0, to_browse=classes.osszespokemon, title="Összes prokemon"):
    clear()
    
    if num_of_first <0: num_of_first = 0
    if num_of_first > len(to_browse):
        num_of_first = len(to_browse)
    to_browse_filtered = []
    for i in range(7):
        if len(to_browse) > num_of_first + i:
            to_browse_filtered.append(to_browse[num_of_first + i])
        else:
            to_browse_filtered.append(classes2.Item([0, "", 0, 0, 0, 0, 0]))
    # choice = menu.generic_menu(title, ["Vissza","Fel", to_browse_filtered[num_of_first + 0].name, to_browse_filtered[num_of_first + 1].name, to_browse_filtered[num_of_first + 2].name, to_browse_filtered[num_of_first + 3].name, to_browse_filtered[num_of_first + 4].name, to_browse_filtered[num_of_first + 5].name, to_browse_filtered[num_of_first + 6].name, "Tovább"])
    choice = menu.generic_menu(title, ["Vissza","Fel", to_browse_filtered[0].name, to_browse_filtered[1].name, to_browse_filtered[2].name, to_browse_filtered[3].name, to_browse_filtered[4].name, to_browse_filtered[5].name, to_browse_filtered[6].name, "Tovább"])
    
    match choice:
        case "1":
            return True
        case "2":
            back = browse(num_of_first - 5, to_browse, title)
            if back == True:
                return True
        case "10":
            back = browse(num_of_first + 5, to_browse, title)
            if back == True:
                return True
        case _:
            if choice.isnumeric():
                if int(choice) in [3,4,5,6,7,8,9]:
                    if type(to_browse_filtered[int(choice)-3]) == classes2.Item:
                        browse(num_of_first, to_browse, title)
                    view_prokemon(num_of_first + (int(choice)-3), to_browse)


def view_prokemon(num, collection=classes.osszespokemon):
    prokemon = collection[num]
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
            filtered = search_by_stat(classes.osszespokemon, prokemon.hp, "1")
            
            browse(0, filtered)
        case "3":
            filtered = search_by_stat(classes.osszespokemon, prokemon.atk, "2")
            
            browse(0, filtered)
        case "4":
            filtered = search_by_stat(classes.osszespokemon, prokemon.defe, "3")
            
            browse(0, filtered)
        case "5":
            filtered = search_by_stat(classes.osszespokemon, prokemon.speed, "4")
            
            browse(0, filtered)
        case _:
            print("Nem opció")
            wait(1)
            view_prokemon(num)

def search_by_stat(collection=classes.osszespokemon, value=None, stat=None):
    filtered = []
    if stat == "1":
        for i in collection:
            if i.hp == value or (-10 < (i.hp - value) < 10):
                filtered.append(i)
    elif stat == "2":
        for i in collection:
            if i.atk == value or (-10 < (i.atk - value) < 10):
                filtered.append(i)
    elif stat == "3":
        for i in collection:
            if i.defe == value or (-10 < (i.defe - value) < 10):
                filtered.append(i)
    elif stat == "4":
        for i in collection:
            if i.speed == value or (-10 < (i.speed - value) < 10):
                filtered.append(i)
    elif stat == "5":
        for i in collection:
            if i.type1.lower() == value.lower() or i.type2.lower() == value.lower():
                filtered.append(i)
    return filtered

def adv_search():
    clear()
    match menu.generic_menu("Keresési lehetőségek", ["Típus", "Életpontok", "Támadás", "Védekezés", "Sebesség", "Vissza"]):
        case "1":
            type = input("Típus: ")
            browse(0, search_by_stat(classes.osszespokemon, type, "5"))
        case "2":
            hp = input("Életpontok: ")
            browse(0, search_by_stat(classes.osszespokemon, int(hp), "1"))
        case "3":
            atk = input("Támadás: ")
            browse(0, search_by_stat(classes.osszespokemon, int(atk), "2"))
        case "4":
            defe = input("Védekezés: ")
            browse(0, search_by_stat(classes.osszespokemon, int(defe), "3"))
        case "5":
            speed = input("Sebesség: ")
            browse(0, search_by_stat(classes.osszespokemon, int(speed), "4"))
        case "6":
            return
    
    

def search():
    clear()
    query = input("Keresés: ")
    results = []
    for i, p in enumerate(classes.osszespokemon):
        if query.lower() in p.name.lower():
            results.append(p)
            
    if query == "":
        return
    if len(results) == 0:
        print("Nincs találat")
        wait(1)
        search()
    else:
        browse(0, results, "Keresési eredmények")
    
    search()
    

def create():
    clear()
    name = input("Prokemon neve: ")
    
    type1 = input("Típus 1: ")

    type2 = input("Típus 2: ")
    
    while True:
        hp = input("Életpontok: ")
        if hp.isnumeric() == False:
            print("Csak számot adjon meg!")
            wait(1)
        else:
            hp = int(hp)
            break
    while True:
        atk = input("Támadás: ")
        if atk.isnumeric() == False:
            print("Csak számot adjon meg!")
            wait(1)
        else:
            atk = int(atk)
            break
    while True:
        defe = input("Védekezés: ")
        if defe.isnumeric() == False:
            print("Csak számot adjon meg!")
            wait(1)
        else:
            defe = int(defe)
            break
    while True:
        speed = input("Sebesség: ")
        if speed.isnumeric() == False:
            print("Csak számot adjon meg!")
            wait(1)
        else:
            speed = int(speed)
            break
    
    new = classes.Pokemon(f"0,{name},{type1},{type2},0,{hp},{atk},{defe},0,0,{speed},0,0")
    classes.osszespokemon.append(new)
    print("Prokemon létrehozása...")
    wait(2)
    print("Prokemon létrehozva!")
    wait(1)
    file = open("pokemon.csv", "a", encoding="utf8")
    file.write(f"{len(classes.osszespokemon)},{name},{type1},{type2},{hp+atk+defe+speed},{hp},{atk},{defe},0,0,{speed},1,False\n")
    

if __name__ == "__main__":
    main(False)