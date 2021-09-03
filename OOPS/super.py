class Person:
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr                                               #person - parent = single inheritance
    def getPerson(self):                                            #person - parent - child = multilevel inheritance
        print("name : ",self.name)
        print("address : ",self.addr)
class Parent(Person):
    def __init__(self,mob,place,name,addr):
        super().__init__(name,addr)
        self.mob=mob
        self.place=place
    def getParent(self):
        print("mob.no : ",self.mob)
        print("place : ",self.place)
b=Parent("9071236488","ernakulam","anaswara","kanjiraparambil")
b.getPerson()
b.getParent()
