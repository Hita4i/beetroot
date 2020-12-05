#Task 1
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

#Task 2




# class Author:
#     def __init__(self, name, country, birthday, books):
#         self.name = name
#         self.country = country
#         self.birthday = birthday
#         self.books = books
#
#
#
#
# class Book(Author):
#
#     def __init__(self, name, year, author):
#         super().__init__(self, name)
#         self.name = name
#         self.year = year
#         self.author = author
#
#
# class Library:
#
#     def __init__(self, name, books: list, authors: list):
#         self.name = name
#         self.books = books
#         self.authors = authors
#
#     def new_book(self, name: str, year: int, author: Author):
#         self.name = name
#         self.year = year
#         self.author = author
#         new_book = Book(self.name, self.country, self.birthday, self.books)
#         self.books.append(new_book)
#         return f'{self.books}'
#
#     def group_by_author(self, name: str, books: str):
#         return [book for book in books if name == name]
#
# author_ = Author(['Анджей Сапковский',
#                   'Польская Народная Республика',
#                   '21 июня 1948',
#                   ['Ведьмак: «Последнее желание»',
#                    'Ведьмак: «Меч Предназначения»',
#                    'Ведьмак: «Кровь эльфов»']])
# library_ = Library()
# book_ = Book([])
#
#
# class Fraction:
#
#     def __init__(self, first_fraction, second_fraction):
#         self.first_fraction = first_fraction
#         self.second_fraction = second_fraction
#
# class Sum(Fraction):
#     def __init__(self, first_fraction, second_fraction):
#         super().__init__(self, first_fraction, second_fraction)
#
#     def sum_(self.first_fraction, second_fraction):
#         x = (first_fraction[0])
#         y = str(first_fraction[1])
#         x2 = second_fraction[0]
#         y2 = second_fraction[1]
#         return x
# my_x = Sum([1/2, 1/3])
# print(my_x)
