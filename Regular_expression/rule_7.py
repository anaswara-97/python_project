import re
x="[a-zA-Z0-9]"   #check abc
m=re.finditer(x,"aVsd @$#5sDT7abc")
for i in m:
    print("position : ",i.start())
    print("group : ",i.group())
    print("--------------")