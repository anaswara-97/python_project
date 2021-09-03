class Teacher:
    clg_name="st.thomas college"
    def __init__(self,tname,tid,sub,dep):
        self.tname=tname
        self.tid=tid
        self.sub=sub
        self.dep=dep
    def getDetails(self):
        print(self.tname)
        print(self.tid)
        print(self.sub)
        print(self.dep)
        print(Teacher.clg_name)
t=Teacher("swathi",12,"mathematics","maths")
t.getDetails()
