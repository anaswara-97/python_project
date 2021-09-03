class Student:
    def studDetails(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name : ",self.name)
        print("age : ",self.age)
    def __str__(self):
        return self.name
f=open("student","r")
for i in f:
    l=i.split(",")
    n=l[0]
    a=l[1]
    s = Student()
    s.studDetails(n,a)
    s.display()
    print(s)