def task1():
    with open('myfile.txt', 'w') as myfile:
        myfile.write('Hello file world.\n')


def task1_2():
    with open('myfile.txt', 'r') as myfile:
        read_myfile = myfile.read()
        print(read_myfile)

    with open('e:\\myfile.txt', 'r') as myfile2:
        read_myfile2 = myfile2.read()
        print(read_myfile2)


def task2():
    pass
