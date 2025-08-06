# Task 1:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Generic sound")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def make_sound(self):
        print("Bark!")
    
    def fetch(self):
        print("Fetching the ball!")

# Run the program
my_dog = Dog("Buddy", "Canine")
my_dog.make_sound()
my_dog.fetch()

# Task 2:

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound(self):
        print("Generic sound")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed
    
    def make_sound(self):
        print("Bark!")
    
    def fetch(self):
        print("Fetching the ball!")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def make_sound(self):
        print("Meow!")
    
    def climb(self):
        print("Climbing the tree!")

# RUn the progeram
my_dog = Dog("Buddy", "Canine", "Golden Retriever")
my_cat = Cat("Whiskers", "Feline")
my_dog.make_sound()
my_cat.make_sound()


# Task 3:

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
    
    def start_engine(self):
        print("Car engine started")

class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_size):
        super().__init__(make, model, year, num_doors)
        self.battery_size = battery_size
    
    def start_engine(self):
        print("Electric motor activated")

# Run the program
my_electric_car = ElectricCar("Tesla", "Model S", 2023, 4, "100 kWh")
my_electric_car.start_engine()

