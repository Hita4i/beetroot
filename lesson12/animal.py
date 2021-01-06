class Animal:

    def talk(self):
        return 'Talk something'


class Dog(Animal):
    def talk(self):
        return 'woof woof'


class Cat(Animal):
    def talk(self):
        return 'meow'


dog = Dog()
cat = Cat()
get = [dog, cat]
for i in get:
    print(i.talk())
