class Person:
    def setDetails(self,ptype,age):
        self.ptype=ptype
        self.age=age
    def getDetails(self):
        print(self.ptype)
        print(self.age)
class Employ(Person):
    def setEmploy(self,name,salary,comp):
        self.name=name
        self.salary=salary
        self.comp=comp
    def getEmploy(self):
        print(self.name)
        print(self.salary)
        print(self.comp)
p=Person()
p.setDetails("employee",32)
p.getDetails()
print("---------------------")
e=Employ()
e.setDetails("employee",32)
e.getDetails()
e.setEmploy("anwar",15000,"infosys")
e.getEmploy()