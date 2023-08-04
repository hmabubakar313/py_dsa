def log_function_call(func):
    def wrapper(*args, **kwargs):
        print('Function "{}" called with arguments {}, {}'.format(
            func.__name__, args, kwargs))
        return func(*args, **kwargs)
    return wrapper


@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b

result1 = add(2, 3)
result2 = multiply(4, 5)
