from ten_thousand.game_logic import GameLogic
import random

class TenThousandGame:
    def __init__(self):
        self.game_logic = GameLogic()
        self.total_points = 0
        self.max_rounds = 10

    def play_round(self, round_number):
        print(f"Starting round {round_number}")
        print(f"Rolling 6 dice...")

        unbanked_points = 0
        remaining_dice = 6


        while True:
            print(f"Rolling {remaining_dice} dice...")
            dice_result = self.game_logic.roll_dice(remaining_dice)
            print("***", " ".join(map(str, dice_result)), "***")

            user_input = input("Enter dice to keep, or (q)uit:\n> ")

            if user_input.lower() == 'q':
                print(f"Thanks for playing. You earned {self.total_points} points")
                break

            user_dice = list(map(int, user_input.split()))
            round_points = self.game_logic.calculate_score(user_dice)
            unbanked_points += round_points
            remaining_dice -= len(user_dice)

            print(f"You have {unbanked_points} unbanked points and {remaining_dice} dice remaining")

            action = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

            if action.lower() == 'b':
                self.total_points += unbanked_points
                print(f"You banked {unbanked_points} points in round {round_number}")
                print(f"Total score is {self.total_points} points")
                break
            elif action.lower() == 'q':
                print(f"Thanks for playing. You earned {self.total_points} points")
                break

    def play(self):
        print("Welcome to Ten Thousand")
        response = input("(y)es to play or (n)o to decline\n> ")

        if response.lower() == 'y':
            for round_number in range(1, self.max_rounds + 1):
                self.play_round(round_number)
                if round_number < self.max_rounds:
                    continue_playing = input("Do you want to play another round? (y/n)\n> ")
                    if continue_playing.lower() != 'y':
                        break

        elif response.lower() == 'n':
            print("OK. Maybe another time.")
        else:
            print("Invalid input. Please enter 'y' or 'n.'")

if __name__ == "__main__":
    game = TenThousandGame()
    game.play()