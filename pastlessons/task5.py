import random

print()
print('-' * 30, 'Задание 1', '-' * 30)
print()

list_of_numbers = []
while len(list_of_numbers) < 10:
    list_of_numbers.append(random.randint(1, 1000))
max_number = max(list_of_numbers)
print(f'Спислк случайных чисел: {list_of_numbers}')
print(f'Самое большое число в списке: {max_number}')

print()
print('-' * 30, 'Задание 2', '-' * 30)
print()

first_list = []
second_list = []
third_list = []
while len(first_list) < 10 and len(second_list) < 10:
    first_list.append(random.randint(1, 10))
    second_list.append(random.randint(1, 10))
third_list = list(set(first_list + second_list))
print(third_list)

print()
print('-' * 30, 'Задание 3', '-' * 30)
print()

my_list1 = list(range(1, 100))
my_list2 = []
for i in my_list1:
    if i % 7 == 0 and i % 5 != 0:
        my_list2.append(i)
print(my_list2)

print([
    i for i in range(100) if i % 7 == 0 and i % 5 != 0
])
