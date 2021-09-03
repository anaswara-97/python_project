class Vehicle:
    def setDetails(self,color,num):
        self.color=color
        self.num=num
    def printDetails(self):
        print("vehicle number : ",self.num)
        print("colour : ",self.color)
class Bus(Vehicle):
    def busDetails(self,permit,rout):
        self.permit=permit
        self.rout=rout
    def busPrint(self):
        print("permit num : ",self.permit)
        print("rout : ",self.rout)
c=Bus()
c.setDetails("red","kl37ab1234")
c.printDetails()
c.busDetails("c000adfg","tpra-alv")
c.busPrint()

