for _ in range(int(input())):
    #n= int(input())
    a=input()
    b=input()
    c=0
    l1=list(a)
    l2=list(b)
    l3=[]
    l4=[]

    for i in range(len(l1)):
        l3.append(ord(l1[i]))
    for i in range(len(l2)):
        l4.append(ord(l2[i]))

    
    for  i in range(len(l3)):
        if l3[i]<l4[i] and c==i:

            c=c+1
    print(c)
            
        
    