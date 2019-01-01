class Book:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content or []
        self.size = len(self.content)

    def read(self, *args, **kwargs):
        raise NotImplementedError

    def write(self, *args, **kwargs):
        raise NotImplementedError


class Novel(Book):
    """класс описывающий книгу и методы работы с ней"""

    def __init__(self, *args, **kwargs):
        """конструктор"""

    def read(self, *args, **kwargs):
        """возвращает страницу"""

    def set_bookmark(self, *args, **kwargs):
        """устанавливает закладку в книгу book"""

    def get_bookmark(self, *args, **kwargs):
        """получает номер страницы установленной закладки в книге book"""

    def write(self, *args, **kwargs):
        """делает запись текста text на страницу page """

    def del_bookmark(self, person):
        """удаляет закладку читателя person, если она установлена"""

class Notebook(Book):
    """класс описывающий тетрадь и методы работы с ней"""

    def __init__(self, *args, **kwargs):
        """конструктор"""

    def read(self, *args, **kwargs):
        """возвращает страницу с номером page"""

    def write(self, *args, **kwargs):
        """делает запись текста text на страницу с номером page """


class Person:
    """класс описывающий человека и методы работы с книгой"""

    def __init__(self, name):
        """конструктор"""

    def read(self, book, page):
        """читаем страницу с номером page в книге book"""

    def write(self, book, page, text):
        """пишем text на страницу с номером page в книге book"""

    def set_bookmark(self, book, page):
        """устанавливаем закладку в книгу book на страницу с номером page"""

    def get_bookmark(self, book):
        """получаем номер страницы установленной закладки в книге book"""

    def del_bookmark(self, book):
        """удаляет закладку читателя person, если она установлена"""