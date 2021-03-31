# This a program on stone paper scissors game.
import random

result = ""
x = "y"
count = 0
comp_count = 0
draw = 0

print(
    """Things to know before starting a game:
    1: Stone
    2: Paper
    3: Scissors
Click on the number on your keyboard to use the above"""
)
while x == "y":
    choice = int(input("\nEnter your choice: "))
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
        break

    print("Now its computer's turn")
    comp = random.randint(1, 3)
    if comp == 1:
        comp_choice = "Stone"
    elif comp == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissor"

    print("Computer's choice is:", comp_choice)
    print("\n" + choice_name + " vs " + comp_choice + "\n")

    if (choice == 1 and comp == 3) or (comp == 1 and choice == 3):
        result = "Stone"
    elif (choice == 3 and comp == 2) or (choice == 2 and comp == 3):
        result = "Scissor"
    elif (choice == 2 and comp == 1) or (choice == 1 and comp == 2):
        result = "Paper"

    if result == choice_name:
        print("User wins")
        count += 1
    elif result == comp_choice:
        print("Computer wins")
        comp_count += 1
    elif choice_name == comp_choice:
        print("Draw, since the choices are same")
        draw += 1
    x = input("\nPress 'y' to play again or anything else to exit: ")

print("\nUser wins:", count)
print("Computer wins:", comp_count)
print("Total draw matches:", draw, "\n")
