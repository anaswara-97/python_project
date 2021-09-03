import re
x="[^a-zA-Z0-9]"   #check special characters
m=re.finditer(x,"acsd @$#5sdabc")
for i in m:
    print( "position : " , i.start() )
    print( "group : " , i.group() )
    print( "--------------" )