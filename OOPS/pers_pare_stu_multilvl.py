class Person:
    def setPerson(self,name,addr):
        self.name=name
        self.addr=addr
    def getPerson(self):
        print("name : ",self.name)
        print("address : ",self.addr)
class Parent(Person):
    def setParent(self,mob,place):
        self.mob=mob
        self.place=place
    def getParent(self):
        print("mob.no : ",self.mob)
        print("place : ",self.place)
class Student(Parent):
    def setStudent(self,name1,course,marks):
        self.name1=name1
        self.course=course
        self.marks=marks
    def getStudent(self):
        print("student name : ",self.name1)
        print("course : ",self.course)
        print("marks : ",self.marks)
p=Person()
p.setPerson("anwar","kanjiraparambil")
p.getPerson()
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
s.setParent(9072802604,"thripunithura")
s.getPerson()
s.getParent()
s.getStudent()