#-----------------------------------------------------------------
from POOP import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()
#-----------------------------------------------------------------
class Car:

    def __init__(self,make,model,year,color):#py art constructor
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
#-----------------------------------------------------------------