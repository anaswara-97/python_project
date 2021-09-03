# first in first out(FIFO)
# 2 operations
#     insertion
#     deletion

que1=[]
size=int(input("enter the size of queue : "))
front=0
rear=0
n=0
def insert():
    global front,rear,size,que1
    if front>=size:
        print("queue is full!")
    else:
        n2 = int(input("enter element : "))
        que1.insert(rear,n2)
        rear+=1
        for i in range(front,rear):
            print(que1[i],end=" ")
def dele():
    global front,rear,size,que1
    if front == rear:
        print("queue is empty!")
    else:
        front+=1
        for i in range(front,rear):
            print(que1[i],end=" ")
while n!=1:
    print("\n1.Insert\n2.Delete\n3.Exit")
    cho=int(input("Enter your choice : "))
    if cho==1:
        insert()
    elif cho==2:
        dele()
    elif cho==3:
        print("Process terminated!")
        exit(0)
    else:
        print("invalid selection")