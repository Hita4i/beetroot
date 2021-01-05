class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.name}'


class Book:
    TOTAL_BOOKS = 0

    def __init__(self, name, year, author: Author):
        self.name = name
        self.year = year
        self.author = author

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}'


class Library:

    def __init__(self, library_name=None):
        self.library_name = library_name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        Book.TOTAL_BOOKS += 1
        return book

    def group_by_author(self, name: Author):
        return f'Автор: {name}\nКниги: {[book for book in self.books if book.author == name]}'\
            .replace('[', '').replace(']', '')

    def group_by_year(self, year):
        return f'Книги {year} года издания: {[book for book in self.books if book.year == year]}'\
            .replace('[', '').replace(']', '')

    def __repr__(self):
        return f'{self.library_name} {self.books} {self.authors}'

    def __str__(self):
        return f'{self.library_name} {self.books} {self.authors}'


sapkowski = Author('Анджей Сапковский', 'Польская Народная Республика', '21.07.1948')
stephen_king = Author('Стивен Эдвин Кинг', ' Портленд, Мэн, США', '21.09.1947')
lib = Library()

lib.new_book('Ведьмак: Последнее желание', 1990, sapkowski)
lib.new_book('Ведьмак: Меч Предназначения', 1992, sapkowski)
lib.new_book('Ведьмак: Кровь эльфов', 1984, sapkowski)
lib.new_book('Жребий', 1975, stephen_king)
lib.new_book('Стрелок', 1982, stephen_king)
lib.new_book('Кладбище домашних животных', 1983, stephen_king)
print(lib.group_by_author(sapkowski))
print(lib.group_by_year(1984))
