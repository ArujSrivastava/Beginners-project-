# This a program on stone paper scissors game.
import random

result = ""
print(
    """Things to know before starting a game:
    1: Stone
    2: Paper
    3: Scissors
Click on the number on your keyboard to use the above"""
)

choice = int(input("Enter your choice: "))
if choice == 1 or choice == 2 or choice == 3:
    if choice == 1:
        choice_name = "Stone"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
    print("Your choice is: ", choice_name)
else:
    print("Enter a valid choice")
    exit()

print("Now its computer's turn")
comp = random.randint(1, 3)
if comp == 1:
    comp_choice = "Stone"
elif comp == 2:
    comp_choice = "Paper"
else:
    comp_choice = "Scissor"

print("Computer's choice is:", comp_choice)
print(choice_name + " Vs " + comp_choice)

if (choice == 1 and comp == 3) or (comp == 1 and choice == 3):
    result = "Stone"
elif (choice == 3 and comp == 2) or (choice == 2 and comp == 3):
    result = "Scissor"
elif (choice == 2 and comp == 1) or (choice == 1 and comp == 2):
    result = "Paper"
elif choice_name == comp_choice:
    print("Draw, since the choices are same")
    exit()

if result == choice_name:
    print("User wins")
else:
    print("Computer wins")

print("Thanks for playing")