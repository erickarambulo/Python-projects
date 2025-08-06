# Challenge Exercise #1:
'''
class Students:
    # the keyword (self)
    # it is used to access variables that belong to that class.
    def GetInformation(self):
        print("student last name is " + self.Lastname)
        print("student first name is " + self.Firstname)
        print("student address name is " + self.Address)
        print("student city name is " + self.City)
        print("student state name is " + self.State)
        print("student zipcode is " + self.Zipcode)

# Creates the Student1 object
Student1 = Students()
Student1.Lastname = "Doe"
Student1.Firstname = "Jane"
Student1.Address = "111 St"
Student1.City = "Santa Ana"
Student1.State = "CA"
Student1.Zipcode = "12345\n"

# Creates the Student2 object
Student2 = Students()
Student2.Lastname = "Cantor"
Student2.Firstname = "Mike"
Student2.Address = "222 St"
Student2.City = "Garden Grove"
Student2.State = "CA"
Student2.Zipcode = "67890\n"

# Creates the Student3 object
Student3 = Students()
Student3.Lastname = "Arambulo"
Student3.Firstname = "Erick"
Student3.Address = "2638 Townley Street"
Student3.City = "Santa Ana"
Student3.State = "CA"
Student3.Zipcode = "92706"

# Calling the function
Student1.GetInformation()
Student2.GetInformation()
Student3.GetInformation()
'''

# Challenge Exercise #2:
'''
class Teacher():
    # using init to create a customized constructor
    # here we have three arguments
    def __init__(self, name, classRoom, course):
        self.name = name
        self.classRoom = classRoom
        self.course = course

    def GetProfessor(self):
        print("Professor name is " + self.name)
        print("Professor assigned class is " + self.classRoom)
        print("Professor is teaching " + self.course + "\n")

# Calling the three arguments
Teacher1 = Teacher("Prof. Sim", "A206", "Python Programming")
Teacher2 = Teacher("Prof. Arambulo", "B221", "C++ Programming")

# Calls class
Teacher1.GetProfessor()
Teacher2.GetProfessor()
'''

# Challenge Exercise #3:
'''
class PI:
    def GetInformation(self, LN, FN, Age, Address, City, State, Zipcode):
        return LN + " , " + FN + " , " + str(Age) + " , " + Address + " , " + City + " , " + State + " , " + Zipcode

PersonalInformation = PI()
PersonalInformation.Lastname = input("Enter the last name: ")
PersonalInformation.Firstname = input("Enter the first name: ")
PersonalInformation.Age = int(input("Enter the age: "))
PersonalInformation.Address = input("Enter the address: ")
PersonalInformation.City = input("Enter the city: ")
PersonalInformation.State = input("Enter the state: ")
PersonalInformation.Zipcode = input("Enter the zipcode: ")

print(PersonalInformation.GetInformation(PersonalInformation.Lastname, PersonalInformation.Firstname, PersonalInformation.Age,
                                         PersonalInformation.Address, PersonalInformation.City, PersonalInformation.State,
                                         PersonalInformation.Zipcode))
'''

# Challenge Exercise #4:
'''
# Import the other class file name
import class7

# Start the main function
def main():
    name = (input("Enter the name: "))
    address = (input("Enter the address: "))
    phone = (input("Enter the phone: "))
    city = (input("Enter the city: "))
    zipcode = (input("Enter the zipcode: "))
    age = (int(input("Enter the age: ")))

    # Call them in order
    customer_obj = class7.Customer(name, address, phone, city, zipcode, age)

    # Final output
    print(f"Hello {customer_obj.get_name()}, your address is {customer_obj.get_address()} "
          f"and your # is {customer_obj.get_phone()}. Your city is {customer_obj.get_city()}, "
          f"zip code {customer_obj.get_zipcode()}, and your age is {customer_obj.get_age()}.")
    
main()
'''

# Challenge Exercise #5:

# Import the other class file name
import class3

# Start the main function
def main():
    
    start_bal = float(input("Enter the starting balance: "))

    # Call the external class3.name of this class, in our case its
    # called BankAccount from the class3
    savings = class3.BankAccount(start_bal)

    pay = float(input("How much were you paid this week? "))
    print("will deposit that amount into your account")

    # The deposit function is passing one argument called amount
    # so we have to fulfill that argument with pay
    savings.deposit(pay)
    # Retrieve the balance from the external class
    print(f"Your account balance is ${savings.get_balance():.2f}")

    cash = float(input("How much would you like to withdrawal? "))
    print("Will withdrawal that amount into your account")

    # Calls the withdraw function from the external class
    # and fulfills the one argument that is passed with cash
    savings.withdraw(cash)
    # Retrieved the balance from the external class
    print(f"Your account balance is ${savings.get_balance():.2f}")

main()