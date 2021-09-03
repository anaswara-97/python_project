class Vehicle:
    def __init__(self,regno,model,clor):
        self.regno=regno
        self.model=model
        self.clor=clor
    def display(self):
        print(self.regno)
        print(self.model)
        print(self.clor)
    def __str__(self):
        #return self.model
         return self.model+self.clor     #more than two values for one object reference(concatination)
v=Vehicle("kl10e1234","Benz","black")
v.display()
print("object reference address : ",v)   # <__main__.Vehicle object at 0x0000027877616208> without using twostring method
                                        #object reference address :  Benzblack with twostring method