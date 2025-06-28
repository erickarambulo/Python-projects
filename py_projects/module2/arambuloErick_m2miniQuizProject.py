# Project #1: Traffic Lights
'''
# Dictionary
traffic_lights = {
    "red": "Drivers please stop. The light is red.",
    "green": "Drivers Please go. The light is green.",
    "yellow": "Drivers, proceed with caution. The light is yellow."
    }

pedestrian_signals = {
    "walk": "Pedestrians, please walk! You are permitted to cross the road!",
    "wait": "Pedestrians, please don't walk! You are not permitted to cross the road!",
    }

direction = {
    "north-south": "North-south crosswalk is safe now!",
    "west-east": "West-east crosswalk is safe now!",
    "nothing": "Both north-south and west-east crosswalk isn't safe! Please wait!"
    }

# Prompt users to enter the color of traffic lights
light = input("Enter the traffic light color (red, green, yellow): ").lower()
print(traffic_lights.get(light, "Invalid input! Please enter red, green, or yellow."))

# if, elif, and else branches FOR four-way intersection simulation
if light == "red":
    print(pedestrian_signals.get("walk"))
    print(direction.get("north-south"))
elif light == "green":
    print(pedestrian_signals.get("wait"))
    print(direction.get("west-east"))
elif light == "yellow":
    print(pedestrian_signals.get("wait"))
    print(direction.get("nothing"))
'''

# Project #2: Clothing Choices Based on Weather

# Prompt users to enter the weather
weather = input("Enter the weather (rainy, sunny, cold): ").lower()

# if, elif, and else branches
if weather == "rainy":
    print("I suggest you to wear a raincoat.")
elif weather == "sunny":
    print("I suggest you to wear a sunglasses.")
elif weather == "cold":
    print("I suggest you to wear a jacket.")
else:
    print("Invalid input! Please enter the weather: (rainy, sunny, or cold).")

