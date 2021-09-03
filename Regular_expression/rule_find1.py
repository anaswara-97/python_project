import re

x="Acv3"
n='[a-zA-Z]+[0-9]$'
m=re.fullmatch(n,x)
if m is not None:
    print("valid")
else:
    print("invalid!")