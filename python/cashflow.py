import copy
for _ in range(int(input())):
    n,m,x= input().split()
    l= list(map(int,input().split()))
    l2= copy.deepcopy(l)
    n= int(n)
    m= int(m)
    x= int(x)
    l1=[]
    passed=0
    for i in l:
        if i>m:
            idx= l.index(i)
            l1.append(idx+1)
            l2[idx]=-1
            passed+=1
    if passed<x:
        while passed<x:
            ma= max(l2)
            if ma!=-1:
                idx2= l.index(ma)
                l1.append(idx2+1)
                passed+=1
    l1.insert(0,passed)
    print(l1)
    
            
    