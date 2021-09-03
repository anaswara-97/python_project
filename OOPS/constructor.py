class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print(self.name,self.age,self.address)
p=Person("anaswara\n",23,"\nkanjiraparambil")
p.display()