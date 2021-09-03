import re
x=open("reg","r")
for i in x:
    l=i.split(" ")
n='[0-9]{10}'
m=re.fullmatch(n,)
if m is not None:
    print("valid")
else:
    print("invalid")
