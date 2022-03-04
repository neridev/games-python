import random

welcome_screen="""
___  ___          _           ___  ____           _
|  \/  |         | |          |  \/  (_)         | |
| .  . | __ _ ___| |_ ___ _ __| .  . |_ _ __   __| |
| |\/| |/ _` / __| __/ _ \ '__| |\/| | | '_ \ / _` |
| |  | | (_| \__ \ ||  __/ |  | |  | | | | | | (_| |
\_|  |_/\__,_|___/\__\___|_|  \_|  |_/_|_| |_|\__,_|
"""
navod="""Pravidla su nasledovne: Ja si myslim cislo od 1 po 10, a ty budes hadat.
Ak chces ukoncit hru napis 'KONIEC'.
Na konci hry uvidis svoj skore."""

print(welcome_screen)
meno_hraca = input("Zadaj svoje meno: ")

print("Super, {}.".format(meno_hraca))
print(navod)

spravne = 0
nespravne = 0
celkom = 0
nahodne_cislo = random.randint(1, 10)

while True:
    tipujem_cislo = str(input('Tvoj tip?:')).lower().strip()
    nahodne_cislo = random.randint(1, 10)
    try:
        if tipujem_cislo == '':
            print('Nastala chyba, nezadal si ziadne cislo, hra bude ukoncena!')
            break
        elif tipujem_cislo == 'koniec':
            print('Koniec hry', meno_hraca, '.')
            print('+-----tvoje skóre-----+')
            print('| správne    |    ', spravne,  '|')
            print('| nesprávne  |    ', nespravne,  '|')
            print('| celkom     |    ', celkom,  '|')
            print('+=====================+')
            break
        elif int(tipujem_cislo) < 1 or int(tipujem_cislo) > 10:
            print('Zadal si cislo mimo razsah 1-10.')
        elif int(tipujem_cislo) == nahodne_cislo:
            print('Super, spravne!!!')
            spravne += 1
            celkom += 1
        elif int(tipujem_cislo) != nahodne_cislo:
            print('Nespravne!')
            nespravne += 1
            celkom += 1
    except Exception as e:
        print('Nastala vynimka:')
        print(e)
