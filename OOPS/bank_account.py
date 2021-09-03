class Bank:
    def account(self,name,acc_type,address):
        self.name=name
        self.acc_type=acc_type
        self.blnce=4000
        self.mblnce=self.blnce
        self.address=address
        print("current balance : ",self.mblnce)
    def deposit(self,amount):
        self.amount=amount
        self.blnce+=amount
        print("rupees credited to your account : ",self.blnce)

    def withdraw(self,amt):
        self.amt = amt
        if self.amt>self.blnce:
            print("insufficient balance")
        else:
            self.blnce-= amt
            print("Balance after withdraw : ", self.blnce)
b=Bank()
b.account("anaswara","savings","kanjiraparambil")
b.deposit(200)
b.withdraw(4500)