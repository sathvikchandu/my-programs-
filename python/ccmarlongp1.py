n,h,x= input().split()
n = int(n)
h = int(h)
x=int(x)
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if(l[i]+x>=h):
        print("YES")
        break
    else:
        count=count+1

if(count==len(l)):
    print("NO")

