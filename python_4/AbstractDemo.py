from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def speed(self,speed):
        pass

    def show(self):
        print("This is Vehicle class")

class Bike(Vehicle):

    def show(self):
        print(" This is Bike Class")
    def speed(self,speed):
        print("I am Bike. My Max Speed Is", speed)

class Car(Vehicle):

    def show(self):
        print(" This is car class")
    def speed(self,speed):
        print("I am Car. My Max Speed Is ",speed)

b1=Bike()
b1.show()
b1.speed(120)


c1=Car()
c1.show()
c1.speed(220)





