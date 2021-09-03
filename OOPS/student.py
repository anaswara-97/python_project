class Student:
    def __init__(self,name,rollno,dep,college):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.college=college
    def display(self):
        print("name : ",self.name)
        print("rollno : ",self.rollno)
        print("department : ",self.dep)
        print("college : ",self.college)
    def __str__(self):
        return str(self.rollno)+self.dep
s=Student("anaswara",1802,"mca","nirmala college muvattupuzha")
s.display()
print(s)