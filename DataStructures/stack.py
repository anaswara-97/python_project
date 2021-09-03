stack=[]
num=int(input("Enter the size of stack : "))
top=0
n=0
def push():
    global num,top
    if top>num:
        print("stack is full!")
    else:
        n2=int(input("enter element : "))
        stack.append(n2)
        top+=1
def display():
    print(stack)
def pop():
    global top,num
    if top<=0:
        print("stack is empty!")
    else:
        stack.pop()
        top-=1
while n!=1:
    print("1.Push\n2.Pop \n3.Display\n4.Exit\n")
    cho=int(input("select your choice : "))
    if cho==1:
        push()
    elif cho==2:
        pop()
    elif cho==3:
        display()
    elif cho==4:
        print("process terminated!")
        exit(0)


# last in first out(LIFO)
# 2 operations
#     push - insertion
#     pop - deletion