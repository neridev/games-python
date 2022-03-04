import sys

def get_input():
    while True:
        try:
            x = int(sys.stdin.readline())
        except Exception:
            print('Zadajte cele cislo!')
            continue
        break
    return x
