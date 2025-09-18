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
    """Browse Pokemon with improved navigation and error handling"""
    while True:
        clear()
        
        if num_of_first < 0: 
            num_of_first = 0
        if num_of_first >= len(to_browse):
            num_of_first = max(0, len(to_browse) - 7)
        
        # Create menu options
        menu_options = ["Vissza"]
        if num_of_first > 0:
            menu_options.append("Előző oldal")
        
        # Add Pokemon names (up to 7)
        pokemon_count = 0
        pokemon_start_index = len(menu_options)
        for i in range(7):
            if num_of_first + i < len(to_browse):
                pokemon = to_browse[num_of_first + i]
                menu_options.append(f"{pokemon.name} (#{num_of_first + i + 1})")
                pokemon_count += 1
            else:
                break
        
        # Add next page option if there are more Pokemon
        if num_of_first + 7 < len(to_browse):
            menu_options.append("Következő oldal")
        
        # Show current page info
        start_num = num_of_first + 1
        end_num = min(num_of_first + 7, len(to_browse))
        full_title = f"{title} ({start_num}-{end_num} / {len(to_browse)})"
        
        choice = menu.generic_menu(full_title, menu_options)
        choice_num = int(choice)
        
        if choice_num == 1:  # Vissza
            return True
        elif choice_num == 2 and num_of_first > 0:  # Előző oldal
            num_of_first = max(0, num_of_first - 7)
        elif choice_num == len(menu_options) and num_of_first + 7 < len(to_browse):  # Következő oldal
            num_of_first += 7
        else:
            # Pokemon selection
            pokemon_index = choice_num - pokemon_start_index
            if 0 <= pokemon_index < pokemon_count:
                actual_index = num_of_first + pokemon_index
                view_prokemon(actual_index, to_browse)
            else:
                print("Érvénytelen választás!")
                wait(1)


def view_prokemon(num, collection=classes.osszespokemon):
    """Display detailed Pokemon information with better formatting"""
    if num >= len(collection):
        print("Prokemon nem található!")
        wait(2)
        return
        
    prokemon = collection[num]
    while True:
        clear()
        print(f"=== {prokemon.name.upper()} ===")
        print("-" * 50)
        print(f"Típus: {prokemon.type1}" + (f" / {prokemon.type2}" if prokemon.type2 else ""))
        print(f"Életpontok: {prokemon.hp}")
        print(f"Támadás: {prokemon.atk}")
        print(f"Védekezés: {prokemon.defe}")
        print(f"Sebesség: {prokemon.speed}")
        print("-" * 50)
        
        options = [
            "Hasonló típusú prokemonok",
            "Hasonló életpontú prokemonok", 
            "Hasonló támadású prokemonok",
            "Hasonló védekezésű prokemonok",
            "Hasonló sebességű prokemonok",
            "Vissza"
        ]
        
        choice = menu.generic_menu(f"{prokemon.name} részletei", options)
        
        match choice:
            case "1":  # Similar type
                filtered = []
                for pokemon in classes.osszespokemon:
                    if (pokemon.type1 == prokemon.type1 or pokemon.type2 == prokemon.type1 or 
                        pokemon.type1 == prokemon.type2 or pokemon.type2 == prokemon.type2):
                        filtered.append(pokemon)
                browse(0, filtered, f"Hasonló típusú prokemonok ({prokemon.type1})")
            case "2":  # Similar HP
                filtered = search_by_stat(classes.osszespokemon, prokemon.hp, "1")
                browse(0, filtered, f"Hasonló életpontú prokemonok (~{prokemon.hp})")
            case "3":  # Similar Attack
                filtered = search_by_stat(classes.osszespokemon, prokemon.atk, "2")
                browse(0, filtered, f"Hasonló támadású prokemonok (~{prokemon.atk})")
            case "4":  # Similar Defense  
                filtered = search_by_stat(classes.osszespokemon, prokemon.defe, "3")
                browse(0, filtered, f"Hasonló védekezésű prokemonok (~{prokemon.defe})")
            case "5":  # Similar Speed
                filtered = search_by_stat(classes.osszespokemon, prokemon.speed, "4")
                browse(0, filtered, f"Hasonló sebességű prokemonok (~{prokemon.speed})")
            case "6":  # Back
                return
            case _:
                print("Érvénytelen választás!")
                wait(1)

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