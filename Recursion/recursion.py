# Task 1
def to_power(x, exp):
    if exp == 0:
        return 1
    if exp < 0:
        return ValueError('This function works only with exp > 0.')
    return to_power(x, exp-1) * x


print(to_power(2, 3))

# Task 2
def is_palindrome(looking_str: str, index: int = 0):
    if len(looking_str) == index:
        return True
    if looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    else:
        return False

print(is_palindrome('sassas'))

# Task 3


def mult(a: int, n: int) -> int:
    if n == 0:
        return n
    if n < 0:
        return ValueError("This function works only with postive integers")
    return mult(a, n-1) + a


print(mult(10, 5))

# Task 4


def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str

    return f'{input_str[-1]}{reverse(input_str[:-1])}'


print(reverse("hello"))

# Task 5


def sum_of_digits(digit_string: str) -> int:
    if len(digit_string) == 0:
        return 0
    try:
        return int(digit_string[0]) + int(sum_of_digits(digit_string[1:]))
    except ValueError:
       print("input string must be digit string")

print(sum_of_digits('123456'))
