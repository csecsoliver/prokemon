from os import system
import time
from classes import clearscreen as clear

def generic_menu(title, options):
    """
    Displays a menu with title and options, returns user's choice with validation
    """
    while True:
        clear()
        print(title)
        print("-" * 60)
        for i in range(10):
            if i < len(options):
                print(f"""│ {f"{i + 1}. {options[i]}".ljust(56)} │""")
            else:
                print("│" + " " * 58 + "│")
        print("-" * 60)
        
        try:
            choice = input("Válasz (szám): ").strip()
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    return choice
                else:
                    print(f"Kérlek válassz 1 és {len(options)} között!")
                    time.sleep(1)
            else:
                print("Kérlek adj meg egy számot!")
                time.sleep(1)
        except (ValueError, KeyboardInterrupt):
            print("Érvénytelen bemenet!")
            time.sleep(1) 

def title_screen():
    """Display the main title screen with error handling"""
    while True:
        clear()
        print("PROKEMON, eskü pokemon")
        print("-" * 60)
        print(f"| 1 - Játék indítása" + " "* 39 + "|")
        print(f"| 2 - Prokedex megnyitása" + " "*34 + "|")
        print(f"| 3 - Kilépés" + " "*46 + "|")
        print("-" * 60)
        try:
            answer = input(f"Válassz (1-3): ").strip()
            if answer in ["1", "2", "3"]:
                return answer
            else:
                print("Kérlek válassz 1, 2 vagy 3 közül!")
                time.sleep(1)
        except (ValueError, KeyboardInterrupt):
            print("Érvénytelen bemenet!")
            time.sleep(1)
    
    