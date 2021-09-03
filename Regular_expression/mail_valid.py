import re

x=input("enter your mail id: ")
n='[a-zA-Z0-9^a-zA-z0-9]+[@][a-z]+[.][a-z]{3}$'
m=re.fullmatch(n,x)
if m is not None:
    print("valid")
else:
    print("invalid")