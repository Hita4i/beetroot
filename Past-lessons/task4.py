import random
print('-' * 30, 'Задание 1', '-' * 30)

random_number = random.randint(1, 10)
while True:
    user_input_number = int(input('Введите число от 1 до 10: '))
    if user_input_number > 10:
        print(f'Ты ввел слишком большое число...\n'
              f'Мы угадываем от 1 до 10, а ты ввел {user_input_number}')
    elif user_input_number < 1:
        print(f'Ты ввел слишком маленькое число...\n'
              f'Мы угадываем от 1 до 10, а ты ввел {user_input_number}')
    elif random_number == user_input_number:
        print('Угадал!')
        break

    else:
        print('Не угадал :(')
        if user_input_number > random_number:
            print('Твое число больше чем задуманное. Давай еще разок!')
        elif user_input_number < random_number:
            print('Твое число меньше чем задуманное. Давай еще разок!')
print('-----> Победа твоя!!! <-----')

print()
print('-' * 30, 'Задание 2', '-' * 30)
print()

while True:
    user_name = input('Введите свое имя: ')
    if len(user_name) <= 0:
        print('Имя какое-то слишком короткое...')
        continue

    elif user_name.isdigit():
        print('Странное имя однако...')
        continue

    user_age = input('Введите свой возраст: ')
    if user_age.isdigit():
        user_age = int(user_age)
        print(f'«Привет {user_name}, в следующий день рождения тебе исполнится {user_age + 1} лет»')
        break

    else:
        print('Что-то пошло не так')

print()
print('-' * 30, 'Задание 3', '-' * 30)
print()

x = 0
user_word = list(input('Введите желаемые символы(не меньше трех): '))
if len(user_word) < 3:
    print('Вы ввели слошком короткое слово')

while x < 6:
    random.shuffle(user_word)
    new_string = ''.join(user_word)
    print(new_string)
    x += 1

print()
print('-' * 30, 'Задание 4', '-' * 30)
print()

x = 23
y = 15
math_expression = x + y
user_answer = int(input(f'Сколько будет {x} + {y}?\nВаш ответ: '))
if user_answer == math_expression:
    print('Отлично!')
else:
    print('Не угадал')
print('-' * 32, 'Конец', '-' * 32)
