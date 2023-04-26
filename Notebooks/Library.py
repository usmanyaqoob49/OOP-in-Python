class Libray():
    def __init__(self, book_list):
        self.available_book_list = book_list
    #to display the available books
    def display_available_books(self):
        #for books in self.available_book_list:
        print(self.available_book_list)
        print()
    
    #to lend a book 
    #it will recieve the name of book user wants
    def lend_book(self, requested_book):
        if requested_book in self.available_book_list:
            print('You have borrowed the book.')
            self.available_book_list.remove(requested_book)
        else:
            print('Book not available')
        print()
    
    #to add book to library
    #to add a book that is returned by the user
    def add_book(self, returned_book_name):
        self.available_book_list.append(returned_book_name)
        print('You have returned the book!')
        
        
        
class Customer():
    #method for requesting for a book
    def request_book(self):
        print('Enter the name of the book you want to borrow: ')
        self.book = input()
        #we will pass this name to lend_book method of Library class
        return self.book
    
    #method for returning a book
    def return_book(self):
        print('Enter the name of the book you are returning: ')
        self.book = input()
        #we will pass this book to add_book() method of Library
        return self.book
    
    
    
#objects
#we will pass the list of books we have when initializing a object
library = Libray(['book1', 'book2', 'book3'])

customer = Customer()



while True:
    print('Enter 1 to display the available books: ')
    print('Enter 2 to request for a book: ')
    print('Enter 3 to return the book: ')
    print('Enter 4 to exit! ')
    user_choice = int(input())
    if user_choice == 1:
        library.display_available_books()
    elif user_choice == 2:
        requested_book = customer.request_book()
        library.lend_book(requested_book)
    elif user_choice == 3:
        return_book = customer.return_book()
        library.add_book(return_book)
    elif user_choice == 4:
        quit()


