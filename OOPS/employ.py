class Employ:
    comp_name="Infosys"
    def setEmploy(self,eid,name,salary,age,dep):
        self.eid=eid
        self.name=name
        self.age=age
        self.salary=salary
        self.dep=dep
    def getEmploy(self):
        print("Id : ",self.eid)
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("Salary : ", self.salary)
        print("Company Name : ", Employ.comp_name)
        print("Department : ", self.dep)
e=Employ()
e.setEmploy(1,"Anwar",15000,30,"production")
e.getEmploy()