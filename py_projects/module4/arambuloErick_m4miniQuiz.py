# Project: Student Grade Calculator

# Four Functions defined
def get_student_info():
    # Ask user to put their answers
    print("Welcome to The Student Grade Calculator!")
    student_id = int(input("\nPlease enter your student ID: "))
    name = input("Please enter your first and last name: ")
    age = int(input("Please enter your age: "))
    address = input("Please enter your address: ")
    city = input("Please enter your city: ")
    state = input("Please enter your state: ")
    zipcode = int(input("Please enter your zipcode: "))

    # I recently learned new way to return multiple from YouTube using dictionary
    return {
        "student_id": student_id,
        "name": name,
        "age": age,
        "address": address,
        "city": city,
        "state": state,
        "zipcode": zipcode
        }

def get_test_scores():
    score1 = int(input("Please enter your 1st test score: "))
    score2 = int(input("Please enter your 2nd test score: "))
    score3 = int(input("Please enter your 3rd test score: "))

    return {
        "score1": score1,
        "score2": score2,
        "score3": score3
        }

def calculate_average(score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return average

def display_student_info(student_info, average_score):
    print("\nStudent Information")
    print(f"Student ID: {student_info['student_id']}")
    print(f"Name: {student_info['name']}")
    print(f"Age: {student_info['age']}")
    print(f"Address: {student_info['address']}")
    print(f"City: {student_info['city']}")
    print(f"State: {student_info['state']}")
    print(f"Zip Code: {student_info['zipcode']}")
    print(f"The student's average for three test scores is {average_score:.2f}")


# Calls function
student_info_result = get_student_info()
test_scores = get_test_scores()
final_average = calculate_average(test_scores['score1'], test_scores['score2'], test_scores['score3'])
display_student_info(student_info_result, final_average)

