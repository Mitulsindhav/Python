class Student:

    def getstudent(self,fname,lname):
        self.f=fname
        self.l=lname
    def printstudent(self):
        print("first Name:",self.f)
        print("Last Name :",self.l)


s1=Student()
#s2=Student()
f=input("Enter First Name :")
l=input("Enter Last Name :")
s1.getstudent(f,l)
s1.printstudent()

#self = class no diffult object  , class purto global use karva mate self use mate 
