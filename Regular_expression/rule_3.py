import re
x="[a-z]"   #check lower cases only
m=re.finditer(x,"acsd @$#5sdABbc")
for i in m:
    print("position : ",i.start())
    print("group : ",i.group())
    print("--------------")