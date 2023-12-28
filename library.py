class Library:
    BOOKS = [
        "Harry Potter and the Sorcerer's Stone",
        "The Lord of the Rings",
        "The Chronicles of Narnia",
        "The Hunger Games"
    ]

    @staticmethod
    def add_books():
        book = input("Enter the book to be added to library: ")
        if book in Library.BOOKS:
            print(f"The book {book} already exists in the library")
        else:
            Library.BOOKS.append(book)
            print(f"The book {book} successfully added to the library!")

    @staticmethod
    def remove_books():
        book = input("Enter the book to be removed from library: ")
        if book not in Library.BOOKS:
            print(f"The book {book} does not exists in the library")
        else:
            Library.BOOKS.remove(book)
            print(f"The book {book} successfully removed from the library!")