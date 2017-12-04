from html.parser import HTMLParser
class Book(object):
    def __init__(self, url = None, name = None, author = None, publication_date = None, price = None, publish_company = None, books_name = None, content = None, ISBN = None):
        self.url = url
        self.__name = name
        self.author = author
        self.publication_date = publication_date
        self.price = price
        self.publish_company = publish_company
        self.books_name = books_name
        self.content = content
        self.ISBN = ISBN

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, data):
        self.__name = data

    def __str__(self):
        return 'book url(%s)\n name(%s)\n author(%s)\n publication_date(%s)\n price(%s)\n publish_company(%s)\n' \
               'books_name(%s)\n ISBN(%s)\n content(%s)\n' % (self.url, self.name, self.author, self.publication_date, \
               self.price, self.publish_company, self.books_name, self.ISBN, self.content)


