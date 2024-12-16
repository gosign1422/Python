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
game_images=[rock,paper,scissors]
# User
cho=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if (0<=cho<=2):
    print("You chose:")
    print(game_images[cho])
    
    # Computer
    comp_choice = random.randint(0, 2)
    print("Computer Chose:")
    print(game_images[comp_choice])

    # Conditions
    if cho == 0 and comp_choice == 2:
        print("You Win")
    elif cho == comp_choice:
        print("Tie")
    elif cho == 0 and comp_choice == 1:
        print("You Lose")
    elif cho == 1 and comp_choice == 0:
        print("You Win")
    elif cho == 1 and comp_choice == 2:
        print("You Lose")
    elif cho == 2 and comp_choice == 1:
        print("You Win")
    elif cho == 2 and comp_choice == 0:
        print("You Lose")

else:
    print("You typed an invalid number. Retry.")