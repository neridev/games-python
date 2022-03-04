# Programmed by following this course: https://youtu.be/t4GbksiCEUE

from game_handler import check_game
from grid_handler import print_grid, create_grid
from input_handler import get_input

rows = 3
columns = 3
empty_sign = '_'
player_dict = {
    0: 'x',
    1: 'o'
}
grid = create_grid(rows, columns)
empty_places = rows*columns
move_counter = 0
game_ended = 0

for round_id in range(1, 6):
    print("Cislo kola je:", round_id)
    for player in range(0, 2):
        while True:
            print('Na tahu je hrac cislo:', player+1)
            print_grid(grid, rows, columns)
            print('Zadajte X suradnicu')
            x = get_input()
            print('Zadajte Y suradnicu')
            y = get_input()
            print('Zadali ste suradnice:', x , y)
            if x >= rows or x < 0 or y >= columns or y < 0:
                print('Zadali ste suradnice mimo hracej plochy, zadajte suradnice znova.')
                continue
            if grid[x][y] != empty_sign:
                print('Policko je obsadene, zadajte nove suradnice.')
                continue
            else:
                break
        grid[x][y] = player_dict[player]
        if check_game(grid, rows, columns, player_dict[player]):
            print('Hrac', player+1, 'vyhral!')
            print_grid(grid, rows, columns)
            game_ended = True
            break
        move_counter += 1
        if move_counter == empty_places:
            print('Nie su uz mozne ziadne taky - REMIZA!')
            print_grid(grid, rows, columns)
            break
    if move_counter == empty_places:
        break
    if game_ended:
        print('GRATULACIA!')
        break