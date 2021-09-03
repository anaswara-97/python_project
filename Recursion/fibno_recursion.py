def fibno(num):
    if num<=1:
        return num
    else:
        return fibno(num-1)+fibno(num-2)
num=int(input("enter the range : "))
print("fibnocci series : ")
for i in range(num):
    print(fibno(num))
