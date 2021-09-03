class Person:
    def setPerson(self,name,add):
        self.name=name
        self.add=add
    def getPerson(self):
        print("name : ",self.name)
        print("address : ",self.add)
class Parent:
    def setParent(self,job):
        self.job=job
    def getParent(self):
        print("job : ",self.job)
class Teacher(Person,Parent):
    def setTeacher(self,name,college,dep):
        self.name=name
        self.college=college
        self.dep=dep
    def getTeacher(self):
        print("name : ",self.name)
        print("department  : ",self.dep)
        print("college : ",self.college)
t=Teacher()
t.setPerson("hari","kanjiraparambil")
t.getPerson()
t.setParent("data analyst")
t.getParent()
t.setTeacher("anwar","st thomas college","computer science")
t.getTeacher()
