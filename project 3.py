class Library:
    
    def __init__(self,listofbooks):
        self.books=listofbooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
             print("\t *" + book)

    
    def borrowBook(self,bookname):
        if bookname in self.books:
            print(f"you have issued {bookname}. please keep it safe and return it within 30 days")
            self.books.remove(bookname)
            return True
        
        else:
            print( f"sorry,{bookname}  is already been issued. ")
            return False
    
    
    def returnBook(self,bookname):
        self.books.append(bookname)
        print(f"thanks , for returning this {bookname}")



class Student:
    def requestBook(self):
        self.book = input("enter the book name:\n")
        return self.book

    def returnBook(self):
        self.book = input("enter the book name you want to return:\n")
        return self.book

if __name__ == "__main__":
    CentralLibrary = Library(["Algorithms","Django","Clrs","Python notes"])
    student =Student()
    #CentralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''=====Welcome to Central Library====
        please choose an option :
        1. listing all the books 
        2. request a book
        3. return a book
        4. exit the library
        '''
        print(welcomeMsg)
        
        a=int(input("enter a choice: "))
        if a==1:
            CentralLibrary.displayAvailableBooks()
        elif a==2:
            CentralLibrary.borrowBook(student.requestBook())

        elif a==3:
            CentralLibrary.returnBook(student.returnBook())

        elif a==4:
            print("thnks for chossing central library: " )
            exit()

        else:
            print("invalid choice!")
    
