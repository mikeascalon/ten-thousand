from ten_thousand.game_logic import GameLogic
import random
import sys

def roll_and_score(roll_dice, remaining_dice, unbanked_points, total_points):
    print(f"Rolling {remaining_dice} dice...")
    dice_result = roll_dice(remaining_dice)
    print("*** ", " ".join(map(str, dice_result)), " ***")

    user_input = input("Enter dice to keep, or (q)uit:\n> ")

    if user_input.lower() == 'q':
        print(f"Thanks for playing. You earned {total_points} points") 
        sys.exit()


    else: 
        # user_dice = list(map(int, user_input.split()))
        user_dice = tuple([int(char) for char in user_input])
        round_points = GameLogic.calculate_score(user_dice)
        unbanked_points += round_points
        remaining_dice -= len(user_dice)

        print(f"You have {unbanked_points} unbanked points and {remaining_dice} dice remaining")
        return [remaining_dice, unbanked_points]

def play_round(roll_dice, round_number, total_points):
    print(f"Starting round {round_number}")

    unbanked_points = 0
    remaining_dice = 6

    # Roll the dice for the first time
    roll_and_score_result = roll_and_score(roll_dice, remaining_dice, unbanked_points,total_points)
    remaining_dice = roll_and_score_result[0]
    unbanked_points = roll_and_score_result[1]

    if remaining_dice == 0:  # Check if the user decided to quit immediately
        print(f"Thanks for playing. You earned {total_points} points")
        
        

    while True:
        action = input("(r)oll again, (b)ank your points or (q)uit:\n> ")

        if action.lower() == 'b':
            total_points += unbanked_points
            print(f"You banked {unbanked_points} points in round {round_number}")
            print(f"Total score is {total_points} points")
            return [total_points, True]  # Indicate to start a new round
        elif action.lower() == 'q':
            print(f"Thanks for playing. You earned {total_points} points")
            # return total_points, False  # Indicate that the game should not continue
            break
            sys.exit()

        roll_and_score_result = roll_and_score(roll_dice, remaining_dice, unbanked_points, total_points)
        remaining_dice = roll_and_score_result[0]
        unbanked_points = roll_and_score_result[1]

        if remaining_dice == 0:  # Check if the user decided to quit after subsequent rolls
            print(f"Thanks for playing. You earned {total_points} points")
            break

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
