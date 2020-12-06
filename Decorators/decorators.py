from functools import wraps
# Task 1


def logger(func):
    @wraps(func)
    def inner(*args):
        print(f'{func.__name__} - {args}')
    return inner


@logger
def add(x, y):
    return x, y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(10, 15)
square_all(15, 30, 60)

# Task 2


def simple_decorator(f):
    @wraps(f)
    def inner(*args, **kwargs):
        result = f(*args, **kwargs)
        bad_words = ['pepsi', 'BMW']
        for word in bad_words:
            if word in result:
                result = result.replace(word, '*')
        print(result)
    return inner('Steve')


@simple_decorator
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"
