from os import system


def generic_menu(options):
    for i in range(len(options)):
        for adat in options:
            print(f'{i} - {adat}')

def fomenu():
    system('cls')
    print('1 - Játék indítása')
    print('2 - Inventory megnyitása') 
    print('3 - Pokemonok hozzáadása')
    print('0 - Kilépés')
    answer = int(input('Válasz: '))
    system('cls')
    match answer:
        case 0:
            exit()
        case 1:
            input('Játék indítása...')
        case 2:
            input('Inventory megnyitása...')
        case 3:
            input('Betöltés...')

fomenu()
generic_menu()