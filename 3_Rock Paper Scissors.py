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
choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if(choice == 0):
    print(rock)
elif (choice == 1):
    print(paper)
elif (choice == 2):
    print(scissors)
else:
    print("Sorry. Your input was invalid.")

game = [rock, paper, scissors]
num = random.randint(0,2)
compchoice = game[num]
if(choice==1 or choice==2 or choice==0):
    print("Computer Chose:")
    print(compchoice)
else:
    print("Computer has no response")


if choice == 0:
    if num == 0:
        print("TIE.Dumass")
    elif num == 1:
        print("YOU LOSE.Lmao ded. Sucks to be you. AI will definitely take your job.")
    elif num == 2:
        print("YOU WIN.Meh,lucky this time")
elif choice == 1:
    if num == 0:
        print("YOU WIN.Meh,lucky this time")
    elif num == 1:
        print("TIE.Dumass")
    elif num == 2:
        print("YOU LOSE.Lmao ded. Sucks to be you. AI will definitely take your job.")
elif choice == 2:
    if num == 0:
        print("YOU LOSE.Lmao ded. Sucks to be you. AI will definitely take your job.")
    elif num == 1:
        print("YOU WIN.Meh,lucky this time")
    elif num==2:
        print("TIE.Dumass")

