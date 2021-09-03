import re
x="[a-zA-Z]"   #check both cases
m=re.finditer(x,"aCsd @F#5sDabc")
for i in m:
    print("position : ",i.start())
    print("group : ",i.group())
    print("--------------")