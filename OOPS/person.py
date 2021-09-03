class Person:
    def setVal(self,name,age):
        self.name=name
        self.age=age
    def getVal(self):
        print("Name : ",self.name)
        print("Age : ", self.age)
p=Person()
p.setVal("ammu",23)
p.getVal()