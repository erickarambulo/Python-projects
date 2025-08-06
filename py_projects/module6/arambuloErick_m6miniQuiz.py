# Mini Quiz #6: Python Dictionary

# Dictionary
class_section_a = {
    "101": {"name": "Alice", "age": 17, "grade": 92},
    "102": {"name": "Bob", "age": 16, "grade": 85}
}

class_section_b = {
}

def add_student(student_id, name, age, grade):
    new_student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    class_section_b[student_id] = new_student
    print(f"Student {name} is added successfully! Student ID: {student_id}")

# Before adding students
print("Before adding new student:")
print(class_section_a)

# Add students 
add_student("103", "Erick", 28, 99)
add_student("104", "Jason", 40, 100)
add_student("105", "Rachel", 35, 82)

# After adding students
print("\nAfter adding new students:")
print(class_section_b)

# Combine (Merge) two dictionaries (class sections)
print(f"\nClass Section A: {class_section_a}")
print(f"Class Section B: {class_section_b}")

# Frequency counter for word occurrences in a text
print(f"\nFrequency counter for word occurrences in a text:")
print(f"Class Section A: {len(class_section_a)}")
print(f"Class Section B: {len(class_section_b)}")

