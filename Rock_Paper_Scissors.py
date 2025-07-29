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
player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n").strip()
computer_choice = random.randint(0,2)
choice_list = [rock,paper,scissors]

# Validate input
if player_choice == "0" or player_choice == "1" or player_choice == "2":
    player_choice_int = int(player_choice)
    # Display Choices
    print(choice_list[player_choice_int])
    print("Computer chose:")
    print(choice_list[computer_choice])

    # Tie
    if player_choice_int == computer_choice:
        print("It's a draw")
    # Multiple Player Win Conditions
    elif player_choice_int == 0 and computer_choice == 2:
        print("You win!")
    elif player_choice_int == 2 and computer_choice == 1:
        print("You win!")
    elif player_choice_int == 1 and computer_choice == 0:
        print("You win!")
    else:
    # Otherwise player looses
        print("You lose")
else:
    print("That's not a valid choice. You lose!")
