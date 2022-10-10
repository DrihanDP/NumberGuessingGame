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