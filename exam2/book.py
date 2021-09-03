class Book:
   def  setDetails(self, book_name, author):
       self.book_name=book_name
       self.author=author
   def display(self):
        print("book_name : ",self.book_name)
        print("author : ",self.author)
class Library(Book):
    def setDetails(self, book_name, author):
        self.book_name = book_name
        self.author = author
    def display2(self):
        print("book_name : ", self.book_name)
        print("author : ", self.author)
b=Book()
b.setDetails("manj","m t vasudevan nair")
b.display()
print("-------")
l=Library()
l.setDetails("agnichirakukal","apj abdul kalam")
l.display2()
l.display()