a = [4,3,1,6,7,4,8,11,34,12]
def bsearch():
    a.sort()
    print(a)
    n = int(input("enter an element: "))
    low = 0
    flag = 0
    up = len(a) - 1
    while low < up:
        mid = low + up // 2
        if n > a[mid]:
            low = mid + 1
        elif n < a[mid]:
            up = mid -1
        elif n == a[mid]:
            flag = 1
            break
    if flag == 1:
        print("found the element")
    else:
        print("not found")
bsearch()
# print("smallest in the list : ",a[0],"\n largest in the list: ",a[-1])