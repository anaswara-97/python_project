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
class Employ(Person,Parent):
    def setEmploy(self,salary,comp):
        self.salary=salary
        self.comp=comp
    def getEmploy(self):
        print("salary : ",self.salary)
        print("company : ",self.comp)
e=Employ()
e.setPerson("hari","kanjiraparambil")
e.getPerson()
e.setParent("data analyst")
e.getParent()
e.setEmploy(35000,"infosys")
e.getEmploy()
