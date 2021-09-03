class Hello:
    def display(self):    # self -- instance keyword
        print("displaying...")
    def dis(self):
        print("continue display...")
h1=Hello()                 #object reference creation
h1.display()
h1.dis()
print("............")
h2=Hello()
h2.dis()
h2.display()

