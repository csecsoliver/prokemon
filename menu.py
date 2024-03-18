from os import system

def generic_menu(title, options):
    for i in range(len(options)):
        for adat in options:
            print(f'{i} - {adat}')

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
