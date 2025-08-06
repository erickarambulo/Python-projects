# Challenge Exercise #1:

DictionaryOfNames = {
    "name": "Alice",
    "age": 25,
    "city": "New York City",
    "state": "New York",
    "zip_code": 10001
}

# Adding and accessing values
DictionaryOfNames["job"] = "Developer"
print(DictionaryOfNames["job"]) # Output: Developer

# Using methods
print(DictionaryOfNames.keys()) # Output: dict_key(['name', 'age', 'city', 'job'])
print(DictionaryOfNames.values()) # Output: dict_values(['Alice', '25', 'New York', 'Developer'])

# Challenge Exercise #2:

# Initialize an empty set to hold the dictionary entries
user_info_set = set()

# Function to collect name and age from the user
def collect_user_info():
    # Create a dictionary to store user info
    user_info = {}

    # Ask the user to input their name and age
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    zip_code = input("Enter your zip-code: ")

    # Add the user input to the dictionary
    user_info["name"] = name
    user_info["age"] = age
    user_info["address"] = address
    user_info["city"] = city
    user_info["state"] = state
    user_info["zip-code"] = zip_code

    # Add the dictionary as an entry in the set
    user_info_set.add(frozenset(user_info.items())) # frozenset is used to allow dictionaries inside sets

    print("\nUser info added successfully!\n")
    return user_info

# Function to display all unique user entries
def display_user_info():
    print("Displaying all unique user entires:\n")
    for user in user_info_set:
        user_dict = dict(user) # Convert frozenset back to a dictionary for displaying
        print(f"Name: {user_dict['name']}, Age: {user_dict['age']}, Address: {user_dict['address']}")
        print(f"City: {user_dict['city']}, State: {user_dict['state']}, Zip-code: {user_dict['zip-code']}")

# Main program loop
while True:
    print("1. Add User Info")
    print("2. Display All User Info")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        collect_user_info()
    elif choice == '2':
        display_user_info()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")

# Challenge Exercise #3: Galilean Moons of Jupiter

# Dictionaries
jupiter_mean_radius = {"Io": 1821.6, "Europa": 1560.8, "Ganymede": 2634.1, "Callisto": 2410.3}
jupiter_surface_gravity = {"Io": 1.796, "Europa": 1.314, "Ganymede": 1.428, "Callisto": 1.235}
jupiter_orbital_period = {"Io": 1.769, "Europa": 3.551, "Ganymede": 7.154, "Callisto": 16.689}

# Ask user to input the name of a Galilean moon of Jupiter
userInput = input("Enter the name of a Galilean moon: ")

# if and else branch
if userInput.capitalize() in jupiter_mean_radius.keys():
    print(f"Information for {userInput.capitalize()}")
    print(f"Mean Radius: {jupiter_mean_radius[userInput.capitalize()]} km")
    print(f"Surface Gravity: {jupiter_surface_gravity[userInput.capitalize()]} meter per square")
    print(f"Orbital Period: {jupiter_orbital_period[userInput.capitalize()]} days")
else:
    print(f"Invalid input! {userInput} is not a valid name.")

