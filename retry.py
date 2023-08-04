def retry_func(function):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print('Exception caught: {}'.format(e))
            return func(*args, **kwargs)
    return wrapper



@retry_func
def func(a=0,b=2):
    print('function')
    return 0/2