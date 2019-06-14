def get_keys_by_value(dictionary, value_to_find):
    list_of_keys = []
    list_of_items = dictionary.items()
    for item  in list_of_items:
        if item[1] == value_to_find:
            list_of_keys.append(item[0])
    return  list_of_keys


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}
        self.average_rating = self.get_average_rating(self.books)

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("E-mail address has been updated\n")
        return address

    def __repr__(self):
        return "user: {name}\ne-mail: {email}\nbooks read: {books}".format(name=self.name, email = self.email, books=self.books)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            print("identical users!\n")
            return True
        
    def read_book(self, book, rating=None):
        self.books[book.title] = rating
        if rating:
            book.add_rating(rating)
        
    def get_average_rating(self, books):
        ratings_total = 0
        for book in self.books:
            ratings_total += self.books[book]
        if len(self.books) > 0:
          average = ratings_total / len(self.books)
        else:
          average = None
        return average

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, new_isbn):
#        if new_isbn in TomeRater.isbns:
#            for book in TomeRater.books.keys:
#                if book.isbn == new_isbn:
#                    print("IBSN already exists in database:\n{}".format(book))
#            return
#        else:
        self.isbn = new_isbn
        print("ISBN has been updated\n")
    
    def add_rating(self, rating=0):
        self.ratings = []
        if 0 <= rating < 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Valid ratings are numbers are from 0 to 4.\n")
     
    def get_average_rating(self):
        if len(self.ratings) < 1:
          return
        ratings_total = 0
        for rating in self.ratings:
            ratings_total += rating or 0
        average = ratings_total / len(self.ratings)
        return average
          
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            print("identical books!\n")
            return True
     
    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title}\nrating: {rating}".format(title=self.title, rating=self.get_average_rating())


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
    
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}\nrating: {rating}".format(title=self.title, author=self.author, rating=self.get_average_rating())


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return subject

    def get_level(self):
        return level

    def __repr__(self):
        return "{title}, a {level} book on {subject}\nrating: {rating}".format(title=self.title, level=self.level, subject=self.subject, rating = self.get_average_rating())
 
 
 
class TomeRater:
    def __init__(self, name):
        self.name = name
        self.users = {}
        self.books = {}
        self.isbns = []
    
    def __repr__(self):
        return "**{name} book rating database**\nNumber of users: {users}\nNumber of books: {books}".format(name=self.name, users=len(self.users), books=len(self.books))
    
    def create_book(self, title, isbn):
        if isbn in self.isbns:
            print("This book already exists in our database.")
        else:
            self.isbns.append(isbn)
            print("New book added.")
            return Book(title, isbn)
    
    def create_fiction(self, title, author, isbn):
        if isbn in self.isbns:
            print("This book already exists in our database.")
        else:
            self.isbns.append(isbn)
            print("New fiction book added")
            return Fiction(title, author, isbn)
    
    def create_non_fiction(self, title, subject, level, isbn):
        if isbn in self.isbns:
            print("This book already exists in our database.")
        else:
            self.isbns.append(isbn)
            print("New non-fiction book added")
            return NonFiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating=0):
        if email not in self.users:
            print("No user with email {email}!\n".format(email=email))
        else:    
            user = self.users.get(email)
            user.read_book(book, rating)
            book.add_rating(rating)
            print("Added \'{}\' to user {}.".format(book.title, email))
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
    
    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("User with email {email} already exists.".format(email=email))
            return
        elif "@" not in email:
            print("Please enter a valid e-mail address.")
            return
        tlds = [".com", ".edu", ".org"]
        for i in tlds:
            if i in email:
                self.users.update({email: User(name, email)})
                print("New user added")
                if user_books:
                    for book in user_books:
                        self.add_book_to_user(book, email)
                return User(name, email)
        else:
            print("Please enter a valid e-mail address.")
 
    def print_catalog(self):
        if list(self.books.keys()) == []:
                print("No books yet.")
        else:
            print("**Catalog:**")
            for book in self.books:
                print(book)
            print("**End of catalog**\n")
            
    def print_users(self):
        if list(self.users.values()) == []:
                print("No users yet.")
        else:
            print("**List of users:**")
            for user in self.users.values():
                print(user)
            print("**End of user list**\n")
    
    def most_read_book(self):
        print("Most read book:")
        most_read = 0
        for book in self.books:
            if self.books[book] > most_read:
                most_read = self.books[book]
        return get_keys_by_value(self.books, most_read)
 
    def highest_rated_book(self):
        print("Highest rated book:")
        highest_av_rating = 0
        best_book = None
        for book in self.books:
            average_rating = book.get_average_rating()
            if average_rating > highest_av_rating:
                highest_av_rating = average_rating
                best_book = book
        return best_book
    
    def most_positive_user(self):
        print("Most positive user:")
        highest_rating = 0
        most_positive = None
        for user in self.users.values():
            if len(user.books) > 2:
                average_rating = user.get_average_rating(user.books)
                if average_rating > highest_rating:
                    highest_rating = average_rating
                    most_positive = user
        print("Average rating: " + str(highest_rating))
        return most_positive