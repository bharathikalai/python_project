class Library():

    def __init__(self,list):
        self.book_list = list
        self.available_books_list = list[:]
        self.books_lent  = {}

    def display_available_book(self):
        for book in self.available_books_list:
            print(book)

    
    def display_all_book(self):
        for book in self.book_list:
            print(book)

    def lend_book(self,name,book):
        if book not in self.book_list:
            print("incorrect book name please check the book list")
            return
        if book in self.available_books_list:
            self.books_lent.update({book:name})
            self.available_books_list.remove(book)
            print("you can take the book ")
        else:
            print("this book is alreday taken by " + self.books_lent[book])
        

    def return_book(self,book):
        del self.book_lent[book]
        self.available_books_list.append(book)

if __name__ == "__main__":
    lib = Library(["alu","kalu","thalu","malu","masu"])
    print("welcome to liberary enter an option")
    while True:
        print("1.display avaolable books")
        print("2. display all books")
        print("3.borrow a book")
        print("4. return a book")
        print("5. quit")
        user_choise = int(input())
        if user_choise == 1:
            lib.display_available_book()
        elif user_choise == 2:
            lib.display_all_book()
        elif user_choise == 3:
            name = input("enter the user name")
            book = input("enter the book name")
            lib.lend_book()
        elif user_choise == 4:
            lib.return_book()
            book = input("enter the book name")
            lib.return_book()

        elif user_choise == 5:
            break
        else:
            print("invalid choics")
