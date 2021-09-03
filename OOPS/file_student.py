class Student:
    def studDetails(self,name,rollno,dep,mark):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
    def display(self):
        print("name : ",self.name)
        print("rollno : ",self.rollno)
        print("department : ", self.dep)
        print("mark : ", self.mark)
    def __str__(self):
        return str(self.rollno)
f=open("stud","r")
for i in f:
    l=i.split(",")
    s=Student()
    name=l[0]
    rollno=l[1]
    dep=l[2]
    mark=l[3]
    s.studDetails(name,rollno,dep,mark)
    s.display()
    print("object ref : ",s,"\n--------")