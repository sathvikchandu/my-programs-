l=[]
a=int(input("press 1 to append and 0 to pop from the stack"))
while a==1 or a==0:
    if a==1:
        b=int(input("enter the number"))
        l.append(b)
    else:
        l.pop()
    a=int(input("press 1 to append and 0 to pop from the stack"))
print(l)    
    