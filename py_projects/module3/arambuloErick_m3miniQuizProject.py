# Project #1: Basic Function Creation

# Function defined
def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming.")


# Ask user to input their name
firstName =  input("Please enter your first name: ")

# Calls function
greet_user(firstName)


# Project #2: Function with Input and Output

# Function defined
def calculate_area():
    # Ask users to input their length and width of a rectangle
    userLength = int(input("Please enter the length of a rectangle: "))
    userWidth = int(input("Please enter the width of a rectangle: "))

    # Calculation
    area = userLength * userWidth
    
    # Return the value
    return area


# Calls function
result = calculate_area()

# Final output
print(f"The area of a rectangle is {result}.")


# Project #3: Rock, Paper, Scissors Game

# Import random module
import random

# Function defined
def play_game():
    # Prompt user to enter their choice
    userChoice = int(input("Please enter a number (1 for Rock, 2 for Paper, and 3 for Scissors): "))
    
    # if, elif, and else branches for user
    if userChoice == 1: # Rock
        print("You choose Rock!")
    elif userChoice == 2: # Paper
        print("You choose Paper!")
    elif userChoice == 3: # Scissors
        print("You choose Scissors")
    else:
        print("Invalid input! Please enter 1, 2, or 3.")

    # Variable declared for robot
    decider = random.randint(1, 3)

    # if, elif, and else branches for robot
    if decider == 1: # Rock
        print("A robot choose Rock!")
    elif decider == 2: # Paper
        print("A robot choose Paper!")
    elif decider == 3: # Scissors
        print("A robot choose Scissors!")

    # if, elif, and else branches for actual game
    if userChoice == 1 and decider == 1:
        print("It's a tie!")
    elif userChoice == 1 and decider == 2:
        print("Robot wins! You lost!")
    elif userChoice == 1 and decider == 3:
        print("Robot lost! You won!")
    elif userChoice == 2 and decider == 1:
        print("Robot lost! You won!")
    elif userChoice == 2 and decider == 2:
        print("It's a tie!")
    elif userChoice == 2 and decider == 3:
        print("Robot wins! You lost!")
    elif userChoice == 3 and decider == 1:
        print("Robot wins! You lost!")
    elif userChoice == 3 and decider == 2:
        print("Robot lost! You won!")
    elif userChoice == 3 and decider == 3:
        print("It's a tie!")

# Calls a function
play_game()

