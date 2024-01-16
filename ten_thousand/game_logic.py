import random

class GameLogic:
    def __init__(self):
        # Initialize any required attributes for the game logic
        pass

    def start_game(self):
        # Add logic to start the game
        pass

    def roll_dice(self):
        # Add logic to simulate rolling dice
        pass

    @staticmethod
    def roll_dice(num_dice):
    # Simulate rolling a given number of dice and return the values
        return [random.randint(1, 6) for _ in range(num_dice)]

    @staticmethod
    def calculate_score(dice_values):
        # Add logic to calculate the score based on the provided dice values
        # Replace this with your actual scoring logic

        if len(dice_values) == 1 and dice_values[0] == 5:
            return 50
        else:
            return sum(dice_values)