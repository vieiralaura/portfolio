#You are going to build a Rock, Paper, Scissors game.
#You will need to use what you have learnt about randomisation and Lists to achieve this.

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

import random
print("Let's play Rock-Paper-Scissors!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))

if user_choice == 0:
    print(rock)

elif user_choice == 1:
    print(paper)

elif user_choice == 2:
    print(scissors)

else:
    print("Invalid choice, please try again.")

print("The computer has chosen:")
computer_choice = random.randint(0,2)

if computer_choice == 0:
    print(rock)

elif computer_choice == 1:
    print(paper)

elif computer_choice == 2:
    print(scissors)
    
if user_choice == computer_choice:
    print("It's a tie!")
elif ((user_choice == 0 and computer_choice ==2) or (user_choice == 2 and computer_choice ==1) or (user_choice == 1 and computer_choice ==0)):
    print("You've won!")
else:
    print("The computer has won!")