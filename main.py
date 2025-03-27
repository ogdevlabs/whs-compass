from src.game import Game
import pyfiglet
import time
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_text(text, delay=0.1):
    for i in range(1, len(text) + 1):
        clear_console()
        print(pyfiglet.figlet_format(text[:i]))
        time.sleep(delay)
def main():
    animated_text('Compass', delay=0.2)
    animated_text('RPS Game', delay=0.2)
    rps = Game()
    print('\n')
    state = True
    while state:
        state = rps.play_round()


if __name__=="__main__":
    main()