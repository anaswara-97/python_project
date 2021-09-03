
def linear(b):
    count=0
    for i in a:
        if b in a:
            count=1
            break
    if count==1:
        print("the elemnt is there")
    else:
        print("not there")
a=[2,44,12,3,11,7,77,56,23,10,15,20,50,79,80]
print(a)
b=int(input("enter the element to check there or not : "))
linear(b)
