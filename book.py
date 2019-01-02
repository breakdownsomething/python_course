class BookIOErrors(Exception):
    pass


class NotExistingExtensionError(BookIOErrors):
    pass


class PermissionDeniedError(BookIOErrors):
    pass


class PageNotFoundError(BookIOErrors):
    pass


class TooLongTextError(BookIOErrors):
    pass


class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, page):
        raise NotImplementedError

    def write(self, page, text):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""
    def __init__(self, author, year, title, content):
        """конструктор"""
        super().__init__(title, content)
        self.author = author # имя автора (строка)
        self.year = year # год издания (целое)
        self.bookmark = dict() # закладки (словарь {читатель:номер страницы})

    def read(self, page):
        """возвращает страницу"""

    def set_bookmark(self, person, page):
        """устанавливает закладку в книгу book"""
        self.bookmark[person] = page

    def get_bookmark(self, person):
        """получает номер страницы установленной закладки в книге book"""
        try:
            return self.bookmark[person]
        except KeyError:
            raise PageNotFoundError

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""
        try:
            self.bookmark.pop(person)
        except KeyError:
            pass

    def write(self, page, text):
        """делает запись текста text на страницу page """


class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, title, size, max_sign, content):
        """конструктор"""

    def read(self, page):
        """возвращает страницу с номером page"""

    def write(self, page, text):
        """делает запись текста text на страницу с номером page """


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""
        self.name = name

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""

    def write(self, book, page, text):
        """пишем на страницу с номером page в книге book"""

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""
        book.set_bookmark(self, page)

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""
        

    def del_bookmark(self, book):
        """удаляет закладку из книги book"""


from string import ascii_lowercase as alphabet
content = [sign for sign in alphabet]
n = Novel('Grin', 1925, 'Gold chain', content)
print(n.__dict__)