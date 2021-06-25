# Higher Lower game
import random
from art import *
from data import *

continue_game = True
user_score = 0


# Create a higher lower game that compares instagram followers
# Correct if pick the option with more followers. If correct score increases and game continues
# If wrong then game ends


def row_selector(list) -> dict:
    row = random.choice(list)
    return row


def get_description(row) -> str:
    row_name = row["name"]
    row_description = row["description"]
    row_country = row["country"]
    return f"{row_name}, {row_description} from {row_country}"


def get_followers(row) -> int:
    followers = row["follower_count"]
    return followers


def get_higher(row1, row2):
    row1_followers = get_followers(row1)
    row2_followers = get_followers(row2)
    larger = max(row1_followers, row2_followers)
    if row1_followers == larger:
        answer = "A"
    elif row2_followers == larger:
        answer = "B"
    return answer


def higher_lower():
    option_a = row_selector(data)
    option_b = row_selector(data)
    while option_a == option_b:
        option_b = row_selector(data)

    print("-------------------------------------------------------------------------------------------")
    print("Here are your options. Can you guess which one has the higher amount of followers?\n")

    print(f"Option A: {get_description(option_a)}")
    print(vs)
    print(f"Option B: {get_description(option_b)}\n")

    user_choice = input("What is your choice (A or B)?\n").upper()

    if get_higher(option_a, option_b) == user_choice:
        print("\nYour guess was correct!")
        global user_score
        user_score += 1
    else:
        print("\nYour guess is incorrect")
        global continue_game
        continue_game = False


# Code for the UI and game
print(logo)
print('Welcome to "Higher or Lower?", can you reach a score of 10?\n')

while continue_game:
    higher_lower()
    print(f"Your score is {user_score}!\n")
    if user_score == 10:
        print("Congratulations, you won the game!")
        continue_game = False

print("Thank you for playing :)")
