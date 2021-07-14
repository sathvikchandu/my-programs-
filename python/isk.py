
import collections
n=int(input())

for i in range(n):
    l1=[]
    n,m,k= input().split()
    n= int(n)
    k= int(k)
    m= int(m)
    count=0
    l = list(map(int,input().split()))
    d= collections.Counter(l)
    for key, values in d.items():
        if values>1 and key<=n:
            l1.append(key)
            count+=1
    
    l1.insert(0,count)
    print(l1)
    for i in l1:
        print(i,end=" ")
    print()
     

