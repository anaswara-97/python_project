a=input("enter the word : ")
b=input("enter an element to check if there or not : ")
count = 0
for i in a:
    if i in b:
        count=1
if(count==1):
    print("present")
else:
    print("not present")