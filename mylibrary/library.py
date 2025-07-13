class Library:
    def __init__(self):
        self.book = None  
    def add_book(self, title, author):
        self.book = {'title': title, 'author': author}  
        print("Book added")

    def remove_book(self):
        self.book = None  
        print("Book removed")

    def show_book(self):
        if self.book:
            print("Book:", self.book['title'], "-", self.book['author'])
        else:
            print("No book available")