# Project #1: Multiply by 10 for Products

# Ask users for their input
number = float(input("Enter a number: "))
product = number * 10

# While loop begins here
while product < 100:
    print(f"Currently product: {product}")
    number = float(input("Enter another number: "))
    product = number * 10

print(f"Final product is {product}.")

# Project #2: Bug Collector

# Variable declared and initialized
total_bugs = 0

# For loop begins here
for day in range(1, 6): # Loop for five days
    bugs_collected = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_collected

# Final output 
print(f"Total bugs collected over five days: {total_bugs}")

# Project #3: Calories Burned

# Variables declared and initialized
calories_per_minute = 4.2
minutes_list = [10, 15, 20, 25, 30]

# Header title 
print("Calories burned on a treadmill:")
# For loop
for minutes in minutes_list:
    calories_burned = calories_per_minute * minutes
    print(f"After {minutes} minutes: {calories_burned:.1f} calories")

# Project #4: Lap Times
# Note to myself: I have to add append, list, min, max, sum, and len for this one

# Ask user to input their number
num_laps = int(input("Enter the number of times you have run around the racetrack: "))

# This is new, list is prepared for append()
lap_times = []
# For loop begins heree
for times in range(num_laps):
    lap_time = float(input(f"Enter the time for lap {times + 1}: "))
    lap_times.append(lap_time)

# Calculation
fastest_lap = min(lap_times)
slowest_lap = max(lap_times)
average_lap = sum(lap_times) / len(lap_times)

print(f"\nFastest lap time: {fastest_lap:.2f} seconds")
print(f"Slowest lap time: {slowest_lap:.2f} seconds")
print(f"Average lap time: {average_lap:.2f} seconds")
