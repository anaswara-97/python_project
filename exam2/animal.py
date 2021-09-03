class Animal:
    def __init__(self,atype,variety):
        self.atype=atype
        self.variety=variety
    def showAnimal(self):
        print("Type : ",self.atype)
        print("Breed variety : ",self.variety)
class Dog(Animal):
    def setDog(self,color,age):
        self.color=color
        self.age=age
    def getDog(self):
        print("Colour : ",self.color)
        print("age : ",self.age)
d=Dog("dog","golden retriever")
d.showAnimal()
d.setDog("golden","2 mnths")
d.getDog()
