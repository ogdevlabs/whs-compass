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
        cpu_choice = self.cpu.get_choice()
