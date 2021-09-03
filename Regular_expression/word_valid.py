import re
x="hello"
n='\w'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("not valid")