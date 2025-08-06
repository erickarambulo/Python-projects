import vehicles

def main():

    used_car1 = vehicles.Automobiles("Audi", 2022, 45000, 80000.0)
    used_car2 = vehicles.Automobiles("Honda", 2022, 45000, 80000.0)

    print("Make: ", used_car1.get_make())
    print("Model: ", used_car1.get_model())
    print("Mileage: ", used_car1.get_mileage())
    print("Price: ", used_car1.get_price())
    print("\n")
    print("Make: ", used_car2.get_make())
    print("Model: ", used_car2.get_model())
    print("Mileage: ", used_car2.get_mileage())
    print("Price: ", used_car2.get_price())
    print("\n")

    truck = vehicles.Truck('Toyota', 'Tacoma', 40000, 12000.0)
    suv = vehicles.SUV('Volvo', 'SE', 30000, 18500.0)
    electric_car = vehicles.ElectricCar("Tesla", "Model Y", 20000, 45000.0)

    # Display the trucks data
    print("The following truck is in inventory")
    print("Make: ", truck.get_make())
    print("Model: ", truck.get_model())
    print("Mileage: ", truck.get_mileage())
    print("Price: ", truck.get_price())
    print("\n")

    # Display the cars data
    print("The following car is in inventory")
    print("Make: ", suv.get_make())
    print("Model: ", suv.get_model())
    print("Mileage: ", suv.get_mileage())
    print("Price: ", suv.get_price())
    print("\n")

    # Display the electric cars data
    print("The following electric cars are in inventory")
    print("Make: ", electric_car.get_make())
    print("Model: ", electric_car.get_model())
    print("Mileage: ", electric_car.get_mileage())
    print("Price: ", electric_car.get_price())

main()

