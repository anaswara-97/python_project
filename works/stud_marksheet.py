sub1= 10 #int(input("enter the marks of first subject :"))
sub2=18 #int(input("enter the marks of second subject : "))
sub3= 17#int(input("enter the marks of third subject : "))
sub4= 19#int(input("enter the marks of fourth subject : "))
sub5= 9#int(input("enter the marks of fifth subject : "))
total=sub1+sub2+sub3+sub4+sub5
print("total mark is : ",total)
avg=total/5
print("average is : ",avg)
if total>=90:
    print("Grade : A+")
elif total>=80:
    print("Grade : A")
elif total>=70:
    print("Grade : B+")
elif total>=60:
    print("Grade : B")
elif total>=50:
    print("Grade : C+")
elif total>=40:
    print("Grade : C")
elif total>=30:
    print("Grade : D+")
else:
    print("Failed")