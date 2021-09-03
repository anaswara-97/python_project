import re
x="[A-Z]"   #check upper cases only
m=re.finditer(x,"Ccsd @B#5sdAbc")
for i in m:
    print("position : ",i.start())
    print("group : ",i.group())
    print("--------------")