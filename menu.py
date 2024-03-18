from os import system

def generic_menu(title, options):
    print(title)
    print("-" * 60)
    for i in range(10):
        if i < len(options):
            print(f"│ {f"{i + 1}. {options[i]}".ljust(56)} │")
        else:
            print("│" + " " * 58 + "│")
    print("-" * 60)

def fomenu():

    system('cls')
    print("PROKEMON")
    print("-" * 60)
    print(f'| 1 - Játék indítása' + ' '* 39 + '|')
    print(f'| 2 - Inventory megnyitása' + ' '*33 + '|')
    print(f'| 3 - Pokemonok hozzáadása' + ' '*33 + '|')
    print(f'| 0 - Kilépés' + ' '*46 + '|')
    print("-" * 60)
    answer = int(input(f'Válasz: '))
    system('cls')
    match answer:
        case 0:
            exit()
        case 1:
            input('Játék indítása...')
            system('cls')
            input('Map betöltése...')
            system('cls')
            input('Karakter előkészítése...')
            system('cls')
            input('Inventory betöltése...')
        case 2:
            input('Inventory megnyitása...')
        case 3:
            input('Betöltés...')

fomenu()
