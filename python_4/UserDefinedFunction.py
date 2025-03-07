#function with no  argument & no return value.

def printLine():
    print("*"*45)

printLine()
print("Welcome To User Defined Function ")
printLine()


#function with argument but no return value.

def add(a,b):
    print("Addition :" ,a+b)

printLine()
add(10,20)
printLine()

#function with argument & return value.

def sub(a,b):
    return a-b

printLine()
ans=sub(10,20) #Biji var use karva mate variable ma store karva mate use thay se 
#print("Subtraction :",ans)
print("Subtraction :",sub(10,20)) #use na karvu hoy to direct print karavi devanu  
printLine()
        
    
