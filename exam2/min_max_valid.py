
import re

x=input("enter string: ")
n='[A-Z]\w[a-zA-Z0-9][A-Z]{5,10}$'
m=re.fullmatch(n,x)
if m is not None:
    print("valid")
else:
    print("invalid")