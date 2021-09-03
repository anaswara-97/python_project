initial = int(input("enter initial value : "))
end = int(input("enter end value : "))
for k in range(0,end):
    if k%2==0:
        for i in range( 0,end, 1):
            for j in range(0, i+1):
                print(k+1, end=' ')
            print()
        # initial += 1
    else:
        for i in range( end,0, -1):
            for j in range(0, i):
                print(k+1, end=' ')
            print()
        # initial += 1



# for i in range( rows,0, -1):
#     for j in range(0, i):
#         print(rows-3, end=' ')
#     print()
# for i in range( 0,rows, 1):
#     for j in range(0, i + 1):
#         print(rows-2, end=' ')
#     print()
#
# for i in range( rows,0, -1):
#     for j in range(0, i):
#         print(rows-1, end=' ')
#     print()