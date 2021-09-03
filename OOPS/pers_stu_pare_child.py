class Person:
    def setPerson(self,name,addr):
        self.name=name
        self.addr=addr                                               #person - parent = single inheritance
    def getPerson(self):                                            #person - parent - child = multilevel inheritance
        print("name : ",self.name)
        print("address : ",self.addr)
class Parent(Person):
    def setParent(self,mob,place):
        self.mob=mob
        self.place=place
    def getParent(self):
        print("mob.no : ",self.mob)
        print("place : ",self.place)
class Student(Person):
    def setStudent(self,name1,course,marks):
        self.name1=name1
        self.course=course
        self.marks=marks
    def getStudent(self):
        print("student name : ",self.name1)
        print("course : ",self.course)
        print("marks : ",self.marks)
class Child(Parent):
    def setChild(self,hobby):
        self.hobby=hobby
    def getChild(self):
        print("hobby : ",self.hobby)

a=Person()
a.setPerson("anwar","kanjiraparambil")
a.getPerson()
print("-----------------------")
pa=Parent()
pa.setParent(9072802604,"thripunithura")
pa.setPerson("anwar","kanjiraparambil")
pa.getPerson()
pa.getParent()
print("-----------------------")
s=Student()
s.setStudent("sreehari","bca",480)
s.setPerson("anwar","kanjiraparambil")
s.getPerson()
s.getStudent()
print("-----------------------")
d=Child()
d.setChild("painting")
d.setPerson("anwar","kanjiraparambil")
d.setParent(9072802604,"thripunithura")
d.getParent()
d.getPerson()
d.getChild()




