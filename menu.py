from os import system


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