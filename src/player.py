class Player:
    def get_choice(self):
        """Player would be entering an input to play;
        player input is limited
        to valid game options"""
        while True:
            choice = input("Enter rock, paper, or scissors: ").strip().lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            elif choice == 'exit':
                return False
            else:
                print(f"Invalid selection: {choice} is not a valid option")