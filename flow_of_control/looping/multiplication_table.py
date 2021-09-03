num=int(input("Enter a number to see multiplication table : "))
print("-----------------------------")
print("Multiplication table of ",num)
print("-----------------------------")
for i in range(1,11):
    print(num,"*",i,"=",num*i)
