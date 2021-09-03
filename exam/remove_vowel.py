a=input("enter the string : ")
s="aeiouAEIOU"
print("string after removing vowels : ")
for i in a:
    if i not in s:
        print(i,end="")
