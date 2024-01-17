import random
import sys

print('HRA - KAMEN, PAPIER, NOZNICE')

# Premenne pre ulozenie - vyhry, prehry, remizy
vyhry = 0
prehry = 0
remizy = 0

while True:  # The main game loop.
    print('%s Vyhry, %s Prehry, %s Remizy' % (vyhry, prehry, remizy))

    while True:  # The player input loop.
        print('Zadaj tvoj tah: (k)amen (p)apier (n)noznice or (q)uit')
        playerMove = str(input('Tvoj tah:')).lower().strip()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove == 'k' or playerMove == 'p' or playerMove == 'n':
            break  # Break out of the player input loop.
        print('Mas na vyber z nasledovnych moznosti: k, p, n, alebo q.')

    # Zobrazenie volby hraca
    if playerMove == 'k':
        print('KAMEN verzus...')
    elif playerMove == 'p':
        print('PAPIER verzus...')
    elif playerMove == 'n':
        print('NOZNICE verzus...')

    # Zobrazenie volby pocitaca
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'k'
        print('KAMEN')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPIER')
    elif randomNumber == 3:
        computerMove = 'n'
        print('NOZNICE')

    # Zobrazenie a ulozenie stavu vyhry/prehry/remizy:
    if playerMove == computerMove:
        print('Je to remiza!')
        remizy = remizy + 1
    elif playerMove == 'k' and computerMove == 'n':
        print('Vyhral si!')
        vyhry = vyhry + 1
    elif playerMove == 'p' and computerMove == 'k':
        print('Vyhral si!')
        vyhry = vyhry + 1
    elif playerMove == 'n' and computerMove == 'p':
        print('Vyhral si!')
        vyhry = vyhry + 1
    elif playerMove == 'k' and computerMove == 'p':
        print('Prehal si!')
        prehry = prehry + 1
    elif playerMove == 'p' and computerMove == 'n':
        print('Prehal si!')
        prehry = prehry + 1
    elif playerMove == 'n' and computerMove == 'k':
        print('Prehal si!')
        prehry = prehry + 1
