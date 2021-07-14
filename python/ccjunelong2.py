for i in range(int(input())):
    a,b,c,d=input().split()
    D=int(a)
    d=int(b)
    p=int(c)
    q= int(d)
    n=int(D/d)
    count=0
    if(n%2==0):
        count+=int(d*(int(n/2)*(2*p+(n-1)*q)))
    else:
        count+=int(d*(n*(p+((n-1)/2)*q)))
    count+=(D%d)*(p+(n)*q)
    print(count)
        
        
    