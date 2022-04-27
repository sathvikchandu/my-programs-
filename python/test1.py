for _ in range(int(input())):
    
    a,b,c= map(int,input().split())
    if 2*b==a+c:
        print("YES")
    elif ((2*b)<a+c):
        if (a+c)%(2*b)==0:
            print("YES")
        else:
            print("NO")
    else:
        if ((2*b)-c)%a==0 or ((2*b)-a)%c==0:
            print("YES")
        else:
            print("NO")

