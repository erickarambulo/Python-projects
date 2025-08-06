# Project #1 (A): Challenge Exercise #1

class AnimalType:
    def eats(self):
        print("This animal likes to eat ?")

class Rabbits(AnimalType):
    def munch(self):
        print("carrots ")

class Birds(Rabbits):
    def munch1(self):
        print("seeds")

class Monkey(Birds):
    def munch2(self):
        print("banana")

RabbitObject = Rabbits()
RabbitObject.eats()
RabbitObject.munch()

# Here we have the Bird Object inheriting from two different classes
BirdObject = AnimalType()
BirdObject = Birds()

BirdObject.eats()
BirdObject.munch1()

# Add 3rd animal
MonkeyObject = Monkey()
MonkeyObject.eats()
MonkeyObject.munch2()


# Project #1 (B): Challenge Exercise #2

class Person:
    def __init__(self, name, age, address, city, state, zipcode):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

# The student class is inheriting from the person class
class Student(Person):
    def __init__(self, name, age, address, city, state, zipcode, studentID, GPA):
        # The super keyword is calling the super class
        # which is the person class and passing name, and age
        super().__init__(name, age, address, city, state, zipcode)

        self.student_id = studentID
        self.GPA = GPA

class Teacher(Person):
    def __init__(self, name, age, address, city, state, zipcode, TeacherID, ClassTeaching):
        super().__init__(name, age, address, city, state, zipcode)

        self.TeacherID = TeacherID
        self.ClassTeaching = ClassTeaching

student1 = Student("Jane Doe", 25, "123 Bristol St.", "Santa Ana", "CA", 92706, 777, 3.8)
print("Student Name:", student1.name)
print("Student Age: ", student1.age)
print("Student Address: ", student1.address)
print("Student City: ", student1.city)
print("Student State: ", student1.state)
print("Student Zipcode: ", student1.zipcode)
print("Student ID: ", student1.student_id)
print("Student GPA: ", student1.GPA)

print("")

teacher1 = Teacher("Ms. Cantor", 30, "456 Circle Dr.", "Irvine", "CA", 10001, 111, "Python")
print("Teacher Name: ", teacher1.name)
print("Teacher Age: ", teacher1.age)
print("Teacher Address: ", teacher1.address)
print("Teacher City: ", teacher1.city)
print("Teacher State: ", teacher1.state)
print("Teacher Zipcode: ", teacher1.zipcode)
print("Teacher ID: ", teacher1.TeacherID)
print("Teacher Course: ", teacher1.ClassTeaching)


# Project #2: Challenge Exercise #4

class Automobiles:
    def __init__(self, make, model, mileage, price, doors):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__doors = doors

    # These are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def set_doors(self, doors):
        self.__doors = doors

    # These are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_doors(self):
        return self.__doors


# Challenge Exercise #5:

from bugs import Bumblebee, Grasshopper

class Main():
    def __init__(self):
        self.bumblebeeObject = Bumblebee()
        self.bumblebeeObject.sting()
        print("\n")
        self.grasshopperObject = Grasshopper()
        self.grasshopperObject.jump()

# Run the program
Main()


# Project #3: Challenge Exercise #6:

class Automobiles:
    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price

    # These are the mutator methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def set_price(self, price):
        self.__price = price

    def set_doors(self, doors):
        self.__doors = doors

    # These are the accessor methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price


# Project #4: Challenge Exercise #7

class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # Mutator methods
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # Accessor methods
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift = shift
        self.__hourly_pay_rate = hourly_pay_rate

    # Mutator methods
    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # Accessor methods
    def get_shift(self):
        return self.__shift

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate

def main():
    # Prompt user for data
    name = input("Enter employee name: ")
    number = int(input("Enter employee number: "))
    shift = int(input("Enter shift number (1 for day, 2 for night): "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))

    # Create ProductionWorker object
    worker = ProductionWorker(name, number, shift, hourly_pay_rate)

    # Display the data
    print("\n Employee Information: ")
    print(f"Name: {worker.get_name()}")
    print(f"Number: {worker.get_number()}")
    print(f"Shift: {'Day' if worker.get_shift() == 1 else 'Night'}")
    print(f"Hourly Pay Rate: ${worker.get_hourly_pay_rate():.2f}")

if __name__ == "__main__":
    main()

