from os import system
import time

def generic_menu(title, options):
    """
    kap egy címet és egy listát, a listában vannak a választási lehetőségek
    ellenőrzés és formázás nélkül adja vissza a felhasználó válaszát
    """
    print(title)
    print("-" * 60)
    for i in range(10):
        if i < len(options):
            print(f"""│ {f"{i + 1}. {options[i]}".ljust(56)} │""")
        else:
            print("│" + " " * 58 + "│")
    print("-" * 60)
    return input("Válasz: ") 

def title_screen():
    system("cls")
    print("PROKEMON, eskü pokemon")
    print("-" * 60)
    print(f"| 1 - Játék indítása" + " "* 39 + "|")
    print(f"| 2 - Inventory megnyitása" + " "*33 + "|")
    print(f"| 3 - Prokedex megnyitása" + " "*33 + "|")
    print(f"| 0 - Kilépés" + " "*46 + "|")
    print("-" * 60)
    try:
        answer = int(input(f"Válasz: "))
    except:
        print("Nem opció.")
        time.sleep(0.5)
        title_screen()
    system("cls")
    match answer:
        case 0:
            exit()
        case 1:
            print("Játék indítása...")
            time.sleep(0.5)
            system("cls")
            print("Map betöltése...")
            time.sleep(0.5)
            system("cls")
            print("Karakter előkészítése...")
            time.sleep(0.5)
            system("cls")
            print("Inventory betöltése...")
            time.sleep(0.5)
        case 2:
            print("Inventory megnyitása...")
            time.sleep(0.5)
        case 3:
            print("Betöltés...")
            time.sleep(0.5)
