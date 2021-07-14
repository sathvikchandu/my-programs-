t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    ans=0
    temp=0
    for j in range(n):
        if(i+1<l[j]):
            temp=1
            break
        ans = ans+(i+1-l[j])
    if(temp==1):
        print("Second") 
    else:
        if(ans%2==1):
            print("First")
        else:
            print("Second")    