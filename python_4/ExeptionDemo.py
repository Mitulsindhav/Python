print("start code ")

try:
    a=int(input("Enter A :"))
    b=int(input("Enter B :"))
    c=a/b
    print("Division :",c)
    l=["Java","python","php","testing"]
    index=int(input("Enter Index Number :"))
    print(l[index])
except ZeroDivisionError as e:
    print("Exception Caught :",e)
except ValueError as e:
    print("Exception Caught :",e)
except IndexError as e:
    print("Exception Caught :",e)
print("End Code")

     

    
    
    
    
