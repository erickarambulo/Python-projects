# Project #1: Car Class
'''
# Class car
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0  

    def accelerate(self):
        self.__speed += 5
        print(f"Accelerating the car! Current speed: {self.__speed} mph")

    def brake(self):
        self.__speed -= 5
        if self.__speed < 0:
            self.__speed = 0 # speed can't go negative
        print(f"Braking the car! Current speed: {self.__speed} mph")

    def get_speed(self):
        return self.__speed

# Create function to run the program
def start_car():
    my_car = Car(2000, "Honda Civic")
    print(f"Starting at {my_car.get_speed()} mph for {my_car._Car__year_model} {my_car._Car__make}! ")

    print("Accelerating the Car!")
    for x in range(5):
        my_car.accelerate()

    print("\nBraking the Car!")
    for y in range(5):
        my_car.brake()

# Run the program
start_car()
'''

# Project #2

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code,
                 phone_number, emergency_contact_name, emergency_contact_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    # Get
    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone_number(self):
        return self.__phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone

    # Set
    def set_first_name(self, name):
        self.__first_name = name

    def set_middle_name(self, name):
        self.__middle_name = name

    def set_last_name(self, name):
        self.__last_name = name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone_number(self, phone):
        self.__phone_number = phone

    def set_emergency_contact_name(self, name):
        self.__emergency_contact_name = name

    def set_emergency_contact_phone(self, phone):
        self.__emergency_contact_phone = phone


class Procedure:
    def __init__(self, procedure_name, date, practitioner, charges):
        self.__procedure_name = procedure_name
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges

    # Get
    def get_procedure_name(self):
        return self.__procedure_name

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges

    # Set
    def set_procedure_name(self, name):
        self.__procedure_name = name

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charges(self, charges):
        self.__charges = charges

# Main Program
def run_patient_charges_program():
    # Create a patient information
    patient1 = Patient(
        first_name = "Erick",
        middle_name = "U.",
        last_name = "Arambulo",
        address = "2638 Townley Street",
        city = "Santa Ana",
        state = "CA",
        zip_code = "92706",
        phone_number = "657-281-9333",
        emergency_contact_name = "Hayley Lee",
        emergency_contact_phone = "111-111-1111"
    )

    # Create three dictionaries
    procedure1 = Procedure(
        procedure_name = "Eye Exam",
        date = "2024-20-06",
        practitioner = "Dr. Nguyen",
        charges = 100.00
    )

    procedure2 = Procedure(
        procedure_name = "X-ray",
        date = "2024-20-06",
        practitioner = "Dr. Smith",
        charges = 500.00
    )

    procedure3 = Procedure(
        procedure_name = "Blood test",
        date = "2024-20-06",
        practitioner = "Dr. Nguyen",
        charges = 20.00
    )

    # Display patient's information
    print("Patient Information:")
    print(f"Name: {patient1.get_first_name} {patient1.get_middle_name()} {patient1.get_last_name()}")
    print(f"Address: {patient1.get_address()} {patient1.get_city()} {patient1.get_state()}")
    print(f"Phone: {patient1.get_phone_number()}")
    print(f"Emergency Contact: {patient1.get_emergency_contact_name()} ({patient1.get_emergency_contact_phone()})")
    print("-----------------------------------------------------------------------------------------------")

    # Display information about all three procedures
    print("\nProcedure Information:")
    procedures = [procedure1, procedure2, procedure3]
    total_charges = 0.0

    procedure_number = 1
    for proc in procedures:
        print(f"Procedure #{procedure_number}:")
        print(f"Name: {proc.get_procedure_name()}")
        print(f"Date: {proc.get_date()}")
        print(f"Practitioner: {proc.get_practitioner()}")
        print(f"Charges: ${proc.get_charges():.2f}\n")
        total_charges += proc.get_charges()
        procedure_number += 1

    # Display total charges of three procedures
    print(f"Total Charges for all procedures: ${total_charges:.2f}")

# Run the program
run_patient_charges_program()

