# Tyler Williams
# SDEV 220
# 02/01/2023
# Create a new object based on a user's input on a car, and then output the result in a neat


class Vehicle():
    pass
class Automobile(Vehicle):
    pass

Vehicle.type = str(input("What type is the vehicle?"))

Automobile.year = int(input("What is the year of the vehicle?"))
Automobile.make = str(input("What is the make of the vehicle?"))
Automobile.model = str(input("What is the model of the vehicle?"))
Automobile.doors = int(input("How many doors does the vehicle have?(2 or 4)"))
Automobile.roof = str(input("What type of roof does the vehicle have?"))

print("Vehicle type:", Vehicle.type.capitalize())
print("Year:", Automobile.year)
print("Make:", Automobile.make.upper())
print("Model:", Automobile.model.capitalize())
print("Number of doors:", Automobile.doors)
print("Type of roof:", Automobile.roof.capitalize())

