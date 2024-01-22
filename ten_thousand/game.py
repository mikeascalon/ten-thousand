from ten_thousand.game_logic import GameLogic
import random
import sys

def roll_and_score(roll_dice, remaining_dice, unbanked_points, total_points):
    print(f"Rolling {remaining_dice} dice...")
    dice_result = roll_dice(remaining_dice)
    print("*** ", " ".join(map(str, dice_result)), " ***")

     # Check for a zilch immediately after rolling
    if GameLogic.calculate_score(dice_result) == 0:
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        return [0, 0]  # Reset remaining dice and unbanked points

    while True:
        user_input = input("Enter dice to keep, or (q)uit:\n> ")

        if user_input.lower() == 'q':
            print(f"Thanks for playing. You earned {total_points} points")
            sys.exit()

        elif user_input.replace(" ", "").isnumeric():
            user_dice = tuple(int(char) for char in user_input if char.isnumeric())

            if all(dice_result.count(digit) >= user_dice.count(digit) for digit in set(user_dice)):
                round_points = GameLogic.calculate_score(user_dice)
                unbanked_points += round_points
                remaining_dice -= len(user_dice)

                print(f"You have {unbanked_points} unbanked points and {remaining_dice} dice remaining")
                return [remaining_dice, unbanked_points]
            else:
                print("Cheater!!! Or possibly made a typo...")
                print("*** ", " ".join(map(str, dice_result)), " ***")
        else:
            print("Invalid input. Please enter a numeric value or 'q' to quit.")

def play_round(roll_dice, round_number, total_points):
    print(f"Starting round {round_number}")

    unbanked_points = 0
    remaining_dice = 6

    while True:
        roll_and_score_result = roll_and_score(roll_dice, remaining_dice, unbanked_points, total_points)
        remaining_dice, unbanked_points = roll_and_score_result

        # Check for Zilch
        if unbanked_points == 0 and remaining_dice == 0:
            print(f"You banked 0 points in round {round_number}")
            print(f"Total score is {total_points} points")
            return [total_points, True]  # End the turn

        if remaining_dice == 0:
            remaining_dice = 6

        action = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

        if action.lower() == 'b':
            total_points += unbanked_points
            print(f"You banked {unbanked_points} points in round {round_number}")
            print(f"Total score is {total_points} points")
            return [total_points, True]
        elif action.lower() == 'q':
            print(f"Thanks for playing. You earned {total_points} points")
            sys.exit()



def play(roller=None):
    roll_dice = roller or GameLogic.roll_dice
    total_points = 0
    max_rounds = 20

    print("Welcome to Ten Thousand")
    response = input("(y)es to play or (n)o to decline\n> ")

    if response.lower() == 'y':
        for round_number in range(1, max_rounds + 1):
            play_round_result = play_round(roll_dice, round_number, total_points)
            total_points = play_round_result[0]
            continue_round = play_round_result[1]
            if not continue_round:
                break
    elif response.lower() == 'n':
        print("OK. Maybe another time")
    elif response.lower() == 'q':
        print(f"Thanks for playing. You earned {total_points} points")
    else:
        print("Invalid input. Please enter 'y' or 'n.'")

if __name__ == "__main__":
    play()  
