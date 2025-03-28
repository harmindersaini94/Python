class Car:
    #This is how we declare a constructor in a Python class
    #self is equivalent to this here
    #self is must here
    def __init__(self, brand = "No Brand", model = "No Model"):
        self.brand = brand
        self.model = model

# So here in member functions, in order to make use of class variable, we have to access them by self, but for that self must be passes as a paramerter to the function
    def getFullName(self):
        print(f"{self.brand} {self.model}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

        def getFullName2(self):
            print(f"{self.brand} {self.model} {self.battery}")
    
#No need to have a new keyword 
myCar1 = Car("Maruti", "SX4")
myCar1.getFullName()
#print(f"{myCar1.brand} : {myCar1.model}")

myCar2 = Car("Ford", "Escape")
myCar2.getFullName()
#print(f"{myCar2.brand} : {myCar2.model}")

myCar3 = Car()
myCar3.getFullName()
#print(f"{myCar3.brand} : {myCar3.model}")#

myCar4 = ElectricCar("Ford", "Escape", "1kwh")
myCar4.getFullName()
myCar4.getFullName2()