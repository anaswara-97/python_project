a=int(input("enter your age : "))
if a < 18:
    raise Exception("you are not eligible")
else:
    print("you are eligible to take vaccine")