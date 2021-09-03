class Student:
    def studDetails(self,name,roll,course,mark):
        self.name=name
        self.roll=roll
        self.course=course
        self.mark=mark
    def display(self):
        print("name : ",self.name)
        print("roll no : ",self.roll)
        print("course : ",self.course)
        print("mark : ",self.mark)
f=open("abc","r")
for i in f:
    l=i.split(",")
    n=l[0]
    ro=l[1]
    co=l[2]
    m=l[3]
    s = Student()
    s.studDetails(n,ro,co,m)
    s.display()

