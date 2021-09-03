# try block and finally block will work always
# but except block work only when an exception is  occured

a=[2,3,4]
index=int(input("enter index : "))
try:
    print(a[index])
except:
    print("index not found")
finally:
    print("exception")