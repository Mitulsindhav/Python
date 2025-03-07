cube1=lambda x:x**3
print(cube1(5))

def cube(x):
    return x*x*x
print("Cube :",cube(10))

ans=lambda a,b:a if a>b else b
print(ans(10,20))




odd_even=lambda a:"a is Even" if a%2==0 else "a is odd"
print(odd_even(10))



max_three = lambda a, b, c: a if (a > b and a > c) else (b if b > c else c)
print(max_three(10,20,30))




