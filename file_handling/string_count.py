f=open("count","r")
for i in f:
    st=i.split(" ")
    s={}
    for j in st:
        if j not in s:
            s.update({j:1})
        else:
            value = int(s[j])
            value += 1
            s.update({j: value})
    print(s)