def oops(x):
    return x[5]


def try_oops():
    try:
        x = oops('abcd')
    except IndexError as ind:
        return f'индекс строки вне диапазона: {ind}'
    return x

print(try_oops())
