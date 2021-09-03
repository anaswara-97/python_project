fixed_amt=20000
withdraw=int(input("Enter the amount to withdraw : "))
blnc=fixed_amt-withdraw
if withdraw>fixed_amt:
    print("insufficient balance!")
else:
    print("withdraw successfully!")
    print("your current balance is : ",blnc)