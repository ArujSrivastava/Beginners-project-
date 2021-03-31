# Guess the number game


import random

chance = 0
count = 1
lower_limit = int(input("Enter the lower limit for guessing game: "))
upper_limit = int(input("Enter the upper limit for guessing game: "))
t = int(input("Enter the number of turn/turns: "))

print(
    "You have to guess a number between",
    lower_limit,
    "and",
    upper_limit,
    "in",
    t,
    "turn/turns",
)

while count <= t:
    n = int(input("\nGuess the number: "))
    x = random.randint(lower_limit, upper_limit)
    if n == x:
        if count == 1:
            print("\nYou win in your ", count, "st turn", sep="")
        elif count == 2:
            print("\nYou win in your ", count, "nd turn", sep="")
        elif count == 3:
            print("\nYou win in your ", count, "rd turn", sep="")
        else:
            print("\nYou win in your ", count, "th turn", sep="")
        break

    elif n != x:
        print("\nYou lose")
        if n < lower_limit or n > upper_limit:
            print("Guess the number between the limits given")
            print("Chance wasted")
            chance += 1
        else:
            print("Try again if chances are left")
    count += 1
print("Number of chance wasted:", chance)
print("\nThanks for playing\n")