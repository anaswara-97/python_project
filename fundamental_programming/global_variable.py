
def display():
    global x          #declaring a local variable as global
    x=6
    print("local",x-3)
display()
print("global",x)      # printing local variabe outside of access