class Car:
    totalCars = 0 # Class Variable

    def __init__(self, brand, model):
        self.__brand = brand # so by using __ we can make it private
        self.__model = model

        # self.totalCars += 1 # This will create a new instance variable for each object as a result the totalCars will not be updated and remain 1 for all
        Car.totalCars += 1

    # Creating getter for the private variables
    def getbrand(self):
        return self.__brand
    
    # Creating getter for the private variables
    def getmodel(self):
        return self.__model
    
    def FuelType(self):
        return "Petrol Or Diesel"
    
    @staticmethod
    def GeneralarDesc():
        print("This is a car class")


class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.__battery = battery

    # Creating getter for the private variables
    def getbattery(self):
        return self.__battery
    
    def FuelType(self): # Even If you are not using any class variable, self is still necessary coz its what attach the method
        # to the class and that is how its gets differentiated for different object
        return "Electricity"


ford = Car("Ford", "Escape")
print(ford.getbrand() + " " + ford.getmodel())
print(ford.FuelType())

tesla = ElectricCar("Tesla", "Model 3", "85kWh")
print(tesla.getbrand() + " " + tesla.getmodel() + " " + tesla.getbattery())
print(tesla.FuelType())
print(tesla.totalCars)

car2 = Car("Car 2", "Model 2")
print(car2.totalCars) 
print(car2.GeneralarDesc())

car3 = Car("Car 3", "Model 3")
print(car3.totalCars) 
print(car3.GeneralarDesc())


# Multiple Inheritance

print("\n   Multiple Inheritance\n")

class Engine():
    def Engine_info(self):
        return "Engine Info"
    
class Battery():
    def Battery_info(self):
        return "Battery Info"
    
class NewCar(Car, Engine,Battery):
    def __init__(self):
        print("This is a new car")


newCar = NewCar()
print(newCar.Engine_info())
print(newCar.Battery_info())
print(newCar.GeneralarDesc())