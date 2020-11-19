def string_manipulation(string):
    first = string[0:2]
    last = string[-2::]
    if len(string) >=2:
        return f'{first}{last}'
    else:
        return ''

print(string_manipulation('helloworld'))

def phone_number(number):
    if len(number) == 10 and number.isdigit():
        return 'Your number is correct'
    elif len(number) < 10:
        return 'Your number is short'
    elif len(number) > 10:
        return 'Your number to long'
    else:
        return 'Еhe number cannot contain letters'

print(phone_number('066602423w'))

def name_check(name):
    my_name = 'vitalii'
    if name == my_name:
        return name == my_name
    else:
        return f'Ne Ok. You enter {name}, but my name is {my_name}'


print(name_check(input().lower()))