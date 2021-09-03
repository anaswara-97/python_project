import re

x=input("enter string: ")
n='[a][0-9]+[b]'
m=re.fullmatch(n,x)
if m is not None:
    print("valid")
else:
    print("invalid")