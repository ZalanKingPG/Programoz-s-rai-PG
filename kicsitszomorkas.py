#rock paper scissors

import random

print("(1): rock, (2): paper, (3): scissors")
user_move = int(input("Választás"))
computer_move = random.randint(1,3)
if computer_move == 1:
    print("Computer chooses rock")
elif computer_move == 2:
    print("Computer chooses paper")
else:
    print("Computer chooses scissors")

if user_move == computer_move:
    print("Tie")
elif user_move == 1 and computer_move == 3:
    print("Win")
elif user_move == 2 and computer_move == 1:
    print("Win")
elif user_move == 3 and computer_move == 2:
    print("Win")
else:
    print("Lose")