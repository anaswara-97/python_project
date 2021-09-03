a={'name':'ammu','age':23,'class':'mca','college':'nirmala'}
print(a)
n=input("enter a key to check present or not : ")
flag=0
for i in a:
    if n in i:
        flag=1
if flag==1:
    print(n,"is present")
else:
    print(n, "is not present")






# a={'name1':'ammu','name2':'anu','name3':'kunju','name4':'meenu'}
# print(a)
# name=input("enter a name to check there or not : ")
# flag=0
# for i in a.items():
#     if name in i:
#         flag=1
#         break
# if flag==1:
#     print("present")
# else:
#     print("not present")