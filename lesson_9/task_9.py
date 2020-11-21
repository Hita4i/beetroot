def task1():
    with open('myfile.txt', 'w') as myfile:
        myfile.write('Hello file world')
task1()
def task1_2():
    with open('myfile.txt', 'r') as myfile:
        p = myfile.read()
    print(p)

task1_2()

def task2():
    pass