import os
import json


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # def writ(self):
    #     with open('person_list.txt', 'w') as p_l:
    #         p_l.write(self.first_name)
    #     with open('person_list.txt', 'r') as p_l:
    #         read_p_l = p_l.read()
    #     return read_p_l

    def __repr__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + str(self.age)


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
        return (self.first_name + ' ' + self.last_name + '\n' + str(self.age) + ' ' + 'Years old' + '\n' +
                self.subject + '\n' + str(self.student_count) + '\n' +
                str(self.salary))


person = Person('Marusia', 'Marusevich', 23)
teacher = Teacher('Nina', 'Mihailovna', 60, 'Biology', 32, 5200)

print(teacher)
print()
print(person)