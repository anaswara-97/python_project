import re
x=open("demo","r")
for i in x:
    l=i.split(" ")
n='[0-9]{10}'
m=re.fullmatch(n,l)
if m is not None:
    print("valid")
else:
    print("invalid")
