from functools import wraps
# Не понял, что хотят в первом задании и потому пишу как-то так:
# Task 1


def dec_func(func):
    def inner():
        print(f'{func} имя декорируемой функции и она выводит: {func()}')
    return inner()


@dec_func
def hello_world():
    return 'Hello decorator'


def sum_num(func):
    def inner(*args):
        print(f'результат другой функции: {sum(args)}')
        print(func)
    return inner


@sum_num
def new_func(x, y):
    return x, y


new_func(10, 15)

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
