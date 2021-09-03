class Person:
    def setPerson(self,name,add):
        self.name=name
        self.add=add
    def getPerson(self):
        print("name : ",self.name)
        print("address : ",self.add)
class Child:
    def setChild(self,clas,school):
        self.clas=clas
        self.scholl=school
    def getChild(self):
        print("class : ",self.clas)
        print("school : ",self.scholl)
class Student(Person,Child):   #multiple inheritance
    def display(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
    def getDisplay(self):
        print("roll no : ",self.rollno)
        print("mark : ",self.mark)

s=Student()
s.setPerson("sreehari","kanjiraparambil")
s.getPerson()
s.setChild(9,"don bosco school")
s.getChild()
s.display(37,80)
s.getDisplay()
