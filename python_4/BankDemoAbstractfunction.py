from abc import ABC,abstractmethod

class Rbi(ABC):

    @abstractmethod
    def Ros(self,Ros):
        pass

    def Intrest(self):
        print("This is Ros class")

class Bank(Rbi):

    def Ros(self):
        print(" This is Bank Class")
    def Intrest(self,Intrest):
        print("I am Bank. My Max Intrest Is", Intrest)



b1=Bank()
b1.Ros()
b1.Intrest(120000)







