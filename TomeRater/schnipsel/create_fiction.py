# Fiction class:
class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}\nrating: {rating}".format(title=self.title, author=self.author, rating=self.get_average_rating())

#TomeRater so far:

class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}
    
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_fiction(self, title, isbn, author):
        return Fiction(title, isbn, author)
    
    def create_non_fiction(self, title, isbn, subject, level): #this seems not to work
        return NonFiction(title, isbn, subject, level)
    
    def add_book_to_user(book, email, rating=None):
        if self.users[email]:
            self.users.get(email).read_book(book, rating)
        else:    
            print("No user with email {email}!".format(email=email))

TomeRater.create_fiction("Ilias", 1000111111, "Homer") #this produces the following error:

#Traceback (most recent call last):
#  File "/home/ben/Nextcloud/codn/programming-with-Python.Cdcdm/Projekte/TomeRater/TomeRater.py", line 145, in <module>
#    TomeRater.create_fiction("Ilias", 1000111111, "Homer")
#TypeError: create_fiction() missing 1 required positional argument: 'author'

