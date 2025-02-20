from src.game import Game


def main():
    rps = Game()

    while True:
        rps.play_round()

        print("Leaving game...")
        return

if __name__=="__main__":
    main()