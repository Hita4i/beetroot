def in_range(start: int, stop: int = None, step: int = 1):
    if stop == None:
        new_start = start
        start = 0
        stop = new_start
    if step > 0:
        while start <= stop - 1:
            yield start
            start += step
    else:
        while start >= stop + 1:
            yield start
            start += step


for item in in_range(10):
    print(item)
