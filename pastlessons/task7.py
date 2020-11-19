# Задание 1
def favorite_movie(movie: str):
    return f'My favorite movie is named "{movie}"'


print(favorite_movie('Gladiator'))
# Задание 2
country_and_capitals = dict()


def make_country(name: str, capital: str):
    country_and_capitals[name] = capital
    return country_and_capitals


make_country(input('Enter country name: '), input('Enter capital: '))
make_country(input('Enter country name: '), input('Enter capital: '))
print(country_and_capitals)


# Задание 3
def make_operation(operator: str, *args: int):
    total = 0
    total_multi = 1
    if operator == '-':
        total = args[0]
        for arguments in args[1:]:
            total -= arguments
        return total
    if operator == '*':
        for arguments in args:
            total_multi *= arguments
        return total_multi
    elif operator == '+':
        total = sum(args)
    return total


print(make_operation('*', 5, 5, -10, -20))
