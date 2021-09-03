import re
count=0
m=re.finditer("abc","aabbabcanacabc")
for i in m:
    print("match occuring position : ",i.start())       #to find where matching occurs,at which position
    print("matching object : ",i.group())               #to group matching object
    count+=1
print("total count = ",count)