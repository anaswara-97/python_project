import re
x="a+"
r="aabB aa c def"
m=re.finditer(x,r)
for i in m:
    print("position : ",i.start())
    print("group : ",i.group())
    print("--------------")