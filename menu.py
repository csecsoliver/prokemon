from os import system
import time
from classes import clearscreen as clear

def generic_menu(title, options):
    """
    kap egy címet és egy listát, a listában vannak a választási lehetőségek
    ellenőrzés és formázás nélkül adja vissza a felhasználó válaszát
    """
    clear()
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
    clear()
    print("PROKEMON, eskü pokemon")
    print("-" * 60)
    print(f"| 1 - Játék indítása" + " "* 39 + "|")
    print(f"| 2 - Prokedex megnyitása" + " "*34 + "|")
    print(f"| 3 - Kilépés" + " "*46 + "|")
    print("-" * 60)
    try:
        answer = int(input(f"Válassz: "))
    except:
        print("Nem opció.")
        time.sleep(1)
        answer = title_screen()
        
    return str(answer)
    
    