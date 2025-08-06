# Project 1:

class Person:
    def __init__(self, name, address, telephone):
        self.name = name
        self.address = address
        self.telephone = telephone

class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, mailing_list):
        super().__init__(name, address, telephone)
        self.customer_number = customer_number
        self.mailing_list = mailing_list

my_customer = Customer(
    "Erick Arambulo",
    "2638 Townley Street",
    "657-281-9333",
    "C17",
    False
)

print(f"Customer Name: {my_customer.name}")
print(f"Customer Address: {my_customer.address}")
print(f"Customer Telephone: {my_customer.telephone}")
print(f"Customer Number: {my_customer.customer_number}")
print(f"On Mailing List: {my_customer.mailing_list}")


# Project #2:

class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

worker = ProductionWorker(
    "Erick Arambulo",
    "E123",
    3,
    19.00
)

print(f"Employee Name: {worker.name}")
print(f"Employee Number: {worker.number}")
print(f"Shift Number: {worker.shift_number}")
print(f"Hourly Pay Rate: ${worker.hourly_pay_rate:.2f}")


