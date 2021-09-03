import re
x="\s"   
m=re.finditer(x,"acsd @$#5sdabc")
for i in m:
    print("position : ",i.start())
    print("group : ",i.group())
    print("--------------")