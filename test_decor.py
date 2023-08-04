def testing_decorator(func):
    def wrapper(*args, **kwargs):
        print("I am decorator")
        return func(*args, **kwargs)
    return wrapper





@testing_decorator
def func(a,b):
    a=2
    b=3
    return a+b

func(2,3)