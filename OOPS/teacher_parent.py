class Parent:
    def __init__(self,job):
        self.job=job
    def getParent(self):
        print("job : ",self.job)
class Teacher(Parent):
    def __init__(self,name,id,college,dep,job):
        super().__init__(job)
        self.name=name
        self.id=id
        self.college=college
        self.dep=dep
    def getTeacher(self):
        print("name : ",self.name)
        print("id : ", self.id)
        print("department  : ",self.dep)
        print("college : ",self.college)
    def __str__(self):
        return self.name+ str(self.id)
t=Teacher("anaswara",1802,"nirmala muvattupuzha","mca","teacher")
t.getParent()
t.getTeacher()
print(t)