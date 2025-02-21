from src.game import Game


def main():
    rps = Game()
    print('Welcome to RPS Game, type exit to leave the game, enjoy =)')
    print('\n')
    state = True
    while state:
        state = rps.play_round()


if __name__=="__main__":
    main()