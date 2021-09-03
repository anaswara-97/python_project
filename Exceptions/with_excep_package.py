l=[2,3,1]
pos=int(input("enter position : "))
try:
    print(l[pos])
except Exception as e:
    print(e.args)