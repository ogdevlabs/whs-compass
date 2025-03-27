# Core game logic
from src.cpu import Cpu
from src.player import Player


class Game:
    CHOICES = ["rock","paper","scissors"]

    def __init__(self):
        self.player = Player()
        self.cpu = Cpu()

    def play_round(self):
        """Handles single game round"""
        player_choice = self.player.get_choice()
        # Terminate is user enter exit
        if not player_choice:
            return False
        cpu_choice = self.cpu.get_choice()
        winner = self.determine_winner(player_choice, cpu_choice)
        print(f"\nYou chose: {player_choice}, CPU chose: {cpu_choice}")
        print(f"Winner: {winner.upper()}" if winner != "draw" else "It's a DRAW!")
        print('\n')
        return True

    def determine_winner(self, player_choice, cpu_choice):
        """Determines the winner of a round."""
        if player_choice == cpu_choice:
            return "draw"
        elif (player_choice == "rock" and cpu_choice == "scissors") or \
                (player_choice == "scissor" and cpu_choice == "paper") or \
                (player_choice == "paper" and cpu_choice == "rock"):
            return "player"
        else:
            return "cpu"
