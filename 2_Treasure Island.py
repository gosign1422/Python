print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U|.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad. Where do you want to go? '
                'Type "left" or "right" ?\n').lower()

if choice1 == "left":
    choice2 = input(('You\'ve come to a lake.'
                     'There is an island in the middle of the lake. '
                     'Type "wait" to wait for a boat. '
                     'Type "swim" to swim across.\n')).lower()
    if (choice2 == "wait"):
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors. "
                        "One red, one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if (choice3 == "red"):
            print("It is a room full of fire. Game Over")
        elif (choice3 == "yellow"):
            print("You found the treasure. YOU WIN!.")
        elif (choice3 == "blue"):
            print("You enter a room full of beasts. GAME OVER")
        else:
            print("You chose a door that doesn't exist. GAME OVER.")
    else:
        print("You got attacked by a shark. GAME OVER.")
else:
    print("You fell into a hole. GAME OVER.")
