l=[]
a=int(input("press 1 to enqueue and 0 to dequeue from the queue"))
while a==1 or a==0:
    if a==1:
        b=int(input("enter the number"))
        l.append(b)
    else:
        if len(l)<1:
            print("The queue is empty")
        else:
            l.pop(0)
    a=int(input("press 1 to append and 0 to pop from the stack"))
print(l)    
    