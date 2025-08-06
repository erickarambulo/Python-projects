# Project #1:

# MAIN DICTIONARY to save information for student ID
main_student_system = {}

# Create a set to prevent duplicated ID
system = set()

# Create add student function
def add_student(student_id, name, age):
    # Adds a new student, will not add new student if there are similar
    student_info = (student_id, name)

    # if statement
    if student_info in system:
        print(f"Error: Student ID: {student_id} and name is {name} already exists in the system.")
        return

    # Dictionary
    student_data = {
        "name": name,
        "age": age,
        "id": student_id
    }

    # Add student to main dictionary
    main_student_system[student_id] = student_data

    # Add unique id to the set to prevent dupplcate
    system.add(student_info)

    # Final output
    print(f"Student name: {name} is added successfully! Student ID is {student_id}")

# Calls function
add_student("10001", "Erick", 28)
add_student("10002", "Jason", 40)
add_student("10003", "Bob", 20)
add_student("10004", "Joshua", 25)

# Test for duplicate error
add_student("10001", "Erick", 28)


# Project #2: (similar to project #1)

# Main dictionary
inventory = {}

# Set to prevent duplicated 
unique_product = set()

def add_product(name, quantity, price):
    # Variable declared with .lower()
    product_name = name.lower()

    # if branch for uniqueness
    if product_name in unique_product:
        print(f"Error! Product {name} is already existing in inventory!")
        return

    # Dictionary
    product_details = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    # Add to the dictionary
    inventory[name] = product_details

    # Add the product name to the set to prevent duplicate
    unique_product.add(product_name)

    # Final output
    print(f"Product {name} is added successfully!\nQuantity: {quantity}\nPrice: ${price:.2f}.")

# Calls function
add_product("Mr. Clean", 20, 10.00)
add_product("Cat Chewy 11 oz", 55, 11.99)
# Test for duplicate error

add_product("Cat Chewy 11 oz", 55, 11.99)
