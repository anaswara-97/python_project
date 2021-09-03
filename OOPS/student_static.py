class Student:
    dep="MCA"  #statis variable -- related to class
    def details(self,name,regno,course):
        self.name=name         #instance variable  -- related to methods
        self.regno=regno
        self.course=course
    def getDetails(self):
        print("...Student Details...")
        print("Name : ",self.name)
        print("Register Number : ", self.regno)   #instance variable accessed through self keyword
        print("Course Year : ", self.course)
        print("Department : ", Student.dep)      #static variable accessed through class name
s=Student()
s.details("Anaswara","mcale1802",2020)
s.getDetails()