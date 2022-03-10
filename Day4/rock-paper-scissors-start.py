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

#Write your code below this line 👇


import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)

game_options = [rock,paper,scissors]

print(f"Your choise: \n {game_options[player_choice]}")
print(f"Computer choise: \n {game_options[computer_choice]}")

if player_choice == computer_choice:
    print("Nobody win")
elif player_choice == 0 and computer_choice == 2:
    print("You win")
elif player_choice == 1 and computer_choice == 0:
    print("You win")
elif player_choice == 2 and computer_choice == 1:
    print("You win")
else:
    print("You lose")
