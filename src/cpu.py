import random
class Cpu:
    def get_choice(self):
        """Randomly selects rock, paper, or scissors."""
        return random.choice(["rock","paper","scissors"])