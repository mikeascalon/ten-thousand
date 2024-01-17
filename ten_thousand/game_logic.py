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



        if len(dice_values) == 1:
            if dice_values[0] == 5:
                return 50
            elif dice_values[0] == 1:
                return 100
            elif dice_values[0] == 2:
                return 0
            elif len(set(dice_values)) == 1 and 1 not in dice_values and 5 not in dice_values:
            #     return sum({
            #         (2): 0,
            #         (3): 0,
            #         (4): 0,
            #         (6): 0
            #     }.get(tuple(sorted(dice_values)), 0))
                return 0
            
        elif len(dice_values) == 2:
            if all(value == 5 for value in dice_values):
                return 100
            elif all(value == 1 for value in dice_values):
                return 200
            elif set(dice_values) == {1, 5}:
                return 150
            elif any(dice_values.count(value) == 2 for value in set(dice_values)):
                # return sum({
                #     (2, 2): 0,
                #     (3, 3): 0,
                #     (4, 4): 0,
                #     (6, 6): 0
                # }.get(tuple(sorted(dice_values)), 0))
                return 0
            
        elif len(dice_values) >= 3:
            count_fives = dice_values.count(5)
            count_ones = dice_values.count(1)
            counts = {num: dice_values.count(num) for num in set(dice_values)}
            if count_ones == 3 and count_fives == 1:
                return 1050
            elif count_fives == 3:
                return 500
            elif sorted(dice_values) == [1, 2, 3, 4, 5, 6]:
                return 1500
            elif any(dice_values.count(value) == 3 for value in set(dice_values)):
                return sum({
                    1: 1000,
                    2: 200,
                    3: 300,
                    4: 400,
                    5: 500,
                    6: 600
                }.get(value, 0) for value in set(dice_values))
            elif any(dice_values.count(value) == 4 for value in set(dice_values)):
                return sum({
                    1: 2000,
                    2: 400,
                    3: 600,
                    4: 800,
                    5: 1000,
                    6: 1200
                }.get(value, 0) for value in set(dice_values))
            elif any(dice_values.count(value) == 5 for value in set(dice_values)):
                return sum({
                    1: 3000,
                    2: 600,
                    3: 900,
                    4: 1200,
                    5: 1500,
                    6: 1800
                }.get(value, 0) for value in set(dice_values))
            elif any(dice_values.count(value) == 6 for value in set(dice_values)):
                return sum({
                    1: 4000,
                    2: 800,
                    3: 1200,
                    4: 1600,
                    5: 2000,
                    6: 2400
                }.get(value, 0) for value in set(dice_values))
            
            elif all(count == 2 for count in counts.values()):
                return 1500

            elif any(dice_values.count(value) < 3 for value in set(dice_values)) and dice_values.count(1) == 0  and dice_values.count(5) == 0:
                return 0
            

        return sum(dice_values)
        # return 0
    