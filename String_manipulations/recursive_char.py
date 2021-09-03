a=input("enter the word : ")
b=""
for i in a:
    if i not in b:
        b+=i
    else:
        print("first recursive character is : ",i)
        break
