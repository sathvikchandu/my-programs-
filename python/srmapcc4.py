for _ in range(int(input())):
    
    n= int(input())
    l1= list(map(int,input().split()))
    l2= list(map(int,input().split()))
    for i in range(1,len(l1)):
        l1[i]=l1[i]-l1[i-1]
    print(l1)
        