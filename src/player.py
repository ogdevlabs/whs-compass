class Player:
    def get_choice(self):
        """Player would be entering an input to play;
        player input is limited
        to valid game options"""
        while True:
            print("Enter q to exit")
            choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
            if choice in ['rock', 'paper', 'scissors']:
                return choice
            elif choice == 'q':
                return False
            else:
                print(f"Invalid selection: {choice} is not a valid option")