# Task 1

def oops():
    x = input('Enter string: ')
    return x[40]


def try_oops():
    try:
        oops()
    except IndexError as ind:
        return f'индекс строки вне диапазона: {ind}'



print(try_oops())


# Task 2
def squared_a_divided_by_b(a, b):

    try:
        a = int(a)
        b = int(b)
        sq = a ** a / b
    except ValueError as value:
        sq = value
        return f'Вы ввели буквы вместо цифр: {sq}'
    except ZeroDivisionError as zero:
        sq = zero
        return f'Вы ввели 0: {zero}'
    return sq


print(squared_a_divided_by_b(input('Введите число А: '), input('Введите число Б: ')))
