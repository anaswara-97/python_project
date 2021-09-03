
import re

x=input("enter string: ")
n='[A-Z][a-z]+'
m=re.fullmatch(n,x)
if m is not None:
    print("valid")
else:
    print("invalid")