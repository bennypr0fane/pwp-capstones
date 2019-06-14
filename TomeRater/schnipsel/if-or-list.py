def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("User with email {email} already exists.".format(email))
            return
        if "@" not in email:
            print("Please enter a valid e-mail address")
            return
        tlds = [".com", ".edu", ".org"]
        for i in tlds:
            if i not in email:
				print("Please enter a valid e-mail address")
            return
    	        self.users.update({email: User(name, email)})
    	    break
            else:
                
            
        else:
            self.users.update({email: User(name, email)})
        if user_books:
            for book in user_books:
                self.add_book_to_user(book, email)
        return User(name, email)
        



