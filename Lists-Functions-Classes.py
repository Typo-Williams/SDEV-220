# Tyler Williams
# SDEV 220
# 02/01/2023
# Create a new object based on a user's input on a car, and then output the result in a neat


class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

type_input = str(input("What type is the vehicle?"))

vehicle_input = Vehicle(vehicle_type= type_input)

year_input = int(input("What is the year of the vehicle?"))
make_input = str(input("What is the make of the vehicle?"))
model_input = str(input("What is the model of the vehicle?"))
doors_input = int(input("How many doors does the vehicle have?(2 or 4)"))
roof_input = str(input("What type of roof does the vehicle have?"))

vehicle_summary = Automobile(year= year_input, make= make_input, model= model_input, doors = doors_input, roof = roof_input)

print("Vehicle type:", vehicle_input.vehicle_type.capitalize())
print("Year:", vehicle_summary.year)
print("Make:", vehicle_summary.make.upper())
print("Model:", vehicle_summary.model.capitalize())
print("Number of doors:", vehicle_summary.doors)
print("Type of roof:", vehicle_summary.roof.capitalize())

