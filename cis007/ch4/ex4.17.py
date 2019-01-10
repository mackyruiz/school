# Ch 4 Exercise 4.17
# Macky Ruiz
# CIS 007
import random

# Prompt user to pick a number:
number = eval(input("scissor (0), rock (1), paper (2): "))

# Generate random computer numbers
computer = random.randint(0, 2)

# Computer is scissor (0)
if computer == 0 and number == 0:
    print("The computer is scissor. You are scissor too. Its a draw.")
elif computer == 0 and number == 1:
    print("The computer is scissor. You are rock. You won.")
elif computer == 0 and number == 2:
    print("The computer is scissor. You are paper. You lost.")

# Computer is rock (1)
elif computer == 1 and number == 0:
    print("The computer is rock. You are scissor. You lost.")
elif computer == 1 and number == 1:
    print("The computer is rock. You are rock too. Its a draw.")
elif computer == 1 and number == 2:
    print("The computer is rock. You are paper. You won.")

# Computer is paper (2)
elif computer == 2 and number == 0:
    print("The computer is paper. You are scissor. You won.")
elif computer == 2 and number == 1:
    print("The computer is paper. You are rock. You lost.")
elif computer == 2 and number == 2:
    print("The computer is paper. You are paper too. Its a draw.")
