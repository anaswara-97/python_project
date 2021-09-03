min=int(input("Enter minimum limit : "))
max=int(input("Enter maximum limit : "))
print("even numbers between",min,"and",max,"are :")
# for i in range(min,max+1):
#     if(i%2==0):
#         print(i)

#while using
i=min
while(i<max+1):
    if(i%2==0):
        print(i)
    i+=1