import re

x=input("enter vehicle number : ")
n='[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}'
m=re.fullmatch(n,x)
if m is not None:
    print("valid")
else:
    print("invalid!")