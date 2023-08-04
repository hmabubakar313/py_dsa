def auth(func):
    def wrappper(*args,**kwargs):
        print("you are authinticated")
        return func(*args,**kwargs)
    return wrappper




@auth
def func():
    print("you aree authinticated")
    return True

func()