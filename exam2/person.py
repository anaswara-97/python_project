class Person:
    def setPerson(self,name,addr):
        self.name=name
        self.addr=addr
    def getPerson(self):
        print("name : ",self.name)
        print("address : ",self.addr)
class Parent():
    def setParent(self,job):
        self.job=job
    def getParent(self):
        print("job : ",self.job)
class Student(Person):
    def setStudent(self,name1,course,marks):
        self.name1=name1
        self.course=course
        self.marks=marks
    def getStudent(self):
        print("student name : ",self.name1)
        print("course : ",self.course)
        print("marks : ",self.marks)
class Teacher(Person,Parent):
    def setTeacher(self,name,college,dep):
        self.name=name
        self.college=college
        self.dep=dep
    def getTeacher(self):
        print("teacher name : ",self.name)
        print("department  : ",self.dep)
        print("college : ",self.college)
s=Student()
s.setStudent("akshitha","bsc",490)
s.getStudent()
s.setPerson("david","anamthuruthil")
s.getPerson()
print("-------------------")
t=Teacher()
t.setPerson("david","anamthuruthil")
t.getPerson()
t.setParent("contractor")
t.getParent()
t.setTeacher("haritha","mar alias college","maths")
t.getTeacher()