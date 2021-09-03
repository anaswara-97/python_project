a="anaswara"
print("word : ",a)
b=input("enter an element to check count : ")
count=0
for i in a:
    if i in b:
        count+=1
if(count>=1):
    print(b,"occures",count,"times")
else:
    print(b, "occures", count, "times")