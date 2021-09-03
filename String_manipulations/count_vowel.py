a=input("enter the word : ")
b="aeiouAEIOU"
count=0
for i in a:
    if i in b:
        count+=1
if(count>=1):
    print("number of vowels : ",count)
else:
    print(count,"vowels")

# convert string into upper and lower case characters
# a="anaswara"
# print(a.upper())
# b="ANASWARA"
# print(b.lower())