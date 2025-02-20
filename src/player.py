class Player:
    @staticmethod
    def get_choice():
        """Player would be entering an input to play,
        player input is limited
        to valid game options"""
        while True:
            choice = input("Enter rock. paper, scissors").strip().lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            print(f"Invalid selection: {choice} is not a valid option")