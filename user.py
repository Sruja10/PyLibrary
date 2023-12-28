from library import *
from exceptions import *

print("Welcome to PyLibrary")


class User:

    @staticmethod
    def book_check(book):
        if book not in Library.BOOKS:
            raise AvailabilityException(f"Apologies, the book '{book}' is not available in the library at the moment")
        else:
            print(f"The book '{book}' is  available in the library")

    @staticmethod
    def token_check(token):
        if token == 0:
            raise TokenException(f"You don't have sufficient token to take a book")
        else:
            pass


    def __init__(self):
        print("Please enter the below details to get started")
        self.name = input("Name: ")
        self.age = int(input("Age: "))
        self.token = int(input("Number of tokens you want to start with: "))

    def token_info(self):
        print(f'Hi {self.name}\nYour token balance is {self.token}')


    def book_to_take(self):
        try:
            self.token_check(self.token)
            book = input("Enter the book you want to take: ")
            self.book_check(book)
            print(f"Happy reading!!")
            self.token -= 1
            Library.BOOKS.remove(book)
            print(f"Your updated token balance is: {self.token}")
        except TokenException as e:
            print(e)
        except AvailabilityException as e:
            print(e)

    def book_to_return(self):
        book = input("Enter the book you want to return: ")
        Library.BOOKS.append(book)
        self.token += 1
        print(f"Thank you for returning the book {self.name}!\nHope it was a good read")
        print(f"Your updated token balance is: {self.token}")
