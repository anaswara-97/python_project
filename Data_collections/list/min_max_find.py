a=[2,3,4,1,0,5,66,2]
min=a[0]
max=a[-1]
for i in a:
    if i<min:
        min=i
    if i>max:
        max=i
print("minimum element: ",min)
print("maximum element: ",max)