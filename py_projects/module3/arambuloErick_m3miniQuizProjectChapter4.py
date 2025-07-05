# Exercise 1: Basic For Loop

# For loop
for x in range(1, 11):
    print(x)


# Exercise 2: Sum of Numbers

# Variable declared
sum = 0

# For loop
for x in range(1, 101):
    sum += x

# Final output
print(sum)


# Exercise 3: Multiplication Table

# Ask user to input an integer
userInput = int(input("Please enter an integer number: "))

# For loop
for x in range(1, 11):
    print(userInput * x)


# Exercise 4: While loop

# Variable declared
x = 1

# While loop
while x < 21:
    # if branch
    if x % 2 == 0:
        print(x)
    
    # iterate by adding 1
    x = x + 1

