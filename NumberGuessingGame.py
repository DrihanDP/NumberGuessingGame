# Number guessing Game

print("Please enter the lower bound number (cannot be less than 0)")
lower_bound = int(input(">"))
if lower_bound < 0:
    while lower_bound < 0:
        print("Value entered is lower than 0, please enter a value that is 0 or higher")
        lower_bound = int(input(">"))
        if lower_bound >= 0: 
            break
print("Please enter the upper bound number")
upper_bound = int(input(">"))
print(f"Think of a number between {lower_bound} and {upper_bound}.")
guess = (upper_bound - lower_bound) // 2
print(f"Is your number {guess}. Please enter 'Yes' or 'No.")
answer = input(">")
if answer == 'yes'.casefold():
    print("I guessed it!")
elif answer == 'no'.casefold():
    print("Is your number higher or lower?")
    higherorlower = input(">")
