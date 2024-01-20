# AI Propmt

## Input 
give me a python file that have this 
Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.
Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

## AI output


Here's a Python file that defines a GameLogic class in a file named game_logic.py with the specified functionality:

```python
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll according to the rules of the game.

        Args:
            dice_roll (tuple): A tuple of integers representing a dice roll.

        Returns:
            int: The score for the given dice roll.
        """
        score = 0
        # Define the scoring rules for the game
        scoring_rules = {
            1: 100,  # Each 1 is worth 100 points
            5: 50,   # Each 5 is worth 50 points
        }

        # Calculate the score based on the rules
        for die in dice_roll:
            if die in scoring_rules:
                score += scoring_rules[die]

        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a specified number of dice and return the results as a tuple.

        Args:
            num_dice (int): The number of dice to roll.

        Returns:
            tuple: A tuple containing random values between 1 and 6.
        """
        if not 1 <= num_dice <= 6:
            raise ValueError("Number of dice must be between 1 and 6")

        dice_results = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice_results

# Example usage:
# dice_roll = GameLogic.roll_dice(5)  # Roll 5 dice
# score = GameLogic.calculate_score(dice_roll)
# print("Dice Roll:", dice_roll)
# print("Score:", score)
```

## Input

User
i need the roll_dice to handle this test
def test_1_dice():
    values = GameLogic.roll_dice(1)
    assert len(values) == 1
    value = values[0]
    assert 1 <= value <= 6


def test_2_dice():
    values = GameLogic.roll_dice(2)
    assert len(values) == 2

    for value in values:
        assert 1 <= value <= 6


def test_3_dice():
    values = GameLogic.roll_dice(3)
    assert len(values) == 3

    for value in values:
        assert 1 <= value <= 6


def test_4_dice():
    values = GameLogic.roll_dice(4)
    assert len(values) == 4

    for value in values:
        assert 1 <= value <= 6


def test_5_dice():
    values = GameLogic.roll_dice(5)
    assert len(values) == 5

    for value in values:
        assert 1 <= value <= 6


def test_6_dice():
    values = GameLogic.roll_dice(6)
    assert len(values) == 6

    for value in values:
        assert 1 <= value <= 6

## AI output

```python
import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        """
        Calculate the score for a given dice roll according to the rules of the game.

        Args:
            dice_roll (tuple): A tuple of integers representing a dice roll.

        Returns:
            int: The score for the given dice roll.
        """
        score = 0
        # Define the scoring rules for the game
        scoring_rules = {
            1: 100,  # Each 1 is worth 100 points
            5: 50,   # Each 5 is worth 50 points
        }

        # Calculate the score based on the rules
        for die in dice_roll:
            if die in scoring_rules:
                score += scoring_rules[die]

        return score

    @staticmethod
    def roll_dice(num_dice):
        """
        Roll a specified number of dice and return the results as a tuple.

        Args:
            num_dice (int): The number of dice to roll.

        Returns:
            tuple: A tuple containing random values between 1 and 6.
        """
        if not 1 <= num_dice <= 6:
            raise ValueError("Number of dice must be between 1 and 6")

        dice_results = tuple(random.randint(1, 6) for _ in range(num_dice))
        return dice_results

# Example usage:
# dice_roll = GameLogic.roll_dice(5)  # Roll 5 dice
# score = GameLogic.calculate_score(dice_roll)
# print("Dice Roll:", dice_roll)
# print("Score:", score)
```
