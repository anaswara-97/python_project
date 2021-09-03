import re

x=input("enter phn number : ")
n='[+][9][1][0-9]{10}'
m=re.fullmatch(n,x)
if m is not None:
    print("valid")
else:
    print("invalid!")