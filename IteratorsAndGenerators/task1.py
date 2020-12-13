my_list = ['q', 'g', 'r', 'uy', 'kk', 'fvb']
my_string = 'jnfsbfglbbgfl'


def with_index(items, start: int = 0):
    for i in items:
        yield start, i
        start += 1


for i, item in with_index(my_list, 3):
    print(i, item)
