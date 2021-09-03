class Animal:
    def aType(self,name):
        self.name=name
        print("Animal name : ",self.name)
    def aType(self,breed,age):
        self.breed=breed
        self.age=age
        print("Breed variety : ",self.breed)
        print("age : ",self.age)
class AnimalType(Animal):
    def aType(self,colr):
        self.colr=colr
        print("Animal colour : ",self.colr)
a=Animal()
b=AnimalType()
a.aType("dog")
a.aType("golden retriever",1)
b.aType("golden")