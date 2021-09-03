a="i love i"
c={}
b=a.split(" ")
print(b)
for i in b:
    if i not in c:
        c.update({i:1})
    else:
        val=int(c[i])
        val+=1
        c.update({i:val})
print(c)
