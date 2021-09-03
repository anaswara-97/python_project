import re
# x="[0-9]"   #check digits OR
x="\d"
m=re.finditer(x,"ac1sd @$#5sda0bc")
for i in m:
    print("position : ",i.start())
    print("group : ",i.group())
    print("--------------")