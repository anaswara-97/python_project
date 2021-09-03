dc={'name':'anu','age':5,'class':3}
print(dc)

print("dc['name'] : ",dc['name'])

dc['age']=7 #updating existing entry
print(dc)

dc['school']="xyz school"  #adding new entry to existing dictionary
print(dc)
 # or,we can use the below method

dc.update({'location':'ernakulam'})
print(dc)
print("--------------------------------")

del dc['name']            #removing specific key-value
print(dc)

dc.clear()
print(dc)              #removing all elements

del dc
# print(dc)              #rremoving declared dictionary itself