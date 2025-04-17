# Question: 
# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped! NO

class Library:
    def __init__(self,no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books
    
    def all_books(self):
        print('S.no. | Books Name')
        for i in range(len(self.books)):
            print(f'{i + 1}     | {self.books[i]}')


    def add_book(self):
        onemore = input("Enter name of the book: ")
        self.books.append(onemore)
        print(f'{onemore} added successfully!')
        yn = input("Want you add more books(y/n): ")
        self.add_book() if yn in 'yYes' else None

    
pustakye = ['harry potter', 'the misery', 'the alchemist', 'eragon', 'the song of ice and fire', '12th fail', 'rich dad poor dad', 'think and grow rich', 'atomic habbit', 'the subtle art of not giving a fuck']
l1 = Library(len(pustakye), pustakye)
l1.all_books()
l1.add_book()
l1.all_books()
