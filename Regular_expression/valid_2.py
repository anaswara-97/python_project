import re
x="56fg"
n='[0-9]{2}[a-z]{2}'
match=re.fullmatch(n,x)
if match is not None:
    print("valid")
else:
    print("not valid")