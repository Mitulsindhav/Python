def decorator(f): # decorate function ni andar function ni rite define thay
    def sample():
        print("This is before Function")
        f()
        print("This is after function")
    return sample

@decorator #Je name nu function banavu e name nu j @ thi pass karva nu function upar pass karavanu 
def star():
    print("*"*50)

star()    
