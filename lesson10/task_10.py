class Person:

    def __init__(self, firstname: str, lastname: str, age: int):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f"Hello, my name is {self.firstname} {self.lastname} and i'm {self.age} years old"


class Dog:

    age_factor = 7

    def __init__(self, dog_age: int):
        self.dog_age = dog_age

    def human_age(self):
        return f'Dog age in human equivalent is {self.age_factor * self.dog_age}'


# class TvController:
#     pass


person1 = Person('Carl', 'Jonson', 26)
person2 = Person('Mr.', 'Morgan', 50)
dog_sharik = Dog(5)
dog_bobik = Dog(3)
