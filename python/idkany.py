"""
for i in range(len(input())):
    l1= list(map(int,input().split()))
    a= l1[0]
    b= l1[1]
    c= l1[2]
    l= list(map(int,input().split()))
    su=0
    for i in l:
        if i>0:
            su+=i
            print("the value of su is ",su)
        elif i==0:
            su-=b
            print("before if the value is ",su)
            if su<=0:
                su=0
                print("aafter if the value is ",su)
    print(su)
    if su>=c:
        print("YES")
    if su<c:
        print("NO")
"""

T = int(input(""))
for i in range(T):
    n,d,h = input("").split()
    N=int(n)
    D=int(d)
    H=int(h)
    arr= input("").split()
    for i in range(N):
        arr[i] = int(arr[i])
    flag = 0
    water_level = 0
    for i in range(N):
        if(arr[i])>0:
            
            water_level = water_level + arr[i]
       
        else:
            water_level = max(water_level-D,0)
            
        if(water_level>H):
            flag = 1
    if(flag==1):
        print("YES")
    else:
        
        print("NO")