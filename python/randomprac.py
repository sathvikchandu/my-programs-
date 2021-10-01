for i in range(int(input())):
    s=input()
    l= list(s)
    l1=[]
    flag=1
    for i in l:
        if i in l1:
            flag=0
            break
        else:
            l1.append(i)

    
    print(len(l1))