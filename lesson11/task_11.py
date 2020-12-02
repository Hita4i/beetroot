

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        return f'{self.first_name} {self.last_name} - {self.age}'


class Student(Person):
    def __init__(self, first_name, last_name, age, student_class, total_evaluation):
        super().__init__(first_name, last_name, age)
        self.student_class = student_class
        self.total_evaluation = total_evaluation

    def evaluation(self, evaluation):
        self.total_evaluation += evaluation


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject, student_count, salary):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.student_count = student_count
        self.salary = salary

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.age} Years old\nSusject is: {self.subject} \n' +\
                    f'Student count is: {self.student_count}\nSalsry: {self.salary}'


person = Person('Marusia', 'Marusevich', 23)
teacher = Teacher('Nina', 'Mihailovna', 60, 'Biology', 32, 5200)

print(teacher)
print()
print(person)


class Mathematician:

    def square_nums(self, items):

        return [i * i for i in items]

    def remove_positives(self, items):

        return [i for i in items if i < 0]

    def filter_leaps(self, items):
        
        return [i for i in items if i % 4 == 0]


s = Mathematician()
print(s.square_nums([2, 6, 5]))
print(s.remove_positives([-1, -5, 6, 10, -20]))
print(s.filter_leaps([2000, 2020, 2015, 2010]))
