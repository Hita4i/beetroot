my_list = ['q', 'g', 'r', 'uy', 'kk', 'fvb']
my_string = 'jnfsbfglbbgfl'
def with_index(items, start: int = 0):
    x = len(items)
    while start < x:
        for item in items:
            start += 1
            print(start - 1, item)


with_index(my_list, 1)
# with_index(my_string, 1)