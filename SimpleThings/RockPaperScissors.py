import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]
cpu_value = random.randint(0, 2)

print("Welcome to RPS!\n")
user_value = int(input("What is your choice? \n(Enter 0 for Rock, 1 for Paper or 2 for Scissors) \n"))

if user_value not in [0, 1, 2]:
    raise ValueError("Input is not 0, 1 or 2. You lose!")
else:
    print(f"\n{rps[user_value]}\n")

print(f"Computer choose:\n{rps[cpu_value]}\n")

if user_value - cpu_value == 2:
    print("You lose")
elif cpu_value - user_value ==2:
    print("You win")
elif cpu_value > user_value:
    print("You lose")
elif cpu_value == user_value:
    print("It's a tie!")
else:
    print("You win")
